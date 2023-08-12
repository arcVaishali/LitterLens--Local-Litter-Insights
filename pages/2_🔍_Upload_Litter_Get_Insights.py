import streamlit as st 

st.set_page_config(
    page_title="Upload and Read",
    page_icon="🔍",
)

st.title(":blue[Upload] Litter Data and Read Litter Data") 

col1, col2 = st.columns([0.5,1])
with col1:
    upload = st.button("Upload")
with col2:
    camera = st.button("Camera")
if camera == True:
    photo = st.camera_input("Take picture")
else:
    photo = st.file_uploader("Upload Photo")
