# import streamlit as st
# from utils.nickname import generate_naadan_nickname

# import os

# # Temp folder for uploaded images
# os.makedirs("temp", exist_ok=True)

# st.header("1. Naadan Nickname Generator")
# name = st.text_input("Enter your name:")
# if st.button("Get Naadan Nickname"):
#     nickname = generate_naadan_nickname(name)
#     st.success(f"Your Naadan Nickname is: {nickname}")





import streamlit as st
import random
import time
import os
from utils.nickname import generate_naadan_nickname

# ---------- SETUP ----------
st.set_page_config(page_title="Naadan Nickname Generator", page_icon="🔥")
os.makedirs("temp", exist_ok=True)

# ---------- STYLES ----------
st.markdown("""
    <style>
    .nickname {
        font-size: 2em;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- AUDIO SNIPPET ----------
def play_audio():
    st.markdown("""
        <audio autoplay>
            <source src="https://www.myinstants.com/media/sounds/myre.mp3" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

# ---------- AI-STYLE NICKNAME GENERATOR ----------
# def generate_naadan_nickname(name):
#     prefixes = ["Aalakkaran", "Kattanchadi", "Mass", "Thallippoli", "Porali", "Vibeeshi", "Kambi"]
#     suffixes = ["Boss", "Mon", "Chekkan", "Appan", "Bro", "Kannappan", "Kutta"]
    
#     if not name:
#         return "Poda Perillatha!"

#     name = name.strip().capitalize()
#     prefix = random.choice(prefixes)
#     suffix = random.choice(suffixes)

#     nickname = f"{prefix} {name} {suffix}"
#     return nickname

# ---------- UI ----------
st.title("🔥 Naadan Nickname Generator")
st.write("_Reveal your inner naadan vibes with a savage nickname!_ 💪")

user_name = st.text_input("Enter your name:")

if st.button("Reveal My Naadan Nickname ✨"):
    if user_name.strip() == "":
        st.error("Myre! Name kodukkada?")
    else:
        with st.spinner("Cooking up something spicy... 🌶️"):
            time.sleep(2)
            nickname = generate_naadan_nickname(user_name)
            st.markdown(f"<p class='nickname'>{nickname}</p>", unsafe_allow_html=True)
            play_audio()
            st.balloons()

        # Optional funny GIF
        st.image("https://media.tenor.com/oRff0AyYzL4AAAAM/mass-entry-thalapathy.gif", caption="Aaru ithu? Naadan Style! 😎", use_column_width=True)
