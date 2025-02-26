import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.buy_me_a_coffee import button
import os

# Trick to preserve the state of your widgets across pages
for k, v in st.session_state.items():
    st.session_state[k] = v
##

st.set_page_config(
    page_title="About",
    page_icon="📰",
    layout="wide"
)

# Works with streamlit==1.17.0
# TODO: Review class names for future versions
st.markdown("""
  <style>
      ul[class="css-j7qwjs e1fqkh3o7"]{
        position: relative;
        padding-top: 2rem;
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
      }
      .css-17lntkn {
        font-weight: bold;
        font-size: 18px;
        color: grey;
      }
      .css-pkbazv {
        font-weight: bold;
        font-size: 18px;
      }
  </style>""", unsafe_allow_html=True)

path = os.path.dirname(__file__)


st.header("About")

st.markdown(
    """
    ### **Brief description of the web app**
    This app is designed to assist medical doctors and provide patients with a 
    fast diagnostic supported by the ChatGPT AI model of [OpenAI](https://openai.com/) based on relevant information such as age, 
    gender, pregnancy state, environmental and historical context, symptoms, observations, and test results conducted in laboratory.
    ### **Why should you buy me a coffee, i.e. donate ?**
    This app uses the ChatGPT AI model through the official API of OpenAI which has a cost. Also, this app is free to use and will 
    remain free to use for all if you support it by buying me a coffee (see the dedicated button and QR code on the left side). 
    Thank you very much in advance for making it possible !
    ### Coming features
    - Differential diagnosis :clipboard:
    - Multilingual interface 🇨🇳 🇧🇷 🇮🇩 🇷🇺 
    ### Versions
    :sparkles: **Current version: V1.123** (2023/03/29) :sparkles:  
    - Updates: Rolling out Spanish and German translations of the UI, bug fixes.

    Version history:
    - v1.121 (2023/03/28): Updates: Rolling out French and Japanese translations of the UI, bug fixes.
    - v1.11 (2023/03/07): Updates: **Highlight** in HTML format the **proposed diagnostic**, **caution message** added, bug fixes.
    - v1.10 (2023/03/02): Updates: **model gpt-3.5-turbo (ChatGPT) integration**, bug fixes, and performance improvements.
    - v1.01 (2023/01/30): Internal pre-release
    ### **Sources**
    - The source code of this app is available [here](https://github.com/GLambard/MDxApp)
    - Anonymous public cases taken from the Brown Hospital Medicine Twitter account [@BrownJHM](https://twitter.com/BrownJHM) 
    are used as illustrating examples on the main page of the app. 
    ### :rotating_light: **Caution message** :rotating_light:
    Please be aware that while the app is designed to assist medical decision-making and check symptoms, 
    the final diagnosis should be made by a licensed medical professional. We recommend 
    seeking additional evaluations and opinions before making any treatment decisions.
    ### **Message from the developer**
    > Dear community,  
    > 
    > I am proud to announce the deployment of this free app that provides medical diagnosis assistance to those in need.  
    > 
    > I want to take this moment to thank the open-source community for their unwavering support in making this project a reality. 
    > Your contributions, in any form, have allowed me to bring this tool to all.  
    > 
    > I hope this app will positively impact people's lives, and I am grateful for the opportunity to serve the community in this way.  
    """, 
    unsafe_allow_html=True
)

