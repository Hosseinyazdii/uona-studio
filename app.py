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

    /* تایتل سفید درخشان و خوانا */
    .nav-bar {
        display: flex; align-items: center; padding: 10px 50px;
        background: rgba(2, 6, 12, 0.8); border-bottom: 1px solid rgba(0, 242, 255, 0.2);
        justify-content: space-between;
    }
    .title-main {
        font-family: 'Cinzel'; color: #ffffff !important; font-size: 3rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; text-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }
    .slogan-main { font-family: 'Montserrat'; color: #00f2ff; font-size: 0.7rem; letter-spacing: 5px; text-transform: uppercase; }

    /* دکمه‌های پورتال: متن مشکی روی فیروزه‌ای */
    .stButton > button {
        background-color: #00f2ff !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 50px !important;
        font-family: 'Montserrat' !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem !important;
        transition: 0.3s;
    }
    .stButton > button:hover { background-color: #ffffff !important; box-shadow: 0 0 15px #00f2ff; }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 15px; padding: 20px; text-align: center; backdrop-filter: blur(10px);
    }
    
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.7rem; margin-top: 8px; }
    .star { color: #ff4b4b; }
    
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 8px; font-weight: 900; font-size: 1.1rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { 
        background-color: #ffffff; color: #111; padding: 20px; border-radius: 0 0 8px 8px; 
        border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 0.95rem; 
        line-height: 1.5; height: 350px; overflow-y: auto;
    }
    
    .footer { 
        position: fixed; bottom: 0; width: 100%; text-align: center; padding: 12px; 
        border-top: 1px solid rgba(0, 242, 255, 0.1); background: rgba(0,0,0,0.5);
        color: #ffffff; opacity: 0.6; font-family: 'Montserrat'; font-size: 0.65rem; font-weight: 300;
    }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- هدر ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    try: st.image("image.png", width=85)
    except: st.markdown("<div style='width:70px; height:70px; background:#00f2ff; border-radius:10px;'></div>", unsafe_allow_html=True)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1><div class="slogan-main">The Art of Cinematic Transformation</div>', unsafe_allow_html=True)

# --- پورتال ---
if st.session_state.page == 'home':
    st.markdown("<br><br><h3 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:4px;'>SELECT DESIGN MODULE</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    modules = [("🎬", "CINEMATIC", "cine"), ("📺", "SERIES", "cine"), ("🎭", "THEATER", "soon"), ("👠", "FASHION", "soon")]
    for idx, (icon, name, target) in enumerate(modules):
        with [c1, c2, c3, c4][idx]:
            st.markdown(f'<div class="module-card"><h1>{icon}</h1><h3>{name}</h3></div>', unsafe_allow_html=True)
            if target == "cine":
                if st.button(f"OPEN {name}", key=name): st.session_state.page = 'cinematic'; st.rerun()
            else: st.button("COMING SOON", disabled=True, key=name)

# --- ماژول Cinematic (تکمیل شده) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    
    def add_n(d): 
        if isinstance(d, dict): return {**{"None": ""}, **d}
        return ["None"] + d

    # دیتاها (بر اساس شیت‌های اصلی)
    gender_d = add_n({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours"})
    age_d = add_n({"Elderly": "collagen loss", "Middle-aged": "fat loss", "Young Adult": "peak elasticity", "Child": "smooth"})
    nat_d = add_n({"Iranian": "prominent nasal bridge", "Saudi": "Peninsular Arab", "European": "Caucasian", "African": "Melanated"})
    era_d = add_n({"Ancient": "Classical", "Medieval": "Gritty", "100 Years Ago": "Period", "Contemporary": "Modern"})
    char_d = add_n({"Heroic Warrior": "Strong", "Sinister Villain": "Harsh", "Scholar": "Refined", "Mercenary": "Rugged"})
    groom_d = add_n({"Clean Shaven": "smooth", "Light Stubble": "short", "Heavy Stubble": "rough", "Full Beard": "natural"})
    sfx_cats = {"Acute Trauma": ["Katana Slash", "Glass Laceration"], "Healing Stages": ["3-Day Wound", "1-Month Scar"], "Bruising": ["Fresh Hematoma", "3-Day Bruise"]}
    
    aging_d = add_n({"Deep Nasolabial Folds": "smile lines", "Crow's Feet": "eye wrinkles", "Liver Spots": "age spots"})
    h_tex_d = add_n({"Afro": "coils", "Wavy": "S-shape", "Curly": "ringlets", "Straight": "silky", "Matted": "weathered"})
    h_col_d = add_n({"Jet black": "Natural", "Espresso": "Dark", "Ash blonde": "Cool", "50% Grey": "even"})
    light_d = add_n({"Rembrandt": "triangle", "Teal and Orange": "cinematic", "Neon Cyberpunk": "edge", "Softbox": "velvety"})
    cam_d = add_n({"85mm Eye-Level": "no distortion", "100mm Macro": "extreme detail", "50mm Dutch": "tilted"})
    size_l = add_n(["4:5 (Portrait)", "16:9 (Widescreen)", "2.39:1 (Anamorphic)", "1:1 (Square)"])
    mat_l = add_n(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin", "Matte Sealer"])

    c_form, c_master = st.columns([2.1, 1])
    with c_form:
        f1, f2, f3 = st.columns(3)
        with f1:
            st.markdown('<p class="label-text">Actor & Identity <span class="star">*</span></p>', unsafe_allow_html=True)
            actor = st.selectbox("", ["None", "No", "Yes"], key="act", label_visibility="collapsed")
            gen = st.selectbox("", list(gender_d.keys()), key="gen", label_visibility="collapsed")
            age = st.selectbox("", list(age_d.keys()), key="age", label_visibility="collapsed")
            st.markdown('<p class="label-text">Hair & Beard Color</p>', unsafe_allow_html=True)
            h_col = st.selectbox("", list(h_col_d.keys()), key="hcol", label_visibility="collapsed")
            st.markdown('<p class="label-text">Hair Texture</p>', unsafe_allow_html=True)
            h_tex = st.selectbox("", list(h_tex_d.keys()), key="htex", label_visibility="collapsed")
        with f2:
            st.markdown('<p class="label-text">Origin & Era <span class="star">*</span></p>', unsafe_allow_html=True)
            nat = st.selectbox("", list(nat_d.keys()), key="nat", label_visibility="collapsed")
            era = st.selectbox("", list(era_d.keys()), key="era", label_visibility="collapsed")
            st.markdown('<p class="label-text">SFX & Trauma</p>', unsafe_allow_html=True)
            s_cat = st.selectbox("", ["None"] + list(sfx_cats.keys()), key="scat", label_visibility="collapsed")
            s_type = st.selectbox("", sfx_cats[s_cat] if s_cat != "None" else ["None"], key="stype", label_visibility="collapsed")
            st.markdown('<p class="label-text">Material Finish</p>', unsafe_allow_html=True)
            mat = st.selectbox("", mat_l, key="mat", label_visibility="collapsed")
        with f3:
            st.markdown('<p class="label-text">Concept & Grooming</p>', unsafe_allow_html=True)
            char = st.selectbox("", list(char_d.keys()), key="char", label_visibility="collapsed")
            groom = st.selectbox("", list(groom_d.keys()), key="groom", label_visibility="collapsed")
            st.markdown('<p class="label-text">Technical & Size <span class="star">*</span></p>', unsafe_allow_html=True)
            cam = st.selectbox("", list(cam_d.keys()), key="cam", label_visibility="collapsed")
            light = st.selectbox("", list(light_d.keys()), key="light", label_visibility="collapsed")
            size_sel = st.selectbox("", size_l, key="psize", label_visibility="collapsed")

    def f(p, v, d=None):
        if v == "None" or not v: return ""
        desc = f" ({d[v]})" if d and v in d and d[v] else ""
        return f"{p}{v}{desc}"

    p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
    p_sfx = f" [SFX STUDY: Apply {s_type} SFX as a makeup layer]." if s_type != "None" else ""
    p_size = f" Aspect Ratio {size_sel}" if size_sel != "None" else ""
    
    final_prompt = f"{p_actor}A professional cinematic{p_size} portrait of a {f('', gen, gender_d)} {f('', age, age_d)} {f('', nat, nat_d)}{f(' from ', era, era_d)}. {f('Concept: ', char, char_d)}. {f('Grooming: ', groom, groom_d)}. {f('Hair: ', h_col, h_col_d)} {f(', Texture: ', h_tex, h_tex_d)}. {f('Makeup Material: ', mat)}. {p_sfx} Technical: {f('', light, light_d)}, {f('', cam, cam_d)}, 8k, raw photography."

    with c_master:
        st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)

st.markdown(f"<div class='footer'>© {datetime.now().year} UONA GROUP | ALL RIGHTS RESERVED</div>", unsafe_allow_html=True)
