import streamlit as st
import socket


st.title("Know your Details")
ok = st.button('Click!...')
if ok:
    # Device IP Address
    hostName = socket.gethostname()
    IPAddr = socket.gethostbyname(hostName)
    st.write("Computer Name : ", hostName)
    st.write("Computer Address : ", IPAddr)


    import requests
    from bs4 import BeautifulSoup
    import json

    userData = requests.get('https://ipinfo.io/')
    userDataObj = userData.json()
    st.subheader('Your Details are as follow')
    st.write("IP Address : "+userDataObj['ip'])
    st.write('hostname : '+userDataObj['hostname'])
    st.write('city : '+userDataObj['city'])
    st.write('region : '+userDataObj['region'])
    st.write('country : '+userDataObj['country'])
    st.write('loc : '+userDataObj['loc'])
    st.write('org : '+userDataObj['org'])
    st.write('postal : '+userDataObj['postal'])
    st.write('timezone : '+userDataObj['ip'])