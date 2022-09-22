import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from Team_Energy_app import Show_Graph, forecast, test_df, figure, test_wd

with st.container():
    st.empty()

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

with st.container():
    if Show_Graph == True:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
        fig_1 = plt.figure(figsize=(15, 6))
        sns.lineplot(x=forecast['ds'],y=forecast['yhat'],label='Forecast');
        sns.lineplot(x=test_df['DateTime'],y=test_df['KWH/hh'],label='Actual');
        fig_2 = figure(figsize=(15,6))
        sns.lineplot(x=test_wd['DateTime'],y=test_wd['temperature'],label='Weather');
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success('Done!')
        st.pyplot(fig_1)
        st.pyplot(fig_2)
