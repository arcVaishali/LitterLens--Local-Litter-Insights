import time
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import urllib.request
from utils import *
import csv
import pandas as pd
import requests
from streamlit_extras.app_logo import add_logo

st.set_page_config(
     page_title="Upload and Read",
     page_icon="🔍",
)

add_logo("assests\logo.png", height=180)

url = "https://sheetdb.io/api/v1/9j2teqwz3t3d9?sheet=login"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    city = data[-1]["location"]
else:
    print("Failed to retrieve data from database. Status code:", response.status_code)

plastice = """Controlling plastic waste is a critical environmental challenge. There are several measures that can be taken to address and control plastic waste:

1. REDUCE SINGLE-USE PLASTICS: Encourage the use of reusable alternatives and phase out or ban certain single-use plastic items like bags, straws, cutlery, and packaging.

2. PROMATE RECYCLING: Implement effective recycling programs and raise awareness about proper sorting and disposal of plastics. Improve infrastructure to ensure that collected plastic waste is actually recycled.

3. EXTENDED PRODUCER RESPONSIBILITY (EPR): Hold manufacturers responsible for the entire lifecycle of their products, including plastic waste management and disposal. This encourages them to design products with recycling and end-of-life considerations in mind.

4. PLASTIC-FREE PACKAGING: Encourage businesses to adopt plastic-free packaging alternatives or use materials that are more easily recyclable or biodegradable.

5. INNOVATIVE MATERIALS: Support research and development of alternative materials to plastic, such as bioplastics, which are made from renewable resources and are more environmentally friendly."""

cardboard = """Controlling cardboard waste involves implementing effective strategies to reduce, reuse, and recycle cardboard materials. Here are measures you can take to control cardboard waste:

1. SOURCE REDUCTION:
Encourage businesses to minimize packaging and use appropriate box sizes to reduce excess cardboard waste.
Implement a "just-in-time" inventory system to prevent overordering and excess packaging.

2. REUSE AND REPURPOSE:
Promote the reuse of cardboard boxes for storage, shipping, or moving purposes.
Establish a community-based cardboard box exchange program for sharing boxes.

3. RECYCLING PROGRMAS:
Set up convenient and accessible cardboard recycling collection points in residential areas and commercial spaces.
Educate residents and businesses about proper cardboard recycling procedures and the importance of flattening boxes before recycling.

4. COMMERCIAL AND INDUSTRIAL PRACTICES:
Encourage businesses to partner with recycling companies to ensure their cardboard waste is properly managed and recycled.
Implement cardboard waste audits to identify areas for reduction and better recycling practices.

5. PRODUCT DESIGN AND PACKAGING GAUIDELINES:
Work with manufacturers to design products with more eco-friendly packaging that uses less cardboard or easily recyclable materials. """

glass = """ Controlling glass waste involves implementing strategies to reduce, reuse, and recycle glass materials. Here are measures you can take to control glass waste:

1. Source Reduction:
Encourage businesses to reduce the use of glass packaging by exploring alternatives like plastic, paper, or metal.
Promote bulk purchasing to minimize single-use glass containers.

2. Reuse and Repurpose:
Establish bottle return or deposit systems to encourage the return of glass beverage containers for cleaning and reuse.
Encourage the reuse of glass jars and bottles for storage, crafts, or DIY projects.

3. Recycling Programs:
Set up accessible glass recycling collection points in residential areas, public spaces, and businesses.
Educate the public about the benefits of glass recycling and proper methods for separating and preparing glass for recycling.

4. Glass-to-Glass Recycling:
Advocate for a closed-loop recycling system where collected glass is processed into new glass products, reducing the need for raw materials.

5. Glass Packaging Design:
Work with manufacturers to design glass packaging that is lighter, more easily recyclable, or has a higher percentage of recycled content.
"""

metal = """
Controlling metal waste involves implementing strategies to reduce, reuse, and recycle metal materials. Here are measures you can take to control metal waste:

1. Source Reduction:
Encourage businesses to minimize metal packaging and explore alternatives like eco-friendly materials.
Promote bulk purchasing to reduce single-use metal containers.

2. Reuse and Repurpose:
Establish metal recycling collection points for scrap metal, encouraging individuals and businesses to bring in old or unused metal items.
Promote the reuse of metal items by encouraging repair and refurbishment.

3. Recycling Programs:
Set up accessible metal recycling collection points in residential areas, public spaces, and businesses.
Educate the public about the importance of metal recycling and proper methods for preparing and disposing of metal waste.

4. Scrap Metal Industry:
Foster partnerships with local scrap yards and recycling centers to ensure efficient and environmentally responsible metal recycling.

5. Metal-to-Metal Recycling:
Promote closed-loop recycling where collected metal is processed into new metal products, reducing the need for virgin resources. """

