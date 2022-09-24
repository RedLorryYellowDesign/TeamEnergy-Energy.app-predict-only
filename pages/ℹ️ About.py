from asyncore import write
import streamlit as st
st.set_page_config(page_title="About", page_icon=":zap:", layout="wide" )

with st.container():
    st.empty()
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.header("About Energy.app")
        st.subheader("Future Applications")
        st.write("""
    We are proud of the models we have made as they demonstrate a
    good proof of concept around energy prediction.  However, with
    better data, there is potential to enrich the model to address
    the following:""")

        st.write("""
            #### Individual usage
            """)

        st.write("""
            For future application, individuals could make use of a tailored
            energy forecasting model with their personal lifestyle information
            (number of residents, income etc) and specific house information (size, insulation etc).
            This would enable them to:

            """)


        st.text("""
        •	Facilitate Climate Change initiatives by consuming energy efficiently
        •	Address EV charging when overall grid consumption is low
        •	Support managing cost and carbon emissions within a household
        •	Add a mechanism for individuals to plan and prepare for their future energy needs
        •	Evaluating a property to buy or lease based on its typical energy usage.  Students etc may need a more detailed breakdown than an EPC rating can provide
        •	Based on a model with further features, recommendations could be made to individuals on the best time for them to use energy.
        •	Individuals could also use this model to identify the best time to charge their EV.  This could be based on the time of day and the weather.  This would be particularly useful for those who have solar panels and are able to charge their EV during the day.
        •	Real estate agents
            """)

        st.write("""
            #### Government / Large power network suppliers
            """)

        st.write("""

    This model can help provide broad scale information about energy consumption within a community based on weather patterns and historical usage. This can be leveraged by network suppliers to planning, execution and maintenance.  Effective planning can accelerate decarbonisation.

    Local government could also use this data to identify outliers.  This could be in the forms of houses with excess energy usage who may benefit from schemes to provide insulation or support.

    Government could also use this data to create pre-emptive plans to avoid fuel poverty for specific households.  In terms of research and development, this would likely save significant time and budget.
                """)

#         st.text("""Future Applications
#     We are proud of the models we have made as they demonstrate a
#     good proof of concept around energy prediction.  However, with
#     better data, there is potential to enrich the model to address
#     the following:

# 	•	Individual usage

#     For future application, individuals could make use of a tailored energy forecasting model with their personal lifestyle information (number of residents, income etc) and specific house information (size, insulation etc).  This would enable them to:
# 	•	Facilitate Climate Change initiatives by consuming energy efficiently
# 	•	Address EV charging when overall grid consumption is low
# 	•	Support managing cost and carbon emissions within a household
# 	•	Add a mechanism for individuals to plan and prepare for their future energy needs
# 	•	Evaluating a property to buy or lease based on its typical energy usage.  Students etc may need a more detailed breakdown than an EPC rating can provide
# 	•	Based on a model with further features, recommendations could be made to individuals on the best time for them to use energy.
#     •	Individuals could also use this model to identify the best time to charge their EV.  This could be based on the time of day and the weather.  This would be particularly useful for those who have solar panels and are able to charge their EV during the day.
# 	•	Real estate agents
#     The models with specific house features could be integrated into websites.  Certain houses could be categorised for marketing purposes.  The model could also supply agents with a competitive advantage and make a particular agency more attractive to the energy conscious buyer or renter.

# 	•	Government / Large power network suppliers

#     This model can help provide broad scale information about energy consumption within a community based on weather patterns and historical usage. This can be leveraged by network suppliers to planning, execution and maintenance.  Effective planning can accelerate decarbonisation.

#     Local government could also use this data to identify outliers.  This could be in the forms of houses with excess energy usage who may benefit from schemes to provide insulation or support.

#     Government could also use this data to create pre-emptive plans to avoid fuel poverty for specific households.  In terms of research and development, this would likely save significant time and budget.
# """)
