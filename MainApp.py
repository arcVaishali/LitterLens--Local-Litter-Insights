import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected_sidebar = option_menu(
        menu_title = None,
        options=["Home page", "Upload Litter", "Retain Litter Info","Contact"],
        icons=["house","upload","info","envelope"],
        default_index=0,

    )

if selected_sidebar == "Home page":
    st.title("Litter free World")
elif selected_sidebar == "Upload Litter":
    st.title("Upload litter")
elif selected_sidebar == "Retain Litter Info":
    st.title("Retain Litter Info")