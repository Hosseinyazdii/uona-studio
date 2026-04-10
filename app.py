import streamlit as st
from datetime import datetime
import os
import json

# 1. تنظیمات پایه
st.set_page_config(page_title="UONA STUDIO | AI PLATFORM", layout="wide", initial_sidebar_state="collapsed")

# --- سیستم لاگین قطعی و بدون کرش (استفاده از فایل‌های مخفی) ---
DB_FILE = ".users_db.json"
HIST_FILE = ".history_db.json"

def load_users():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f: json.dump({"hossein": "1234"}, f)
    with open(DB_FILE, "r") as f: return json.load(f)

def save_user(u, p):
    users = load_users()
    users[u] = p
    with open(DB_FILE, "w") as f: json.dump(users, f)

def load_history():
    if not os.path.exists(HIST_FILE):
        with open(HIST_FILE, "w") as f: json.dump([], f)
    with open(HIST_FILE, "r") as f: return json.load(f)

def save_history_entry(entry):
    data = load_history()
    data.insert(0, entry)
    with open(HIST_FILE, "w") as f: json.dump(data, f)

# 2. استایل
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
        font-family: 'Cinzel'; color: #ffffff !important; font-size: 3.2rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
    }

    label, .stMarkdown p, .label-text { 
        color: #00e5ff !important; 
        font-family: 'Montserrat' !important; font-weight: 700 !important; 
        text-transform: uppercase !important; font-size: 0.75rem !important; 
    }

    /* باکس‌های یوزرنیم و پسورد و اینپوت Others */
    div[data-baseweb="input"] > div {
        background-color: rgba(0, 20, 40, 0.8) !important;
        border: 1px solid rgba(0, 242, 255, 0.5) !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="input"] input {
        color: #ffffff !important;
        font-weight: bold !important;
    }

    /* دایره‌ها و متن‌های رادیو باتن (Login/Register) */
    div[role="radiogroup"] { 
        background: rgba(0, 242, 255, 0.05); padding: 10px 20px; 
        border-radius: 10px; border: 1px solid rgba(0, 242, 255, 0.2); 
    }
    div[role="radiogroup"] label p { color: #ffffff !important; }

    /* رنگ تب‌های PROMPT BUILDER و HISTORY */
    .stTabs [data-baseweb="tab-list"] button {
        color: #7b8ea8 !important;
        font-family: 'Cinzel', serif !important;
        font-size: 1.1rem !important;
        background-color: transparent !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #00f2ff !important;
        border-bottom: 2px solid #00f2ff !important;
    }

    /* رنگ متن تاریخچه‌های ذخیره شده */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(0, 242, 255, 0.2) !important;
        border-radius: 10px !important;
    }
    div[data-testid="stExpander"] summary p {
        color: #00f2ff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: bold !important;
    }

    /* استایل پایه دکمه‌ها */
    .stButton > button {
        border: none !important; border-radius: 12px !important;
        font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px;
        transition: 0.3s;
    }
    .stButton > button:hover { background-color: #ffffff !important; color: #000 !important; transform: scale(1.02); }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px; padding: 25px; text-align: center; backdrop-filter: blur(15px);
    }
    
    /* تغییر اختصاصی برای ۴ کلمه (فیروزه‌ای تیره با سایه طلایی) */
    .module-title { 
        font-family: 'Cinzel'; 
        color: #008b8b !important; /* فیروزه‌ای تیره */
        text-shadow: 0 0 12px rgba(255, 215, 0, 0.8) !important; /* سایه طلایی */
        letter-spacing: 3px; 
    }

    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 10px; font-weight: 900; border-radius: 12px 12px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { background-color: #ffffff; color: #111; padding: 20px; border-radius: 0 0 12px 12px; border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; line-height: 1.5; height: 350px; overflow-y: auto; }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; background: rgba(0,0,0,0.6); color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem; }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

if 'auth_status' not in st.session_state: st.session_state.auth_status = False
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- صفحه لاگین ---
if not st.session_state.auth_status:
    col_l, col_r = st.columns([1, 1.2])
    with col_l:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): 
            st.image("logo.PNG", width=250) 
        else: 
            st.markdown("<div style='width:200px;height:200px;background:#00f2ff;border-radius:50%; display:flex; align-items:center; justify-content:center; color:black; font-weight:900;'>LOGO</div>", unsafe_allow_html=True)
    with col_r:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px; text-shadow: 0 0 15px #00f2ff;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        
        mode = st.radio("SELECT MODE", ["Login", "Register"], horizontal=True)
        u_name = st.text_input("USERNAME", placeholder="Enter your username...")
        u_pass = st.text_input("PASSWORD", type="password", placeholder="Enter your password...")
        
        users_db = load_users()
        
        if mode == "Login":
            st.markdown("""<style>div.stButton > button { background-color: #00f2ff !important; color: #000000 !important; box-shadow: 0 0 15px rgba(0, 242, 255, 0.4); }</style>""", unsafe_allow_html=True)
            if st.button("SIGN IN"):
                if u_name in users_db and users_db[u_name] == u_pass:
                    st.session_state.auth_status = True; st.session_state.user = u_name; st.rerun()
                else: st.error("Access Denied: Invalid Credentials")
        else:
            st.markdown("""<style>div.stButton > button { background-color: #ff00aa !important; color: #ffffff !important; box-shadow: 0 0 15px rgba(255, 0, 170, 0.4); }</style>""", unsafe_allow_html=True)
            if st.button("CREATE ACCOUNT"):
                if u_name and u_pass:
                    save_user(u_name, u_pass)
                    st.success(f"User '{u_name}' Registered! Switch to Login to enter.")
                else:
                    st.warning("Please fill both fields.")
    st.stop()

