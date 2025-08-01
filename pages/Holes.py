import streamlit as st
from utils.vada_hole import analyze_vada_hole
import os

# Temp folder for uploaded images
os.makedirs("temp", exist_ok=True)

st.header("3.Vada Hole Size Analyzer")
vada_file = st.file_uploader("Upload a Parippu Vada image", type=["jpg", "jpeg", "png"])
if vada_file:
    temp_path = os.path.join("temp", "temp_vada.jpg")
    with open(temp_path, "wb") as f:
        f.write(vada_file.read())
    result = analyze_vada_hole(temp_path)
    st.info(result)
