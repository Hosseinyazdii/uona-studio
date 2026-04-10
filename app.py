import streamlit as st
from datetime import datetime
import os

# 1. تنظیمات پایه و حذف اسکرول
st.set_page_config(page_title="UONA STUDIO | AI PLATFORM", layout="wide", initial_sidebar_state="collapsed")

# استایل اختصاصی نئونی و مدرن
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh;
        overflow: hidden !important;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    /* تایتل نئونی فیروزه‌ای روشن */
    .title-main {
        font-family: 'Cinzel'; color: #00f2ff !important; font-size: 3rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; 
        text-shadow: 0 0 20px rgba(0, 242, 255, 0.9), 0 0 10px rgba(255, 255, 255, 0.4);
    }

    /* دکمه‌های پورتال با متن مشکی و سایه سفید */
    .stButton > button {
        background-color: #00f2ff !important; color: #000000 !important;
        border: none !important; border-radius: 12px !important;
        font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
        transition: 0.3s;
    }
    .stButton > button:hover { background-color: #ffffff !important; box-shadow: 0 0 25px #00f2ff; transform: scale(1.02); }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px; padding: 25px; text-align: center; backdrop-filter: blur(15px);
    }
    .module-title {
        font-family: 'Cinzel'; color: white;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.6);
        letter-spacing: 3px;
    }

    /* استایل تب‌ها */
    .stTabs [data-baseweb="tab-list"] { gap: 50px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { 
        font-family: 'Cinzel'; color: white !important; font-size: 1.2rem !important; 
        border-bottom: 2px solid transparent !important;
    }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #00f2ff !important; color: #00f2ff !important; }

    .label-text { color: #00f2ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.7rem; margin-top: 5px; }
    
    .master-box { 
        background-color: #ffffff; color: #111; padding: 25px; border-radius: 12px; 
        border-left: 12px solid #00f2ff; font-family: 'Montserrat'; font-size: 1.1rem; 
        line-height: 1.7; height: 320px; overflow-y: auto; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    .footer { 
        position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; 
        border-top: 1px solid rgba(0, 242, 255, 0.1); background: rgba(0,0,0,0.6);
        color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem;
    }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; text-shadow: 0 0 10px rgba(255,255,255,0.5); }
    </style>
    """, unsafe_allow_html=True)

# --- سیستم مدیریت نشست و دیتابیس کاربران ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'users' not in st.session_state: st.session_state.users = {"hossein": "1234"} # یوزر پیش‌فرض
if 'history' not in st.session_state: st.session_state.history = []
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- صفحه لاگین ---
if not st.session_state.auth:
    col_l, col_r = st.columns([1, 1])
    with col_l:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=200)
    with col_r:
        st.markdown("<h1 style='color:#00f2ff; font-family:Cinzel;'>UONA LOGIN</h1>", unsafe_allow_html=True)
        mode = st.radio("Choose Mode", ["Login", "Create Account"], horizontal=True)
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        
        if mode == "Login":
            if st.button("ENTER PLATFORM"):
                if user in st.session_state.users and st.session_state.users[user] == pwd:
                    st.session_state.auth = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("Invalid Credentials")
        else:
            if st.button("REGISTER"):
                if user and pwd:
                    st.session_state.users[user] = pwd
                    st.success("Account Created! Please Login.")
                else: st.warning("Fill all fields.")
    st.stop()

# --- هدر پلتفرم ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("logo.PNG"): st.image("logo.PNG", width=85)
with h_col2:
    st.markdown(f'<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- محتوای اصلی ---
if st.session_state.page == 'home':
    st.markdown("<br><br><h3 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:4px;'>SELECT DESIGN MODULE</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    modules = [("🎬", "MOVIE", "cine"), ("📺", "SERIES", "cine"), ("🎭", "THEATER", "soon"), ("👠", "FASHION", "soon")]
    for idx, (icon, name, target) in enumerate(modules):
        with [c1, c2, c3, c4][idx]:
            st.markdown(f'<div class="module-card"><h1>{icon}</h1><h3 class="module-title">{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"ENTER {name}", key=name): st.session_state.page = 'cinematic'; st.rerun()
            else: st.button("COMING SOON", disabled=True, key=name)

elif st.session_state.page == 'cinematic':
    if st.button("← BACK TO PORTAL"): st.session_state.page = 'home'; st.rerun()
    
    tab_builder, tab_history = st.tabs(["🏗️ PROMPT BUILDER", "📜 DESIGN HISTORY"])
    
    with tab_builder:
        def add_n(d): return ["None"] + d + ["Others"]
        
        # دیتاهای کامل (Hair, Age, Nat, SFX, etc.)
        age_opt = ["Elderly", "Middle-aged", "Young Adult", "Child"]
        nat_opt = ["Iranian", "Saudi", "European", "African", "Asian"]
        sfx_opt = ["Katana Slash", "Glass Wound", "Bruise", "Burn"]
        
        c_form, c_master = st.columns([2.1, 1])
        with c_form:
            f1, f2, f3 = st.columns(3)
            with f1:
                st.markdown('<p class="label-text">Identity</p>', unsafe_allow_html=True)
                gen_v = st.selectbox("Gender", ["Male", "Female", "Androgynous"], key="gen")
                age_v = st.selectbox("Age Range", add_n(age_opt), key="age")
                st.markdown('<p class="label-text">Hair Detail</p>', unsafe_allow_html=True)
                hc_v = st.selectbox("Hair Color", add_n(["Jet Black", "Grey", "Blonde"]), key="hcol")
            with f2:
                st.markdown('<p class="label-text">Origin</p>', unsafe_allow_html=True)
                nat_v = st.selectbox("Nationality", add_n(nat_opt), key="nat")
                st.markdown('<p class="label-text">SFX</p>', unsafe_allow_html=True)
                sfx_v = st.selectbox("Trauma Type", add_n(sfx_opt), key="sfx")
            with f3:
                st.markdown('<p class="label-text">Technical</p>', unsafe_allow_html=True)
                cam_v = st.selectbox("Camera", add_n(["85mm", "100mm Macro", "35mm"]), key="cam")
                size_v = st.selectbox("Size", add_n(["4:5", "16:9", "1:1"]), key="size")

        # ساخت پرامپت
        final_p = f"Professional cinematic portrait, {gen_v}, {age_v}, {nat_v}. Hair: {hc_v}. SFX: {sfx_v}. Tech: {cam_v}, {size_v}, 8k raw photo."

        with c_master:
            st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)
            
            st.write("---")
            proj_name = st.text_input("Project Name (for history)", placeholder="e.g. Joker Test 01")
            if st.button("💾 SAVE TO HISTORY"):
                if proj_name:
                    entry = {
                        "user": st.session_state.current_user,
                        "name": proj_name,
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "prompt": final_p
                    }
                    st.session_state.history.insert(0, entry)
                    st.success(f"Project '{proj_name}' Saved!")
                else: st.warning("Please enter a name first.")

    with tab_history:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>YOUR SAVED DESIGNS</h3>", unsafe_allow_html=True)
        user_history = [h for h in st.session_state.history if h["user"] == st.session_state.current_user]
        
        if not user_history:
            st.info("No saved prompts yet. Start designing!")
        else:
            for item in user_history:
                with st.expander(f"📌 {item['name']} | {item['time']}"):
                    st.code(item['prompt'])
                    st.button("Copy Prompt", key=item['time'])

# فوتر
st.markdown(f"<div class='footer'>© {datetime.now().year} <span class='uona-tag'>UONA GROUP</span>. ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
