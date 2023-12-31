import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contact",
    page_icon=":envelope_with_arrow:",
)


components.html(
    """
    <script src="https://cdn.tailwindcss.com"></script>
    <h2 class="lg:text-6xl md:text-3xl sm:text-2xl dark:text-white text-black font-medium mb-5">Contact</h2>
    <form class="flex flex-col" method="post" id="sheetdb-form" action="https://sheetdb.io/api/v1/9j2teqwz3t3d9?sheet=contact">
        <div class="my-4">
            <h2 class="text-xl font-bold mb-2 dark:text-white text-black">Name</h2>
            <input required type="text" class="h-14 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg" name="data[name]">
        </div>
        <div class="my-4">
            <h2 class="text-xl font-bold mb-2 dark:text-white text-black">Email</h2>
            <input required type="email" class="h-14 w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg" name="data[email]">
        </div>
        <div class="my-4">
            <h2 class="text-xl font-bold mb-2 dark:text-white text-black">Issue</h2>
            <textarea required class="w-full text-white bg-black dark:border-white border-slate-500 border-4 focus:outline-none p-4 rounded-lg" name="data[issue]" cols="30" rows="10"></textarea>
        </div>
        <button class="text-xl mb-4 font-bold text-black p-4 bg-lime-400 rounded-full w-fit" type="submit">Submit</button>
    </form>
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
            alert('Successfully submited to the developer team')
            });
        });
    </script>       
    """,
    height=764,
)