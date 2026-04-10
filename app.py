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

    .nav-bar {
        display: flex; align-items: center; padding: 10px 50px;
        background: rgba(2, 6, 12, 0.8); border-bottom: 1px solid rgba(0, 242, 255, 0.2);
    }
    .title-main {
        font-family: 'Cinzel'; color: #ffffff; font-size: 3rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; 
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
    }

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
    
    .module-title {
        font-family: 'Cinzel'; color: white;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
        letter-spacing: 3px;
    }
    
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.65rem; margin-top: 4px; }
    
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 10px; font-weight: 900; font-size: 1.2rem; border-radius: 12px 12px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { 
        background-color: #ffffff; color: #111; padding: 25px; border-radius: 0 0 12px 12px; 
        border-left: 12px solid #00f2ff; font-family: 'Montserrat'; font-size: 1rem; 
        line-height: 1.7; height: 380px; overflow-y: auto; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    .footer { 
        position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; 
        border-top: 1px solid rgba(0, 242, 255, 0.1); background: rgba(0,0,0,0.6);
        color: #ffffff; font-family: 'Montserrat'; font-size: 0.65rem;
    }
    .uona-tag { 
        color: #0a192f !important; font-weight: 900; background: rgba(0, 242, 255, 0.2); 
        padding: 2px 6px; border-radius: 4px;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- هدر ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    if os.path.exists("logo.PNG"): st.image("logo.PNG", width=85)
    else: st.markdown("<div style='width:70px; height:70px; background:#00f2ff; border-radius:10px;'></div>", unsafe_allow_html=True)
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

# --- ماژول Cinematic ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    
    def add_n(d): 
        if isinstance(d, dict): return {**{"None": ""}, **d}
        return ["None"] + d + ["Others"]

    # دیتاها
    gender_d = add_n({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours", "Androgynous": "blend features"})
    age_d = add_n({"Elderly / Senior": "collagen loss", "Middle-aged": "initial sagging", "Young Adult": "peak elasticity", "Child": "smooth skin"})
    nat_d = add_n({"Iranian": "Indo-Aryan features", "Saudi": "Peninsular Arab", "European": "Caucasian", "African": "Sub-Saharan"})
    era_d = add_n({"Ancient": "Classical styling", "Medieval": "Gritty textures", "100 Years Ago": "Period growth", "Contemporary": "Modern lighting"})
    char_d = add_n({"Heroic Warrior": "Strong jawline", "Sinister Villain": "Harsh shadows", "Scholar": "Refined", "Mercenary": "Rugged"})
    groom_d = add_n({"Clean Shaven": "smooth skin", "Light Stubble": "short hairs", "Heavy Stubble": "rough texture", "Full Beard": "natural growth", "Goatee": "chin beard"})
    sfx_cats = {"Acute Trauma": ["Fresh Katana Slash", "Glass Laceration", "Chemical Burn"], "Healing Stages": ["3-Day Wound", "1-Month Scar"], "Bruising": ["Fresh Hematoma", "3-Day Bruise"]}
    aging_d = add_n({"Deep Nasolabial Folds": "smile lines", "Crow's Feet": "eye wrinkles", "Liver Spots": "age spots", "Sagging Jowls": "loose skin"})
    h_tex_d = add_n({"Afro": "structural coils", "Wavy": "S-shape waves", "Curly": "defined ringlets", "Straight": "silky", "Matted": "weathered textures"})
    h_col_d = add_n({"Jet black": "Natural tone", "Espresso": "Dark brown", "Ash blonde": "Cool blonde", "50% Salt & Pepper": "mixed grey"})
    light_d = add_n({"Rembrandt": "triangle lighting", "Teal and Orange": "cinematic colors", "Neon Cyberpunk": "edge glow", "Softbox": "velvety shadows"})
    cam_d = add_n({"85mm Eye-Level": "no distortion", "100mm Macro": "extreme detail", "35mm Low-Angle": "hero shot"})
    size_l = add_n(["4:5 (Portrait)", "16:9 (Widescreen)", "2.39:1 (Anamorphic)", "1:1 (Square)"])
    mat_l = add_n(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin Finish", "Matte Sealer"])

    c_form, c_master = st.columns([2.1, 1])
    with c_form:
        f1, f2, f3 = st.columns(3)
        with f1:
            st.markdown('<p class="label-text">Actor Ref</p>', unsafe_allow_html=True)
            actor = st.selectbox("", ["None", "No", "Yes"], key="act", label_visibility="collapsed")
            st.markdown('<p class="label-text">Gender & Age</p>', unsafe_allow_html=True)
            gen_v = st.selectbox("", list(gender_d.keys()), key="gen", label_visibility="collapsed")
            age_v = st.selectbox("", list(age_d.keys()), key="age", label_visibility="collapsed")
            st.markdown('<p class="label-text">Hair & Beard Color</p>', unsafe_allow_html=True)
            hc_v = st.selectbox("", list(h_col_d.keys()), key="hcol", label_visibility="collapsed")
            hc = st.text_input("Custom Color...", key="hc_c") if hc_v == "Others" else hc_v
            st.markdown('<p class="label-text">Hair Texture</p>', unsafe_allow_html=True)
            ht_v = st.selectbox("", list(h_tex_d.keys()), key="htex", label_visibility="collapsed")
            ht = st.text_input("Custom Texture...", key="ht_c") if ht_v == "Others" else ht_v
        with f2:
            st.markdown('<p class="label-text">Origin & Era</p>', unsafe_allow_html=True)
            nat_v = st.selectbox("", list(nat_d.keys()), key="nat", label_visibility="collapsed")
            era_v = st.selectbox("", list(era_d.keys()), key="era", label_visibility="collapsed")
            st.markdown('<p class="label-text">SFX & Trauma</p>', unsafe_allow_html=True)
            scat = st.selectbox("", ["None"] + list(sfx_cats.keys()), key="scat", label_visibility="collapsed")
            styp = st.selectbox("", sfx_cats[scat] if scat != "None" else ["None"], key="styp", label_visibility="collapsed")
            st.markdown('<p class="label-text">Makeup Material</p>', unsafe_allow_html=True)
            mat_v = st.selectbox("", mat_l, key="mat", label_visibility="collapsed")
            mat = st.text_input("Custom Material...", key="mat_c") if mat_v == "Others" else mat_v
        with f3:
            st.markdown('<p class="label-text">Concept & Grooming</p>', unsafe_allow_html=True)
            char_v = st.selectbox("", list(char_d.keys()), key="char", label_visibility="collapsed")
            groom_v = st.selectbox("", list(groom_d.keys()), key="groom", label_visibility="collapsed")
            st.markdown('<p class="label-text">Technical Details</p>', unsafe_allow_html=True)
            cam_v = st.selectbox("", list(cam_d.keys()), key="cam", label_visibility="collapsed")
            light_v = st.selectbox("", list(light_d.keys()), key="light", label_visibility="collapsed")
            size_v = st.selectbox("", size_l, key="psize", label_visibility="collapsed")

    # منطق پرامپت
    def f(p, v, d=None):
        if v == "None" or not v or v == "Others": return ""
        desc = f" ({d[v]})" if d and v in d and d[v] else ""
        return f"{p}{v}{desc}"

    p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
    p_sfx = f" [SFX STUDY: Apply {styp} SFX as a makeup layer]." if styp != "None" else ""
    p_size = f" Aspect Ratio {size_v}" if size_v != "None" and size_v != "Others" else ""
    
    final_p = f"{p_actor}A professional cinematic{p_size} portrait of a {f('', gen_v, gender_d)} {f('', age_v, age_d)} {f('', nat_v, nat_d)}{f(' from ', era_v, era_d)}. {f('Concept: ', char_v, char_d)}. {f('Grooming: ', groom_v, groom_d)}. {f('Hair Color: ', hc_v if hc_v != 'Others' else hc, h_col_d)} {f(', Texture: ', ht_v if ht_v != 'Others' else ht, h_tex_d)}. {f('Skin: ', aging_d[list(aging_d.keys())[1]], aging_d)}. {f('Material: ', mat_v if mat_v != 'Others' else mat)}. Technical: {f('', light_v, light_d)}, {f('', cam_v, cam_d)}, 8k raw photography, subsurface scattering."

    with c_master:
        st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_p}</div>', unsafe_allow_html=True)

# 4. فوتر
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} <span class="uona-tag">UONA GROUP</span>. ALL RIGHTS RESERVED
    </div>
    """, unsafe_allow_html=True)
