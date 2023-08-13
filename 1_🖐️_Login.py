import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Login",
    page_icon=":raised_hand_with_fingers_splayed:",
)

add_logo("assests\logo.png", height=180)

components.html(
    """
    <script src="https://cdn.tailwindcss.com"></script>

    <div class="flex flex-col w-full">
      <h2 class="text-6xl dark:text-white text-black font-medium mb-5">Sign up for info</h2>
      <form method="post" id="sheetdb-form" action="https://sheetdb.io/api/v1/9j2teqwz3t3d9?sheet=login">
        <div class="my-4">
            <h2 class="text-xl font-bold mb-2 dark:text-white text-black">Name</h2>
            <input required type="text" class="h-14 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg" name="data[name]">
        </div>
        <div class="my-4">
            <h2 class="text-xl font-bold mb-2 dark:text-white text-black">Location</h2>
            <select name="data[location]" class="h-18 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-5 rounded-lg">
                <option value="Delhi">Delhi</option>
                <option value="Bangalore">Bangalore</option>
                <option value="Chennai">Chennai</option>
                <option value="Hyderabad">Hyderabad</option>
            </select>
        </div>
        <div class="my-4">
            <h2 class="text-xl font-bold mb-2 dark:text-white text-black">Locality</h2>
            <input required type="text" class="h-14 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg" name="data[locality]">
        </div>
        <button class="text-xl mt-4 font-bold text-black p-4 bg-lime-400 rounded-full w-fit" type="submit">
          Submit
        </button>
      </form>
    </div>
    <script>
        var form = document.getElementById('sheetdb-form');
        form.addEventListener("submit", e => {
            e.preventDefault();
            fetch(form.action, {
                method : "POST",
                body: new FormData(document.getElementById("sheetdb-form")),
            }).then(
                response => response.json()
            ).then((html) => {
            alert('Successfully submited uploaded')
            });
        });
    </script>
    """,
    height=520,
)