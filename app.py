import streamlit as st
from datetime import datetime
import os
import json

# 1. تنظیمات پایه و معماری پلتفرم
st.set_page_config(page_title="UONA STUDIO | AI SAAS", layout="wide", initial_sidebar_state="collapsed")

# --- سیستم دیتابیس مخفی (یوزرها و تاریخچه) ---
DB_FILE = ".users_db.json"
HIST_FILE = ".history_db.json"

def load_data(file, default):
    if not os.path.exists(file):
        with open(file, "w") as f: json.dump(default, f)
    with open(file, "r") as f: return json.load(f)

def save_data(file, data):
    with open(file, "w") as f: json.dump(data, f)

# 2. استایل بصری (اصلاح رنگ‌ها و سایه‌ها طبق اسکرین‌شات‌ها)
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
        font-family: 'Cinzel'; color: #ffffff !important; font-size: 3rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
    }

    /* فیروزه‌ای متوسط برای لیبل‌ها */
    label, .stMarkdown p, .label-text { 
        color: #00bcd4 !important; 
        font-family: 'Montserrat' !important; font-weight: 700 !important; 
        text-transform: uppercase !important; font-size: 0.75rem !important; 
    }

    /* اصلاح باکس‌های ورودی لاگین */
    div[data-baseweb="input"] > div {
        background-color: rgba(0, 20, 40, 0.9) !important;
        border: 1px solid rgba(0, 242, 255, 0.4) !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="input"] input { color: #ffffff !important; font-weight: bold !important; }

    /* دکمه‌های رادیویی */
    div[role="radiogroup"] { 
        background: rgba(0, 242, 255, 0.05); padding: 10px 20px; 
        border-radius: 10px; border: 1px solid rgba(0, 242, 255, 0.2); 
    }
    div[role="radiogroup"] label p { color: #ffffff !important; }

    /* اصلاح رنگ کلمات ۴گانه (فیروزه‌ای تیره + سایه طلایی) */
    .module-title { 
        font-family: 'Cinzel'; 
        color: #008b8b !important; 
        text-shadow: 0 0 12px rgba(255, 215, 0, 0.8) !important; 
        letter-spacing: 3px; font-weight: 900;
    }

    /* اصلاح رنگ تب‌ها */
    .stTabs [data-baseweb="tab-list"] button {
        color: #7b8ea8 !important; font-family: 'Cinzel', serif !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #00f2ff !important; border-bottom: 2px solid #00f2ff !important;
    }

    /* دکمه‌های اختصاصی لاگین و رجیستر */
    .btn-login > div > button { background-color: #00f2ff !important; color: #000 !important; }
    .btn-reg > div > button { background-color: #ff00aa !important; color: #fff !important; }

    .stButton > button {
        border: none !important; border-radius: 12px !important;
        font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px; transition: 0.3s;
    }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px; padding: 25px; text-align: center; backdrop-filter: blur(15px);
    }

    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 10px; font-weight: 900; border-radius: 12px 12px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { background-color: #ffffff; color: #111; padding: 20px; border-radius: 0 0 12px 12px; border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; line-height: 1.5; height: 350px; overflow-y: auto; }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; background: rgba(0,0,0,0.6); color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem; }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# 3. مدیریت نشست و امنیت
if 'auth' not in st.session_state: st.session_state.auth = False
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- ورود به پلتفرم ---
if not st.session_state.auth:
    col_l, col_r = st.columns([1, 1.2])
    with col_l:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=250)
    with col_r:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px; text-shadow: 0 0 15px #00f2ff;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        mode = st.radio("SELECT MODE", ["Login", "Register"], horizontal=True)
        u_name = st.text_input("USERNAME")
        u_pass = st.text_input("PASSWORD", type="password")
        
        users = load_data(DB_FILE, {"hossein": "1234"})
        if mode == "Login":
            st.markdown('<div class="btn-login">', unsafe_allow_html=True)
            if st.button("SIGN IN"):
                if u_name in users and users[u_name] == u_pass:
                    st.session_state.auth = True; st.session_state.user = u_name; st.rerun()
                else: st.error("Access Denied")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="btn-reg">', unsafe_allow_html=True)
            if st.button("CREATE ACCOUNT"):
                if u_name and u_pass:
                    users[u_name] = u_pass; save_data(DB_FILE, users)
                    st.success("Registered! Switch to Login.")
            st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- هدر و ناوبری ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("logo.PNG"): st.image("logo.PNG", width=85)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- پورتال اصلی (DASHBOARD) ---
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

# --- ماژول کاراکتر ساز (CHARACTER BUILDER) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    t_builder, t_hist = st.tabs(["🏗️ PROMPT BUILDER", "📜 HISTORY"])

    with t_builder:
        def add_n(d): return ["None"] + d + ["Others"]
        c_form, c_master = st.columns([2.2, 1])
        
        with c_form:
            f1, f2, f3 = st.columns(3)
            with f1:
                st.markdown('<p class="label-text">Actor & Identity</p>', unsafe_allow_html=True)
                act = st.selectbox("Actor Ref", ["None", "No", "Yes"])
                gen = st.selectbox("Gender", ["Male", "Female", "Androgynous"])
                age = st.selectbox("Age Range", ["Elderly", "Middle-aged", "Young Adult", "Child"])
                
                h_
    /* فیروزه‌ای متوسط برای لیبل‌ها */
    label, .stMarkdown p, .label-text { 
        color: #00bcd4 !important; 
        font-family: 'Montserrat' !important; font-weight: 700 !important; 
        text-transform: uppercase !important; font-size: 0.75rem !important; 
    }

    /* اصلاح باکس‌های ورودی لاگین */
    div[data-baseweb="input"] > div {
        background-color: rgba(0, 20, 40, 0.9) !important;
        border: 1px solid rgba(0, 242, 255, 0.4) !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="input"] input { color: #ffffff !important; font-weight: bold !important; }

    /* دکمه‌های رادیویی */
    div[role="radiogroup"] { 
        background: rgba(0, 242, 255, 0.05); padding: 10px 20px; 
        border-radius: 10px; border: 1px solid rgba(0, 242, 255, 0.2); 
    }
    div[role="radiogroup"] label p { color: #ffffff !important; }

    /* اصلاح رنگ کلمات ۴گانه (فیروزه‌ای تیره + سایه طلایی) */
    .module-title { 
        font-family: 'Cinzel'; 
        color: #008b8b !important; 
        text-shadow: 0 0 12px rgba(255, 215, 0, 0.8) !important; 
        letter-spacing: 3px; font-weight: 900;
    }

    /* اصلاح رنگ تب‌ها */
    .stTabs [data-baseweb="tab-list"] button {
        color: #7b8ea8 !important; font-family: 'Cinzel', serif !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #00f2ff !important; border-bottom: 2px solid #00f2ff !important;
    }

    /* دکمه‌های اختصاصی لاگین و رجیستر */
    .btn-login > div > button { background-color: #00f2ff !important; color: #000 !important; }
    .btn-reg > div > button { background-color: #ff00aa !important; color: #fff !important; }

    .stButton > button {
        border: none !important; border-radius: 12px !important;
        font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px; transition: 0.3s;
    }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px; padding: 25px; text-align: center; backdrop-filter: blur(15px);
    }

    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 10px; font-weight: 900; border-radius: 12px 12px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { background-color: #ffffff; color: #111; padding: 20px; border-radius: 0 0 12px 12px; border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; line-height: 1.5; height: 350px; overflow-y: auto; }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; background: rgba(0,0,0,0.6); color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem; }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# 3. مدیریت نشست و امنیت
if 'auth' not in st.session_state: st.session_state.auth = False
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- ورود به پلتفرم ---
if not st.session_state.auth:
    col_l, col_r = st.columns([1, 1.2])
    with col_l:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=250)
    with col_r:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px; text-shadow: 0 0 15px #00f2ff;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        mode = st.radio("SELECT MODE", ["Login", "Register"], horizontal=True)
        u_name = st.text_input("USERNAME")
        u_pass = st.text_input("PASSWORD", type="password")
        
        users = load_data(DB_FILE, {"hossein": "1234"})
        if mode == "Login":
            st.markdown('<div class="btn-login">', unsafe_allow_html=True)
            if st.button("SIGN IN"):
                if u_name in users and users[u_name] == u_pass:
                    st.session_state.auth = True; st.session_state.user = u_name; st.rerun()
                else: st.error("Access Denied")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="btn-reg">', unsafe_allow_html=True)
            if st.button("CREATE ACCOUNT"):
                if u_name and u_pass:
                    users[u_name] = u_pass; save_data(DB_FILE, users)
                    st.success("Registered! Switch to Login.")
            st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- هدر و ناوبری ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("logo.PNG"): st.image("logo.PNG", width=85)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- پورتال اصلی (DASHBOARD) ---
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

# --- ماژول کاراکتر ساز (CHARACTER BUILDER) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    t_builder, t_hist = st.tabs(["🏗️ PROMPT BUILDER", "📜 HISTORY"])

    with t_builder:
        def add_n(d): return ["None"] + d + ["Others"]
        c_form, c_master = st.columns([2.2, 1])
        
        with c_form:
            f1, f2, f3 = st.columns(3)
            with f1:
                st.markdown('<p class="label-text">Actor & Identity</p>', unsafe_allow_html=True)
                act = st.selectbox("Actor Ref", ["None", "No", "Yes"])
                gen = st.selectbox("Gender", ["Male", "Female", "Androgynous"])
                age = st.selectbox("Age Range", ["Elderly", "Middle-aged", "Young Adult", "Child"])
                
                h_
