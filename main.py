import json
import streamlit as st
import subprocess

if __name__ == "__main__":
    st.title("Instagram Profile Scraper")

    st.write("This is a simple Instagram profile scraper. \
        It uses Selenium to scrape the profile page of a given user. \
        It returns the following information: \
        username, biography, number of posts, number of followers, number of following, \
        and whether the profile is private or not.")

    with st.form("my_form"):
        username = st.text_input("Enter your Instagram username")
        password = st.text_input("Enter your Instagram password", type="password")
        profile = st.text_input("Enter the profile you want to scrape")
        submit_button = st.form_submit_button(label="Go")

    if submit_button:
        subprocess.run(["python3", "scraper.py", username, password, profile])
        st.write(json.load(open("{}.json".format(profile), "r")))
    
    
