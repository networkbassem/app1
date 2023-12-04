import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


st.set_page_config(page_title="LOG", page_icon=":bar_chart:", layout="wide")

# --- User Auth ---
names = ["ziko byte","fanto byte"]
usernames = ["ziko","fanto"]

# --- LOAD HASHED PASSWORDS ---
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "ChatBot dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("LOGIN","MAIN")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("please enter your username and password")

if authentication_status:









# --- SIDEBAR ---
    authenticator.logout("Logout","sidebar")
    st.sidebar.title(f"Welcome {name}")
    #st.header(":mailbox: Get In Touch With Me!")