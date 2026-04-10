import streamlit as st
from datetime import datetime

# 1. تنظیمات پایه و حذف اسکرول
st.set_page_config(page_title="UONA STUDIO | AI SYSTEM", layout="wide", initial_sidebar_state="collapsed")

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

    /* هدر */
    .nav-bar {
        display: flex; align-items: center; padding: 10px 50px;
        background: rgba(2, 6, 12, 0.8); border-bottom: 1px solid rgba(0, 242, 255, 0.2);
    }
    .title-main {
        font-family: 'Cinzel'; color: #ffffff; font-size: 3rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; text-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
    }

    /* استایل دکمه‌های پورتال با افکت Shadow Serif */
    .stButton > button {
        background-color: #00f2ff !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 12px !important;
        font-family: 'Cinzel', serif !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 1rem !important;
        box-shadow: 3px 3px 0px rgba(0,0,0,0.5); /* Shadow effect */
        transition: 0.3s;
    }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.05); }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 15px; padding: 20px; text-align: center; backdrop-filter: blur(10px);
    }
    
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.7rem; margin-top: 5px; }
    
    .master-box { 
        background-color: #ffffff; color: #111; padding: 20px; border-radius: 8px; 
        border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; 
        line-height: 1.5; height: 320px; overflow-y: auto;
    }
    
    /* فوتر با رنگ سرمه‌ای برای UONA GROUP */
    .footer { 
        position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; 
        border-top: 1px solid rgba(0, 242, 255, 0.1); background: rgba(0,0,0,0.6);
        color: #ffffff; font-family: 'Montserrat'; font-size: 0.7rem;
    }
    .uona-tag { color: #001f3f !important; font-weight: 900; } /* سرمه‌ای تیره */
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- هدر ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    st.image("logo.png", width=90) # استفاده از فایل لوگو در گیت‌هاب
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1>', unsafe_allow_html=True)

# --- پورتال ---
if st.session_state.page == 'home':
    st.markdown("<br><br><h3 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:4px;'>SELECT MODULE</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    modules = [("🎬", "MOVIE", "cine"), ("📺", "SERIES", "cine"), ("🎭", "THEATER", "soon"), ("👠", "FASHION", "soon")]
    for idx, (icon, name, target) in enumerate(modules):
        with [c1, c2, c3, c4][idx]:
            st.markdown(f'<div class="module-card"><h1>{icon}</h1><h3>{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"ENTER {name}", key=name): st.session_state.page = 'cinematic'; st.rerun()
            else: st.button("COMING SOON", disabled=True, key=name)

# --- ماژول Cinematic ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    
    def add_options(d): return ["None"] + d + ["Others"]

    c_form, c_master = st.columns([2.1, 1])
    with c_form:
        f1, f2, f3 = st.columns(3)
        with f1:
            st.markdown('<p class="label-text">Actor Reference</p>', unsafe_allow_html=True)
            actor = st.selectbox("", ["None", "No", "Yes"], key="act", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">Age Range</p>', unsafe_allow_html=True)
            age_opt = ["Elderly", "Middle-aged", "Young Adult", "Child"]
            age = st.selectbox("", add_options(age_opt), key="age", label_visibility="collapsed")
            if age == "Others": age = st.text_input("Type Age...", key="age_custom")

            st.markdown('<p class="label-text">Hair Texture</p>', unsafe_allow_html=True)
            h_tex_opt = ["Afro", "Wavy", "Curly", "Straight", "Matted"]
            h_tex = st.selectbox("", add_options(h_tex_opt), key="htex", label_visibility="collapsed")
            if h_tex == "Others": h_tex = st.text_input("Type Texture...", key="htex_custom")

        with f2:
            st.markdown('<p class="label-text">Nationality</p>', unsafe_allow_html=True)
            nat_opt = ["Iranian", "Saudi", "European", "African", "Asian"]
            nat = st.selectbox("", add_options(nat_opt), key="nat", label_visibility="collapsed")
            if nat == "Others": nat = st.text_input("Type Nationality...", key="nat_custom")

            st.markdown('<p class="label-text">SFX Trauma</p>', unsafe_allow_html=True)
            sfx_opt = ["Katana Slash", "Glass Wound", "Bruise", "Burn"]
            sfx = st.selectbox("", add_options(sfx_opt), key="sfx", label_visibility="collapsed")
            if sfx == "Others": sfx = st.text_input("Type SFX...", key="sfx_custom")

            st.markdown('<p class="label-text">Material Finish</p>', unsafe_allow_html=True)
            mat_opt = ["Silicone", "Matte Sealer", "Alcohol Palette"]
            mat = st.selectbox("", add_options(mat_opt), key="mat", label_visibility="collapsed")
            if mat == "Others": mat = st.text_input("Type Material...", key="mat_custom")

        with f3:
            st.markdown('<p class="label-text">Grooming Style</p>', unsafe_allow_html=True)
            groom_opt = ["Clean Shaven", "Full Beard", "Stubble"]
            groom = st.selectbox("", add_options(groom_opt), key="groom", label_visibility="collapsed")
            if groom == "Others": groom = st.text_input("Type Grooming...", key="groom_custom")

            st.markdown('<p class="label-text">Camera & Lens</p>', unsafe_allow_html=True)
            cam_opt = ["85mm Eye-Level", "100mm Macro", "35mm Low-Angle"]
            cam = st.selectbox("", add_options(cam_opt), key="cam", label_visibility="collapsed")
            if cam == "Others": cam = st.text_input("Type Camera...", key="cam_custom")

            st.markdown('<p class="label-text">Frame Size</p>', unsafe_allow_html=True)
            size_opt = ["4:5 (Portrait)", "16:9 (Widescreen)", "1:1 (Square)"]
            size = st.selectbox("", add_options(size_opt), key="size", label_visibility="collapsed")
            if size == "Others": size = st.text_input("Type Size...", key="size_custom")

    # فرمول Master Prompt
    final_p = f"A professional cinematic portrait of a {age} {nat}. Concept: {groom}. Texture: {h_tex}. SFX: {sfx}. Material: {mat}. Technical: {cam}, {size}, 8k raw photography."

    with c_master:
        st.markdown('<div style="background:#00f2ff; color:black; padding:8px; font-weight:900; text-align:center;">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)

# 6. فوتر
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} <span class="uona-tag">UONA GROUP</span>. ALL RIGHTS RESERVED.
    </div>
    """, unsafe_allow_html=True)
