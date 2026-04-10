import streamlit as st
from datetime import datetime

# 1. تنظیمات پایه و حذف اسکرول
st.set_page_config(page_title="UONA STUDIO | AI SYSTEM", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700&display=swap');
    
    /* قفل کردن صفحه برای جلوگیری از اسکرول */
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh;
        overflow: hidden !important;
    }
    
    #MainMenu, footer, header {visibility: hidden;}

    /* هدر مینی‌مال و خوانا */
    .nav-bar {
        display: flex;
        align-items: center;
        padding: 10px 40px;
        background: rgba(2, 6, 12, 0.8);
        border-bottom: 1px solid rgba(0, 242, 255, 0.2);
        justify-content: space-between;
    }
    .nav-title { 
        font-family: 'Cinzel'; color: #ffffff; font-size: 3rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; text-shadow: 0 0 20px rgba(0, 242, 255, 0.3);
    }
    .nav-slogan { font-family: 'Montserrat'; color: #00f2ff; font-size: 0.7rem; letter-spacing: 5px; opacity: 0.8; text-transform: uppercase; }

    /* کارت‌های پورتال */
    .module-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: 0.3s;
        backdrop-filter: blur(10px);
    }
    .module-card:hover { border-color: #00f2ff; background: rgba(0, 242, 255, 0.05); }
    
    /* تنظیمات فرم برای جا شدن در صفحه */
    .stSelectbox { margin-bottom: -10px !important; }
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.75rem; margin-bottom: 2px; }
    .star { color: #ff4b4b; }
    
    .master-box { 
        background-color: #ffffff; color: #111; padding: 20px; border-radius: 8px; 
        border-left: 8px solid #00f2ff; font-family: 'Montserrat'; font-size: 1rem; 
        line-height: 1.6; height: 400px; overflow-y: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# مدیریت صفحات
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- هدر ثابت با قابلیت آپلود لوگو ---
h_col1, h_col2 = st.columns([1, 5])
with h_col1:
    try:
        st.image("image.png", width=90) # فایل لوگوی خودت را با این نام آپلود کن
    except:
        st.markdown("<div style='width:80px; height:80px; background:#00f2ff; border-radius:10px;'></div>", unsafe_allow_html=True)
with h_col2:
    st.markdown('<h1 class="nav-title">UONA STUDIO</h1><div class="nav-slogan">Cinematic Character Intelligence</div>', unsafe_allow_html=True)

# --- صفحه اصلی (PORTAL) ---
if st.session_state.page == 'home':
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    modules = [("🎬", "CINEMATIC", "cine"), ("📺", "SERIES", "cine"), ("🎭", "THEATER", "soon"), ("👠", "FASHION", "soon")]
    
    for idx, (icon, name, target) in enumerate(modules):
        with [c1, c2, c3, c4][idx]:
            st.markdown(f'<div class="module-card"><h1 style="font-size:3rem;">{icon}</h1><h3>{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"ENTER {name}", key=name):
                    st.session_state.page = 'cinematic'; st.rerun()
            else:
                st.button("COMING SOON", disabled=True, key=name)

# --- بخش Cinematic با طبقه بندی SFX ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    
    # دیتابیس طبقه بندی شده SFX
    sfx_categories = {
        "Acute Trauma (جراحت حاد)": ["Fresh Katana/Sword Slash", "Glass Laceration with Shards", "Blunt Force Contusion", "Chemical Acid Burn"],
        "Healing Stages (مراحل بهبودی)": ["3-Day Old Wound (Scabbing)", "1-Week Old Wound (Granulation)", "1-Month Old Scar"],
        "Bruising (کبودی)": ["Fresh Periorbital Hematoma", "24-Hour Old Bruise", "3-Day Old Bruise", "15-Day Old Fading Bruise"],
        "Skin Conditions (مشکلات پوستی)": ["1st Degree Sunburn", "2nd Degree Burn", "Bilateral Vitiligo", "Diffuse Hyperpigmentation"]
    }

    col_form, col_master = st.columns([1.8, 1])
    
    with col_form:
        f1, f2 = st.columns(2)
        with f1:
            actor = st.selectbox("Actor Reference *", ["None", "No", "Yes"])
            gender = st.selectbox("Gender *", ["Masculine / Male", "Feminine / Female", "Androgynous"])
            # طبقه بندی دوم در SFX
            sfx_cat = st.selectbox("SFX Category (طبقه بندی جراحت)", list(sfx_categories.keys()))
            sfx_type = st.selectbox("Specific Trauma (انتخاب جراحت)", sfx_categories[sfx_cat])
        with f2:
            age = st.selectbox("Age Range *", ["Elderly", "Middle-aged", "Young Adult", "Adolescent"])
            nat = st.selectbox("Nationality *", ["Iranian", "Emirati", "Saudi", "European", "African"])
            groom = st.selectbox("Grooming", ["Clean Shaven", "Full Beard", "Stubble"])

    # فرمول Master Prompt
    final_p = f"A professional cinematic portrait of a {gender} {age} {nat}. Character: {actor}. SFX Detail: {sfx_type}. 8k, subsurface scattering, raw photo."

    with col_master:
        st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)

# فوتر مینی‌مال
st.markdown(f"<div style='position:fixed; bottom:10px; width:100%; text-align:center; color:white; opacity:0.5; font-size:0.7rem;'>© {datetime.now().year} UONA GROUP | ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
