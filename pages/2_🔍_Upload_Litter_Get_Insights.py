import streamlit as st 

def submit():
    pass

st.set_page_config(
    page_title="Upload and Read",
    page_icon="🔍",
)

st.title(":blue[Upload] Litter Data and Read Litter Data") 

col1, col2 = st.columns([1,1])
with col1:
    upload = st.button("Upload", use_container_width=True)
with col2:
    camera = st.button("Camera", use_container_width=True)


def photo():
    key = True
    if camera == True:
        photo = st.camera_input("Take picture")
        if photo is not None:
            key = False
        st.button("Submit", on_click=submit(), disabled=key, use_container_width=True)
    else:
        photo = st.file_uploader("Upload image")
        if photo:
            st.image(photo)
        if photo is not None:
            key = False
        st.button("Submit", on_click=submit(), disabled=key, use_container_width=True)

photo()









