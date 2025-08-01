import streamlit as st
from PIL import Image
from utils.pappadam import check_pappadam_roundness

import os

# Temp folder for uploaded images
os.makedirs("temp", exist_ok=True)

st.title("🥠 Chappathi Roundness Checker")

uploaded = st.file_uploader("Upload a Chappathi photo", type=["jpg", "png", "jpeg"])
if uploaded:
    st.image(uploaded, width=300)
    with open("temp.jpg", "wb") as f:
        f.write(uploaded.read())

    result = check_pappadam_roundness("temp.jpg")
    st.success(result)
