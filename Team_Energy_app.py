# ---| TEAM ENERGY STREAMLIT WEB APP |--->>>>
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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import time
import json
from Team_Energy.predict  import *
from Team_Energy.data import create_data, get_weather
# ---| VERIABLES |--->>>>
Show_Graph = False
User_Group_Selected = 0
# ---| PAGE CONFIGURATION |--->>>>
st.set_page_config(page_title="Energy.app", page_icon=":zap:", layout="wide",menu_items = {"about":"https://redlorryyellowdesign-teamenergy-energy-a-team-energy-app-xg55r5.streamlitapp.com/About"} )
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
# ---| IMPORTING LOTTIE ASSEST |---
Team_Lottie_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vctzcozn.json")
House_Energy_Animation = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ulfrygzw.json")
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

def find_value(x):
    forecast2 = forecast.copy()
    forecast2['day_of_month'] = forecast2.ds.dt.day
    forecast_grouped = forecast2.groupby('day_of_month').sum()
    if x == 'low':
        return forecast_grouped.min()
    if x == 'high':
        return forecast_grouped.max()
# ---| SIDE BAR |--->>>>
with st.sidebar:
    st.image('Images/Team_Energy_Logo.png', width=200)
    st.title("Built By Team Energy")
    st.write("This app is designed to help you understand your energy usage and how it compares to other households.")
    st_lottie(House_Energy_Animation, speed=0.8, reverse=False, loop=True, height=250, key=None)
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
    tab0, tab1, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Intro","Tariff Type", "House Type","Ownership Status","Number of Bedrooms","Household Income","Submit"])
    with tab0:
        st.write("This app will help you to predict your energy consumption")
        st.write("All you need to do is answer a few questions, sounds good?")
        st.write("Let's get started. Just click on the next tab called 'Tariff Type' to get started")
    with tab1:
        st.write("Please select your current tariff")
        User_Tarrif_Selected = st.selectbox('Pick one', ["","Standard Tariff", "Dynamic Tariff"])

        if User_Tarrif_Selected == "Standard Tariff":
            User_Tarrif_Selected = "Std"
            st.write("You have selected Standard Tariff")

        elif User_Tarrif_Selected == "Dynamic Tariff":
            User_Tarrif_Selected = "ToU"
            st.write("You have selected Dynamic Tariff")
        else:
            st.warning("Please select a tariff")

        with tab3:
            st.write("What is your house type?")
            Question_1 = st.selectbox('Pick one', ["",'Detached house', "Flat or Maisonette", "Semi-detached house","Terraced house"], key="Question_1")
            if Question_1 != "":
                st.write("Please select an option")

        with tab4:
            st.write("What is your property ownership status?")
            Question_2 = st.selectbox('Pick one', ["",'Owned outright', 'Mortgaged', 'Shared/Equity Ownerhsip','Privately Rented', 'Social renting'], key="Question_2")
            if Question_2 != "":
                st.write("Please select an option")
        with tab5:
            st.write("How many bedrooms does your house have?")
            Question_3 = st.selectbox('Pick one', ["",'1 bedroom', '2 bedrooms', '3 bedrooms', '4+ bedrooms'], key="Question_3")
            if Question_3 != "":
                st.write("Please select an option")
        with tab6:
            st.write("What is your estimated household income?")
            Question_4 = st.selectbox('Pick one', ["",'£0-£20,000', '£20,000-£40,000','£40,000-£60,000','£80,000 +'], key="Question_4")
            if Question_4 != "":
                st.write("Please select an option")

        with tab7:
            col1,col2 = st.columns(2)
            with col1:
                #Submit Button
                if st.button("Submit"):
                    # Predict_Model(User_Tarrif_Selected,User_Group_Selected )
                    if User_Tarrif_Selected != "" and Question_1 != "" and Question_2 != "" and Question_3 != "" and Question_4 != "":
                        User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)
                        with st.spinner('Spinning up the hard drives...'):
                            time.sleep(5)

                            User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)
                            name = User_Group_Selected
                            tariff = User_Tarrif_Selected
                            # ---| IMPORT JOBLIT MODEL |--->>>>
                            filename = f'Team_Energy/models/model_{name}_{tariff}.joblib'
                            m = joblib.load(filename)
                            st.success('All working well...')
                        # ---| PREDICTING |--->>>>
                        m = joblib.load(filename)
                        with st.spinner('Last part! This can take a second or two...'):
                            time.sleep(5)
                            train_df, test_df = create_data(name = name, tariff = tariff)
                            train_wd, test_wd = get_weather(train_df, test_df)
                            forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
                            Show_Graph = True
                            mape = evaluate(test_df['KWH/hh'], forecast['yhat'])
                            acuracy = (1 - mape)
                        st.success('Plotting graphs now...')


            with col2:
                # resets the questions
                if st.button("Reset"):
                    User_Tarrif_Selected = ""
                    Question_1 = ""
                    Question_2 = ""
                    Question_3 = ""
                    Question_4 = ""
                    st.write("Please select your options again")

with st.container():
    if Show_Graph == True:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
        fig_1 = plt.figure(figsize=(15, 6));
        plt.ylabel('Energy usage in KWH per half hour')
        plt.xlabel('Forecast date range')
        plt.title('Forecasted Energy vs Actual Energy Usage')
        sns.lineplot(x=forecast['ds'],y=forecast['yhat'],label='Forecast');
        x = test_df['DateTime'].loc[(test_df['DateTime'] <= '2014-02-14')]
        sns.lineplot(x=x,y=test_df['KWH/hh'],label='Actual', color='red');
        fig_2 = figure(figsize=(15,6))
        max_test = 13.40
        min_test =  0.23
        forecast_min = find_value('low').round(2)
        forecast_max = find_value('high').round(2)
        elecf=[1.196367,1.164487,1.052873,0.949678,0.910947,0.863625,0.846739,0.857709,0.877138,0.962776,1.095168,1.222492]
        co2=0.309 # kg/kwh emission
        annual_consumption=round((forecast.sum()/elecf[1])*np.sum(elecf),2)
        annual_co2=round(co2*annual_consumption,2)

        total_usage = forecast.sum()
        tu = total_usage.to_string().strip("yhatdtype:float64")
        tu2 = float(tu)
        tu3 = round(tu2,2)
        average_usage = 330.47
        average_annual_consumption=round((average_usage/elecf[1])*np.sum(elecf),2)
        annual_co2 = annual_co2.to_string().strip("yhatdtype:float64")
        col1, col2, col3 = st.columns(3)
        col1.metric("February Use vs Average (KWH)", tu3, average_usage)
        col2.metric("Annual Energy Consumption (KWH)", annual_consumption, average_annual_consumption)
        col3.metric("High vs Average High (KWH)", forecast_max, max_test)
        st.subheader(f'Predicted Annual Carbon Footprint: {annual_co2} Kg CO₂')
        st.pyplot(fig_1);
        mape = evaluate(test_df['KWH/hh'], forecast['yhat'])
        # st.write(f'MAPE: {mape}')
        accuracy = np.round((1 - mape) *100,2)
        st.subheader(f'Forecast accuracy: {accuracy} %')

# ---| FOOTER SECTION|--->>>>
with st.container():
    st.write("---")
    Flooter_col_1, Flooter_col_2, Flooter_col_3, Flooter_col_4 = st.columns(4)
    with Flooter_col_1:
        st.subheader("The Team")
        st.write("This app was created by Team Energy. Team Energy is a group of 4 students from Le Wagon's Data Science Bootcamp. Team Energy is made up of the following members:")
    with Flooter_col_2:
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
