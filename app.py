import streamlit as st
from datetime import datetime
import os

# 1. تنظیمات پایه و حذف اسکرول
st.set_page_config(page_title="UONA STUDIO | AI PLATFORM", layout="wide", initial_sidebar_state="collapsed")

# 2. استایل اختصاصی نئونی
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh; overflow: hidden !important;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    /* استایل نئونی تایتل */
    .title-main {
        font-family: 'Cinzel'; color: #ffffff !important; font-size: 3.2rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
    }

    /* اصلاح رنگ متون ورودی و لیبل‌ها برای خوانایی ۱۰۰٪ */
    label, .stMarkdown p, .label-text { 
        color: #00e5ff !important; 
        font-family: 'Montserrat' !important; font-weight: 700 !important; 
        text-transform: uppercase !important; font-size: 0.75rem !important; 
    }
    
    /* استایل رادیو باتن (Login/Register) */
    .stRadio div[role="radiogroup"] {
        background: rgba(0, 242, 255, 0.05); padding: 10px; border-radius: 10px; border: 1px solid rgba(0, 242, 255, 0.2);
    }

    .stButton > button {
        background-color: #00f2ff !important; color: #000000 !important;
        border: none !important; border-radius: 12px !important;
        font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.02); }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px; padding: 25px; text-align: center; backdrop-filter: blur(15px);
    }
    .module-title { font-family: 'Cinzel'; color: white; text-shadow: 0 0 10px rgba(255, 255, 255, 0.4); }

    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 10px; font-weight: 900; border-radius: 12px 12px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { background-color: #ffffff; color: #111; padding: 20px; border-radius: 0 0 12px 12px; border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; line-height: 1.5; height: 350px; overflow-y: auto; }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; background: rgba(0,0,0,0.6); color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem; }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# 3. مدیریت دیتابیس پایدار یوزرها در Session State
if 'users_registry' not in st.session_state:
    st.session_state.users_registry = {"hossein": "1234"}
if 'auth_status' not in st.session_state: st.session_state.auth_status = False
if 'history' not in st.session_state: st.session_state.history = []
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- پورتال لاگین با اصلاح رنگ و استایل ---
if not st.session_state.auth_status:
    col_l, col_r = st.columns([1, 1.2])
    with col_l:
        st.markdown("<br><br>", unsafe_allow_html=True)
        # استفاده از لوگوی آپلود شده
        if os.path.exists("image.png"): st.image("image.png", width=250)
    with col_r:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px; text-shadow: 0 0 15px #00f2ff;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        mode = st.radio("SELECT MODE", ["Login", "Register"], horizontal=True)
        u_name = st.text_input("USERNAME", placeholder="Enter your username...")
        u_pass = st.text_input("PASSWORD", type="password", placeholder="Enter your password...")
        
        if mode == "Login":
            if st.button("SIGN IN"):
                if u_name in st.session_state.users_registry and st.session_state.users_registry[u_name] == u_pass:
                    st.session_state.auth_status = True; st.session_state.user = u_name; st.rerun()
                else: st.error("Access Denied: Invalid Credentials")
        else:
            if st.button("CREATE ACCOUNT"):
                if u_name and u_pass:
                    st.session_state.users_registry[u_name] = u_pass
                    st.success(f"User '{u_name}' Registered! Switch to Login to enter.")
    st.stop()

# --- هدر اصلی ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("image.png"): st.image("image.png", width=85)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- صفحه پورتال ---
if st.session_state.page == 'home':
    st.markdown("<br><br><h3 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:4px;'>SELECT MODULE</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    modules = [("🎬", "MOVIE", "cine"), ("📺", "SERIES", "cine"), ("🎭", "THEATER", "soon"), ("👠", "FASHION", "soon")]
    for idx, (icon, name, target) in enumerate(modules):
        with [c1, c2, c3, c4][idx]:
            st.markdown(f'<div class="module-card"><h1>{icon}</h1><h3 class="module-title">{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"ENTER {name}", key=name): st.session_state.page = 'cinematic'; st.rerun()
            else: st.button("COMING SOON", disabled=True, key=name)

# --- ماژول Cinematic (۱۲ سوال کامل) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    t_builder, t_hist = st.tabs(["🏗️ PROMPT BUILDER", "📜 HISTORY"])

    with t_builder:
        def add_n(d): return ["None"] + d + ["Others"]
        
        c_form, c_master = st.columns([2.2, 1])
        with c_form:
            f1, f2, f3 = st.columns(3)
            with f1:
                actor = st.selectbox("Actor Ref *", ["None", "No", "Yes"])
                gen = st.selectbox("Gender *", ["Male", "Female", "Androgynous"])
                age = st.selectbox("Age Range *", ["Elderly", "Middle-aged", "Young Adult", "Child"])
                h_col = st.selectbox("Hair Color", add_n(["Jet Black", "Espresso", "Ash Blonde", "Salt & Pepper"]))
            with f2:
                nat = st.selectbox("Nationality *", add_n(["Iranian", "Saudi", "European", "African"]))
                era = st.selectbox("Era / Period", add_n(["Ancient", "Medieval", "100 Years Ago", "Contemporary"]))
                sfx = st.selectbox("Trauma / SFX", add_n(["Katana Slash", "Bruise", "Glass Wound", "Burn"]))
                mat = st.selectbox("Material Finish", add_n(["Silicone", "Matte Sealer", "Alcohol Palette"]))
            with f3:
                char = st.selectbox("Character Concept", add_n(["Warrior", "Villain", "Scholar", "Royal"]))
                groom = st.selectbox("Grooming Style", add_n(["Clean Shaven", "Full Beard", "Stubble", "Goatee"]))
                cam = st.selectbox("Camera & Lens *", add_n(["85mm", "100mm Macro", "35mm Low-Angle"]))
                light = st.selectbox("Lighting Style", add_n(["Rembrandt", "Teal & Orange", "Neon"]))
                size = st.selectbox("Frame Size", add_n(["4:5", "16:9", "2.39:1", "1:1"]))

        final_p = f"Professional cinematic portrait, {size}, {gen}, {age}, {nat}. Concept: {char}, {groom}. Hair: {h_col}. SFX: {sfx}. Material: {mat}. Tech: {cam}, {light}, 8k raw photo."

        with c_master:
            st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)
            p_name = st.text_input("Project Name:")
            if st.button("💾 SAVE TO HISTORY"):
                if p_name:
                    st.session_state.history.insert(0, {"user": st.session_state.user, "name": p_name, "time": datetime.now().strftime("%Y-%m-%d %H:%M"), "prompt": final_p})
                    st.success("Design Saved!")

    with t_hist:
        u_h = [h for h in st.session_state.history if h["user"] == st.session_state.user]
        if not u_h: st.info("No saved designs in this session.")
        for item in u_h:
            with st.expander(f"📌 {item['name']} | {item['time']}"):
                st.code(item['prompt'])

st.markdown(f"<div class='footer'>© {datetime.now().year} <span class='uona-tag'>UONA GROUP</span>. ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
