import streamlit as st
import base64

st.set_page_config(page_title="DaWave Fanmily", page_icon="👍", layout="centered")

# ---- CSS & Animation ----
st.markdown("""
    <style>
    body {
        background-color: white;
    }
    .spin-emoji {
        font-size: 100px;
        animation: spin-shrink 2s forwards;
        display: flex;
        justify-content: center;
    }
    @keyframes spin-shrink {
        0% { transform: rotate(0deg) scale(1); opacity: 1; }
        100% { transform: rotate(720deg) scale(0.2); opacity: 1; margin-top: -80px;}
    }
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    .top-emoji {
        font-size: 30px;
        margin-top: -10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Initial spinning emoji ----
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    st.markdown('<div class="spin-emoji">👍👍</div>', unsafe_allow_html=True)
    st.session_state.loaded = True

# ---- Title with small emoji ----
st.markdown("""
<div class="title-container">
    <div class="top-emoji">👍👍</div>
    <h1>DaWave Fanmily</h1>
</div>
""", unsafe_allow_html=True)

# ---- Helper for playing sound ----
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# ---- Buttons ----
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Good Song"):
        autoplay_audio("fart.mp3")  # <- put your fart.mp3 in same folder

with col2:
    if st.button("Cute Pic"):
        st.image("mirror.jpg", caption="Mirror")  # <- replace with your mirror image

with col3:
    if st.button("Ramon"):
        st.image("bald_old_man.jpg", caption="Ramon")  # <- replace with your image

with col4:
    if st.button("Nice"):
        st.markdown("""
        <div class="spin-emoji" style="font-size:60px; animation: spin-shrink 1.5s forwards; opacity:0.2;">
            👍
        </div>
        """, unsafe_allow_html=True)
