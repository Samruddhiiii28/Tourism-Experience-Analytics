import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load model
model = joblib.load('best_lgb_model.pkl')

st.set_page_config(page_title='Tourism Experience Analytics App', layout='centered')
st.title('🌍 Tourism Experience Analytics App')

#Sidebar Navigation
section=st.sidebar.radio("Select Section", ["Visit Mode Prediction", "Attraction Recommendaton", "Tourism Insights Dashboard"])

# 1 .Visit Mode Prediction
if section == "Visit Mode Prediction":
    st.header('Predict User Visit Mode')
    visit_month=st.slider('Visit Month', 1, 12, 1)
    total_visit=st.number_input('TotalVisits', 1, 50, 5)
    attraction_popularity=st.number_input('Attraction Popularity', 1, 500, 50)

    if st.button('Predict Visit Mode'):
        input_data = pd.DataFrame({
            'VisitMonth': [visit_month],
            'TotalVisits': [total_visit],
            'AttractionPopularity': [attraction_popularity]
    })
        visit_mode_labels={0:"Business", 1:"Couples", 2:"Family", 3:"Friends"}
        
        prediction = model.predict(input_data)
        predicted_label = visit_mode_labels[prediction[0]]
        st.success(f'Predicted Visit Model: {predicted_label}')


#2. Attraction Recommendation
elif section == "Attraction Recommendaton":
    st.header(' Personalized Attraction Recommendation')
    user_preference=st.selectbox('Select Your Preference',
                                 ['Beach', 'Museum', 'Park', 'Historical Site', 'Adventure'])
    
    #Dummy recommendations based on user preference
    recommendations = {
        'Beach': ['Bondi Beach', 'Copacabana', 'Waikiki Beach'],
        'Museum': ['Louvre', 'Metropolitan Museum of Art', 'British Museum'],
        'Park': ['Central Park', 'Hyde Park', 'Ueno Park'],
        'Historical Site': ['Colosseum', 'Great Wall of China', 'Machu Picchu'],
        'Adventure': ['Grand Canyon', 'Mount Everest Base Camp', 'Amazon Rainforest']
    }
    st.subheader('Recommended Attractions:')
    for attraction in recommendations[user_preference]:
        st.write(". " + attraction)

#3. Tourism Insights Dashboard
elif section == "Tourism Insights Dashboard":
    st.header('Tourism Insights Dashboard')
    #Dummy data for visualization
    sample_data =pd.DataFrame ({
        "Region": ['Europe', 'Asia', 'America','Africa'],
        "Average Rating": [4.3, 4.5, 4.2,4.0],
        "Total Visits": [1200, 15000, 1000, 800]
    })
    
    #Line Chart
    col1, col2= st.columns(2)
    with col1:
        st.subheader('Average Rating by Region')
        fig, ax = plt.subplots()
        sns.barplot(x='Region', y='Average Rating', data=sample_data)
        st.pyplot(fig)
    
    with col2:
        st.subheader('Number of Visitors by Region')
        fig2, ax = plt.subplots()
        sns.lineplot(x='Region', y='Total Visits',marker='o', data=sample_data)
        st.pyplot(fig2)
