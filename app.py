import streamlit as st
from datetime import datetime
import os
import json
import base64

# ==========================================
# 1. تنظیمات پلتفرم و دیتابیس
# ==========================================
st.set_page_config(
    page_title="UONA STUDIO | AI SAAS", 
    page_icon="logo.PNG", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

DB_FILE = ".users_db.json"
PROJ_FILE = ".projects_db.json"

def load_json(file, default):
    if not os.path.exists(file):
        with open(file, "w") as f: json.dump(default, f)
    with open(file, "r") as f: return json.load(f)

def save_json(file, data):
    with open(file, "w") as f: json.dump(data, f)

def find_bg_file():
    possible_names = ["background.jpg", "background.jpeg", "background.png", "Background.jpg", "BACKGROUND.JPG"]
    for name in possible_names:
        if os.path.exists(name):
            return name
    return None

def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    
    mime_type = "image/png" if image_file.lower().endswith('.png') else "image/jpeg"
    
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"], .stApp {{
            background: linear-gradient(rgba(2,6,12,0.85), rgba(10,25,47,0.85)), url(data:{mime_type};base64,{encoded_string}) !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# 2. دیتابیس مگا پرامپت V2.0
# ==========================================

GENDER_LIST = ["Masculine / Male", "Feminine / Female", "Androgynous"]
AGE_LIST = ["Child / Pre-adolescent", "Adolescent / Teenager", "Young Adult (Early 20s)", "Middle-aged (Late 40s)", "Elderly / Senior", "Ancient / Centenarian"]

NAT_DESC = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure",
    "Syrian": "Levantine features, straight profile",
    "Turkish": "Eurasian features, strong facial contours, dark hair",
    "Indian": "South Asian features, deep-set dark eyes",
    "American": "Diverse North American features, varied skin tones",
    "European": "Caucasian features, prominent brow ridge, fair complexion",
    "African": "Sub-Saharan features, broad nasal structure, deep melanated skin",
    "Chinese": "East Asian features, epicanthic folds, high cheekbones"
}

ERA_DESC = {
    "Contemporary / Modern Day": "Current lighting, digital photography look",
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures",
    "Before Common Era (BCE)": "Ancient civilization styling, rudimentary tools",
    "Pre-Islamic Era": "Traditional regional heritage, antique textures",
    "Ancient Era (Hellenistic/Roman)": "Classical features, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures",
    "200 Years ago (Early 19th Century)": "Regency style, era-specific grooming",
    "150 years ago (Victorian Era)": "Formal, structured, refined textures",
    "100 Years ago (Roaring 20s)": "Vintage aesthetic, early 20th-century grooming",
    "50 Years ago (1970s Retro)": "Analog film look, warm hues",
    "Futuristic / Cyberpunk": "Neon accents, synthetic materials",
    "Post-Apocalyptic": "Dirty, weathered, distressed textures"
}

# --- بخش تخصصی آرک‌ها طبق سند V2.0 ---
AGING_ARC_DATA = {
    "Wrinkles": ["Dynamic lines (crow's feet)", "Fixed nasolabial folds", "Deep perioral creases", "Advanced parchment-like rhytids"],
    "Sagging": ["Youthful malar pads", "Softened jawline", "Structural jowls", "Facial atrophy/sunken temples"],
    "Texture": ["Uniform tone", "Uneven grain", "Patchy hyperpigmentation", "Senile liver spots"],
    "Hair": ["Baseline density", "20% Salt & Pepper", "80% depigmented", "Full white/wispy texture"]
}

SFX_TRAUMA_ARC_DATA = {
    "Bruises": ["Fresh Crimson Erythema", "Violet Hematoma", "Green-Yellow Oxidation", "Faint Amber Resolution"],
    "Abrasions": ["Friction stippling", "Coagulated brown crust", "Rigid eschar texture", "Pink epithelial layer"],
    "Burns": ["Flash Erythema", "Vesiculation (blisters)", "Raw pink exudate", "Hyperpigmented desquamation"],
    "Acid": ["Chemical bubbling", "Deep dermal pits", "Charred leathery eschar", "Atrophic sunken scar"]
}

