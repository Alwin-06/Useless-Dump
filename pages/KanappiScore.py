import streamlit as st
from utils.kanappi import kanappi_score_from_image
import os
from PIL import Image

# Temp folder for uploaded images
os.makedirs("temp", exist_ok=True)

# Stylish header
st.markdown("## 🕶️ Kanappi Score Analyzer")
st.caption("Upload your selfie and discover how much 'Kanappi' vibe you give off!")

# File uploader
kanappi_file = st.file_uploader("📸 Upload your stylish selfie", type=["jpg", "jpeg", "png"])

if kanappi_file:
    temp_path = os.path.join("temp", "temp_selfie.jpg")
    
    # Save uploaded image
    # with open(temp_path, "wb") as f:
    #     f.write(kanappi_file.read())

    image = Image.open(kanappi_file).convert("RGB")
    image.save(temp_path)


    # Preview uploaded selfie
    st.image(temp_path, caption="Here's your vibe check selfie 👀", width=300)

    # Run Kanappi score logic
    try:
        score, comment = kanappi_score_from_image(temp_path)

        # Fancy result display
        st.markdown(f"""
        <div style="background-color:#f0f0f5;padding:15px;border-radius:10px;margin-top:15px">
            <h4>💯 Your Kanappi Score: <span style='color:#e63946'>{score}/100</span></h4>
            <p>🗯️ <i>{comment}</i></p>
        </div>
        """, unsafe_allow_html=True)

        if score >= 70:
            st.balloons()

    except Exception as e:
        st.error(f"😅 Oops! Couldn't analyze the selfie properly. Try another image.\n\nError: {str(e)}")















# import streamlit as st
# from utils.kanappi import kanappi_score_from_image
# from streamlit_extras.let_it_rain import rain
# import random
# import os

# # Create a temporary folder if not exists
# os.makedirs("temp", exist_ok=True)

# st.set_page_config(page_title="Kanappi Score Analyzer", page_icon="🔥")

# # Title
# st.markdown("""
#     <h1 style='text-align: center; color: #ff4b4b;'>🔥 Kanappi Score Analyzer 🔥</h1>
#     <p style='text-align: center;'>Upload your selfie to see how much of a <strong>Kanappi</strong> you are 😉</p>
# """, unsafe_allow_html=True)

# # File uploader
# kanappi_file = st.file_uploader("📸 Upload your most confident selfie (or worst...)", type=["jpg", "jpeg", "png"])

# if kanappi_file:
#     # Save temporarily
#     temp_path = os.path.join("temp", "temp_selfie.jpg")
#     with open(temp_path, "wb") as f:
#         f.write(kanappi_file.read())

#     # Show uploaded image
#     st.image(temp_path, caption="🧍‍♂️ That's you, myree!", width=250)

#     # Score from image
#     score, comment = kanappi_score_from_image(temp_path)

#     # Display score visually
#     st.subheader(f"🎯 Kanappi Score: `{score}/100`")
#     st.progress(score)

#     # Add Rain/Confetti
#     if score >= 80:
#         rain(emoji="🔥", font_size=40, falling_speed=7, animation_length="infinite")
#     elif score >= 50:
#         rain(emoji="🕶️", font_size=35, falling_speed=4, animation_length=3)
#     else:
#         rain(emoji="💩", font_size=40, falling_speed=5, animation_length=3)

#     # Funny reaction images
#     if score >= 85:
#         st.image("https://media.giphy.com/media/3orieQEA4ofp1tqT3m/giphy.gif", caption="Full power Kanappi!🔥")
#     elif score >= 60:
#         st.image("https://media.giphy.com/media/LMcB8XospGZO8UQq87/giphy.gif", caption="Mone… stylish aanu! 😎")
#     elif score >= 30:
#         st.image("https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif", caption="Mone… Kurachu work cheyyam da! 🧐")
#     else:
#         st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", caption="Myree… ithu onnumalla 💀")

#     # Naadan commentary
#     naadan_comments = [
#         "Myree! Ithaanallo style.",
#         "Kure mass aanu nee!",
#         "Pattichu nilkku! Full kanappi.",
#         "Enthina da oru attittam!",
#         "Style ullu, but confidence kurav aanu!",
#         "Myre... enthina itra over confidence?",
#         "PSC padikkende da ithinte shesham."
#     ]
#     st.info(f"🗣️ {random.choice(naadan_comments)}")

#     st.success(f"🧠 AI Analysis Comment: {comment}")
