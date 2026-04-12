import streamlit as st
from datetime import datetime
import os
import json
import base64

# ==========================================
# 1. PLATFORM CONFIG
# ==========================================
st.set_page_config(
    page_title="UONA STUDIO | AI SFX ARCHITECT", 
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
        if os.path.exists(name): return name
    return None

def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    mime_type = "image/png" if image_file.lower().endswith('.png') else "image/jpeg"
    st.markdown(f"""<style>[data-testid="stAppViewContainer"] {{ background: linear-gradient(rgba(2,6,12,0.85), rgba(10,25,47,0.85)), url(data:{mime_type};base64,{encoded_string}) !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important; }}</style>""", unsafe_allow_html=True)

# ==========================================
# 2. MASTER DATABASE V2.0 (UONA SPEC)
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
    "Indian": "South Asian features, deep-set dark eyes, warm undertones",
    "American": "Diverse North American features, varied facial structures",
    "European": "Caucasian features, prominent brow ridge, fair complexion",
    "African": "Sub-Saharan features, broad nasal structure, deep melanated skin",
    "Chinese": "East Asian features, epicanthic folds, high cheekbones"
}

ERA_DESC = {
    "Contemporary / Modern Day": "Current lighting, digital photography look",
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures, survivalist look",
    "Before Common Era (BCE)": "Ancient civilization styling, rudimentary tools",
    "Pre-Islamic Era": "Traditional regional heritage, antique textures",
    "Ancient Era (Hellenistic/Roman)": "Classical features, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures, atmospheric mood",
    "200 Years ago (Early 19th Century)": "Regency style, era-specific grooming",
    "150 years ago (Victorian Era)": "Formal, structured, refined textures",
    "100 Years ago (Roaring 20s)": "Vintage aesthetic, early 20th-century lighting",
    "50 Years ago (1970s Retro)": "Analog film look, warm hues, vintage hair",
    "Futuristic / Cyberpunk": "Neon accents, synthetic materials, high-tech glow",
    "Post-Apocalyptic": "Dirty, weathered, distressed textures"
}

CHAR_TYPE_DESC = {
    "Heroic Warrior": "Strong jawline, confident gaze, slight battle wear",
    "Sinister Villain": "Harsh shadows, menacing expression, sharp features",
    "Scholar / Intellectual": "Refined appearance, focused eyes, thoughtful pose",
    "Royal / Aristocratic": "Elegant posture, pristine skin, luxury textures",
    "Mercenary / Outlaw": "Rugged, weathered, scars, untamed grooming",
    "Mystic / Shaman": "Otherworldly look, spiritual paint, ethereal lighting",
    "Corporate Executive / CEO": "Clean-cut, authoritative, sharp professional lighting",
    "Elite Athlete / Fitness Pro": "Defined muscularity, healthy skin glow",
    "Bohemian Artist": "Creative styling, messy hair, expressive eyes",
    "Average Citizen": "Naturalistic, candid, everyday lighting",
    "Blue-collar / Technician": "Grime, work-worn skin, functional appearance",
    "Academic Student": "Youthful, inquisitive, natural-soft lighting",
    "High-fashion Model": "Angular features, studio lighting, flawless skin",
    "Retiree / Grandparent": "Dignified aging, soft textures, wisdom-filled gaze",
    "Urban / Street Style": "Modern edge, trendy accessories",
    "Rural / Outdoorsman": "Sun-damaged skin, practical gear",
    "Red Carpet / Gala Guest": "Glamorous, high-contrast lighting",
    "Ailing / Sickly Character": "Pale skin, dark circles, visible veins"
}

GROOM_DESC = {
    "Saudi Anchor Beard": "Sharp angular form connected to chin",
    "Pyramidal Moustache": "Wide edges with narrow top",
    "Clean Shaven": "Smooth skin, no stubble finish",
    "Light Stubble": "Very short uniform shade pattern",
    "Heavy Stubble": "Thicker rough texture, irregular growth",
    "Designer Stubble": "Precisely trimmed sharp edges",
    "Shadow Fade Beard": "Faded sides, dense chin hair",
    "Goatee (No Mustache)": "Chin beard only, clean upper lip",
    "Classic Goatee": "Chin beard connected to mustache",
    "Short Boxed Beard": "Short full beard, square edges",
    "Long Full Beard": "Long thick natural growth pattern",
    "Unkempt Beard": "Messy disheveled texture",
    "Scruffy Beard": "Patchy slightly dirty grooming",
    "Viking Beard": "Long thick braided strands",
    "Warrior Beard": "Thick rugged battle-worn texture",
    "Short Sideburns": "Above ear level",
    "Mutton Chops": "Wide sideburns connected to mustache",
    "Soul Patch": "Small patch below lower lip"
}

