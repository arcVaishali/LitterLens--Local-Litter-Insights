import time
import streamlit as st
import numpy as np
from PIL import Image
import urllib.request
from utils import *

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
  st.info(e)
  pass





































# import streamlit as st 
# import pandas as pd
# import numpy as np
# from tensorflow import keras
# from keras.layers import Dense
# from keras.models import Sequential, load_model

# def submit(photoVar):
#     modelName = load_model('model.h5')
#     litterType = modelName.predict(photoVar)  
#     # litterType = "plastic straw" 
#     # fd = pd.read_csv("https://docs.google.com/spreadsheets/d/1Y4hpSyCz2s4xM1wzV7gRUjA_uVrbeoDML6_odknJxOc/edit#gid=0")
#     # litterCount = fd[["count"]]
#     # litterCount = litterCount + 1 
#     # df = pd.DataFrame( [ litterType , litterCount ] ) 
#     # df.to_csv( df , index = False ) 
#     pass

# st.set_page_config(
#     page_title="Upload and Read",
#     page_icon="🔍",
# )

# st.title(":blue[Upload] Litter Data and Read Litter Data") 

# col1, col2 = st.columns([1,1])
# with col1:
#     upload = st.button("Upload", use_container_width=True)
# with col2:
#     camera = st.button("Camera", use_container_width=True)

# # st.button("Submit", use_container_width=True)



# def photo():
#     key = True
#     if camera == True:
#         photoVar = st.camera_input("Take picture")
#         if photoVar is not None:
#             key = False
#         st.button("Submit", on_click=submit(), disabled=key, use_container_width=True)
#     else:
#         photoVar = st.file_uploader("Upload image")
#         if photoVar:
#             st.image(photoVar)
#         if photoVar is not None:
#             key = False
#         st.button("Submit", on_click=submit(photoVar), disabled=key, use_container_width=True)

# photo()

# # data = pd.DataFrame(
# #     np.random.randn(20),
# #     columns=["Litter rate"]
# # )
# # st.subheader("Bar graph: ")
# # st.bar_chart(data=data, x=None, y=None, width=0, height=0, use_container_width=True)









