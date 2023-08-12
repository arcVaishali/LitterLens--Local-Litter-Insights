import streamlit as st 

st.set_page_config(
    page_title="Home",
    page_icon=":house:",
)

st.title("Litter Insight and Segregation ")
st.divider()
st.markdown("#### About us")
st.markdown("#### Inspiration")
st.markdown("##### Case Study - 1 ")
st.markdown("We saw the success story of [KabadiWallah Connect](), a Chennai based startup, it provided an IoT based point of pickup i.e. an IoT based dustbin which monitored waste collection and notified nearby Kabadiwallahs when it required disposal. Enabling such a system organised the Recyclable Waste Collection in India which is an informal sector which lags structure and also reduced risks that Kabadiwallahs (level-0 waste picker are called so in India) used to take in their daily life to find and segregate waste, thereby improving their livelihoods.") 
st.divider()
st.markdown(">What if we could reduce the risks even more that the Kabadiwallahs take to segregating waste by diving knee deep into the waste?")
st.divider()

st.markdown("##### Case Study - 2 ")
st.markdown("[Literati]() is a Litter data collection and analysis app based in US. This app has been used by various lawmakers and school administrations in US to get insights on what type of waste are being mostly generated in their city and school campus respectively and how they can reduce it.")

st.title("A step towards :green[Litter free World]")
st.markdown("# What we aim for?")









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
   
   
