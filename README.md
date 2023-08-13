# LitterLens- Local Litter Insights

## About us
Our project Litter Insight and Segregation, as the name suggests aims to provide a local litter dataset to local administration and policy makers of Resident Welfare Societies and Colonies, based on which they can make policies to make reasonable and achievable local changes in lifestyle of residents. We believe waste collection and management systems should be decentralised, as it is then the waste management becomes sustainable, reduces carbon footprint for transportation and gives local authorities more control.

In addition to contributing in creating a dataset and making analysis, our project also aims to make lives of Level 0 Waster Pickers (called Kabadiwallahs in India) less riskier, simple and make their livelihoods better by creating a ML model that classifies waste into recyclable and non-recylable litter by feeding it image of waste. This ML model when powered by an IoT based dustbin can help segregation of waste even faster and easier. Even local people can use this website to segregate waste into recyclable and non-recyclable waste bins.

## Features
- Provides portal for Litter Image Uploading and Analysis for litter distribution in their locality.
- It aims at providing relevant results.
- Helps segregating wastes less riskier for waste pickers and easier for normal people.

## Inspiration

### Case Study - 1
We saw the success story of [KabadiWallah Connect](https://www.kabadiwallaconnect.in/), a Chennai based startup, it provided an IoT based point of pickup i.e. an IoT based dustbin which monitored waste collection and notified nearby Kabadiwallahs when it required disposal. Enabling such a system organised the Recyclable Waste Collection in India which is an informal sector which lags structure and also reduced risks that Kabadiwallahs (level-0 waste picker are called so in India) used to take in their daily life to find and segregate waste, thereby improving their livelihoods.

**Report by** [ITU Hub](https://www.itu.int/hub/2021/07/indian-firms-digital-solution-for-urban-waste-pickers/)

#### Our Remarks
>What if we could reduce the risks even more that the Kabadiwallahs take to segregating waste by diving knee deep into the waste?

>Why not create an ML model that can segregate waste into as recyclable and non-recyclable based on data provided by IoT enabled dustbins (an image sensor will capture image of waste at the type of disposal)?

### Case Study - 2
[Litterati](https://www.litterati.org/) is a Litter data collection and analysis app based in US. This app has been used by various lawmakers and school administrations in US to get insights on what type of waste are being mostly generated in their city and school campus respectively and how they can reduce it.

**Report by Science Learn Hub** [Citizen Science Project-Litterati](https://www.sciencelearn.org.nz/resources/2752-litterati)

#### Our Remarks
>As claimed earlier, waste management systems must be decentralised and locale specific.

>Hence, to enable this why not make it local and available in India?

## Outcome
Our project aims at helping people make data informed life choices that are sustainable and also simplifies life of level 0 waste pickers and helps them in segregating waste using ML model. Our initial brainstorming resulted in creation of [LitterLens](https://litter-insight-and-segregation-eptbtokgzyygokv88wzfpz.streamlit.app/) which is powered by streamlit, tensorflow, pandas, numpy, pytorch, html, javascript, SheetDB, Google sheets, TailwindCSS and Matplotlib. Besides it is also powered by hardwork of our fellow contributors- [Dileep]() [Vaishali]() [Kesav]() and [Maruthi Karthik Singh]()  

## View Demo 
[LitterLens](https://litter-insight-and-segregation-eptbtokgzyygokv88wzfpz.streamlit.app/) 

## What it does 
- It allows user to input the image of litter in two ways- from the local device and from the image URL. It take the image as input and uses the Machine Learning Model which we have created using Tensorflow, Keras, Python and other ML libraries to classify the image into-
 + paper
 + trash 
 + metal
 + cardboard 
 + plastic
 + glass 
and then further classifies the litter into as recyclable and biodegradable.
- It also takes the name of user, their location (right now we have only included 4 cities- Hyderabad, Bangalore, Chennai and Delhi) and their locality (this feature is not yet implemented) during login and gives the litter analytics (in the form of bar graph between litter type (cardboard, paper, plastic, glass, metal, trash) and the count of litter in their city (right now the count will be city based, later on we will make it more local by adding locality feature). In addition to this our website also gives insights to user on how they can reduce that particular litter production by making sustainable changes in lifestyle.

## How we built it
We built our project with love, patience and hardwork using following tools and technologies-
- For machine Learning Model->
 + Tensorflow 
 + Python 
 + Pandas
 + Numpy 
 + Matplotlib 
 + Keras 
 + Pytorch   
 + Jupyter 
 + OS
- For Front-end of our Website->
 + streamlit 
 + python
 + pandas
 + numpy 
 + matplotlib 
 + HTML 
 + TailwindCSS 
 +  JavaScript 
- For backend and Database -> 
 + SheetDB 
 + Google Sheets 
 + Kaggle Dataset (for ML model) 
- For code hosting -> 
 + GitHub 
- For Deployment -> 
 + Streamlit Cloud

## Challenges we ran into 
- We had trouble importing Machine Learning Model into our website.
- We had problems implementing the prediction algorithm via webpage.
- We had problems connecting Google sheets with our website.
- We had trouble deploying the app on streamlit cloud.
But these issue got resolved in time with our hardwork and teamwork. We were successful in collaborating with one another using Discord and were connected throughout the Hackathon. We are grateful to Katie Youth Hacks for giving us the opportunity to collaborate with such resourceful people and also improved our tech skills in streamlit, machine learning and web development.

## Accomplishments that we're proud of

## What we learned

## What's next for LitterLens-Local Litter Insights
