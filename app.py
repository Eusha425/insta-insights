import streamlit as st
import data_loader as dl
import analyser as anl
import visualiser as vl
import exporter as ex
import snapshot_manager as sm

FOLLOWING_UPLOADED = False
FOLLOWER_UPLOADED = False

# session state to retain analysis results after script reruns 
# (e.g., when the download button is clicked), so that the data 
# and interface do not reset to their default state.
if 'analyse_button_state' not in st.session_state:
    st.session_state.analyse_button_state = False
if 'non_follower_state' not in st.session_state:
    st.session_state.non_follower_state = None
if 'unrequited_followers_state' not in st.session_state:
    st.session_state.unrequited_followers_state = None
if 'mutual_state' not in st.session_state:
    st.session_state.mutual_state = None

# section for title and description phase 1
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
            #st.write(followers)
            st.success("✅ Followers file loaded successfully.")
            FOLLOWER_UPLOADED = True

upload_file_following = st.file_uploader("Upload the following file: ")
if upload_file_following:
    if '.json' not in upload_file_following.name:
        st.error("Please upload a JSON file")
    else:
        following = dl.find_following(upload_file_following)
        if following is None:
            st.error("❌ Could not read following data. Make sure the file is the correct Instagram export (usually named 'following.json').")
        else:
            #st.write(following)
            st.success("✅ Following file loaded successfully.")
            FOLLOWING_UPLOADED = True

st.sidebar.markdown("### 📱 Follower Insights")
st.sidebar.info("Built with ❤️ using Streamlit.\n\nCreated by Eusha.")

analyse_button = st.button("Analyse data")

if analyse_button:
    if FOLLOWER_UPLOADED == True and FOLLOWING_UPLOADED == True:
        with st.spinner("Analysing..."):
            non_followers, unrequited_followers, mutual = anl.following_follower_analysis(following, followers)
            st.session_state.non_follower_state = non_followers
            st.session_state.unrequited_followers_state = unrequited_followers
            st.session_state.mutual_state = mutual
            st.session_state.analyse_button_state = True



if st.session_state.analyse_button_state and st.session_state.mutual_state is not None and st.session_state.unrequited_followers_state is not None and st.session_state.non_follower_state is not None:
    
    st.subheader("🔴 Not Following You Back")
    st.write(st.session_state.non_follower_state)
    st.caption(f"Total: {len(st.session_state.non_follower_state)}")

    st.subheader("🟢 You Are Not Following Back")
    st.write(st.session_state.unrequited_followers_state)
    st.caption(f"Total: {len(st.session_state.unrequited_followers_state)}")

    st.subheader("🔁 Mutual Followers")
    st.write(st.session_state.mutual_state)
    st.caption(f"Total: {len(st.session_state.mutual_state)}")

    
    # col1, col2 = st.columns(2)

    # with col1:
    #     st.subheader("You are not followed back")
    #     st.write("You are not following back")
    #     st.write("Mutuals")

    # with col2:
    #     st.write(st.session_state.non_follower_state)
    #     st.write(f"total: {len(st.session_state.non_follower_state)}")
    #     st.write(st.session_state.unrequited_followers_state)
    #     st.write(f"total: {len(st.session_state.unrequited_followers_state)}")

    #     st.write(st.session_state.mutual_state)
    #     st.write(f"total: {len(st.session_state.mutual_state)}")
    
    
    
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
        
    snapshot = st.button("Save a snapshot")
    if snapshot:
        if sm.save_snapshot(followers, following):
            st.success("Snapshot saved")