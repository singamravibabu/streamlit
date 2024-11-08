import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=0.0)
height = st.number_input("Enter your height (m):", min_value=0.0)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.write("Please enter a valid height.")
