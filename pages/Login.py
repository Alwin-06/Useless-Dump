import streamlit as st
import cv2
import numpy as np
import os
import time

st.set_page_config(page_title="🔐 Fun Login")

if "step" not in st.session_state:
    st.session_state.step = 1

st.title("🔐 Overcomplicated Login System")

if st.session_state.step == 1:
    st.subheader("Step 1: Solve the 3x3 Rubik's Cube")
    if "grid" not in st.session_state:
        st.session_state.grid = ["⬜"] * 9

    cols = st.columns(3)
    for i in range(9):
        if cols[i % 3].button(st.session_state.grid[i], key=f"btn_{i}"):
            st.session_state.grid[i] = "🟩" if st.session_state.grid[i] != "🟩" else "⬜"

    if all(cell == "🟩" for cell in st.session_state.grid):
        st.success("Rubik’s Cube solved! Proceeding to Step 2...")
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.subheader("Step 2: Make a Funny Face")
    img = st.camera_input("Take a funny face selfie")
    if img:
        bytes_data = img.getvalue()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            st.success("Funny face detected!")
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("No face detected. Try again with exaggeration!")

elif st.session_state.step == 3:
    st.subheader("Step 3: Enter Morse Password (Reversed)")
    st.write("Hint: password 'hi' → reversed → '.. ....'")

    morse = ".. ...."
    user_input = st.text_input("Enter Morse:")
    if st.button("Submit"):
        if user_input.strip() == morse:
            st.success("Access Granted! Redirecting...")
            time.sleep(2)
            st.switch_page("pages/StandingGuy.py")
        else:
            st.error("Wrong Morse. Try again.")