import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Login",
    page_icon=":raised_hand_with_fingers_splayed:",
)

components.html(
    """
    <script src="https://cdn.tailwindcss.com"></script>

    <div class="flex flex-col w-full">
      <h2 class="text-4xl dark:text-white text-black font-medium">Sign up for info</h2>
      <form method="post" id="sheetdb-form" action="https://sheetdb.io/api/v1/9j2teqwz3t3d9?sheet=login">
        <div class="my-4">
          <label class="block text-xl dark:text-white text-black font-bold mb-2" for="name">
            Name
          </label>
          <input
            class="h-14 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg"
            id="name"
            name="data[name]"
            type="text"
            required
          />
        </div>
        <div class="my-4">
          <label class="block text-xl dark:text-white text-black font-bold mb-2" for="location">
            Loacation
          </label>
          <input
            class="h-14 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg"
            id="location"
            name="data[loacation]"
            type="text"
            required
          />
        </div>
        <div class="my-4">
          <label class="block text-xl dark:text-white text-black font-bold mb-2" for="locality">
            Locality
          </label>
          <input
            class="h-14 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg"
            id="locality"
            name="data[locality]"
            type="text"
            required
          />
        </div>
        <button class="text-xl font-bold text-black p-4 bg-lime-400 rounded-full w-fit" type="submit">
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
    height=442,
)