# ==========================================
# 3. PHASE III: DYNAMIC ARC ENGINE
# ==========================================

AGING_ARC = {
    "Wrinkles": ["Dynamic lines (crow's feet)", "Fixed nasolabial folds", "Deep perioral creases", "Advanced parchment-like rhytids"],
    "Sagging": ["Youthful malar pads", "Softened jawline", "Structural jowls/ptosis", "Facial atrophy/sunken cheeks"],
    "Texture": ["Uniform tone", "Uneven grain/lentigines", "Patchy hyperpigmentation", "Senile liver spots/capillaries"],
    "Hair": ["Baseline density", "20% Salt & Pepper", "80% dominant white", "Full depigmentation/wispy"]
}

SFX_TRAUMA_ARC = {
    "Bruises": ["Fresh Crimson Erythema", "Violet Hematoma", "Green-Yellow Oxidation", "Faint Amber Resolution"],
    "Abrasions": ["Friction stippling", "Coagulated brown crust", "Rigid eschar texture", "Pink epithelial layer"],
    "Burns": ["Flash Erythema", "SFX Vesiculation (blisters)", "Raw pink exudate tissue", "Hyperpigmented desquamation"],
    "Acid": ["Chemical bubbling", "Deep dermal pits", "Charred leathery eschar", "Atrophic sunken scar"]
}

TECH_LENS = {"Macro 100mm": "Extreme close-up, macro skin pores", "Portrait 85mm": "Golden standard portrait, shallow DOF", "Wide 35mm": "Environmental context, slight distortion"}
TECH_LIGHT = {"Rembrandt Lighting": "45-degree key light, triangle shadow", "Softbox Studio": "Uniform soft light, SFX clarity", "Rim Lighting": "Backlit silhouette edges", "Top-Down Harsh": "Texture revealing forensic light"}

# ==========================================
# 4. STREAMLIT LOGIC & UI
# ==========================================

if 'auth' not in st.session_state: st.session_state.auth = False
if 'route' not in st.session_state: st.session_state.route = 'login'
if 'step' not in st.session_state: st.session_state.step = 1
if 'draft' not in st.session_state: 
    st.session_state.draft = {
        "gen":"Masculine / Male", "age":"Young Adult (Early 20s)", "nat":"Iranian", "era":"Contemporary / Modern Day",
        "char":"Average Citizen", "groom":"Clean Shaven", "tex":"Straight (Sleek)", "light":"Rembrandt Lighting",
        "cam":"Portrait 85mm", "arc_type":"None", "arc_sub":"None"
    }

def go_to(route): st.session_state.route = route; st.rerun()

