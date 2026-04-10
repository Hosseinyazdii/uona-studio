import streamlit as st

# تنظیمات صفحه برای حذف اسکرول و ظاهر مدرن
st.set_page_config(page_title="UONA STUDIO", layout="wide", initial_sidebar_state="collapsed")

# تزریق CSS برای اعمال استایل‌های اختصاصی شما
st.markdown("""
    <style>
    /* حذف اسکرول و تنظیم پس‌زمینه */
    .main {
        background-color: #0a0a0a;
        overflow: hidden;
    }
    
    /* 1. هدر با تایتل سفید درخشان */
    .shiny-header {
        color: #ffffff;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255,255,255,0.8), 0 0 20px rgba(255,255,255,0.4);
        padding: 10px;
        margin-bottom: 20px;
    }

    /* 2. دکمه‌های مشکی روی فیروزه‌ای */
    .stButton>button {
        background-color: #00f2ff;
        color: black;
        border-radius: 0px;
        border: none;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        box-shadow: 0 0 15px #00f2ff;
    }

    /* 4. فوتر مینی‌مال غیر بولد */
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 12px;
        color: #666;
        font-weight: 300; /* غیر بولد */
    }
    
    /* استایل فیلدهای ورودی */
    input {
        background-color: rgba(255,255,255,0.05) !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. نمایش هدر
st.markdown('<div class="shiny-header">UONA STUDIO</div>', unsafe_allow_html=True)

# 2. پورتال ۴ تایی
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("CHARACTER DESIGN")
with col2: st.button("SFX LIBRARY")
with col3: st.button("PRODUCTION")
with col4: st.button("AI ENGINE")

st.write("---")

# 3. فرم کامل با ۱۵ بخش در دو ستون
col_a, col_b = st.columns(2)

with col_a:
    project = st.text_input("Project Name")
    artist = st.text_input("Artist")
    category = st.selectbox("Category", ["SFX", "Cinematic", "Cyberpunk"])
    camera = st.text_input("Camera") # اضافه شده
    pic_size = st.text_input("Pic Size") # اضافه شده
    lens = st.text_input("Lens Type")
    lighting = st.text_input("Lighting")
    skin = st.text_input("Skin Texture")

with col_b:
    color_grade = st.text_input("Color Grade")
    env = st.text_input("Environment")
    shutter = st.text_input("Shutter Speed")
    iso = st.text_input("ISO")
    fps = st.text_input("Frame Rate")
    engine = st.text_input("Render Engine")
    fmt = st.text_input("Export Format")

# دکمه نهایی ثبت
if st.button("GENERATE DATA"):
    st.success("Character Data Processed!")

# 4. فوتر
st.markdown('<div class="footer">© 2026 UONA STUDIO | All Rights Reserved | Powered by Hossein Yazdi</div>', unsafe_allow_html=True)
