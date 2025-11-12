import streamlit as st
import data_loader as dl
import analyser as anl
import visualiser as vl
import exporter as ex
import snapshot_manager as sm
import deactivate_manager as dm


# session state to retain analysis results after script reruns 
# (e.g., when the download button is clicked), so that the data 
# and interface do not reset to their default state.
if 'analyse_button_state' not in st.session_state:
    st.session_state.analyse_button_state = False
if 'remove_deactive_button_state' not in st.session_state:
    st.session_state.remove_deactive_button_state = False
if 'non_follower_state' not in st.session_state:
    st.session_state.non_follower_state = None
if 'unrequited_followers_state' not in st.session_state:
    st.session_state.unrequited_followers_state = None
if 'mutual_state' not in st.session_state:
    st.session_state.mutual_state = None
if 'FOLLOWER_UPLOADED' not in st.session_state:
    st.session_state.FOLLOWER_UPLOADED = False
if 'FOLLOWING_UPLOADED' not in st.session_state:
    st.session_state.FOLLOWING_UPLOADED = False


# section for title and description
st.title("📊 Instagram Follower Insights")
st.markdown("""
Easily analyse your Instagram connections by uploading your exported **followers** and **following** data.

Discover:
- 🔍 Who doesn't follow you back
- 🧭 Who you're not following back
- 🤝 Your mutual followers
- 📈 Visual summaries of your network
- 💾 Export your results as CSV or TXT

> All processing happens locally - your data stays private.
""")


# upload the files
upload_file_followers = st.file_uploader("Upload the followers file: ")

if upload_file_followers:
    if '.json' not in upload_file_followers.name:
        st.error("Please upload a JSON file") 
    else:
        followers = dl.find_followers(upload_file_followers)
        if followers is None:
            st.error("❌ Could not read followers. Make sure the file is the correct Instagram export (usually named 'followers_1.json').")
        else: 
            st.success("✅ Followers file loaded successfully.")
            st.session_state.FOLLOWER_UPLOADED = True

upload_file_following = st.file_uploader("Upload the following file: ")
if upload_file_following:
    if '.json' not in upload_file_following.name:
        st.error("Please upload a JSON file")
    else:
        following = dl.find_following(upload_file_following)
        if following is None:
            st.error("❌ Could not read following data. Make sure the file is the correct Instagram export (usually named 'following.json').")
        else:
            st.success("✅ Following file loaded successfully.")
            st.session_state.FOLLOWING_UPLOADED = True

st.sidebar.markdown("### 📱 Follower Insights")
st.sidebar.info("Built with ❤️ using Streamlit.\n\nCreated by Eusha.")

analyse_button = st.button("Analyse data")

if analyse_button:
    if st.session_state.FOLLOWER_UPLOADED and st.session_state.FOLLOWING_UPLOADED:
        with st.spinner("Analysing..."):
            non_followers, unrequited_followers, mutual = anl.following_follower_analysis(following, followers)
            st.session_state.non_follower_state = non_followers
            st.session_state.unrequited_followers_state = unrequited_followers
            st.session_state.mutual_state = mutual
            st.session_state.analyse_button_state = True



