import streamlit as st

# تنظیمات اصلی صفحه برای حذف حاشیه‌ها و اسکرول
st.set_page_config(
    page_title="UONA STUDIO | Control Panel",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تزریق CSS برای استایل اختصاصی حسین یزدی (UONA STUDIO)
st.markdown("""
    <style>
    /* حذف اسکرول و تنظیمات کلی */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0a0a0a !important;
        overflow: hidden !important;
        height: 100vh;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* 1. هدر با تایتل سفید درخشان */
    .uona-header {
        color: #ffffff;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        font-size: 40px;
        letter-spacing: 5px;
        text-shadow: 0 0 15px rgba(255,255,255,0.8), 0 0 30px rgba(255,255,255,0.4);
        padding: 20px 0;
        margin-top: -50px;
    }

    /* 2. پورتال فیروزه‌ای با متن مشکی */
    div.stButton > button {
        background-color: #00f2ff !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 0px !important;
        font-weight: 900 !important;
        width: 100%;
        height: 50px;
        transition: 0.4s;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background-color: #ffffff !important;
        box-shadow: 0 0 20px #00f2ff !important;
    }

    /* استایل فرم و فیلدها */
    .stTextInput input, .stSelectbox div {
        background-color: rgba(255,255,255,0.05) !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    
    label {
        color: #00f2ff !important;
        font-size: 13px !important;
        font-weight: 300 !important;
    }

    /* 4. فوتر مینی‌مال غیر بولد */
    .uona-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #444;
        font-size: 11px;
        padding: 10px;
        font-weight: normal;
        background: #0a0a0a;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Header
st.markdown('<h1 class="uona-header">UONA STUDIO</h1>', unsafe_allow_html=True)

# 2. Portal (4 Buttons)
p_col1, p_col2, p_col3, p_col4 = st.columns(4)
with p_col1: st.button("CHARACTER DESIGN")
with p_col2: st.button("SFX LIBRARY")
with p_col3: st.button("PRODUCTION")
with p_col4: st.button("AI ENGINE")

st.markdown("<br>", unsafe_allow_html=True)

# 3. Form - 15 Sections
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("Project Name", key="f1")
        st.text_input("Artist", value="Hossein Yazdi", key="f2")
        st.selectbox("Category", ["SFX Makeup", "Character Design", "VFX Base"], key="f3")
        st.text_input("Camera", placeholder="e.g. ARRI Alexa Mini", key="f4") # Camera
        st.text_input("Pic Size", placeholder="e.g. 8192 x 4320", key="f5") # Pic Size
        st.text_input("Lens Type", key="f6")
        st.text_input("Lighting Setup", key="f7")
        st.text_input("Skin Texture Detail", key="f8")

    with col2:
        st.text_input("Color Grade Profile", key="f9")
        st.text_input("Environment / HDRI", key="f10")
        st.text_input("Shutter Speed", key="f11")
        st.text_input("ISO", key="f12")
        st.text_input("Frame Rate (FPS)", key="f13")
        st.text_input("Render Engine", key="f14")
        st.text_input("Export Format", key="f15")

# 4. Footer
st.markdown('<div class="uona-footer">© 2026 UONA STUDIO | CINEMATIC MAKEUP DESIGN | POWERED BY HOSSEIN YAZDI</div>', unsafe_allow_html=True)
