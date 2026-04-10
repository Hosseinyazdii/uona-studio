import streamlit as st
from datetime import datetime
import os

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
        letter-spacing: 12px; margin: 0; 
        /* افکت سایه سفید ملایم */
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.6), 0 0 5px rgba(255, 255, 255, 0.3);
    }

    /* دکمه‌های پورتال */
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
        transition: 0.3s;
    }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.05); }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 15px; padding: 20px; text-align: center; backdrop-filter: blur(10px);
    }
    
    /* افکت سایه سفید ملایم برای تایتل‌های پورتال */
    .module-title {
        font-family: 'Cinzel'; color: white;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
        letter-spacing: 3px;
    }
    
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.7rem; margin-top: 5px; }
    
    .master-box { 
        background-color: #ffffff; color: #111; padding: 20px; border-radius: 8px; 
        border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; 
        line-height: 1.5; height: 320px; overflow-y: auto;
    }
    
    /* فوتر */
    .footer { 
        position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; 
        border-top: 1px solid rgba(0, 242, 255, 0.1); background: rgba(0,0,0,0.6);
        color: #ffffff; font-family: 'Montserrat'; font-size: 0.7rem;
    }
    /* افکت سایه سفید ملایم برای UONA GROUP در فوتر */
    .uona-tag { 
        color: #0a192f !important; font-weight: 900; background: rgba(0, 242, 255, 0.2); 
        padding: 2px 6px; border-radius: 4px;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- هدر ثابت ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    # لوگو با نام فایل صحیح
    if os.path.exists("logo.PNG"):
        st.image("logo.PNG", width=90)
    else:
        st.markdown("<div style='width:80px; height:80px; background:#00f2ff; border-radius:10px; display:flex; align-items:center; justify-content:center; color:black; font-weight:900;'>UONA</div>", unsafe_allow_html=True)
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

# --- ماژول Cinematic (تکمیل شده) ---
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
            age_val = st.selectbox("", add_options(age_opt), key="age", label_visibility="collapsed")
            age = st.text_input("Type Age...", key="age_custom") if age_val == "Others" else age_val

            st.markdown('<p class="label-text">Hair & Beard Color</p>', unsafe_allow_html=True)
            h_col_opt = ["Jet Black", "Espresso Brown", "Ash Blonde", "Sandy Chestnut", "Salt & Pepper"]
            h_col_val = st.selectbox("", add_options(h_col_opt), key="hcol", label_visibility="collapsed")
            h_col = st.text_input("Type Color...", key="hcol_custom") if h_col_val == "Others" else h_col_val

            st.markdown('<p class="label-text">Hair Texture</p>', unsafe_allow_html=True)
            h_tex_opt = ["Afro-Textured", "Wavy (Type 2)", "Curly (Type 3)", "Straight (Sleek)", "Coarse & Wiry", "Fine & Wispy", "Disheveled & Matted", "Braided / Cornrows"]
            h_tex_val = st.selectbox("", add_options(h_tex_opt), key="htex", label_visibility="collapsed")
            h_tex = st.text_input("Type Texture...", key="htex_custom") if h_tex_val == "Others" else h_tex_val

        with f2:
            st.markdown('<p class="label-text">Nationality</p>', unsafe_allow_html=True)
            nat_opt = ["Iranian", "Egyptian", "Emirati", "Saudi", "Kuwaiti", "Syrian", "American", "Indian", "Chinese", "African", "European", "Turkish"]
            nat_val = st.selectbox("", add_options(nat_opt), key="nat", label_visibility="collapsed")
            nat = st.text_input("Type Nationality...", key="nat_custom") if nat_val == "Others" else nat_val

            st.markdown('<p class="label-text">SFX Trauma</p>', unsafe_allow_html=True)
            sfx_opt = ["Fresh Katana Slash", "Glass Wound", "Blunt Force Contusion", "Chemical Acid Burn", "Sunburn", "Vitiligo"]
            sfx_val = st.selectbox("", add_options(sfx_opt), key="sfx", label_visibility="collapsed")
            sfx = st.text_input("Type SFX...", key="sfx_custom") if sfx_val == "Others" else sfx_val

            st.markdown('<p class="label-text">Skin Details (Aging/Texture)</p>', unsafe_allow_html=True)
            aging_opt = ["Deep Nasolabial Folds", "Crow's Feet", "hooded eyelids", "paper-thin skin", "Liver Spots", "Sagging Jowls"]
            aging_val = st.selectbox("", add_options(aging_opt), key="aging", label_visibility="collapsed")
            aging = st.text_input("Type Details...", key="aging_custom") if aging_val == "Others" else aging_val

        with f3:
            st.markdown('<p class="label-text">Grooming Style</p>', unsafe_allow_html=True)
            groom_opt = ["Clean Shaven", "Full Beard", "Stubble", "Shadow Fade", "Goatee", "Mustache Only"]
            groom_val = st.selectbox("", add_options(groom_opt), key="groom", label_visibility="collapsed")
            groom = st.text_input("Type Grooming...", key="groom_custom") if groom_val == "Others" else groom_val

            st.markdown('<p class="label-text">Camera & Lighting</p>', unsafe_allow_html=True)
            cam_opt = ["85mm Eye-Level", "100mm Macro", "35mm Low-Angle", "Dutch Angle"]
            cam_val = st.selectbox("", add_options(cam_opt), key="cam", label_visibility="collapsed")
            cam = st.text_input("Type Camera...", key="cam_custom") if cam_val == "Others" else cam_val
            
            light_opt = ["Rembrandt Lighting", "Cold Rim Lighting", "Chiaroscuro", "Teal and Orange", "God Rays"]
            light_val = st.selectbox("", add_options(light_opt), key="light", label_visibility="collapsed")
            light = st.text_input("Type Lighting...", key="light_custom") if light_val == "Others" else light_val

            st.markdown('<p class="label-text">Material & Frame Size</p>', unsafe_allow_html=True)
            mat_opt = ["Encapsulated Silicone", "Translucent Skin Finish", "Matte Sealer", "Alcohol Palette"]
            mat_val = st.selectbox("", add_options(mat_opt), key="mat", label_visibility="collapsed")
            mat = st.text_input("Type Material...", key="mat_custom") if mat_val == "Others" else mat_val
            
            size_opt = ["4:5 (Portrait)", "16:9 (Widescreen)", "2.39:1 (Anamorphic)", "1:1 (Square)"]
            size_val = st.selectbox("", add_options(size_opt), key="size", label_visibility="collapsed")
            size = st.text_input("Type Size...", key="size_custom") if size_val == "Others" else size_val

    # فرمول Master Prompt تایید شده و متمرکز (دقیقا مثل اکسل)
    p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
    p_sfx = f" [SFX STUDY: Apply {sfx} SFX as a makeup layer]." if sfx != "None" else ""
    p_size = f" Aspect Ratio {size}" if size != "None" else ""
    
    final_p = f"{p_actor}A professional cinematic{p_size} portrait of a {age} {nat}. Concept: {groom}. Skin: {aging}. Hair: {h_col} ({h_tex}).{p_sfx} Material: {mat}. Technical: {light}, {cam}, 8k raw photography, subsurface scattering."

    with c_master:
        st.markdown('<div style="background:#00f2ff; color:black; padding:8px; font-weight:900; text-align:center;">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)

# 6. فوتر
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} <span class="uona-tag">UONA GROUP</span>. ALL RIGHTS RESERVED.
    </div>
    """, unsafe_allow_html=True)
