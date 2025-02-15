import os
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu 

#set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks",
                    layout="wide")

#getting the working directory Of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

#loading the saved Models
diabetes_model = pickle.load(open(r"C:\Users\Harsh Kesarwani\Documents\Prediction of Disease Outbreaks\Training_models\diabetes_model.sav", 'rb'))
heart_disease_model= pickle.load(open(r"C:\Users\Harsh Kesarwani\Documents\Prediction of Disease Outbreaks\Training_models\heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\Harsh Kesarwani\Documents\Prediction of Disease Outbreaks\Training_models\parkinsons_model.sav",'rb'))


#sidebar for Navigation
with st.sidebar:
    selected = option_menu("Prediction of Disease Outbreaks System",
                            
                        ['Diabetes Prediction',
                        'Heart Disease prediction',
                        'Parkinsons Prediction'],
                        menu_icon='hospital-fill',
                        icons=['activity', 'heart','person'],
                        default_index=0)

#Diabtes Prediction Page
if selected=="Diabetes Prediction":
    #Page Title
    st.title("Diabetes Prediction using ML")

    #getting the input data from user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    
    with col2:
        Glucose = st.text_input("Glucose Level")
    
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("insulin Level")
    with col3:
        BMI= st.text_input("BMI Value")
    with col1:
        DiabetesPedigreefunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age=st.text_input("Age of the Person")

    #code for Prediction
    diab_diagnosis= ''

    #creating a button
    if st.button("Diabetes Test Result"):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreefunction, Age]
        
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0]==1:
            diab_diagnosis = "The Person is Diabetic"
        else:
            diab_diagnosis = "The Person is not Diabetic"

    st.success(diab_diagnosis)

#Heart Disease
if selected =="Heart Disease prediction":
    #Page Title
    st.title("Heart Disease prediction using ML")

    #getting the input data from user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    
    with col2:
        sex = st.text_input("Sex")
    
    with col3:
        cp = st.text_input("Chest Pain Types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholerstrol in mg/dl")
    with col3:
        fbs= st.text_input("fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach=st.text_input("Maximum heart rate achieved")
    with col3:
        exang = st.text_input("exercisse Induced Angina")
    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope= st.text_input("slope of the Peak Exercise ST segment")
    with col3:
        ca = st.text_input("Major Vessels coloured by FLourosopy")
    with col1:
        thal= st.text_input("thal: 0 = normal; 1 = fixed defects; 2 = reversible defect")

    #code for Prediction
    heart_diagnosis = ''

    #creating a button

    if st.button("Heart Disease Test Result"):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0]==1:
            heart_diagnosis = "The Person is having Heart Disease"
        else:
            heart_diagnosis = "The Person is not having Heart Disease "

    st.success(heart_diagnosis)


#Parkinson's Disease
if selected =="Parkinsons Prediction":
    #Page Title
    st.title("Parkinson's Disease prediction using ML")

    #getting the input data from user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    
    with col2:
        fhi = st.text_input("MDVP:FHi(Hz)")
    
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col1:
        RAP= st.text_input("MDVP:RAP")
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
    with col3:
        DDP = st.text_input("Jitter:DDP")
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col1:
        APQ3 = st.text_input("Shimmer: APQ3")
    with col2:
        APQS = st.text_input("Shimmer: APQS")
    with col3:
        APQ = st.text_input("MDVP: APQ")
    with col4:
        DDA = st.text_input("Shimmer:DDA")
    with col5:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("spread1")
    with col5:
        spread2 = st.text_input("spread2")
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input("PPE")
    
    parkinsons_diagnosis= ''
    if st.button("Parkinson's Test Result"):
        user_input= [fo,fhi, flo, Jitter_percent, Jitter_Abs,
                    RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQS,
                    APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2,D2, PPE]
        
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis = "The Person is has Parkinson's Disease"
        else:
            parkinsons_diagnosis = "The Person does not hav Parkinson's Disease"

    st.success(parkinsons_diagnosis)