if st.session_state.analyse_button_state and st.session_state.mutual_state is not None and st.session_state.unrequited_followers_state is not None and st.session_state.non_follower_state is not None:
    
    st.subheader("🙅‍♂️ Not Following You Back (One-sided)")
    st.table(st.session_state.non_follower_state)
    st.caption(f"Total: {len(st.session_state.non_follower_state)}")

    st.subheader("👀 You’re Not Following Back (Unreciprocated)")
    st.table(st.session_state.unrequited_followers_state)
    st.caption(f"Total: {len(st.session_state.unrequited_followers_state)}")

    st.subheader("🤝 Mutual Followers (Following Each Other)")
    st.table(st.session_state.mutual_state)
    st.caption(f"Total: {len(st.session_state.mutual_state)}")

    st.subheader("👻 Remove Deactivated Accounts")

    with st.container():
        st.markdown(
            "<p style='font-size:16px;'>"
            "Enter names of deactivated accounts below (one per line), "
            "or upload a text file containing the list."
            "</p>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([2, 1])
        with col1:
            deactivated_accounts = st.text_area(
                "Enter manually",
                placeholder="e.g.\nAlice\nBob\nCharlie",
                height=150
            )
        with col2:
            upload_deactive_file = st.file_uploader("Upload list file (.txt)", type=["txt"])

    st.markdown("")  # light spacing

    remove_deactive_button = st.button("Remove deactive accounts")
    if remove_deactive_button:
        if upload_deactive_file:
            st.session_state.non_follower_state = dm.remove_deactive(st.session_state.non_follower_state, dm.extract_names_from_file(upload_deactive_file))

        st.session_state.non_follower_state = dm.remove_deactive(st.session_state.non_follower_state, deactivated_accounts)
        st.session_state.unrequited_followers_state = dm.remove_deactive(st.session_state.unrequited_followers_state, deactivated_accounts)
        st.rerun()


    fig = vl.visualisation(
        st.session_state.mutual_state,
        st.session_state.non_follower_state,
        st.session_state.unrequited_followers_state
    )
    st.subheader("📊 Visual Summary")
    st.pyplot(fig)

    st.subheader("💾 Export Your Data")
    download_option = st.selectbox("Select download format", ("CSV", "Text"), index=None)

    if download_option == "CSV":        
        download_button = st.download_button(
            label= "Download data", data=ex.streamlit_export_csv(
                st.session_state.non_follower_state,
                st.session_state.unrequited_followers_state,
                st.session_state.mutual_state
            ), 
            file_name="data.csv", mime="text/csv", icon=":material/download:")
    elif download_option == "Text":
        download_button = st.download_button(
            label= "Download data", data=ex.streamlit_export_txt(
                st.session_state.non_follower_state,
                st.session_state.unrequited_followers_state,
                st.session_state.mutual_state
            ), 
            file_name="data.txt", mime="text/plain", icon=":material/download:")
        
    snapshot = st.button("Save this as snapshot")
    if snapshot:
        if sm.save_snapshot(followers, following):
            st.success("Snapshot saved")
        else:
            st.error("Unable to save snapshot, try again later")

    snapshot_option_name = st.selectbox("Select snapshot", options=sm.list_snapshots(), index=None)
    if snapshot_option_name:
        with st.expander("📅 Compare with Previous Snapshot"):

            snapshot_follower = sm.load_follower_from_snapshot(snapshot_option_name)
            snapshot_following = sm.load_following_from_snapshot(snapshot_option_name)

            snapshot_data = anl.following_follower_analysis(snapshot_following, snapshot_follower)
            
            if snapshot_data is not None:
            
                followers_lost = sm.get_followers_lost(followers, snapshot_follower)
                if followers_lost is not None:
                    st.subheader("📉 Lost Followers Since Snapshot")
                    st.table(followers_lost)
            
                followers_gained = sm.get_followers_gain(followers, snapshot_follower)
                if followers_gained is not None:
                    st.subheader("📈 New Followers Since Snapshot")
                    st.table(followers_gained)

                mutual_info = sm.get_mutual_analysis(st.session_state.mutual_state, snapshot_data)

                st.subheader("🤝 Mutuals Gained")
                st.table(mutual_info[0])

                st.subheader("💔 Mutuals Lost")
                st.table(mutual_info[1])

                st.markdown("---")
                col1, col2, col3, col4 = st.columns(4)
                st.markdown("### 📶 Net Follower Change")
                col1.metric("New Followers", len(followers_gained), delta=len(followers_gained))
                col2.metric("Unfollowers", len(followers_lost), delta=-len(followers_lost))
                col3.metric("Mutuals Gained", len(mutual_info[0]))
                col4.metric("Mutuals Lost", len(mutual_info[1]))
                st.markdown(f"**+{len(followers_gained)}** new followers, **-{len(followers_lost)}** lost followers → **Net: {len(followers_gained) - len(followers_lost)}**")
                st.markdown("---")

                st.markdown("### 🧠 Key Takeaways")
                if len(followers_gained) > len(followers_lost):
                    st.success("You're gaining more followers than you're losing! 📈")
                elif len(followers_gained) < len(followers_lost):
                    st.warning("You lost more followers than you gained. Consider reviewing your content strategy. 😕")
                else:
                    st.info("Your follower count is stable.")
