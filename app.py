import streamlit as st
from datetime import datetime
import os

# 1. تنظیمات پایه
st.set_page_config(page_title="UONA STUDIO | AI PLATFORM", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh; overflow: hidden !important;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    .title-main {
        font-family: 'Cinzel'; color: #00f2ff !important; font-size: 3rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; 
        text-shadow: 0 0 20px rgba(0, 242, 255, 0.9), 0 0 10px rgba(255, 255, 255, 0.4);
    }

    .stButton > button {
        background-color: #00f2ff !important; color: #000000 !important;
        border: none !important; border-radius: 12px !important;
        font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    }
    
    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px; padding: 25px; text-align: center; backdrop-filter: blur(15px);
    }

    .label-text { color: #00f2ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.65rem; margin-top: 4px; }
    .master-box { background-color: #ffffff; color: #111; padding: 20px; border-radius: 12px; border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 1rem; line-height: 1.6; height: 320px; overflow-y: auto; }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; background: rgba(0,0,0,0.6); color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem; }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# --- مدیریت دیتابیس موقت (تا قبل از وصل شدن به دیتابیس واقعی) ---
if 'users_db' not in st.session_state:
    st.session_state.users_db = {"hossein": "1234", "uona": "2024"} # اکانت‌های دائمی در کد

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'history_log' not in st.session_state:
    st.session_state.history_log = []

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# --- منطق لاگین ---
if not st.session_state.authenticated:
    c_login1, c_login2 = st.columns([1, 1.2])
    with c_login1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=220)
    with c_login2:
        st.markdown("<h1 style='color:#00f2ff; font-family:Cinzel; margin-top:80px;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        tab_log, tab_reg = st.tabs(["LOGIN", "CREATE ACCOUNT"])
        
        with tab_log:
            u_name = st.text_input("Username", key="login_u")
            u_pass = st.text_input("Password", type="password", key="login_p")
            if st.button("SIGN IN"):
                if u_name in st.session_state.users_db and st.session_state.users_db[u_name] == u_pass:
                    st.session_state.authenticated = True
                    st.session_state.user_now = u_name
                    st.rerun()
                else:
                    st.error("Invalid Username or Password")
        
        with tab_reg:
            new_u = st.text_input("New Username", key="reg_u")
            new_p = st.text_input("New Password", type="password", key="reg_p")
            if st.button("REGISTER"):
                if new_u and new_p:
                    st.session_state.users_db[new_u] = new_p
                    st.success(f"User {new_u} registered! Please go to Login tab.")
                else:
                    st.warning("Please fill all fields.")
    st.stop()

# --- هدر اصلی ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("logo.PNG"): st.image("logo.PNG", width=85)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- محتوای پورتال ---
if st.session_state.current_page == 'home':
    st.markdown("<br><br><h3 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:4px;'>SELECT DESIGN MODULE</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    modules = [("🎬", "MOVIE", "cine"), ("📺", "SERIES", "cine"), ("🎭", "THEATER", "soon"), ("👠", "FASHION", "soon")]
    for idx, (icon, name, target) in enumerate(modules):
        with [c1, c2, c3, c4][idx]:
            st.markdown(f'<div class="module-card"><h1>{icon}</h1><h3 style="font-family:Cinzel; color:white; text-shadow: 0 0 10px rgba(255,255,255,0.5);">{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"ENTER {name}", key=f"btn_{name}"): 
                    st.session_state.current_page = 'cinematic'; st.rerun()
            else: st.button("COMING SOON", disabled=True, key=f"btn_{name}")

# --- ماژول Cinematic ---
elif st.session_state.current_page == 'cinematic':
    if st.button("← BACK"): st.session_state.current_page = 'home'; st.rerun()
    
    tab_build, tab_history = st.tabs(["🏗️ PROMPT BUILDER", "📜 HISTORY"])

    with tab_build:
        # دیتابیس (خلاصه برای جلوگیری از ارور، شما می‌توانید تمام ۳۹ مدل ریش را اینجا بگذارید)
        gen_opts = ["Male", "Female", "Androgynous"]
        age_opts = ["Elderly", "Middle-aged", "Young Adult", "Child"]
        nat_opts = ["Iranian", "Saudi", "European", "African", "Asian", "Others"]
        
        c_form, c_master = st.columns([2.1, 1])
        with c_form:
            f1, f2, f3 = st.columns(3)
            with f1:
                st.markdown('<p class="label-text">Actor & Identity</p>', unsafe_allow_html=True)
                actor = st.selectbox("Reference", ["None", "No", "Yes"])
                gender = st.selectbox("Gender", gen_opts)
                age = st.selectbox("Age", age_opts)
            with f2:
                st.markdown('<p class="label-text">Origin & SFX</p>', unsafe_allow_html=True)
                nat = st.selectbox("Nationality", nat_opts)
                sfx = st.selectbox("Trauma", ["None", "Katana Slash", "Bruise", "Others"])
                mat = st.selectbox("Material", ["Silicone", "Matte Sealer", "Others"])
            with f3:
                st.markdown('<p class="label-text">Technical</p>', unsafe_allow_html=True)
                cam = st.selectbox("Camera", ["85mm", "100mm Macro", "Others"])
                light = st.selectbox("Lighting", ["Rembrandt", "Neon", "Others"])
                size = st.selectbox("Size", ["4:5", "16:9", "1:1", "Others"])

        prompt_res = f"Professional cinematic portrait, {gender}, {age}, {nat}. SFX: {sfx}. Material: {mat}. Tech: {cam}, {light}, {size}, 8k raw photo."

        with c_master:
            st.markdown('<div style="background:#00f2ff; color:black; padding:10px; font-weight:900; text-align:center; border-radius:10px 10px 0 0;">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="master-box">{prompt_res}</div>', unsafe_allow_html=True)
            save_name = st.text_input("Project Name:")
            if st.button("💾 SAVE TO HISTORY"):
                if save_name:
                    st.session_state.history_log.insert(0, {"user": st.session_state.user_now, "name": save_name, "time": datetime.now().strftime("%H:%M"), "prompt": prompt_res})
                    st.success("Project Saved!")

    with tab_history:
        my_h = [h for h in st.session_state.history_log if h["user"] == st.session_state.user_now]
        if not my_h: st.info("No projects saved yet.")
        for item in my_h:
            with st.expander(f"📌 {item['name']} | {item['time']}"):
                st.code(item['prompt'])

st.markdown(f"<div class='footer'>© {datetime.now().year} <span class='uona-tag'>UONA GROUP</span>. ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
