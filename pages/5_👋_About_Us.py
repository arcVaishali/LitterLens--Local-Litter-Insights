import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contact",
    page_icon=":wave:",
)

st.title("About Us")

components.html(
    """
    <script src="https://cdn.tailwindcss.com"></script>
    <div class="flex w-full flex-col items-center">
      <h1 class="text-5xl font-semibold underline underline-offset-8 mb-12 dark:text-white text-black decoration-neutral-500">The Team</h1>
      <div class="flex flex-row flex-wrap justify-center gap-8">
        <div class="bg-white dark:bg-black p-6 h-[40rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
          <img class="h-24 w-24 rounded-full mb-4"
            src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/Vaishali.png?token=GHSAT0AAAAAAB66LMHJTZUNFI3YNYQFUGAGZGXXAEQ" alt="Vaishali">
          <h1 class="text-3xl text-center dark:text-white text-black">Vaishali</h1>
          <p class="text-xl mb-3 text-black dark:text-white">Front-end developer and UX/UI developer</p>
          <p class="text-2xl text-black dark:text-white">I am a B.Tech Computer Science 2nd year student at GL Bajaj,
            Greater Noida contributing in open source, contributing as a front-end developer and UX/UI developer in
            hackathons, Leetcoding and learning web development, DSA, Blockchain and Machine Learning. I learn by doing.
            Eat, Code, Repeat.</p>

          <div class="flex flex-row gap-14 my-4">
            <a class="h-14 w-14" href="https://www.linkedin.com/in/vaishali-p-97326221b/">
              <img src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/linkedIn.png?token=GHSAT0AAAAAAB66LMHIQHEW3YEL5PLHP2EGZGXXJ2Q" alt="">
            </a>
            <a class="h-14 w-14" href="https://github.com/arcVaishali/">
              <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/github.png?token=GHSAT0AAAAAAB66LMHI4CHTGE4N5PFYAAV2ZGXXKVQ" alt="">
            </a>
          </div>
        </div>
        <div class="bg-white dark:bg-black p-6 h-[42rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
          <img class="h-24 w-24 rounded-full mb-4"
            src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/Kesav.jpg?token=GHSAT0AAAAAAB66LMHI5FU7XMVWBIJQW2YAZGXW76Q"
            alt="Kesav">
          <h1 class="text-3xl text-center dark:text-white text-black">Kesav Nagendra</h1>
          <p class="text-xl mb-3 text-black dark:text-white">Data Science & Machine Learning</p>
          <p class="text-2xl text-black dark:text-white">Enthusiastic Electronic Engineer with knowledge and hands on
            experience in the electrical and electronic industry. My interests lie primarily in computational algorithms,
            robotics systems, and optimization. I am deeply inclined towards Computing, AI/ML/DL, Algorithm Design, IoT,
            Robotics, Embedded Systems, and System Design and applying them practically on hardware. I am always open to
            learning new concepts and networking.</p>

            <div class="flex flex-row gap-14 my-4">
            <a class="h-14 w-14" href="https://www.linkedin.com/in/kesav-nagendra-0185021b9/">
              <img src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/linkedIn.png?token=GHSAT0AAAAAAB66LMHIQHEW3YEL5PLHP2EGZGXXJ2Q" alt="">
            </a>
            <a class="h-14 w-14" href="https://github.com/kesavn-13/">
              <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/github.png?token=GHSAT0AAAAAAB66LMHI4CHTGE4N5PFYAAV2ZGXXKVQ" alt="">
            </a>
          </div>
        </div>
        <div class="bg-white dark:bg-black p-6 h-[32rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
          <img class="h-24 w-24 rounded-full mb-4"
            src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/Maruthi.png?token=GHSAT0AAAAAAB66LMHJKHQ4HXRFEZRLVN5OZGXXASA"
            alt="Maruthi">
          <h1 class="text-3xl text-center dark:text-white text-black">Maruthi Karthik Singh</h1>
          <p class="text-xl mb-3 text-black dark:text-white">Web developer</p>
          <p class="text-2xl text-black dark:text-white">I am a high school student who loves web development. I enjoy creating beautiful and functional websites using HTML, CSS, JavaScript, Vue, and other front-end technologies. I am also eager to learn more about backend development </p>

          <div class="flex flex-row gap-14 my-4">
            <a class="h-14 w-14" href="https://www.linkedin.com/in/maruthikarthiksingh/">
              <img src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/linkedIn.png?token=GHSAT0AAAAAAB66LMHIQHEW3YEL5PLHP2EGZGXXJ2Q" alt="">
            </a>
            <a class="h-14 w-14" href="https://github.com/MaruthiSingh/">
              <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/github.png?token=GHSAT0AAAAAAB66LMHI4CHTGE4N5PFYAAV2ZGXXKVQ" alt="">
            </a>
          </div>
        </div>
        <div class="bg-white dark:bg-black p-6 h-[42rem] w-[32rem] rounded-lg flex flex-col items-center justify-around">
          <img class="h-24 w-24 rounded-full mb-4"
            src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/Dileep.jpeg?token=GHSAT0AAAAAAB66LMHJXCR4CBPPOQIQ5VGCZGXWZGQ"
            alt="Dileep K">
          <h1 class="text-3xl text-center dark:text-white text-black">Dileep K</h1>
          <p class="text-xl mb-3 text-black dark:text-white">Web developer</p>
          <p class="text-2xl text-black dark:text-white">I am a B.Tech Electrical & Computer Engineering student at
            Amrita University, driven by an insatiable fascination for the realm of Computer Science and its revolutionary
            impacts. My journey involves immersing myself in the intricacies of coding, algorithms, and the forefront of
            technological advancements. I am open to continuous learning and dedicated to reshaping the future through the
            art of code and creative problem-solving.</p>

          <div class="flex flex-row gap-14 my-4">
            <a class="h-14 w-14" href="https://www.linkedin.com/in/dileep-ka/">
              <img src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/linkedIn.png?token=GHSAT0AAAAAAB66LMHIQHEW3YEL5PLHP2EGZGXXJ2Q" alt="">
            </a>
            <a class="h-14 w-14" href="https://github.com/Dileep2608">
              <img class="dark:bg-white bg-black rounded-full" src="https://raw.githubusercontent.com/arcVaishali/Litter-Insight-and-Segregation/master/assests/github.png?token=GHSAT0AAAAAAB66LMHI4CHTGE4N5PFYAAV2ZGXXKVQ" alt="">
            </a>
          </div>  
        </div>
      </div>


    """,
    height=2690,
)