# ---| TEAM ENERGY STREAMLIT WEB APP |--->>>>
# >>>> Site Structure & Desing
# |--------| ------------------------------------------ |
# |SIDE BAR| Page Title                                 |
# |--------| Page Into Text                             |
# |--------| My Pic | MY Work Experience | My Education |
# |--------| ------------------------------------------ |
# |--------|                                            |
# |--------| ------------------------------------------ |
# |--------| Footer                                     |
# |--------| ------------------------------------------ |
# ---| ALL IMPORT LIBRARIES |--->>>>
# ---| BASE STREAMLIT LIBRARIES |--->>>>
from decimal import FloatOperation
from multiprocessing.sharedctypes import Value
from pickle import FALSE
from re import X
import requests # Allows use of URL imports
import streamlit as st # Allows compatibility with Streamlit
from streamlit_lottie import st_lottie # Allows lottie animation
from PIL import Image # Image manipulation
# ---| DATASCIANCE LIBRARIES |--->>>>
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import plotly.figure_factory as ff
import time
# ---| VERIABLES |--->>>>
API_MODE = False
Show_Graph = False
Lottie_off = False
User_Group_Selected = 0
# ---| API ON/OFF DEPENDENT LIBRARIES |--->>>>
if API_MODE == False:
    from Team_Energy.predict  import *
    from Team_Energy.data import create_data, get_weather
# ---| PAGE CONFIGURATION |--->>>>
st.set_page_config(page_title="Team Energy Le Wagon Project", page_icon=":zap:", layout="wide", initial_sidebar_state="expanded")
# ---| LOAD CSS FOR STYLEING |---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style/style.css")
# ---| LOTTIE ANIMATION FUNCTIONS |--->>>>
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ---| CALL API FROM GCP |--->>>>
def API_REQUESTS(url):
    if API_MODE == True:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    else:
        st.write("API Call is set to False, Please Enable API Call")
# ---| POST API |--->>>>
def API_POST(url, data):
    if API_MODE == True:
        r = requests.post(url, data=data)
        if r.status_code != 200:
            return None
        return r.json()
    else:
        st.write("API Call is set to False, Please Enable API Call")

# ---| SEABORN PLOT FUNCTIONS |--->>>>
def seabon_line_plot(x, y, title, xlabel, ylabel, hue=None):
    fig_01, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=x, y=y, hue=hue)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig_01)
# ------>>>>
def seabon_bar_plot(df, x, y, title, xlabel, ylabel, hue=None):
    fig_02, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x=x, y=y, hue=hue)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig_02)
# ---| PLOTLY PLOT FUNCTIONS |--->>>>
def plotly_line_plot(df, x, y, title, xlabel, ylabel, hue=None):
    fig_03 = py.line(df, x=x, y=y, title=title, labels={x:xlabel, y:ylabel}, color=hue)
    st.plotly_chart(fig_03)


def compute_accuracy(y_true, y_pred):
    correct_predictions = 0
    # iterate over each label and check
    for true, predicted in zip(y_true, y_pred):
        if true == predicted:
            correct_predictions += 1
    # compute the accuracy
    accuracy = correct_predictions/len(y_true)
    return accuracy

# ---| IMPORTING LOTTIE ASSEST |---
if Lottie_off == False:
    lottie_coding_Data_Science_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xl3sktpc.json")
    Team_Lottie_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vctzcozn.json")
    Loding_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ibxFWH.json")
# ---| IMPORTING IMAGES |--->>>>
# ---| SIDE BAR |--->>>>
with st.sidebar:
    st.image('Images/Team_Energy_Logo.png', width=200)
    st.title("  By Team Energy")

# st.download_button('Downoload your data', data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, disabled=False)
# ---| Questions |--->>>>
Q1dict = {
    ""'Detached house' : 4,
    "Flat or Maisonette": 0,
    "Semi-detached house": 2,
    "Terraced house": 0
}
Q2dict = {""'Owned outright': 3,
    'Mortgaged': 2,
    'Shared/Equity Ownerhsip': 1,
    'Privately Rented': 0,
    'Social renting': 0
    }

Q3dict = {""'1 bedroom': 0,
    '2 bedrooms': 1,
    '3 bedrooms': 2,
    '4+ bedrooms': 4}

