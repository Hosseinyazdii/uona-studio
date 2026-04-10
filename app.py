import streamlit as st
from datetime import datetime
import os

# 1. تنظیمات پایه و حذف اسکرول
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

    .stTabs [data-baseweb="tab-list"] { gap: 50px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { font-family: 'Cinzel'; color: white !important; font-size: 1.1rem !important; }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #00f2ff !important; color: #00f2ff !important; }

    .label-text { color: #00f2ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.65rem; margin-top: 4px; }
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 10px; font-weight: 900; font-size: 1.1rem; border-radius: 12px 12px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { background-color: #ffffff; color: #111; padding: 20px; border-radius: 0 0 12px 12px; border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 1rem; line-height: 1.6; height: 350px; overflow-y: auto; }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; background: rgba(0,0,0,0.6); color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem; }
    .uona-tag { color: #0a192f !important; font-weight: 900; background: #00f2ff; padding: 2px 8px; border-radius: 4px; text-shadow: 0 0 8px rgba(255,255,255,0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- سیستم پایداری یوزرها ---
if 'users' not in st.session_state: st.session_state.users = {"hossein": "1234"}
if 'auth' not in st.session_state: st.session_state.auth = False
if 'history' not in st.session_state: st.session_state.history = []
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- صفحه لاگین ---
if not st.session_state.auth:
    col_l, col_r = st.columns([1, 1.2])
    with col_l:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=220)
    with col_r:
        st.markdown("<h1 style='color:#00f2ff; font-family:Cinzel; margin-top:100px;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        mode = st.radio("Mode", ["Login", "Register"], horizontal=True)
        u_in = st.text_input("Username")
        p_in = st.text_input("Password", type="password")
        if mode == "Login":
            if st.button("ENTER"):
                if u_in in st.session_state.users and st.session_state.users[u_in] == p_in:
                    st.session_state.auth = True; st.session_state.c_user = u_in; st.rerun()
                else: st.error("Incorrect details.")
        else:
            if st.button("CREATE ACCOUNT"):
                if u_in and p_in:
                    st.session_state.users[u_in] = p_in; st.success("Created! Switch to Login.")
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
            st.markdown(f'<div class="module-card"><h1>{icon}</h1><h3 class="module-title">{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"ENTER {name}", key=name): st.session_state.page = 'cinematic'; st.rerun()
            else: st.button("COMING SOON", disabled=True, key=name)

# --- ماژول Cinematic (فول دیتا) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    t_builder, t_hist = st.tabs(["🏗️ PROMPT BUILDER", "📜 HISTORY"])

    with t_builder:
        def add_n(d): 
            if isinstance(d, dict): return {**{"None": ""}, **d}
            return ["None"] + d + ["Others"]

        # دیتابیس کامل بر اساس فایل های اکسل
        gender_d = add_n({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours"})
        age_d = add_n({"Elderly / Senior": "collagen loss", "Middle-aged": "initial sagging", "Young Adult": "peak elasticity", "Child": "smooth skin"})
        nat_d = add_n({"Iranian": "prominent nasal bridge", "Saudi": "Peninsular Arab", "European": "Caucasian", "African": "Sub-Saharan"})
        era_d = add_n({"Ancient": "Classical", "Medieval": "Gritty", "100 Years Ago": "Period", "Contemporary": "Modern"})
        char_d = add_n({"Heroic Warrior": "Strong", "Sinister Villain": "Harsh", "Scholar": "Refined", "Mercenary": "Rugged"})
        groom_d = add_n({"Clean Shaven": "smooth", "Light Stubble": "short", "Heavy Stubble": "rough", "Full Beard": "natural", "Goatee": "chin beard"})
        sfx_cats = {"Acute Trauma": ["Katana Slash", "Glass Laceration"], "Healing Stages": ["3-Day Wound", "1-Month Scar"], "Bruising": ["Fresh Hematoma", "3-Day Bruise"]}
        aging_d = add_n({"Deep Nasolabial Folds": "smile lines", "Crow's Feet": "eye wrinkles", "Liver Spots": "age spots"})
        h_tex_d = add_n({"Afro": "coils", "Wavy": "S-shape", "Curly": "ringlets", "Straight": "silky", "Matted": "weathered"})
        h_col_d = add_n({"Jet black": "Natural", "Espresso": "Dark", "Ash blonde": "Cool", "50% Salt & Pepper": "mixed grey"})
        light_d = add_n({"Rembrandt": "triangle", "Teal and Orange": "cinematic", "Neon Cyberpunk": "edge", "Softbox": "velvety"})
        cam_d = add_n({"85mm Eye-Level": "no distortion", "100mm Macro": "extreme detail", "35mm Low-Angle": "hero shot"})
        size_l = add_n(["4:5 (Portrait)", "16:9 (Widescreen)", "2.39:1 (Anamorphic)", "1:1 (Square)"])
        mat_l = add_n(["Silicone", "Translucent Skin", "Matte Sealer", "Alcohol Palette"])

        c_form, c_master = st.columns([2.1, 1])
        with c_form:
            f1, f2, f3 = st.columns(3)
            with f1:
                st.markdown('<p class="label-text">Identity</p>', unsafe_allow_html=True)
                act = st.selectbox("Actor Reference", ["None", "No", "Yes"], key="act")
                gen_v = st.selectbox("Gender", list(gender_d.keys()), key="gen")
                age_v = st.selectbox("Age Range", list(age_d.keys()), key="age")
                st.markdown('<p class="label-text">Hair Detail</p>', unsafe_allow_html=True)
                hc_v = st.selectbox("Hair Color", list(h_col_d.keys()), key="hcol")
                ht_v = st.selectbox("Hair Texture", list(h_tex_d.keys()), key="htex")
            with f2:
                st.markdown('<p class="label-text">Origin & SFX</p>', unsafe_allow_html=True)
                nat_v = st.selectbox("Nationality", list(nat_d.keys()), key="nat")
                era_v = st.selectbox("Era", list(era_d.keys()), key="era")
                scat = st.selectbox("SFX Category", ["None"] + list(sfx_cats.keys()), key="scat")
                styp = st.selectbox("Trauma", sfx_cats[scat] if scat != "None" else ["None"], key="styp")
                mat_v = st.selectbox("Material", mat_l, key="mat")
            with f3:
                st.markdown('<p class="label-text">Grooming & Tech</p>', unsafe_allow_html=True)
                char_v = st.selectbox("Concept", list(char_d.keys()), key="char")
                groom_v = st.selectbox("Grooming", list(groom_d.keys()), key="groom")
                cam_v = st.selectbox("Camera", list(cam_d.keys()), key="cam")
                light_v = st.selectbox("Lighting", list(light_d.keys()), key="light")
                size_v = st.selectbox("Frame Size", size_l, key="psize")

        def f(p, v, d=None):
            if v == "None" or not v: return ""
            return f"{p}{v} ({d[v]})" if d and v in d and d[v] else f"{p}{v}"

        final_p = f"Professional cinematic portrait, {f('', gen_v, gender_d)}, {f('', age_v, age_d)}, {f('', nat_v, nat_d)}. Concept: {f('', char_v, char_d)}. Grooming: {f('', groom_v, groom_d)}. SFX: {styp}. Tech: {f('', cam_v, cam_d)}, {f('', light_v, light_d)}, {size_v}, 8k raw photo."

        with c_master:
            st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)
            proj = st.text_input("Name this project to save...")
            if st.button("💾 SAVE"):
                if proj:
                    st.session_state.history.insert(0, {"user": st.session_state.c_user, "name": proj, "time": datetime.now().strftime("%H:%M"), "prompt": final_p})
                    st.success("Saved to history tab!")

    with t_hist:
        u_h = [h for h in st.session_state.history if h["user"] == st.session_state.c_user]
        if not u_h: st.info("No saved prompts yet.")
        for item in u_h:
            with st.expander(f"📌 {item['name']} | {item['time']}"):
                st.code(item['prompt'])

st.markdown(f"<div class='footer'>© {datetime.now().year} <span class='uona-tag'>UONA GROUP</span>. ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
