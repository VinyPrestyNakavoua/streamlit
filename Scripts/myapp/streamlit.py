# creating my first streamlit app
import streamlit as st

st.title("Welcome to my first Streamlit App")
st.write("This is a simple app to get started with Streamlit")

# Input example
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")



