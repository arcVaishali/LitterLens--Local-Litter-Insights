import streamlit as st 
import pandas as pd
import numpy as np

def predict():
    pass

def submit():
    # litterType = predict()
    litterType = "plastic straw" 
    fd = pd.read_csv("https://docs.google.com/spreadsheets/d/1Y4hpSyCz2s4xM1wzV7gRUjA_uVrbeoDML6_odknJxOc/edit#gid=0")
    litterCount = litterCount + 1 
    df = pd.DataFrame( [ litterType , litterCount ] ) 




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

data = pd.DataFrame(
    np.random.randn(20),
    columns=["Litter rate"]
)
st.subheader("Bar graph: ")
st.bar_chart(data=data, x=None, y=None, width=0, height=0, use_container_width=True)









