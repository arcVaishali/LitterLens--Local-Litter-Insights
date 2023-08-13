import time
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import urllib.request
from utils import *
import csv
import pandas as pd

def graph():
  count = []
  with open("database/litter_count.csv", mode='r') as file:
    litter_data = csv.reader(file)
    for lines in litter_data:
      count.append(lines[0])
  data = {'Litter':litter_type, 'Litter count':[int(i) for i in count]}
  df = pd.DataFrame(data)
  st.subheader("Live trash count graph:")
  st.bar_chart(df.set_index('Litter'))

def suggestions():
  count = []
  with open("database/litter_count.csv", mode='r') as file:
    litter_data = csv.reader(file)
    for lines in litter_data:
      count.append(lines[0])

  num = [int(i) for i in count]

  if max(num) == num[0]:
    st.warning("Cardboard waste is more")
  elif max(num) == num[1]:
    st.warning("Glass waste is more")
  elif max(num) == num[2]:
    st.warning("Metal waste is more")
  elif max(num) == num[3]:
    st.warning("Paper waste is more")
  elif max(num) == num[4]:
    st.warning("Plastic waste is more")
  elif max(num) == num[5]:
    st.warning("Trash waste is more")
  else:
    st.warning("nothing")

def show_insights():
  graph()
  suggestions()




litter_type = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
recylable = ['paper', 'cardboard', 'metal', 'plastic', 'glass']
biodegradable = ['trash']

def litter_count_update(litter):
  litter_type = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
  count = []

  with open("database/litter_count.csv", mode='r') as file:
    litter_data = csv.reader(file)
    for lines in litter_data:
      count.append(lines[0])

  litter_type_index = litter_type.index(litter)
  count[litter_type_index] = str(int(count[litter_type_index])+1)

  with open("database/litter_count.csv",'w', newline='') as file:
    writer = csv.writer(file)
    for i in count:
      writer.writerow([i])


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
        litter = labels[np.argmax(prediction[0], axis=-1)]
        st.info('Hey! The uploaded image has been classified as " {} waste " '.format(litter))   
        if litter in recylable:
          st.info("{} is RECYLABLE WASTE".format(litter))
        elif litter in biodegradable:
          st.info("{} is BIODEGRADABLE WASTE".format(litter))
        litter_count_update(litter)
except Exception as e:
  st.info("Our model will begin it's work once you feed it the input😁⬆️")
  pass

x = st.button("Get Insights", use_container_width=True)
if x:
  show_insights()

