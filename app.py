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

    .nav-bar {
        display: flex; align-items: center; padding: 10px 50px;
        background: rgba(2, 6, 12, 0.8); border-bottom: 1px solid rgba(0, 242, 255, 0.2);
        justify-content: space-between;
    }
    .title-main {
        font-family: 'Cinzel'; color: #ffffff; font-size: 3.2rem; font-weight: 800; 
        letter-spacing: 12px; margin: 0; text-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
    }
    .slogan-main { font-family: 'Montserrat'; color: #00f2ff; font-size: 0.75rem; letter-spacing: 5px; text-transform: uppercase; }

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
        padding: 10px 20px !important;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #ffffff !important;
        box-shadow: 0 0 15px #00f2ff;
    }

    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 15px; padding: 20px; text-align: center; backdrop-filter: blur(10px);
    }
    
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.7rem; margin-top: 8px; }
    .star { color: #ff4b4b; }
    
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 8px; font-weight: 900; font-size: 1.1rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { 
        background-color: #ffffff; color: #111; padding: 20px; border-radius: 0 0 8px 8px; 
        border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 1rem; 
        line-height: 1.6; height: 380px; overflow-y: auto;
    }
    
    .footer { 
        position: fixed; bottom: 0; width: 100%; text-align: center; padding: 15px; 
        border-top: 1px solid rgba(0, 242, 255, 0.1); background: rgba(0,0,0,0.5);
        color: #ffffff; opacity: 0.6; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 300;
    }
    .uona-tag { color: #00f2ff; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- هدر ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    try: st.image("image.png", width=90)
    except: st.markdown("<div style='width:80px; height:80px; background:#00f2ff; border-radius:12px;'></div>", unsafe_allow_html=True)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1><div class="slogan-main">The Art of Cinematic Transformation</div>', unsafe_allow_html=True)

# --- پورتال ---
if st.session_state.page == 'home':
    st.markdown("<br><br><h3 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:4px;'>SELECT DESIGN MODULE</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="module-card"><h1>🎬</h1><h3>CINEMATIC</h3></div>', unsafe_allow_html=True)
        if st.button("OPEN MODULE", key="cine"): st.session_state.page = 'cinematic'; st.rerun()
    with c2:
        st.markdown('<div class="module-card"><h1>📺</h1><h3>SERIES</h3></div>', unsafe_allow_html=True)
        if st.button("OPEN MODULE", key="series"): st.session_state.page = 'cinematic'; st.rerun()
    with c3:
        st.markdown('<div class="module-card" style="opacity:0.4;"><h1>🎭</h1><h3>THEATER</h3></div>', unsafe_allow_html=True)
        st.button("COMING SOON", disabled=True, key="th")
    with c4:
        st.markdown('<div class="module-card" style="opacity:0.4;"><h1>👠</h1><h3>FASHION</h3></div>', unsafe_allow_html=True)
        st.button("COMING SOON", disabled=True, key="fs")

# --- ماژول Cinematic ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK"): st.session_state.page = 'home'; st.rerun()
    
    def add_n(d): 
        if isinstance(d, dict): return {**{"None": ""}, **d}
        return ["None"] + d

    # دیتاها
    gender_d = add_n({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours", "Androgynous": "blend of features"})
    age_d = add_n({"Child / Pre-adolescent": "textureless skin", "Adolescent / Teenager": "oily skin", "Young Adult (Early 20s)": "peak elasticity", "Middle-aged (Late 40s)": "initial fat loss", "Elderly / Senior": "collagen loss", "Ancient / Centenarian": "paper-thin skin"})
    nat_d = add_n({"Iranian": "prominent nasal bridge", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Saudi": "Peninsular Arab features", "Kuwaiti": "Northern Gulf", "Syrian": "Levantine features", "American": "Diverse structures", "Indian": "South Asian", "Chinese": "East Asian", "African": "Deep melanated", "European": "Caucasian", "Turkish": "Eurasian"})
    era_d = add_n({"Stone Age": "Primitive", "BCE": "Ancient", "Pre-Islamic": "Traditional", "Ancient Era": "Classical", "Medieval": "Gritty", "200 Years Ago": "Regency", "150 Years Ago": "Victorian", "100 Years Ago": "Roaring 20s", "50 Years Ago": "Analog film", "Contemporary": "Current lighting", "Futuristic": "High-tech glow", "Post-Apocalyptic": "Weathered"})
    char_d = add_n({"Heroic Warrior": "Strong jawline", "Sinister Villain": "Harsh shadows", "Scholar": "Refined", "Royal": "Elegant", "Mercenary": "Rugged", "Mystic": "Otherworldly", "CEO": "Clean-cut", "Athlete": "Defined", "Artist": "Creative", "Citizen": "Naturalistic", "Technician": "Grime", "Student": "Youthful", "Model": "Angular", "Grandparent": "Dignified", "Urban": "Modern edge", "Outdoorsman": "Sun-damaged", "Gala Guest": "Glamorous", "Sickly": "Pale skin"})
    groom_d = add_n({"Saudi Anchor": "sharp angled", "Pyramidal Moustache": "wide base", "Clean Shaven": "smooth", "Light Stubble": "short", "Heavy Stubble": "rough", "Designer Stubble": "precisely trimmed", "Shadow Fade": "smooth gradient", "Goatee": "chin beard", "Classic Goatee": "connected", "Van Dyke": "pointed", "Anchor Beard": "thin", "Short Boxed": "square edges", "Medium Boxed": "structured", "Long Full": "natural growth", "Unkempt": "messy", "Scruffy": "patchy", "Wild": "chaotic", "Bedouin": "weathered", "Viking": "braided", "Medieval": "period growth", "Philosopher": "soft", "Warrior": "rugged", "Graying": "mixed-tone", "Split Texture": "dual-textured", "Short Sideburns": "above ear", "Mid-Ear": "tragus level", "Long Sideburns": "ear lobe", "Extra-Long": "pass lobe", "High Sideburns": "temple level", "Tapered": "faded", "Square": "clean edges", "Pointed": "triangle", "Rounded": "circular", "Pencil": "thin line", "Flared": "wide", "Angled": "slanted", "Mutton Chops": "wide full", "Friendly Mutton": "connected", "Soul Patch": "below lip"})
    sfx_cats = {
        "Acute Trauma": ["Fresh Katana/Sword Slash", "Glass Laceration", "Blunt Force Contusion", "Chemical Acid Burn"],
        "Healing Stages": ["3-Day Old Wound", "1-Week Old Wound", "1-Month Old Scar", "1-Year Old Keloid", "5-Year Old Atrophic Scar"],
        "Bruising": ["Fresh Periorbital Hematoma", "24-Hour Old Bruise", "3-Day Old Bruise", "15-Day Old Fading Bruise"],
        "Skin Conditions": ["1st Degree Sunburn", "2nd Degree Burn", "Bilateral Vitiligo", "Diffuse Hyperpigmentation"]
    }
    aging_d = add_n({"Deep Nasolabial Folds": "smile lines", "Pronounced Crow's Feet": "eye wrinkles", "Hooded Eyelids": "sagging lids", "Dermal Crepiness": "paper skin", "Visible Liver Spots": "age spots", "Sagging Jowls": "loose skin", "Frontal Rhytids": "forehead ridges", "Periorbital Hollows": "sunken eyes", "Vertical Lip Lines": "mouth wrinkles", "Age-related Telangiectasia": "capillaries"})
    light_d = add_n({"Rembrandt": "triangle light", "Cold Rim": "blue backlight", "Chiaroscuro": "contrast", "Teal and Orange": "cinematic", "God Rays": "linear", "Golden Hour": "sunset", "High-Key": "bright", "Low-Key": "moody", "Neon Cyberpunk": "edge light", "Hard Top": "harsh shadow", "Candlelight": "unsteady", "Softbox": "velvety"})
    cam_d = add_n({"85mm Eye-Level": "no distortion", "100mm Macro": "extreme detail", "50mm Dutch": "tilted tension", "35mm Low-Angle": "hero shot", "24mm High-Angle": "thinning", "200mm Profile": "compressed", "50mm Top-Down": "design focus", "85mm Three-Quarter": "standard"})
    size_l = add_n(["4:5 (Portrait)", "16:9 (Widescreen)", "2.39:1 (Anamorphic)", "1:1 (Square)", "9:16 (Vertical)"])

    c_form, c_master = st.columns([1.8, 1])
    with c_form:
        f1, f2 = st.columns(2)
        with f1:
            st.markdown('<p class="label-text">Actor Reference <span class="star">*</span></p>', unsafe_allow_html=True)
            actor = st.selectbox("Actor Reference", ["None", "No", "Yes"], key="act", label_visibility="collapsed")
            st.markdown('<p class="label-text">Gender & Age <span class="star">*</span></p>', unsafe_allow_html=True)
            gen = st.selectbox("Gender", list(gender_d.keys()), key="gen", label_visibility="collapsed")
            age = st.selectbox("Age Range", list(age_d.keys()), key="age", label_visibility="collapsed")
            st.markdown('<p class="label-text">Skin Aging & Texture</p>', unsafe_allow_html=True)
            age_tex = st.selectbox("Aging Details", list(aging_d.keys()), key="atex", label_visibility="collapsed")
            st.markdown('<p class="label-text">SFX Category <span class="star">*</span></p>', unsafe_allow_html=True)
            s_cat = st.selectbox("SFX Category", ["None"] + list(sfx_cats.keys()), key="scat", label_visibility="collapsed")
            st.markdown('<p class="label-text">Specific Trauma / Wound</p>', unsafe_allow_html=True)
            s_type = st.selectbox("Specific Wound", sfx_cats[s_cat] if s_cat != "None" else ["None"], key="stype", label_visibility="collapsed")
        with f2:
            st.markdown('<p class="label-text">Nationality & Era <span class="star">*</span></p>', unsafe_allow_html=True)
            nat = st.selectbox("Nationality", list(nat_d.keys()), key="nat", label_visibility="collapsed")
            era = st.selectbox("Historical Era", list(era_d.keys()), key="era", label_visibility="collapsed")
            st.markdown('<p class="label-text">Character Concept & Grooming</p>', unsafe_allow_html=True)
            char = st.selectbox("Character Concept", list(char_d.keys()), key="char", label_visibility="collapsed")
            groom = st.selectbox("Grooming Style", list(groom_d.keys()), key="groom", label_visibility="collapsed")
            st.markdown('<p class="label-text">Camera & Lens Perspective <span class="star">*</span></p>', unsafe_allow_html=True)
            cam = st.selectbox("Camera Perspective", list(cam_d.keys()), key="cam", label_visibility="collapsed")
            st.markdown('<p class="label-text">Lighting Environment</p>', unsafe_allow_html=True)
            light = st.selectbox("Lighting Environment", list(light_d.keys()), key="light", label_visibility="collapsed")
            st.markdown('<p class="label-text">Frame Size / Aspect Ratio</p>', unsafe_allow_html=True)
            size_sel = st.selectbox("Aspect Ratio", size_l, key="psize", label_visibility="collapsed")

    def f(p, v, d=None):
        if v == "None" or not v: return ""
        desc = f" ({d[v]})" if d and v in d and d[v] else ""
        return f"{p}{v}{desc}"

    p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
    p_sfx = f" [SFX STUDY: Apply {s_type} SFX as a makeup layer]." if s_type != "None" else ""
    p_size = f" Aspect Ratio {size_sel}" if size_sel != "None" else ""
    p_aging = f", with {f('', age_tex, aging_d)}" if age_tex != "None" else ""
    
    final_prompt = f"{p_actor}A professional cinematic{p_size} portrait of a {f('', gen, gender_d)} {f('', age, age_d)}{p_aging} {f('', nat, nat_d)}{f(' from the ', era, era_d)}. {f('Concept: ', char, char_d)}. {f('Grooming: ', groom, groom_d)}.{p_sfx} Technical: {f('', light, light_d)}, {f('', cam, cam_d)}, 8k, raw photography."

    with c_master:
        st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)

# 6. فوتر
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} <span class="uona-tag">UONA GROUP</span>. ALL RIGHTS RESERVED. | 
        CINEMATIC CHARACTER AI PLATFORM
    </div>
    """, unsafe_allow_html=True)
