import streamlit as st
from datetime import datetime
import os
import json

# 1. تنظیمات پایه
st.set_page_config(page_title="UONA STUDIO | AI PLATFORM", layout="wide", initial_sidebar_state="collapsed")

# تابع ذخیره و لود یوزرها برای پایداری ۱۰۰٪
def load_users():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f: json.dump({"hossein": "1234"}, f)
    with open("users.json", "r") as f: return json.load(f)

def save_user(u, p):
    users = load_users()
    users[u] = p
    with open("users.json", "w") as f: json.dump(users, f)

# استایل اختصاصی
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh; overflow: hidden !important;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    /* اصلاح رنگ لیبل‌ها در صفحه لاگین */
    .stTextInput label { color: #00f2ff !important; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.8rem; }
    
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
    .master-box { background-color: #ffffff; color: #111; padding: 20px; border-radius: 12px; border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; line-height: 1.5; height: 320px; overflow-y: auto; }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; background: rgba(0,0,0,0.6); color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem; }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# مدیریت نشست
if 'auth' not in st.session_state: st.session_state.auth = False
if 'history' not in st.session_state: st.session_state.history = []
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- لاگین پایدار ---
if not st.session_state.auth:
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=220)
    with c2:
        st.markdown("<h1 style='color:#00f2ff; font-family:Cinzel; margin-top:80px;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        mode = st.radio("SELECT MODE", ["Login", "Register"], horizontal=True)
        u_name = st.text_input("USERNAME")
        u_pass = st.text_input("PASSWORD", type="password")
        
        users_db = load_users()
        if mode == "Login":
            if st.button("SIGN IN"):
                if u_name in users_db and users_db[u_name] == u_pass:
                    st.session_state.auth = True; st.session_state.user = u_name; st.rerun()
                else: st.error("Incorrect details.")
        else:
            if st.button("CREATE ACCOUNT"):
                if u_name and u_pass:
                    save_user(u_name, u_pass); st.success("Account Registered! Switch to Login.")
    st.stop()

# --- هدر ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("logo.PNG"): st.image("logo.PNG", width=85)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- پورتال ---
if st.session_state.page == 'home':
    st.markdown("<br><br><h3 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:4px;'>SELECT MODULE</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    modules = [("🎬", "MOVIE", "cine"), ("📺", "SERIES", "cine"), ("🎭", "THEATER", "soon"), ("👠", "FASHION", "soon")]
    for idx, (icon, name, target) in enumerate(modules):
        with [c1, c2, c3, c4][idx]:
            st.markdown(f'<div class="module-card"><h1>{icon}</h1><h3 style="font-family:Cinzel; color:white; text-shadow: 0 0 10px rgba(255,255,255,0.5);">{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"OPEN {name}", key=name): st.session_state.page = 'cinematic'; st.rerun()
            else: st.button("COMING SOON", disabled=True, key=name)

# --- ماژول Cinematic (12 سوال کامل) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    t_builder, t_hist = st.tabs(["🏗️ PROMPT BUILDER", "📜 HISTORY"])

    with t_builder:
        def add_n(d): return ["None"] + d + ["Others"]
        
        c_form, c_master = st.columns([2.1, 1])
        with c_form:
            f1, f2, f3 = st.columns(3)
            with f1:
                st.markdown('<p class="label-text">Actor & Identity</p>', unsafe_allow_html=True)
                actor = st.selectbox("Actor Ref", ["None", "No", "Yes"])
                gen = st.selectbox("Gender", ["Male", "Female", "Androgynous"])
                age = st.selectbox("Age Range", ["Elderly", "Middle-aged", "Young Adult", "Child"])
                st.markdown('<p class="label-text">Hair Detail</p>', unsafe_allow_html=True)
                h_col = st.selectbox("Hair Color", add_n(["Jet Black", "Espresso", "Ash Blonde", "Salt & Pepper"]))
                h_tex = st.selectbox("Hair Texture", add_n(["Afro", "Wavy", "Curly", "Straight", "Matted"]))
            with f2:
                st.markdown('<p class="label-text">Origin & Era</p>', unsafe_allow_html=True)
                nat = st.selectbox("Nationality", add_n(["Iranian", "Saudi", "European", "African"]))
                era = st.selectbox("Era", add_n(["Ancient", "Medieval", "100 Years Ago", "Contemporary"]))
                st.markdown('<p class="label-text">SFX & Material</p>', unsafe_allow_html=True)
                sfx = st.selectbox("Trauma", add_n(["Katana Slash", "Bruise", "Glass Wound"]))
                mat = st.selectbox("Material", add_n(["Silicone", "Matte Sealer", "Alcohol Palette"]))
            with f3:
                st.markdown('<p class="label-text">Concept & Grooming</p>', unsafe_allow_html=True)
                char = st.selectbox("Concept", add_n(["Warrior", "Villain", "Scholar", "Royal"]))
                groom = st.selectbox("Grooming", add_n(["Clean Shaven", "Full Beard", "Stubble", "Goatee"]))
                st.markdown('<p class="label-text">Technical Details</p>', unsafe_allow_html=True)
                cam = st.selectbox("Camera", add_n(["85mm", "100mm Macro", "35mm"]))
                light = st.selectbox("Lighting", add_n(["Rembrandt", "Teal & Orange", "Neon"]))
                size = st.selectbox("Frame Size", add_n(["4:5", "16:9", "2.39:1", "1:1"]))

        final_p = f"Professional cinematic portrait, {size}, {gen}, {age}, {nat}. Concept: {char}, {groom}. Hair: {h_col} ({h_tex}). SFX: {sfx}. Material: {mat}. Tech: {cam}, {light}, 8k raw photo."

        with c_master:
            st.markdown('<div style="background:#00f2ff; color:black; padding:8px; font-weight:900; text-align:center; border-radius:10px 10px 0 0;">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)
            p_name = st.text_input("Project Name:")
            if st.button("💾 SAVE"):
                if p_name:
                    st.session_state.history.insert(0, {"user": st.session_state.user, "name": p_name, "time": datetime.now().strftime("%H:%M"), "prompt": final_p})
                    st.success("Saved!")

    with t_hist:
        u_h = [h for h in st.session_state.history if h["user"] == st.session_state.user]
        if not u_h: st.info("No saved prompts.")
        for item in u_h:
            with st.expander(f"📌 {item['name']} | {item['time']}"):
                st.code(item['prompt'])

st.markdown(f"<div class='footer'>© {datetime.now().year} <span class='uona-tag'>UONA GROUP</span>. ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
