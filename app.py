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
# 2. دیتابیس مگا پرامپت (V2.1 - Scientific Logic)
# ==========================================

GENDER_LIST = ["Masculine / Male", "Feminine / Female", "Androgynous"]
AGE_LIST = ["Child / Pre-adolescent", "Adolescent / Teenager", "Young Adult (Early 20s)", "Middle-aged (Late 40s)", "Elderly / Senior", "Ancient / Centenarian"]

NAT_DESC = {"Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin", "Egyptian": "North African features, warm bronze skin tone", "Emirati": "Gulf Arab features, sharp jawline, tanned skin", "Saudi": "Peninsular Arab features, high cheekbones", "Kuwaiti": "Northern Gulf features", "Syrian": "Levantine features", "Turkish": "Eurasian features", "Indian": "South Asian features", "American": "Diverse features", "European": "Caucasian features", "African": "Sub-Saharan features", "Chinese": "East Asian features"}
ERA_DESC = {"Contemporary / Modern Day": "Current lighting, sharp details", "Stone Age / Prehistoric": "Primitive aesthetic, raw textures", "Before Common Era (BCE)": "Ancient civilization styling", "Pre-Islamic Era": "Traditional regional heritage", "Ancient Era (Hellenistic/Roman)": "Classical features", "Medieval / Dark Ages": "Gritty, rustic, heavy textures", "Victorian Era": "Formal, structured", "1970s Retro": "Analog film look", "Futuristic / Cyberpunk": "Neon accents", "Post-Apocalyptic": "Dirty, weathered textures"}
CONCEPTS = {"Heroic Warrior": "Strong jawline, confident gaze", "Sinister Villain": "Harsh shadows, menacing expression", "Scholar / Intellectual": "Refined appearance", "Royal / Aristocratic": "Elegant posture", "Mercenary / Outlaw": "Rugged, weathered", "Mystic / Shaman": "Otherworldly look", "Corporate CEO": "Clean-cut professional", "Elite Athlete": "Defined muscularity", "Ailing Character": "Pale skin, dark circles"}
GROOM_DESC = {"Saudi Anchor Beard": "Sharp angular form", "Pyramidal Moustache": "Wide edges", "Clean Shaven": "Smooth skin", "Light Stubble": "Very short stubble", "Heavy Stubble": "Thicker rough texture", "Goatee": "Chin beard only", "Full Beard": "Natural dense growth"}
TECH_LENS = {"85 mm Lens": "Portrait, shallow DOF", "100 mm Macro": "Extreme detail, skin pores", "35 mm Lens": "Cinematic context"}
TECH_LIGHT = {"Rembrandt Lighting": "Dramatic triangle shadow", "Cinematic Golden Hour": "Soft warm sunset", "High-Key Studio": "Clear SFX visibility", "Neon Cyberpunk": "Colorful rim light"}

# ==========================================
# 3. مدیریت وضعیت (State Machine)
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'route' not in st.session_state: st.session_state.route = 'login'
if 'step' not in st.session_state: st.session_state.step = 1

if 'draft' not in st.session_state: 
    st.session_state.draft = {
        "actor":"None", "gen":"Masculine / Male", "age":"Young Adult (Early 20s)", "nat":"Iranian", 
        "era":"Contemporary / Modern Day", "h_col":"None", "h_tex":"None", "sfx":"None", "mat":"None", 
        "char":"Average Citizen", "groom":"Clean Shaven", "cam":"85 mm Lens", "light":"Rembrandt Lighting", "size":"16:9",
        "arc_type":"None", "arc_stages": 4, "scenario_text": ""
    }

def go_to(route): st.session_state.route = route; st.rerun()
def next_step(): st.session_state.step += 1; st.rerun()
def prev_step(): st.session_state.step -= 1; st.rerun()
def add_n(lst): return ["None"] + lst + ["Others"]

# ==========================================
# 4. موتور پردازش هوشمند (Logic Engine)
# ==========================================
def generate_prompt(draft):
    # Baseline Constants
    baseline = f"Uona Studio Signature (Scientific Makeup Design). [Fixed Technical: {draft['cam']}, {draft['light']}, {draft['size']}]. "
    identity = f"Character Identity: {draft['gen']}, Base Age {draft['age']}, Nationality: {draft['nat']}, Type: {draft['char']}. Grooming: {draft['groom']}. "
    
    # Intelligence Layer (Phase 3)
    progression = ""
    if draft['arc_type'] != "None":
        progression = f"HORIZONTAL TRIPTYCH ARC. Four stages divided by 1px separators. Scenario: {draft['scenario_text']}. "
        if draft['arc_type'] == "Makeup/Aging":
            progression += "SCIENTIFIC AGING LOGIC: Inject [Epidermal thinning, Bone density loss, Solar lentigines, Gravity-induced ptosis]. "
        elif draft['arc_type'] == "SFX/Trauma":
            progression += "SCIENTIFIC TRAUMA LOGIC: Color Shift from wet crimson to dark scabbing, Material Transformation to fibrous scar tissue. "
        
        progression += f"PROGRESSION LABELS: Initial -> Spread -> Damage -> Final. PROGRESS LINE ACTIVE."
    
    final_p = baseline + identity + progression + " 8k, hyper-realistic, subsurface scattering, focus on prosthetic makeup accuracy."
    return " ".join(final_p.split())