# ==========================================
# 3. مدیریت وضعیت (State Machine)
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'plan' not in st.session_state: st.session_state.plan = "UONA Core"
if 'route' not in st.session_state: st.session_state.route = 'login'
if 'step' not in st.session_state: st.session_state.step = 1

if 'draft' not in st.session_state: 
    st.session_state.draft = {
        "actor":"None", "gen":"Masculine / Male", "age":"Young Adult (Early 20s)", "nat":"Iranian", 
        "era":"Contemporary / Modern Day", "h_col":"None", "h_tex":"None", "sfx":"None", "mat":"None", 
        "char":"None", "groom":"None", "cam":"None", "light":"None", "size":"None",
        "age_prog":"None", "sfx_prog":"None"
    }

def go_to(route): st.session_state.route = route; st.rerun()
def next_step(): st.session_state.step += 1; st.rerun()
def prev_step(): st.session_state.step -= 1; st.rerun()
def add_n(lst): return ["None"] + lst + ["Others"]

# ==========================================
# 4. موتور تولید پرامپت (V2.0 Core)
# ==========================================
def generate_prompt(draft):
    is_arc = (draft['age_prog'] != "None") or (draft['sfx_prog'] != "None")
    
    prompt = "Uona Studio Signature: [Neutral Matte Background, Cinematic Color Grading, Prosthetic Makeup Application]. "
    
    if is_arc:
        prompt += "Horizontal Character progression sheet, horizontal triptych. Three side-by-side panels separated by sharp glowing neon vertical lines. The EXACT SAME character facial identity across all frames. "
        
        if draft['age_prog'] != "None":
            cat = draft['age_prog']
            stages = AGING_ARC_DATA[cat]
            prompt += f"Timeline Aging Arc: {cat}. Stage 1: {stages[0]}. Stage 2: {stages[1]}. Stage 3: {stages[3]}. "
            prompt += "Label text at bottom of each panel: 'Initial Stage', 'Mid Progression', 'Final State'. "
        
        elif draft['sfx_prog'] != "None":
            cat = draft['sfx_prog']
            stages = SFX_TRAUMA_ARC_DATA[cat]
            prompt += f"SFX Trauma Timeline: {cat}. Stage 1: {stages[0]}. Stage 2: {stages[1]}. Stage 3: {stages[3]}. "
            prompt += "Label text at bottom: 'Fresh', 'Healing', 'Resolved'. "
    else:
        prompt += f"A professional cinematic portrait of a {draft['age']} {draft['gen']} from {draft['nat']}. "

    prompt += f"Technical: 8k UHD, cinematic raw photography, {draft['cam']}, {draft['light']}. focus on prosthetic makeup accuracy."
    return prompt

