import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected_sidebar = option_menu(
        menu_title = None,
        options=["Home page", "Upload Litter", "Waste Segregation Tool","Contact"],
        icons=["house","upload","info","envelope"],
        default_index=0,

    )

if selected_sidebar == "Home page":
    st.title("Litter free World")
elif selected_sidebar == "Upload Litter and Get Insights ":
    st.title("Upload Litter Data and Read Litter Data")
elif selected_sidebar == "Waste Segregation Tool":
    st.title("Upload image of Litter our model will predict its ")
    st.markdown("- Name ")
    st.markdown("- Type ")
    st.markdown("- other data ") 
   
   