# ==========================================
# 5. رابط کاربری (UI Engine - NO CHANGES)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%); height: 100vh; overflow-x: hidden; }
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    div.element-container:has(.logo-marker) + div.element-container button { background-color: transparent !important; border: none !important; box-shadow: none !important; padding: 0 !important; height: auto !important; display: flex !important; justify-content: flex-start !important; }
    div.element-container:has(.logo-marker) + div.element-container button p { color: #00f2ff !important; font-family: 'Cinzel', serif !important; font-size: 1.5rem !important; font-weight: 900 !important; text-transform: uppercase !important; }
    .title-main { font-family: 'Cinzel'; color: #ffffff !important; font-size: 2.5rem; font-weight: 800; letter-spacing: 10px; margin: 0; text-shadow: 0 0 15px rgba(0, 242, 255, 0.5); }
    label, .stMarkdown p { color: #00e5ff !important; font-family: 'Montserrat' !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.75rem !important; }
    div[data-baseweb="input"] > div { background-color: rgba(0, 20, 40, 0.9) !important; border: 1px solid rgba(0, 242, 255, 0.4) !important; border-radius: 10px !important; }
    .stButton > button { border: none !important; border-radius: 8px !important; font-family: 'Cinzel', serif !important; font-weight: 900 !important; text-transform: uppercase; background-color: #00f2ff !important; color: #000000 !important; }
    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 25px; backdrop-filter: blur(10px); margin-bottom: 20px; }
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 30px; color: #4a5d73; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 900; }
    .step-active { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 6. مسیرهای اپلیکیشن (App Routes)
# ==========================================

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
                st.session_state.auth = True; st.session_state.user = u_name; st.session_state.plan = "MASTER APEX"
                go_to('dashboard')
    st.stop()

if st.session_state.route != 'login':
    c_head1, c_head2 = st.columns([1, 3])
    with c_head1:
        st.markdown('<span class="logo-marker"></span>', unsafe_allow_html=True)
        if st.button("UONA STUDIO"): go_to('dashboard')
    with c_head2:
        st.markdown(f'<div style="text-align:right; color:white; font-family:Montserrat; font-size:0.8rem; padding-top:15px;">{st.session_state.plan} | {st.session_state.user.upper()}</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(0,242,255,0.2); margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)

if st.session_state.route == 'dashboard':
    bg = find_bg_file()
    if bg: add_bg_from_local(bg)
    st.markdown("<h2 class='title-main' style='text-align:center;'>CONTROL CENTER</h2>", unsafe_allow_html=True)
    c1, _, _ = st.columns(3)
    with c1:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>🎬</h1><h3>WORKFLOW V2.1</h3></div>', unsafe_allow_html=True)
        if st.button("START ARCHITECT", key="b1", use_container_width=True): st.session_state.step = 1; go_to('builder')

elif st.session_state.route == 'builder':
    st.markdown(f"""<div class="step-indicator"><span class="{'step-active' if st.session_state.step==1 else ''}">1. BASELINE</span> ➔ <span class="{'step-active' if st.session_state.step==2 else ''}">2. ARC CONFIG</span> ➔ <span class="{'step-active' if st.session_state.step==3 else ''}">3. REVIEW</span></div>""", unsafe_allow_html=True)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    d = st.session_state.draft

    if st.session_state.step == 1:
        st.markdown("<h4 style='color:#00f2ff;'>Phase 1: Character & Technical Baseline</h4>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            d['gen'] = st.selectbox("GENDER", GENDER_LIST)
            d['age'] = st.selectbox("BASE AGE", AGE_LIST)
            d['nat'] = st.selectbox("NATIONALITY", list(NAT_DESC.keys()))
            d['char'] = st.selectbox("CHARACTER TYPE", list(CONCEPTS.keys()))
        with c2:
            d['groom'] = st.selectbox("GROOMING", list(GROOM_DESC.keys()))
            d['cam'] = st.selectbox("CAMERA LENS", list(TECH_LENS.keys()))
            d['light'] = st.selectbox("CINEMATIC LIGHTING", list(TECH_LIGHT.keys()))
            d['size'] = st.selectbox("ASPECT RATIO", ["16:9", "4:5", "2.39:1", "1:1"])
        if st.button("NEXT ➔"): next_step()

    elif st.session_state.step == 2:
        st.markdown("<h4 style='color:#00f2ff;'>Phase 2: Arc Configuration</h4>", unsafe_allow_html=True)
        d['arc_type'] = st.selectbox("SELECT ARC TYPE", ["None", "Makeup/Aging", "SFX/Trauma", "Hybrid"])
        d['arc_stages'] = st.slider("NUMBER OF STAGES", 2, 6, 4)
        d['scenario_text'] = st.text_area("SCENARIO DESCRIPTION (e.g., A bullet wound getting infected over 30 days)", placeholder="Write your cinematic scenario here...")
        
        c1, c2 = st.columns(2)
        if c1.button("⬅ BACK"): prev_step()
        if c2.button("NEXT ➔"): next_step()

    elif st.session_state.step == 3:
        st.markdown("<h4 style='color:#00f2ff;'>Phase 4: Expert Output Review</h4>", unsafe_allow_html=True)
        final_prompt = generate_prompt(d)
        st.info(final_prompt)
        c1, c2 = st.columns(2)
        if c1.button("⬅ EDIT"): prev_step()
        if c2.button("SAVE & GENERATE 🚀"): go_to('result')
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.route == 'result':
    st.markdown("<h2 class='title-main'>FINAL MAKEUP DOCUMENT</h2>", unsafe_allow_html=True)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.code(generate_prompt(st.session_state.draft))
    if st.button("RETURN TO DASHBOARD"): go_to('dashboard')
    st.markdown('</div>', unsafe_allow_html=True)