paper = """Controlling paper waste is essential for sustainable resource management. Here are measures you can take to effectively control paper waste:

1. Promote Digitalization:
Encourage businesses and individuals to transition to digital documents and communications whenever possible.
Use electronic signatures and online forms to reduce paper consumption.

2. Print Mindfully:
Encourage double-sided printing to reduce paper usage.
Set default printer settings to black and white and draft mode for internal documents.

3. Paperless Billing and Statements:
Advocate for paperless billing options with utility companies and financial institutions.
Encourage people to opt for electronic statements and invoices.

4. Reuse and Recycle:
Promote the reuse of paper for note-taking, scrap paper, or packaging material.
Establish accessible recycling programs to ensure proper disposal of used paper.

5. Sustainable Paper Procurement:
Encourage businesses to source paper products from sustainably managed forests or consider recycled content.
Support the use of certified paper (e.g., FSC or PEFC) to ensure responsible forest management."""

trash = """Controlling trash waste is essential for managing environmental impact and resource consumption. Here are measures you can take to effectively control trash waste:

1. Source Reduction:
Promote buying products with minimal packaging to reduce waste generation.
Encourage businesses to implement bulk purchasing and avoid over-packaging.

2. Waste Segregation:
Educate the public about proper waste segregation for recycling, composting, and landfill-bound items.
Provide clear and accessible bins for different waste streams.

3. Composting Programs:
Establish or support community composting programs for organic waste like food scraps and yard trimmings.
Encourage backyard composting for households with garden spaces.

4. Reduce Single-Use Items:
Advocate for the reduction of single-use plastics, utensils, and packaging.
Promote the use of reusable alternatives in daily life.

5. Recycling Initiatives:
Collaborate with local recycling centers to ensure proper collection, processing, and recycling of materials.
Educate residents about acceptable recycling materials and practices."""

litter_type = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
recylable = ['paper', 'cardboard', 'metal', 'plastic', 'glass']
biodegradable = ['trash']
cities = ['Delhi', 'Bangalore', 'Chennai', 'Hyderabad', 'Mumbai']
file_name = "database/{}.csv".format(city)

def graph():
  count = []
  with open(file_name, mode='r') as file:
    litter_data = csv.reader(file)
    for lines in litter_data:
      count.append(lines[0])
  data = {'Litter':litter_type, 'Litter count':[int(i) for i in count]}
  df = pd.DataFrame(data)
  st.subheader("Live trash count graph:")
  st.bar_chart(df.set_index('Litter'))

def suggestions():
  count = []
  with open(file_name, mode='r') as file:
    litter_data = csv.reader(file)
    for lines in litter_data:
      count.append(lines[0])

  num = [int(i) for i in count]

  if max(num) == num[0]:
    st.warning("Cardboard waste is more in {}".format(city))
    st.warning(cardboard)
  elif max(num) == num[1]:
    st.warning("Glass waste is more in {}".format(city))
    st.warning(glass)
  elif max(num) == num[2]:
    st.warning("Metal waste is more in {}".format(city))
    st.warning(metal)
  elif max(num) == num[3]:
    st.warning("Paper waste is more in {}".format(city))
    st.warning(paper)
  elif max(num) == num[4]:
    st.warning("Plastic waste is more in {}".format(city))
    st.warning(plastice)
  elif max(num) == num[5]:
    st.warning("Trash waste is more in {}".format(city))
    st.warning(trash)

def show_insights():
  graph()
  suggestions()

def litter_count_update(litter):
  litter_type = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
  count = []

  with open(file_name, mode='r') as file:
    litter_data = csv.reader(file)
    for lines in litter_data:
      count.append(lines[0])

  litter_type_index = litter_type.index(litter)
  count[litter_type_index] = str(int(count[litter_type_index])+1)

  with open(file_name,'w', newline='') as file:
    writer = csv.writer(file)
    for i in count:
      writer.writerow([i])


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

button_text = "Get insights of {} litter distrubition".format(city)
x = st.button(button_text, use_container_width=True)
if x:
  show_insights()