Q4dict = {""'£0-£20,000':0,
    '£20,000-£40,000': 1,
    '£40,000-£60,000': 1,
    '£80,000 +': 4}

def questions(Q1, Q2, Q3, Q4):
    total_values = Q1dict[Q1] + Q2dict[Q2] + Q3dict[Q3] + Q4dict[Q4]
    if total_values > 10:
        User_Group_Selected = 'A'
    elif total_values in range(5,9):
        User_Group_Selected = 'H'
    elif total_values < 5:
        User_Group_Selected = 'Q'
    return User_Group_Selected
# api check
@st.experimental_memo
def api_check_call(check=False):
    url = f"https://team-weather-lewagon-sf2mcflzda-ew.a.run.app"
    if check == True:
        r = requests.get(url/AlL_Good)
        if r.status_code != 200:
            return None
        return r.json()
    else:
        st.write("API Call is set to False, Please Enable API Call")

@st.experimental_memo
<<<<<<< Updated upstream
def Mode_Predict_Run(User_Tarrif_Selected, User_Group_Selected):
    name = User_Group_Selected
    tariff = User_Tarrif_Selected
    # ---| IMPORT JOBLIT MODEL |--->>>>
    filename = f'Team_Energy/model_{name}_{tariff}.joblib'
    m = joblib.load(filename)
    with st.spinner('Spinning up the Hard Drives'):
        time.sleep(5)
    st.success('All Working Well')
        # ---| PREDICTING |--->>>>
    m = joblib.load(filename)
    with st.spinner('Last Part! This can take a second or two'):
        time.sleep(5)
    train_df, test_df = create_data(name = name, tariff = tariff)
    train_wd, test_wd = get_weather(train_df, test_df)
    forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
    Show_Graph = True
    st.success('Done, Plostting Graphis now.')
    return forecast, Show_Graph
=======
def api_model_call(model,name, tariff):
    url = f"https://team-weather-lewagon-sf2mcflzda-ew.a.run.app"
    if model == RNN:
        sel_model = "RNN_predict"
    elif model == predict:
        sel_model = "predict"
    else:
        return "Please select a model"
    name = name
    tariff = tariff
>>>>>>> Stashed changes

# ---| HEADER SECTION |--->>>>
with st.container():
    Header_col_1, Header_col_2, Header_col_3, Header_col_4 = st.columns(4)
    with Header_col_1:
        st.title("Energy.app")
    with Header_col_2:
        st.empty()
    with Header_col_3:
        st.empty()
    with Header_col_4:
        st.empty()
