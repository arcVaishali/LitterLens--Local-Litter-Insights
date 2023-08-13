import time
import streamlit as st
import numpy as np
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image
import urllib.request
from utils import *

st.set_page_config(
     page_title="Upload and Read",
     page_icon="🔍",
)

# sheet_id = '1Y4hpSyCz2s4xM1wzV7gRUjA_uVrbeoDML6_odknJxOc'
# df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
# print(df)

labels = gen_labels()

html_temp = '''
    <div style =  padding-bottom: 20px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
    <center><h1>Garbage Segregation</h1></center>
    
    </div>
    '''

st.markdown(html_temp, unsafe_allow_html=True)
html_temp = '''
    <div>
    <h2></h2>
    <center><h3>Please upload Waste Image to find its Category</h3></center>
    </div>
    '''
st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown(html_temp, unsafe_allow_html=True)
opt = st.selectbox("How do you want to upload the image for classification?\n", ('Please Select', 'Upload image via link', 'Upload image from device'))
if opt == 'Upload image from device':
    file = st.file_uploader('Select', type = ['jpg', 'png', 'jpeg'])
    st.set_option('deprecation.showfileUploaderEncoding', False)
    if file is not None:
        image = Image.open(file)

elif opt == 'Upload image via link':

  try:
    img = st.text_input('Enter the Image Address')
    image = Image.open(urllib.request.urlopen(img))
    
  except:
    if st.button('Submit'):
      show = st.error("Please Enter a valid Image Address!")
      time.sleep(4)
      show.empty()

try:
  if image is not None:
    st.image(image, width = 300, caption = 'Uploaded Image')
    if st.button('Predict'):
        img = preprocess(image)

        model = model_arc()
        model.load_weights("model.h5")

        prediction = model.predict(img[np.newaxis, ...])
        st.info('Hey! The uploaded image has been classified as " {} waste " '.format(labels[np.argmax(prediction[0], axis=-1)]))     
except Exception as e:
  st.info("Our model will begin it's work once you feed it the input😁⬆️")
  pass



st.markdown("### For Your Reference")
dic = {"Recylable":["paper","cardboard","metal","plastic","glass"],"Biodegradable":["trash"," " , " " , " ", " "]}
df = pd.DataFrame(dic)
st.write(df)



