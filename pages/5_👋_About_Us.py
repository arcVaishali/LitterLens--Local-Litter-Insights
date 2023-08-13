import streamlit as st 
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Contact",
    page_icon=":wave:",
)

add_logo("assests\logo.png", height=180)

components.html(
    """
    <script src="https://cdn.tailwindcss.com"></script>
      <h2 class="text-6xl dark:text-white text-black font-bold mb-12">About Us</h2>
      <div class="flex w-full flex-col items-center">
        <h1 class="text-5xl font-semibold underline underline-offset-8 mb-12 dark:text-white text-black decoration-neutral-500">The Team</h1>
        <div class="flex flex-row flex-wrap justify-center gap-8">
          <div class="bg-black text-white p-6 h-[40rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
            <img class="h-24 w-24 rounded-full mb-4"
              src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/Vaishali.png" alt="Vaishali">
            <h1 class="text-3xl text-center">Vaishali</h1>
            <p class="text-xl mb-3 ">Front-end developer and UX/UI developer</p>
            <p class="text-2xl">I am a B.Tech Computer Science 2nd year student at GL Bajaj,
              Greater Noida who loves to contribute in open source and as a Front-end and UX/UI Developer in
              Hackathons. Moreover I spends hours Leetcoding and learning Web Development, DSA, Blockchain and Machine Learning. I learn by doing.
              Eat, Code, Repeat.</p>

            <div class="flex flex-row gap-14 my-4">
              <a class="h-14 w-14" target="_blank" href="https://www.linkedin.com/in/vaishali-p-97326221b/">
                <img src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/linkedIn.png" alt="">
              </a>
              <a class="h-14 w-14" target="_blank" href="https://github.com/arcVaishali/">
                <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/github.png" alt="">
              </a>
            </div>
          </div>
          <div class="bg-black text-white p-6 h-[42rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
            <img class="h-24 w-24 rounded-full mb-4"
              src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/Kesav.jpeg"
              alt="Kesav">
            <h1 class="text-3xl text-center">Kesav Nagendra</h1>
            <p class="text-xl mb-3 ">Data Science & Machine Learning</p>
            <p class="text-2xl">Enthusiastic Electronic Engineer with knowledge and hands on
              experience in the electrical and electronic industry. My interests lie primarily in computational algorithms,
              robotics systems, and optimization. I am deeply inclined towards Computing, AI/ML/DL, Algorithm Design, IoT,
              Robotics, Embedded Systems, and System Design and applying them practically on hardware. I am always open to
              learning new concepts and networking.</p>

              <div class="flex flex-row gap-14 my-4">
              <a class="h-14 w-14" target="_blank" href="https://www.linkedin.com/in/kesav-nagendra-0185021b9/">
                <img src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/linkedIn.png" alt="">
              </a>
              <a class="h-14 w-14" target="_blank" href="https://github.com/kesavn-13/">
                <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/github.png" alt="">
              </a>
            </div>
          </div>
          <div class="bg-black text-white p-6 h-[32rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
            <img class="h-24 w-24 rounded-full mb-4"
              src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/Maruthi.png"
              alt="Maruthi">
            <h1 class="text-3xl text-center">Maruthi Karthik Singh</h1>
            <p class="text-xl mb-3 ">Web developer</p>
            <p class="text-2xl">I am a high school student who loves web development. I enjoy creating beautiful and functional websites using HTML, CSS, JavaScript, Vue, and other front-end technologies. I am also eager to learn more about backend development </p>

            <div class="flex flex-row gap-14 my-4">
              <a class="h-14 w-14" target="_blank" href="https://www.linkedin.com/in/maruthikarthiksingh/">
                <img src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/linkedIn.png" alt="">
              </a>
              <a class="h-14 w-14" target="_blank" href="https://github.com/MaruthiSingh/">
                <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/github.png" alt="">
              </a>
            </div>
          </div>
          <div class="bg-black text-white p-6 h-[42rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
            <img class="h-24 w-24 rounded-full mb-4"
              src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/Dileep.jpeg"
              alt="Dileep K">
            <h1 class="text-3xl text-center">Dileep K A</h1>
            <p class="text-xl mb-3 ">Web developer</p>
            <p class="text-2xl">I am a B.Tech Electrical & Computer Engineering student at
              Amrita University, driven by an insatiable fascination for the realm of Computer Science and its revolutionary
              impacts. My journey involves immersing myself in the intricacies of coding, algorithms, and the forefront of
              technological advancements. I am open to continuous learning and dedicated to reshaping the future through the
              art of code and creative problem-solving.</p>

            <div class="flex flex-row gap-14 my-4">
              <a class="h-14 w-14" target="_blank" href="https://www.linkedin.com/in/dileep-ka/">
                <img src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/linkedIn.png" alt="">
              </a>
              <a class="h-14 w-14" target="_blank" href="https://github.com/Dileep2608">
                <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/LitterLens--Local-Litter-Insights/master/assests/github.png" alt="">
              </a>
            </div>  
          </div>
        </div>

        <hr class="my-8 w-full h-1 bg-black dark:bg-white">
          <h1 class="text-5xl font-semibold underline underline-offset-8 mb-12 dark:text-white text-black text-center decoration-neutral-500">Tech Stack</h1>
          <div class="rounded-lg flex flex-row p-2 flex-wrap gap-14 w-full items-center justify-center">
            <div class="flex flex-col items-center">
              <a href="https://streamlit.io/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg py-3 px-6">
                  <img class=" h-12 w-14" src="https://avatars.githubusercontent.com/u/45109972?s=200&v=4" alt="">
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">Streamlit</h1>
              </a>
            </div>
            <div class="flex flex-col items-center">
              <a href="https://pandas.pydata.org/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg py-3 px-6">  
                  <img class="bg-[#130654] h-12 w-18" src="https://pandas.pydata.org/static/img/pandas_white.svg" alt="">
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">Pandas</h1>
              </a>
            </div>
            <div class="flex flex-col items-center">
              <a href="https://www.tensorflow.org/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg p-2">
                  <img class="h-12 w-18"
                    src="https://www.gstatic.com/devrel-devsite/prod/ve7ce216351f398481fccad3cbbc60c699e78bde8533bfe4daa150955665bb2bf/tensorflow/images/lockup.svg"
                    alt="">
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">Tensorflow</h1>
              </a>
            </div>
            <div class="flex flex-col items-center">
              <a href="https://matplotlib.org/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg p-2">
                  <img class="h-12 w-18" src="https://matplotlib.org/_static/logo_dark.svg" alt="">
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">Matplotlib</h1>
              </a>
            </div>
            <div class="flex flex-col items-center">
              <a href="https://numpy.org/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg p-2">
                  <img class="h-12 w-12" src="https://numpy.org/images/logo.svg" alt="">
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">Numpy</h1>
              </a>
            </div>
            <div class="flex flex-col items-center">
              <div class="dark:bg-white bg-slate-400 rounded-lg p-2">
                <img class="h-20 w-20" src="https://static.javatpoint.com/images/javascript/javascript_logo.png" alt="">
              </div>
              <h1 class="text-2xl dark:text-white text-black text-center my-4">JavaScript</h1>
            </div>
            <div class="flex flex-col items-center">
              <a href="https://tailwindcss.com/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg p-2">
                  <svg viewBox="0 0 248 31" class="dark:text-slate-900 text-white w-auto h-5">
                    <path fill-rule="evenodd" clip-rule="evenodd"
                      d="M25.517 0C18.712 0 14.46 3.382 12.758 10.146c2.552-3.382 5.529-4.65 8.931-3.805 1.941.482 3.329 1.882 4.864 3.432 2.502 2.524 5.398 5.445 11.722 5.445 6.804 0 11.057-3.382 12.758-10.145-2.551 3.382-5.528 4.65-8.93 3.804-1.942-.482-3.33-1.882-4.865-3.431C34.736 2.92 31.841 0 25.517 0zM12.758 15.218C5.954 15.218 1.701 18.6 0 25.364c2.552-3.382 5.529-4.65 8.93-3.805 1.942.482 3.33 1.882 4.865 3.432 2.502 2.524 5.397 5.445 11.722 5.445 6.804 0 11.057-3.381 12.758-10.145-2.552 3.382-5.529 4.65-8.931 3.805-1.941-.483-3.329-1.883-4.864-3.432-2.502-2.524-5.398-5.446-11.722-5.446z"
                      fill="#38bdf8"></path>
                    <path fill-rule="evenodd" clip-rule="evenodd"
                      d="M76.546 12.825h-4.453v8.567c0 2.285 1.508 2.249 4.453 2.106v3.463c-5.962.714-8.332-.928-8.332-5.569v-8.567H64.91V9.112h3.304V4.318l3.879-1.143v5.937h4.453v3.713zM93.52 9.112h3.878v17.849h-3.878v-2.57c-1.365 1.891-3.484 3.034-6.285 3.034-4.884 0-8.942-4.105-8.942-9.389 0-5.318 4.058-9.388 8.942-9.388 2.801 0 4.92 1.142 6.285 2.999V9.112zm-5.674 14.636c3.232 0 5.674-2.392 5.674-5.712s-2.442-5.711-5.674-5.711-5.674 2.392-5.674 5.711c0 3.32 2.442 5.712 5.674 5.712zm16.016-17.313c-1.364 0-2.477-1.142-2.477-2.463a2.475 2.475 0 012.477-2.463 2.475 2.475 0 012.478 2.463c0 1.32-1.113 2.463-2.478 2.463zm-1.939 20.526V9.112h3.879v17.849h-3.879zm8.368 0V.9h3.878v26.06h-3.878zm29.053-17.849h4.094l-5.638 17.849h-3.807l-3.735-12.03-3.771 12.03h-3.806l-5.639-17.849h4.094l3.484 12.315 3.771-12.315h3.699l3.734 12.315 3.52-12.315zm8.906-2.677c-1.365 0-2.478-1.142-2.478-2.463a2.475 2.475 0 012.478-2.463 2.475 2.475 0 012.478 2.463c0 1.32-1.113 2.463-2.478 2.463zm-1.939 20.526V9.112h3.878v17.849h-3.878zm17.812-18.313c4.022 0 6.895 2.713 6.895 7.354V26.96h-3.878V16.394c0-2.713-1.58-4.14-4.022-4.14-2.55 0-4.561 1.499-4.561 5.14v9.567h-3.879V9.112h3.879v2.285c1.185-1.856 3.124-2.749 5.566-2.749zm25.282-6.675h3.879V26.96h-3.879v-2.57c-1.364 1.892-3.483 3.034-6.284 3.034-4.884 0-8.942-4.105-8.942-9.389 0-5.318 4.058-9.388 8.942-9.388 2.801 0 4.92 1.142 6.284 2.999V1.973zm-5.674 21.775c3.232 0 5.674-2.392 5.674-5.712s-2.442-5.711-5.674-5.711-5.674 2.392-5.674 5.711c0 3.32 2.442 5.712 5.674 5.712zm22.553 3.677c-5.423 0-9.481-4.105-9.481-9.389 0-5.318 4.058-9.388 9.481-9.388 3.519 0 6.572 1.82 8.008 4.605l-3.34 1.928c-.79-1.678-2.549-2.749-4.704-2.749-3.16 0-5.566 2.392-5.566 5.604 0 3.213 2.406 5.605 5.566 5.605 2.155 0 3.914-1.107 4.776-2.749l3.34 1.892c-1.508 2.82-4.561 4.64-8.08 4.64zm14.472-13.387c0 3.249 9.661 1.285 9.661 7.89 0 3.57-3.125 5.497-7.003 5.497-3.591 0-6.177-1.607-7.326-4.177l3.34-1.927c.574 1.606 2.011 2.57 3.986 2.57 1.724 0 3.052-.571 3.052-2 0-3.176-9.66-1.391-9.66-7.781 0-3.356 2.909-5.462 6.572-5.462 2.945 0 5.387 1.357 6.644 3.713l-3.268 1.82c-.647-1.392-1.904-2.035-3.376-2.035-1.401 0-2.622.607-2.622 1.892zm16.556 0c0 3.249 9.66 1.285 9.66 7.89 0 3.57-3.124 5.497-7.003 5.497-3.591 0-6.176-1.607-7.326-4.177l3.34-1.927c.575 1.606 2.011 2.57 3.986 2.57 1.724 0 3.053-.571 3.053-2 0-3.176-9.66-1.391-9.66-7.781 0-3.356 2.908-5.462 6.572-5.462 2.944 0 5.386 1.357 6.643 3.713l-3.268 1.82c-.646-1.392-1.903-2.035-3.375-2.035-1.401 0-2.622.607-2.622 1.892z"
                      fill="currentColor"></path>
                  </svg>
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">Tailwind CSS</h1>
              </a>
            </div>
            <div class="flex flex-col items-center">
              <a href="https://sheetdb.io/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg py-3 px-6"> 
                  <img class="h-16 w-16 rounded-lg" src="https://avatars.githubusercontent.com/u/32489070?v=4" alt="">
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">SheetDB</h1>
              </a>
            </div>
            <div class="flex flex-col items-center">
              <a href="https://pytorch.org/" target="_blank">
                <div class="dark:bg-white bg-slate-400 rounded-lg py-3 px-6"> 
                  <img class="h-16 w-16 rounded-lg" src="https://pytorch.org/assets/images/logo-icon.svg" alt="">
                </div>
                <h1 class="text-2xl dark:text-white text-black text-center my-4">Pytorch</h1>
              </a>
            </div>
          </div>
    </div>

    """,
    height=3515,
)