import streamlit as st
import requests

st.title("Currency Converter")

base_currency = st.selectbox("Base Currency", ["USD", "EUR", "GBP"])
target_currency = st.selectbox("Target Currency", ["USD", "EUR", "GBP"])
amount = st.number_input("Amount to Convert:", min_value=0.0, value=1.0)

if st.button("Convert"):
    # Example URL: replace with a real API endpoint
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(api_url)
    data = response.json()
    exchange_rate = data["rates"].get(target_currency, 1)
    converted_amount = amount * exchange_rate
    st.write(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
