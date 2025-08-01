# updated_app.py - Stylish Multi-Page Naadan Vibes

import streamlit as st
import os

st.set_page_config(
    page_title="Naadan Vibes",
    page_icon="🔥",
    layout="wide"
)

# Inject custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
        }
        .title {
            text-align: center;
            font-size: 3em;
            color: #ff4500;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #ffffff;
            margin-bottom: 20px;
        }
        .block-box {
            background-color: rgba(127, 127, 127, 0.8);
            padding: 20px;
            margin: 15px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            cursor: pointer;
            text-decoration: none;
            color: inherit;
            display: block;
        }
        .block-box h3 {
        color: white;
        }
        .block-box p {
            color: white;
        }
        .block-box:hover {
            background-color: rgba(127, 127, 127, 0.9);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title">🔥 Naadan Vibes 🔥</div>
<div class="subtitle">
    The most uselessly fun app ever built with love & coconut oil 🥥
</div>
""", unsafe_allow_html=True)

# Main layout in columns for homepage preview
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <a href="/Nickname" target="_self" style="text-decoration: none;">
        <div class="block-box">
            <h3>🧡 1. Naadan Nickname Generator</h3>
            <p>Discover your true local legend identity based on your name.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    <a href="/KanappiScore" target="_self" style="text-decoration: none;">
        <div class="block-box">
            <h3>😈 2. Kanappi Score Analyzer</h3>
            <p>Upload your selfie to know your inner Kanappi vibes.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    <a href="/Proposal" target="_self" style="text-decoration: none;">
        <div class="block-box">
            <h3>💘 3. Proposal Success Meter</h3>
            <p>Type the names of both and find out what is hidden between you guys.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/Holes" target="_self" style="text-decoration: none;">
        <div class="block-box">
            <h3>🍟 4. Vada Hole Size Estimator</h3>
            <p>How holy is your Parippu Vada? Upload and find out.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    <a href="/Roundness" target="_self" style="text-decoration: none;">
        <div class="block-box">
            <h3>🥠 5. Chappathi Roundness Checker</h3>
            <p>Is your Chappathi perfectly round? Let's judge it!</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
        <a href="/Login" target="_self" style="text-decoration: none;">
            <div class="block-box">
                <h3>🌟 Bonus: Click Here and See the Magic Inside!</h3>
                <p>Start your journey through the most overcomplicated login ever!</p>
            </div>
        </a>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<hr>
<p style="text-align:center; color: gray;">Built by the Naadan ML Gang</p>
""", unsafe_allow_html=True)

# Ensure temp folder exists
os.makedirs("temp", exist_ok=True)












# # updated_app.py - Stylish Multi-Page Naadan Vibes

# import streamlit as st
# import os

# st.set_page_config(
#     page_title="Naadan Vibes",
#     page_icon="🔥",
#     layout="wide"
# )

# # Inject custom CSS
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
#         }
#         .title {
#             text-align: center;
#             font-size: 3em;
#             color: #ff4500;
#             font-weight: bold;
#             margin-bottom: 10px;
#         }
#         .subtitle {
#             text-align: center;
#             font-size: 1.2em;
#             color: #444;
#             margin-bottom: 20px;
#         }
#         .block-box {
#             background-color: rgba(127, 127, 127, 0.8);
#             padding: 20px;
#             margin: 15px;
#             border-radius: 15px;
#             box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div class="title">🔥 Naadan Vibes 🔥</div>
# <div class="subtitle">
#     The most uselessly fun ML-powered app ever built with love & coconut oil 🥥
# </div>
# """, unsafe_allow_html=True)

# # Main layout in columns for homepage preview
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("""
#     <div class="block-box">
#         <h3>🧡 1. Naadan Nickname Generator</h3>
#         <p>Discover your true local legend identity based on your name.</p>
#         <a href="/Nickname" target="_self">Try it now ➔</a>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="block-box">
#         <h3>😈 2. Kanappi Score Analyzer</h3>
#         <p>Upload your selfie to know your inner Kanappi vibes.</p>
#         <a href="/Kanappi%20Score" target="_self">Analyze Score ➔</a>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="block-box">
#         <h3>🍟 3. Vada Hole Size Estimator</h3>
#         <p>How holy is your Parippu Vada? Upload and find out.</p>
#         <a href="/Holes" target="_self">Measure Hole ➔</a>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="block-box">
#         <h3>🥠 4. Pappadam Roundness Checker</h3>
#         <p>Is your Pappadam perfectly round? Let's judge it!</p>
#         <a href="/Roundness" target="_self">Check Roundness ➔</a>
#     </div>
#     """, unsafe_allow_html=True)

# # Footer
# st.markdown("""
# <hr>
# <p style="text-align:center; color: gray;">Built with 🚀 by the Naadan ML Gang</p>
# """, unsafe_allow_html=True)

# # Ensure temp folder exists
# os.makedirs("temp", exist_ok=True)












# import streamlit as st
# from utils.nickname import generate_naadan_nickname
# from utils.kanappi import kanappi_score_from_image
# from utils.vada_hole import analyze_vada_hole
# from utils.pappadam import check_pappadam_roundness
# import os

# # Temp folder for uploaded images
# os.makedirs("temp", exist_ok=True)

# st.set_page_config(page_title="Naadan Life Evaluator 3000™")
# st.title("🧠 Naadan Life Evaluator 3000™")

# # Nickname Generator
# st.header("1. Naadan Nickname Generator")
# name = st.text_input("Enter your name:")
# if st.button("Get Naadan Nickname"):
#     nickname = generate_naadan_nickname(name)
#     st.success(f"Your Naadan Nickname is: {nickname}")

# # Kanappi Score
# st.header("2. Kanappi Score Analyzer")
# kanappi_file = st.file_uploader("Upload your selfie", type=["jpg", "jpeg", "png"])
# if kanappi_file:
#     temp_path = os.path.join("temp", "temp_selfie.jpg")
#     with open(temp_path, "wb") as f:
#         f.write(kanappi_file.read())
#     score, comment = kanappi_score_from_image(temp_path)
#     st.success(f"Kanappi Score: {score}/100 – {comment}")

# # Vada Hole Size Analyzer
# st.header("3. Parippu Vada Hole Size Analyzer")
# vada_file = st.file_uploader("Upload a Parippu Vada image", type=["jpg", "jpeg", "png"])
# if vada_file:
#     temp_path = os.path.join("temp", "temp_vada.jpg")
#     with open(temp_path, "wb") as f:
#         f.write(vada_file.read())
#     result = analyze_vada_hole(temp_path)
#     st.info(result)

# # Pappadam Roundness Analyzer
# st.header("4. Pappadam Roundness Index")
# pap_file = st.file_uploader("Upload a Pappadam image", type=["jpg", "jpeg", "png"])
# if pap_file:
#     temp_path = os.path.join("temp", "temp_pap.jpg")
#     with open(temp_path, "wb") as f:
#         f.write(pap_file.read())
#     result = check_pappadam_roundness(temp_path)
#     st.warning(result)
