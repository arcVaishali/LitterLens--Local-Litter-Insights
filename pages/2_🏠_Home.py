import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Home",
    page_icon=":house:",
)

st.title(
    "Litter Insight and Segregation- A step towards :green[Litter free World]")

st.divider()


# =======ABOUT=======
st.header("About us")

st.markdown("Our project :green[Litter Insight and Segregation], as the name suggests aims to provide a **local litter dataset** to local administration and policy makers of Resident Welfare Societies and Colonies, based on which they can make policies to :green[make reasonable and achievable local changes in lifestyle of residents]. We believe waste collection and management systems should be decentralised, as it is then the waste management becomes sustainable, reduces carbon footprint for transportation and gives local authorities more control.")

st.markdown(" ")
# We can add images here

st.markdown("In addition to contributing in creating a dataset and making analysis, our project also aims to make lives of Level 0 Waster Pickers (called Kabadiwallahs in India) less riskier, simple and make their livelihoods better by creating a ML model that classifies waste into recyclable and non-recylable litter by feeding it image of waste. This ML model when powered by an IoT based dustbin can help segregation of waste even faster and easier")
# We can add images here


# =========FEATURES========
st.header("Features")
st.markdown("- Provides portal for Litter Image Uploading and Analysis")
st.markdown("- It aims at providing relevant results")
st.markdown("- Helps segregating wastes less riskier")

# We can add images here


# =========INSPIRATION========
st.header("Inspiration")

st.subheader("Case Study - 1 ")

st.markdown("We saw the success story of [KabadiWallah Connect](https://www.kabadiwallaconnect.in/), a Chennai based startup, it provided an IoT based point of pickup i.e. an IoT based dustbin which monitored waste collection and notified nearby Kabadiwallahs when it required disposal. Enabling such a system organised the Recyclable Waste Collection in India which is an informal sector which lags structure and also reduced risks that Kabadiwallahs (level-0 waste picker are called so in India) used to take in their daily life to find and segregate waste, thereby improving their livelihoods.")

st.markdown(
    "**Report by** [ITU Hub](https://www.itu.int/hub/2021/07/indian-firms-digital-solution-for-urban-waste-pickers/)")

st.divider()

st.header("Our Remarks")

st.markdown(">What if we could reduce the risks even more that the Kabadiwallahs take to segregating waste by diving knee deep into the waste?")

st.markdown(">Why not create an ML model that can segregate waste into as recyclable and non-recyclable based on data provided by IoT enabled dustbins (an image sensor will capture image of waste at the type of disposal)?")

st.divider()

st.subheader("Case Study - 2 ")

st.markdown("[Litterati](https://www.litterati.org/) is a Litter data collection and analysis app based in US. This app has been used by various lawmakers and school administrations in US to get insights on what type of waste are being mostly generated in their city and school campus respectively and how they can reduce it.")

st.markdown(
    "**Report by Science Learn Hub** [Citizen Science Project-Litterati](https://www.sciencelearn.org.nz/resources/2752-litterati)")

st.header("Our Remarks")

st.markdown(
    ">As claimed earlier, waste management systems must be decentralised and locale specific.")

st.markdown(
    ">Hence, to enable this why not make it local and available in India?")

st.divider()


# ========OUTCOME==========
st.header("Outcome")
st.markdown("Our project aims at helping people make data informed life choices that are sustainable and also simplifies life of level 0 waste pickers")


# from streamlit_option_menu import option_menu


# with st.sidebar:
#     selected_sidebar = option_menu(
#         menu_title = None,
#         options=["Home page", "Upload Litter, Get Insights", "Waste Segregation Tool","Contact"],
#         icons=["house","upload","info","envelope"],
#         default_index=0,

#     )

# if selected_sidebar == "Home page":
#     st.title("Litter free World")
# elif selected_sidebar == "Upload Litter, Get Insights":
#     st.title("Upload Litter Data and Read Litter Data")
# elif selected_sidebar == "Waste Segregation Tool":
#     st.title("Upload image of Litter our model will predict its ")
#     st.markdown("- Name ")
#     st.markdown("- Type ")
#     st.markdown("- other data ")
