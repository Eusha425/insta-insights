import streamlit as st

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

upload_file_following = st.file_uploader("Upload the following file: ")
if upload_file_following:
    if '.json' not in upload_file_following:
        st.error("Please upload a JSON file")