# برگرداندن دکمه‌های فرم‌ها به فیروزه‌ای
st.markdown("""<style>div.stButton > button { background-color: #00f2ff !important; color: #000000 !important; box-shadow: 0 0 15px rgba(0, 242, 255, 0.3); }</style>""", unsafe_allow_html=True)

# --- هدر اصلی نرم‌افزار ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("logo.PNG"): st.image("logo.PNG", width=85)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- پورتال اصلی ---
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

# --- ماژول Cinematic ---
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
                
                h_col_val = st.selectbox("Hair Color", add_n(["Jet Black", "Espresso", "Ash Blonde", "Salt & Pepper"]))
                h_col = st.text_input("Type Custom Hair Color", key="hc_c") if h_col_val == "Others" else h_col_val

            with f2:
                nat_val = st.selectbox("Nationality *", add_n(["Iranian", "Saudi", "European", "African"]))
                nat = st.text_input("Type Custom Nationality", key="nat_c") if nat_val == "Others" else nat_val
                
                era_val = st.selectbox("Era / Period", add_n(["Ancient", "Medieval", "100 Years Ago", "Contemporary"]))
                era = st.text_input("Type Custom Era", key="era_c") if era_val == "Others" else era_val
                
                sfx_val = st.selectbox("Trauma / SFX", add_n(["Katana Slash", "Bruise", "Glass Wound", "Burn"]))
                sfx = st.text_input("Type Custom SFX", key="sfx_c") if sfx_val == "Others" else sfx_val
                
                mat_val = st.selectbox("Material Finish", add_n(["Silicone", "Matte Sealer", "Alcohol Palette"]))
                mat = st.text_input("Type Custom Material", key="mat_c") if mat_val == "Others" else mat_val

            with f3:
                char_val = st.selectbox("Character Concept", add_n(["Warrior", "Villain", "Scholar", "Royal"]))
                char = st.text_input("Type Custom Concept", key="char_c") if char_val == "Others" else char_val
                
                groom_val = st.selectbox("Grooming Style", add_n(["Clean Shaven", "Full Beard", "Stubble", "Goatee"]))
                groom = st.text_input("Type Custom Grooming", key="groom_c") if groom_val == "Others" else groom_val
                
                cam_val = st.selectbox("Camera & Lens *", add_n(["85mm", "100mm Macro", "35mm Low-Angle"]))
                cam = st.text_input("Type Custom Camera", key="cam_c") if cam_val == "Others" else cam_val
                
                light_val = st.selectbox("Lighting Style", add_n(["Rembrandt", "Teal & Orange", "Neon"]))
                light = st.text_input("Type Custom Lighting", key="light_c") if light_val == "Others" else light_val
                
                size_val = st.selectbox("Frame Size", add_n(["4:5", "16:9", "2.39:1", "1:1"]))
                size = st.text_input("Type Custom Size", key="size_c") if size_val == "Others" else size_val

        final_p = f"Professional cinematic portrait, {size}, {gen}, {age}, {nat}. Concept: {char}, {groom}. Hair: {h_col}. SFX: {sfx}. Material: {mat}. Tech: {cam}, {light}, 8k raw photo."

        with c_master:
            st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)
            p_name = st.text_input("Project Name:")
            if st.button("💾 SAVE TO HISTORY"):
                if p_name:
                    entry = {"user": st.session_state.user, "name": p_name, "time": datetime.now().strftime("%Y-%m-%d %H:%M"), "prompt": final_p}
                    save_history_entry(entry)
                    st.success("Design Saved to Database!")

    with t_hist:
        all_history = load_history()
        u_h = [h for h in all_history if h["user"] == st.session_state.user]
        if not u_h: st.info("No saved designs found.")
        for item in u_h:
            with st.expander(f"📌 {item['name']} | {item['time']}"):
                st.code(item['prompt'])

# 4. فوتر
st.markdown(f"<div class='footer'>© {datetime.now().year} <span class='uona-tag'>UONA GROUP</span>. ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
