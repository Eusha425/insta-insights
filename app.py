import streamlit as st
import data_loader as dl
#st.write("Hello world")

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

upload_file_following = st.file_uploader("Upload the following file: ")
if upload_file_following:
    if '.json' not in upload_file_following.name:
        st.error("Please upload a JSON file")

    else:
        following = dl.find_following(upload_file_following)
        st.write(following)