# ---| MAIN SECTION |--->>>>  Cleaned
with st.container():
    tab0, tab1, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Intro","Tarrif Type", "House Type","Home owner?","Number of Bedrooms","Household Income","Submit"])
    with tab0:
        st.write("This app will help you to predict your energy consumption")
        st.write("All you need to do is answer a few questions, sound good?")
        st.write("Let's get started. Just click on the next tab called Q1 to")
        st.write("get started")
    with tab1:
        st.write("Please Select your Tariff Type your currently on")
        User_Tarrif_Selected = st.selectbox('Pick one', ["","Fixed Tariff", "Variable Tariff"])
        if User_Tarrif_Selected == "Fixed Tariff":
            User_Tarrif_Selected = "Std"
            st.write("You have selected Fixed Tariff")
        elif User_Tarrif_Selected == "Variable Tariff":
            User_Tarrif_Selected = "ToU"
            st.write("You have selected Variable Tariff")
        else:
            st.warning("Please select a tariff")

        with tab3:
            st.write("What is your house type?")
            Question_1 = st.selectbox('Pick one', ["",'Detached house', "Flat or Maisonette", "Semi-detached house","Terraced house"], key="Question_1")
            if Question_1 != " ":
                st.write("Please select an option")

        with tab4:
            st.write("What is your property ownership status?")
            Question_2 = st.selectbox('Pick one', ["",'Owned outright', 'Mortgaged', 'Shared/Equity Ownerhsip','Privately Rented', 'Social renting'], key="Question_2")
            if Question_2 != " ":
                st.write("Please select an option")
        with tab5:
            st.write("How many Bedrooms does your house have?")
            Question_3 = st.selectbox('Pick one', ["",'1 bedroom', '2 bedrooms', '3 bedrooms', '4+ bedrooms'], key="Question_3")
            if Question_3 != " ":
                st.write("Please select an option")
        with tab6:
            st.write("What is your estimated household income?")
            Question_4 = st.selectbox('Pick one', ["",'£0-£20,000', '£20,000-£40,000','£40,000-£60,000','£80,000 +'], key="Question_4")
            if Question_4 != " ":
                st.write("Please select an option")

        with tab7:
        # Submit Button
            st.empty()
            if st.button("Submit"):
                # Predict_Model(User_Tarrif_Selected,User_Group_Selected )
                if User_Tarrif_Selected != "" and Question_1 != "" and Question_2 != "" and Question_3 != "" and Question_4 != "":
                    User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)
                    # forecast = Mode_Predict_Run(User_Tarrif_Selected = User_Tarrif_Selected,User_Group_Selected = User_Group_Selected)

                    with st.spinner(f'Calling the model for Acorn group: {User_Group_Selected}'):
                        time.sleep(5)
                        st.success('Good so far')
                        # User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)
                        name = User_Group_Selected
                        tariff = User_Tarrif_Selected
                        # ---| IMPORT JOBLIT MODEL |--->>>>
                        filename = f'Team_Energy/model_{name}_{tariff}.joblib'
                        m = joblib.load(filename)
                        with st.spinner('Spinning up the Hard Drives'):
                            time.sleep(5)
                        st.success('All Working Well')
                        # ---| PREDICTING |--->>>>
                        m = joblib.load(filename)
                        with st.spinner('Last Part! This can take a second or two'):
                            time.sleep(5)
                        train_df, test_df = create_data(name = name, tariff = tariff)
                        train_wd, test_wd = get_weather(train_df, test_df)
                        forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
                        Show_Graph = True
                        st.success('Done, Plotting Graphs now.')
                        compute_accuracy(forecast, train_df)
with st.container():
    if Show_Graph == True:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
        fig_1 = plt.figure(figsize=(15, 6))
        plt.ylabel('KWH/hh')
        plt.title('Forecasted Energy vs Actual Energy Usage Demo')
        sns.lineplot(x=forecast['ds'],y=forecast['yhat'],label='Forecast');
        #sns.lineplot(x=test_df['DateTime'],y=test_df['KWH/hh'],label='Actual');
        x = test_df['DateTime'].loc[(test_df['DateTime'] <= '2014-02-14')]
        sns.lineplot(x=x,y=test_df['KWH/hh'],label='Actual')
        fig_2 = figure(figsize=(15,6))
        sns.lineplot(x=test_wd['DateTime'],y=test_wd['temperature'],label='Weather');
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success('Done!')
        st.pyplot(fig_1)
        st.pyplot(fig_2)
# ---| PLOTLY GRAPH |--->>>>
        fig_py_1 = px.line(forecast, x="ds", y="yhat", title='Your Energy Consumption Over the next month')
        fig_py_3 = px.line(test_wd, x="DateTime", y="temperature", title='How the weather will affect your energy consumption over the next month')
        st.plotly_chart(fig_py_1)
        st.plotly_chart(fig_py_3)
# ---| FOOTER SECTION|--->>>>
with st.container():
    st.write("---")
    Flooter_col_1, Flooter_col_2, Flooter_col_3, Flooter_col_4 = st.columns(4)
    with Flooter_col_1:
        st.subheader("The Team")
        st.write("This app was created by the Team Energy. The Team Energy is a group of 4 students from Le Wagon Data Science Bootcamp. The Team Energy is made up of the following members:")
    with Flooter_col_2:
        if Lottie_off == False:
            st_lottie (Team_Lottie_Animation, speed=1, key="i")
    with Flooter_col_3:
        st.write("Zenan Ahmed")
        st.write("[ZenanAH](https://github.com/ZenanAH)")
        st.write("---")
        st.write("Chris Cockerill")
        st.write("[Ruston3](https://github.com/Ruston3)")
    with Flooter_col_4:
        st.write("Jordan Harris")
        st.write("[RedLorryYellowDesign](https://github.com/RedLorryYellowDesign)")
        st.write("---")
        st.write("Jordan Haynes")
        st.write("[haynesj1](https://github.com/haynesj1)")
# ---| END OF CODE |--->>>>
