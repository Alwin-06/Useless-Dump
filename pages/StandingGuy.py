import streamlit as st
import random
import time

st.set_page_config(page_title="Standing Guy", page_icon="🧍")

st.title("🧍 The Virtual Standing Guy")
st.image("https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif", width=200)

# 🔁 Embed with max minimal YouTube branding allowed
st.markdown("""
<iframe width="560" height="315"
src="https://www.youtube.com/embed/SXHMnicI6Pg?autoplay=1&controls=0&loop=1&playlist=SXHMnicI6Pg&modestbranding=1&rel=0&showinfo=0"
frameborder="0"
allow="autoplay; encrypted-media"
allowfullscreen>
</iframe>
""", unsafe_allow_html=True)

# Status message that changes every minute
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

if "status" not in st.session_state:
    st.session_state.status = "Still standing."

status_list = [
    "Still standing.",
    "Knees hurt a bit.",
    "Thinking about lunch.",
    "Why am I here?",
    "Wind is strong today...",
    "Contemplating life."
]

if time.time() - st.session_state.last_update > 60:
    st.session_state.status = random.choice(status_list)
    st.session_state.last_update = time.time()

st.markdown(f"### {st.session_state.status}")
