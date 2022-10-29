import streamlit as st
st.header("This is my BMI APP")
w=st.number_input("what is your weight")
h =st.number_input("what is your height")
if st.button("calaculate"):
    BMI = (w/(h**2))
    
    BMI = round(BMI,1)
    if BMI<18.5:
        st.write(f"Your BMI Is :{BMI}\nUnderweight")
    elif 18.4< BMI<25:
        st.write(f"Your BMI IS : {BMI}\nNormal")
    elif 24.9<BMI<30:
        st.write(f"Your BMI IS :{BMI}\nOverweight")
    elif 29.9<BMI < 35:
       st.write(f"Your BMI IS : {BMI}\nClass 2 Obesity")
    elif 34.9<BMI < 40:
        st.write(f"Your BMI IS :{BMI}\nClass 2 obesity")
    else:
       st.write(f"Your BMI IS : {BMI}\nExtreme Obesity")
    
             