# --- CSS INTEGRATION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #02060c; color: white; }
    .title-main { font-family: 'Cinzel'; color: #ffffff; font-size: 2.2rem; letter-spacing: 8px; text-align: center; text-shadow: 0 0 15px #00f2ff; }
    .glass-panel { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1); border-radius: 15px; padding: 30px; backdrop-filter: blur(10px); }
    .stButton > button { background-color: #00f2ff !important; color: black !important; font-family: 'Cinzel'; font-weight: 900; border-radius: 5px; }
    label { color: #00f2ff !important; font-family: 'Montserrat' !important; font-size: 0.8rem !important; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# ROUTE: LOGIN
# ==========================================
if st.session_state.route == 'login':
    c1, c2 = st.columns([1, 1])
    with c1:
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=300)
    with c2:
        st.markdown("<h1 class='title-main'>UONA STUDIO</h1>", unsafe_allow_html=True)
        u = st.text_input("ACCESS ID")
        p = st.text_input("SECURITY KEY", type="password")
        if st.button("AUTHENTICATE"):
            if u == "sep" and p == "1386sy":
                st.session_state.auth = True
                go_to('builder')
            else: st.error("ACCESS DENIED")
    st.stop()

# ==========================================
# ROUTE: BUILDER (PHASE I & II)
# ==========================================
if st.session_state.route == 'builder':
    st.markdown("<h1 class='title-main'>CHARACTER ARCHITECT V2.0</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    d = st.session_state.draft
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        d['gen'] = st.selectbox("GENDER", GENDER_LIST)
        d['age'] = st.selectbox("BASE AGE", AGE_LIST)
        d['nat'] = st.selectbox("NATIONALITY", list(NAT_DESC.keys()))
        
    with col2:
        d['era'] = st.selectbox("TIME PERIOD", list(ERA_DESC.keys()))
        d['char'] = st.selectbox("CHARACTER TYPE", list(CHAR_TYPE_DESC.keys()))
        
        # Rule 1 Logic: Gender Lock
        if d['gen'] == "Feminine / Female":
            st.warning("Grooming Locked for Female")
            d['groom'] = "Clean Shaven"
        else:
            d['groom'] = st.selectbox("GROOMING", list(GROOM_DESC.keys()))

    with col3:
        d['light'] = st.selectbox("LIGHTING", list(TECH_LIGHT.keys()))
        d['cam'] = st.selectbox("CAMERA / LENS", list(TECH_LENS.keys()))
        
        # Rule 2 Logic: Age Lock for SFX
        arc_options = ["None", "Aging Arc"]
        if d['age'] not in ["Child / Pre-adolescent", "Adolescent / Teenager"]:
            arc_options.append("SFX Trauma Arc")
        
        d['arc_type'] = st.selectbox("PROGRESSION ARC", arc_options)
        
        if d['arc_type'] == "Aging Arc":
            d['arc_sub'] = st.selectbox("AGING CATEGORY", list(AGING_ARC.keys()))
        elif d['arc_type'] == "SFX Trauma Arc":
            d['arc_sub'] = st.selectbox("TRAUMA CATEGORY", list(SFX_TRAUMA_ARC.keys()))

    if st.button("ASSEMBLE MASTER PROMPT", use_container_width=True):
        go_to('result')
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE: RESULT (PHASE III & MASTER FORMULA)
# ==========================================
elif st.session_state.route == 'result':
    st.markdown("<h1 class='title-main'>PROMPT ENGINE</h1>", unsafe_allow_html=True)
    d = st.session_state.draft
    is_arc = d['arc_type'] != "None"
    
    prompt = "Uona Studio Signature Style: [Neutral Matte Background, Photorealistic, Cinematic Color Grading]. "
    
    if is_arc:
        prompt += "Horizontal Character progression sheet, horizontal triptych. Three panels separated by vertical neon lines. The EXACT SAME character in a sequential timeline. "
        prompt += f"IDENTITY: {d['gen']}, {d['nat']} ({NAT_DESC[d['nat']]}), {d['era']}. "
        prompt += f"BASE STYLE: {d['char']}. Grooming: {d['groom']}. "
        
        if d['arc_type'] == "Aging Arc":
            stages = AGING_ARC[d['arc_sub']]
            prompt += f"PROGRESSION: [Aging Arc - {d['arc_sub']}]. "
            prompt += f"Panel 1: {stages[0]} (Initial). Panel 2: {stages[1]} (Mid). Panel 3: {stages[3]} (Final). "
        else:
            stages = SFX_TRAUMA_ARC[d['arc_sub']]
            prompt += f"PROGRESSION: [Cinematic SFX Trauma Arc - {d['arc_sub']}]. "
            prompt += f"Panel 1: {stages[0]} (Initial Stage). Panel 2: {stages[1]} (Spread). Panel 3: {stages[3]} (Final State). "
    else:
        prompt += f"A professional cinematic portrait of a {d['age']} {d['gen']} from {d['nat']}. "
        prompt += f"Era: {d['era']}. Character Type: {d['char']}. Grooming: {d['groom']}. "

    prompt += f"TECHNICAL: {TECH_LENS[d['cam']]}, {TECH_LIGHT[d['light']]}, 8k UHD, Subsurface scattering, Prosthetic Makeup Application focus."

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.code(prompt, language="markdown")
    if st.button("⬅ RE-ARCHITECT"): go_to('builder')
    st.markdown('</div>', unsafe_allow_html=True)