# ==========================================
# 5. موتور استایل (CSS Engine - ORIGINAL UI)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%);
        height: 100vh; overflow-x: hidden;
    }

    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    div.element-container:has(.logo-marker) + div.element-container button {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        height: auto !important;
        display: flex !important;
        justify-content: flex-start !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button p {
        color: #00f2ff !important;
        font-family: 'Cinzel', serif !important;
        font-size: 1.5rem !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
    }

    .title-main { font-family: 'Cinzel'; color: #ffffff !important; font-size: 2.5rem; font-weight: 800; letter-spacing: 10px; margin: 0; text-shadow: 0 0 15px rgba(0, 242, 255, 0.5); }
    .subtitle { color: #00f2ff; font-family: 'Montserrat'; font-size: 0.8rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 30px;}

    label, .stMarkdown p { color: #00e5ff !important; font-family: 'Montserrat' !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.75rem !important; }

    div[data-baseweb="input"] > div { background-color: rgba(0, 20, 40, 0.9) !important; border: 1px solid rgba(0, 242, 255, 0.4) !important; border-radius: 10px !important; }
    
    .stButton > button {
        border: none !important; border-radius: 8px !important; font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; background-color: #00f2ff !important; color: #000000 !important;
    }

    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 25px; backdrop-filter: blur(10px); margin-bottom: 20px; }
    
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 30px; color: #4a5d73; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 900; }
    .step-active { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 6. مسیرها (Routes)
# ==========================================

# --- LOGIN ---
if st.session_state.route == 'login':
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=280)
    with c2:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px;'>RESTRICTED ACCESS</h1>", unsafe_allow_html=True)
        u_name = st.text_input("USERNAME")
        u_pass = st.text_input("PASSWORD", type="password")
        if st.button("AUTHENTICATE", use_container_width=True):
            if u_name == "sep" and u_pass == "1386sy":
                st.session_state.auth = True
                st.session_state.user = u_name
                st.session_state.plan = "MASTER APEX"
                go_to('dashboard')
    st.stop()

# --- HEADER (Visible on all pages) ---
if st.session_state.route != 'login':
    c_head1, c_head2 = st.columns([1, 3])
    with c_head1:
        st.markdown('<span class="logo-marker"></span>', unsafe_allow_html=True)
        if st.button("UONA STUDIO"): go_to('dashboard')
    with c_head2:
        st.markdown(f'<div style="text-align:right; color:white; font-family:Montserrat; font-size:0.8rem; padding-top:15px;">{st.session_state.plan} | {st.session_state.user.upper()}</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(0,242,255,0.2); margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)

# --- DASHBOARD ---
if st.session_state.route == 'dashboard':
    bg = find_bg_file()
    if bg: add_bg_from_local(bg)
    st.markdown("<h2 class='title-main' style='text-align:center;'>CONTROL CENTER</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>🎬</h1><h3>NEW PROJECT</h3></div>', unsafe_allow_html=True)
        if st.button("START", key="b1", use_container_width=True): st.session_state.step = 1; go_to('builder')
    with c2:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>📂</h1><h3>LIBRARY</h3></div>', unsafe_allow_html=True)
        st.button("OPEN", key="b2", use_container_width=True)
    with c3:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>⚙️</h1><h3>SETTINGS</h3></div>', unsafe_allow_html=True)
        st.button("CONFIG", key="b3", use_container_width=True)

# --- CHARACTER BUILDER (STEPS) ---
elif st.session_state.route == 'builder':
    st.markdown(f"""<div class="step-indicator"><span class="{'step-active' if st.session_state.step==1 else ''}">1. IDENTITY</span> ➔ <span class="{'step-active' if st.session_state.step==2 else ''}">2. PROGRESSION</span> ➔ <span class="{'step-active' if st.session_state.step==3 else ''}">3. TECHNICAL</span></div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    d = st.session_state.draft

    if st.session_state.step == 1:
        d['gen'] = st.selectbox("GENDER", GENDER_LIST)
        d['age'] = st.selectbox("AGE", AGE_LIST)
        d['nat'] = st.selectbox("NATIONALITY", list(NAT_DESC.keys()))
        if st.button("NEXT ➔"): next_step()

    elif st.session_state.step == 2:
        # Rule: Lock SFX if age < 22
        is_young = d['age'] in ["Child / Pre-adolescent", "Adolescent / Teenager"]
        
        d['age_prog'] = st.selectbox("AGING ARC", add_n(list(AGING_ARC_DATA.keys())))
        
        if is_young:
            st.warning("SFX Arcs locked for base age.")
            d['sfx_prog'] = "None"
        else:
            d['sfx_prog'] = st.selectbox("SFX TRAUMA ARC", add_n(list(SFX_TRAUMA_ARC_DATA.keys())))
            
        c1, c2 = st.columns(2)
        if c1.button("⬅ BACK"): prev_step()
        if c2.button("NEXT ➔"): next_step()

    elif st.session_state.step == 3:
        d['cam'] = st.selectbox("CAMERA", ["Portrait 85mm", "Macro 100mm", "Wide 35mm"])
        d['light'] = st.selectbox("LIGHTING", ["Rembrandt Lighting", "Softbox Studio", "Rim Lighting"])
        
        c1, c2 = st.columns(2)
        if c1.button("⬅ BACK"): prev_step()
        if c2.button("GENERATE PROMPT 🚀"): go_to('result')
    st.markdown('</div>', unsafe_allow_html=True)

# --- RESULT ---
elif st.session_state.route == 'result':
    st.markdown("<h2 class='title-main'>FINAL ARCHITECTURE</h2>", unsafe_allow_html=True)
    p = generate_prompt(st.session_state.draft)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.code(p, language="markdown")
    if st.button("⬅ BACK TO DASHBOARD"): go_to('dashboard')
    st.markdown('</div>', unsafe_allow_html=True)
