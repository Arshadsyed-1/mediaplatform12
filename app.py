import streamlit as st
st.title("Media Platform")
login,signup = st.tabs(["Login","Signup"])

with login:
    st.header("login")
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password",type="password")
        submitted = st.form_submit_button("Login")

with signup:
    st.header("Signup")
    with st.form("signup_form"):
        name = st.text_input("Naame")
        email = st.text_input("Email")
        password = st.text_input("password",type = "password")
        submitted = st.form_submit_button("Signup")