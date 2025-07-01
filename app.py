import streamlit as st
import data_loader as dl
import analyser as anl
#st.write("Hello world")
FOLLOWING_UPLOADED = False
FOLLOWER_UPLOADED = False

# section for title and description phase 1
st.title("📊 Instagram Follower Insights")
st.write("Description here....")

# upload the files
upload_file_followers = st.file_uploader("Upload the followers file: ")
#print(upload_file_followers)
if upload_file_followers:
    if '.json' not in upload_file_followers.name:
        #st.write("invalid file type")
        st.error("Please upload a JSON file")
        # data = pd.read_json(upload_file_followers)
        # print(data)
        # st.write(data)
        
    else:
        followers = dl.find_followers(upload_file_followers)
        st.write(followers)
        FOLLOWER_UPLOADED = True

upload_file_following = st.file_uploader("Upload the following file: ")
if upload_file_following:
    if '.json' not in upload_file_following.name:
        st.error("Please upload a JSON file")

    else:
        following = dl.find_following(upload_file_following)
        st.write(following)
        FOLLOWING_UPLOADED = True

# if upload_file_followers and upload_file_following:
#     if '.json' not in upload_file_followers.name:
#         st.error("Please upload a JSON file")
#     elif '.json' not in upload_file_following.name:
#         st.error("Please upload a JSON file")
#     else:
#         followers = dl.find_followers(upload_file_followers)
#         st.write(followers)
#         following = dl.find_following(upload_file_following)
#         st.write(following)

#         non_followers, unrequited_followers, mutual = anl.following_follower_analysis(following, followers)

analyse_button = st.button("Analyse data")

if analyse_button:
    if FOLLOWER_UPLOADED == True and FOLLOWING_UPLOADED == True:
        non_followers, unrequited_followers, mutual = anl.following_follower_analysis(following, followers)
        st.write("in condition")

