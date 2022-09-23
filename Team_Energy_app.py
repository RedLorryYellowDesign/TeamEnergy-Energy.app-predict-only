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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import time
import json
from Team_Energy.predict  import *
from Team_Energy.data import create_data, get_weather
import webbrowser

# ---| VERIABLES |--->>>>
API_MODE = False
Show_Graph = False
Lottie_off = False
User_Group_Selected = 0
# ---| PAGE CONFIGURATION |--->>>>
st.set_page_config(page_title="Energy.app", page_icon=":zap:", layout="wide", initial_sidebar_state="auto",
        menu_items=
        "About Energy.app",
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
        })
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
if Lottie_off == False:
    lottie_coding_Data_Science_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xl3sktpc.json")
    Team_Lottie_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vctzcozn.json")
    Loding_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ibxFWH.json")
    House_Energy_Animation = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ulfrygzw.json")
# ---| IMPORTING IMAGES |--->>>>

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
        r = requests.get(url/all_Good)
        if r.status_code != 200:
            return None
        return r.json()
    else:
        st.write("API Call is set to False, Please Enable API Call")

@st.experimental_memo
def api_model_select(model, name, tariff):
    url = f"https://team-energy-model-api-sf2mcflzda-ew.a.run.app/model/{model}?name={name}&tariff={tariff}"
    r = requests.get(url)
    if r.status_code != 200:
        return st.write("Oh No Something Went Wrong")
    r.json
    return r.json()

def plot_graphs(test_set,predicted_consumption):
    df_plot=test_df['2014':].copy()
    df_plot.rename(columns={'KWH/hh':'Test'},inplace=True)
    df_plot['Predicted']=predicted_consumption
    plt.figure(figsize=(18,6))
    plt.plot(df_plot)
    plt.title('Electricity Consumption Prediction')
    plt.xlabel('Time')
    plt.ylabel('Consumption (kWh/hh)')
    plt.legend()
    plt.show()

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
    st_lottie(House_Energy_Animation, speed=1, reverse=False, loop=True, height=250, key=None)
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
            if Question_1 != " ":
                st.write("Please select an option")

        with tab4:
            st.write("What is your property ownership status?")
            Question_2 = st.selectbox('Pick one', ["",'Owned outright', 'Mortgaged', 'Shared/Equity Ownerhsip','Privately Rented', 'Social renting'], key="Question_2")
            if Question_2 != " ":
                st.write("Please select an option")
        with tab5:
            st.write("How many bedrooms does your house have?")
            Question_3 = st.selectbox('Pick one', ["",'1 bedroom', '2 bedrooms', '3 bedrooms', '4+ bedrooms'], key="Question_3")
            if Question_3 != " ":
                st.write("Please select an option")
        with tab6:
            st.write("What is your estimated household income?")
            Question_4 = st.selectbox('Pick one', ["",'£0-£20,000', '£20,000-£40,000','£40,000-£60,000','£80,000 +'], key="Question_4")
            if Question_4 != " ":
                st.write("Please select an option")

        with tab7:
            col1,col2 = st.columns(2)
            with col1:
                #Submit Button
                if st.button("Submit"):
                    # Predict_Model(User_Tarrif_Selected,User_Group_Selected )
                    if User_Tarrif_Selected != "" and Question_1 != "" and Question_2 != "" and Question_3 != "" and Question_4 != "":
                        User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)
                        # forecast = Mode_Predict_Run(User_Tarrif_Selected = User_Tarrif_Selected,User_Group_Selected = User_Group_Selected)

                        with st.spinner(f'Calling the model for Acorn group: {User_Group_Selected}'):
                            time.sleep(5)
                            st.success('Good so far...')
                            # User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)
                            name = User_Group_Selected
                            tariff = User_Tarrif_Selected
                            # ---| IMPORT JOBLIT MODEL |--->>>>
                            filename = f'Team_Energy/model_{name}_{tariff}.joblib'
                            m = joblib.load(filename)
                            with st.spinner('Spinning up the hard drives...'):
                                time.sleep(5)
                            st.success('All working well...')
                            # ---| PREDICTING |--->>>>
                            m = joblib.load(filename)
                            with st.spinner('Last part! This can take a second or two...'):
                                time.sleep(5)
                            train_df, test_df = create_data(name = name, tariff = tariff)
                            train_wd, test_wd = get_weather(train_df, test_df)
                            forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
                            Show_Graph = True
                            st.success('Plotting graphs now...')
                            mape = evaluate(test_df['KWH/hh'], forecast['yhat'])
                            # st.write(f'MAPE: {mape}')
                            acuracy = (1 - mape)
                            #st.write(f'Accuracy: {acuracy}')
            # with col2:
            #     if st.button("Submit +"):
            #         if User_Tarrif_Selected != "" and Question_1 != "" and Question_2 != "" and Question_3 != "" and Question_4 != "":
            #             User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)
            #             name = User_Group_Selected
            #             tariff = User_Tarrif_Selected
            #             model = "RNN_predict"
            #             api_json = api_model_select(model, name, tariff)
            #             predict_json = api_json['prediction'][0]
            #             acuracy = api_json['accuracy']
            #             predict = pd.DataFrame(predict_json)
            #             # test_set_json = api_json['test_set']
            #             # test_set = pd.DataFrame(test_set_json)
            #             st.write(f'Accuracy: {acuracy}')
            #             ajusted_acuracy = (1-acuracy) * 100
            #             st.write(predict)
            #             #st.write(f'Accuracy: {ajusted_acuracy}')
            #             st.line_chart(predict)
            #             plot_graphs('''test_set=test_set''',predicted_consumption=predict)
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
        sns.lineplot(x=test_wd['DateTime'],y=test_wd['temperature'],label='Weather',color='red',alpha=0.5, linewidth=3, linestyle='--'), plt.ylabel('Temperature (C)'), plt.title('Temperature vs Time');
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success('Done!')
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
        #st.pyplot(fig_2);

# ---| FOOTER SECTION|--->>>>
with st.container():
    st.write("---")
    Flooter_col_1, Flooter_col_2, Flooter_col_3, Flooter_col_4 = st.columns(4)
    with Flooter_col_1:
        st.subheader("The Team")
        st.write("This app was created by Team Energy. Team Energy is a group of 4 students from Le Wagon's Data Science Bootcamp. Team Energy is made up of the following members:")
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
