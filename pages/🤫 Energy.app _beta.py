# ---| TEAM ENERGY STREAMLIT WEB APP |--->>>>
# ---| BASE STREAMLIT LIBRARIES |--->>>>
from decimal import FloatOperation
from ipaddress import collapse_addresses
from multiprocessing.sharedctypes import Value
from pickle import FALSE
from re import X
import requests # Allows use of URL imports
import streamlit as st # Allows compatibility with Streamlit
from streamlit_lottie import st_lottie # Allows lottie animation
from PIL import Image # Image manipulation
# ---| DATASCIANCE LIBRARIES |--->>>>
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import time
import json


def load_lottieurl_1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ---| IMPORTING LOTTIE ASSEST |---
No_Acsess = load_lottieurl_1("https://assets4.lottiefiles.com/packages/lf20_slGFhN.json")
hale9000 = load_lottieurl_1("https://assets4.lottiefiles.com/private_files/lf30_5ouyxit5.json")
st.title ("Top Secret Energy.app_beta")

st_lottie(No_Acsess, speed=0.8, reverse=False, loop=True, height=400, key=None)
st.subheader("This app is currently in beta.  That means no looking!. Got it?. Good. We are watching you.")
st.write("Dont make me call Hal 9000 on you!")

if st.button("I promise not to look", key="Hals_comming"):
    st.text("I know you are lying, Hal 9000 is on his way")
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(hale9000, speed=0.8, reverse=False, loop=True, height=300, key="hal_9000")
    with col2:
        st.text("Hal 9000 has been activated")
        st.text("..........")
        st.text("..........")
        st.text("..........")
        st.text("""
                Message from HAL 9000:
                'I'm sorry Dave, I'm afraid I can't
                do that', Wait your david right?
                error 404: David not found
                HAL-9000.EXE has crashed
                """)
