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
      <h2 class="text-3xl dark:text-white text-black font-medium">Sign up for info</h2>
      <form method="post" id="sheetdb-form" action="https://sheetdb.io/api/v1/9j2teqwz3t3d9?sheet=login">
        <div class="my-4">
          <label class="block text-xl dark:text-white text-black font-medium mb-4" for="name">
            Name
          </label>
          <input
            class="border border-gray-400 p-2 w-full rounded-lg"
            id="name"
            name="data[name]"
            placeholder="*Enter Your Name*"
            type="text"
            required
          />
        </div>
        <div class="my-4">
          <label class="block text-xl dark:text-white text-black p-2 font-medium mb-4" for="location">
            Loacation
          </label>
          <input
            class="border border-gray-400 p-2 w-full rounded-lg"
            id="location"
            name="data[loacation]"
            placeholder="*Enter Your Location*"
            type="text"
            required
          />
        </div>
        <div class="my-4">
          <label class="block text-xl dark:text-white text-black p-2 font-medium mb-4" for="locality">
            Locality
          </label>
          <input
            class="border border-gray-400 p-2 mb-4 w-full rounded-lg"
            id="locality"
            name="data[locality]"
            placeholder="*Enter Your Locality*"
            type="text"
            required
          />
        </div>
        <button class="text-xl font-bold text-black p-3 bg-lime-400 rounded-full w-fit" type="submit">
          Submit
        </button>
      </form>
    </div>
    <script>
        
    </script>
    """,
    height=458,
)