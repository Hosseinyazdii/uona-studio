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
# 2. دیتابیس جامع و هوشمند سینمایی
# ==========================================
ACTORS_LIST = [
    "Cillian Murphy", "Tom Hardy", "Joaquin Phoenix", "Mads Mikkelsen", 
    "Keanu Reeves", "Brad Pitt", "Oscar Isaac", "Javier Bardem", 
    "Christian Bale", "Timothee Chalamet"
]

HAIR_COLORS = {
    "Jet Black": "Jet black / Natural deep black, cool undertones",
    "Espresso Brown": "Deep espresso brown / Dark chocolate",
    "Chestnut Brown": "Medium chestnut brown / Warm tones",
    "Ash Blonde": "Ash blonde (Cool tone, matte finish)",
    "Golden Blonde": "Golden blonde (Warm, sun-kissed)",
    "Platinum Blonde": "Platinum / Ice blonde, almost white",
    "Ginger / Auburn": "Vibrant ginger, copper, or deep auburn",
    "Salt & Pepper (10% Grey)": "Mostly dark with 10% faint grey hairs",
    "Salt & Pepper (30% Grey)": "Noticeable grey streaks, 30% grey",
    "Salt & Pepper (50% Grey)": "Even mix of grey and dark hair",
    "Salt & Pepper (70% Grey)": "Mostly grey/silver with dark roots",
    "Silver / Steel Grey": "Pure silver, steel grey tone",
    "Pure White": "Pure white, aged hair",
    "Dyed Unnatural": "Cyberpunk/Alternative dyed hair (Neon tones)"
}

CONCEPTS = {
    "Heroic Protagonist": "Strong jawline, determined gaze, slightly battle-worn, confident posture",
    "Sinister Villain": "Harsh angular shadows, menacing expression, sharp and calculating features",
    "Battle-Hardened Mercenary": "Scars, grime, rugged, exhausted but highly alert",
    "Aristocratic Royalty": "Elegant, pristine flawless skin, arrogant or noble posture, luxury textures",
    "Street Rogue / Outlaw": "Hooded or secretive, unpolished, survivalist look, sharp eyes",
    "Wise Scholar / Mentor": "Aged gracefully, thoughtful gentle gaze, refined appearance",
    "Cybernetic / Augmented": "Tech implants, synthetic skin patches, sci-fi integration",
    "Mystic / Shaman": "Ethereal look, tribal face paint or tattoos, distant otherworldly stare",
    "Everyday Citizen / Peasant": "Naturalistic, unglamorous, relatable everyday appearance",
    "Horror / Undead Entity": "Sunken eyes, pale or decaying skin, terrifying aura",
    "Corporate Executive": "Sharp, confident, immaculate grooming, authoritative"
}

LIGHT_DESC = {
    "Rembrandt Lighting": "Classic dramatic portrait lighting, distinct triangle of light on one cheek",
    "Cinematic Teal & Orange": "Hollywood blockbuster color grading, warm highlights, cool teal shadows",
    "Chiaroscuro (High Contrast)": "Renaissance style, extreme contrast between deep pitch-black shadows and bright highlights",
    "Harsh Midday Sun": "Hard, sharp shadows, realistic high-intensity outdoor daylight",
    "Overcast / Diffused Light": "Soft, shadowless, moody natural lighting",
    "Neon / Cyberpunk Glow": "Vibrant practical lights, glowing pink, blue, or green hues",
    "Under-lighting (Monster)": "Light positioned below the face, casting eerie upward shadows (horror style)",
    "Silhouette / Rim Light": "Subject mostly dark, strong backlight outlining the edges of the face/hair",
    "Golden Hour": "Warm, directional, soft sunlight associated with sunset/sunrise",
    "Firelight / Candlelight": "Warm, flickering, low-light ambient illumination, intimate mood",
    "Interrogation / Bare Bulb": "Top-down harsh light, gritty, realistic police-room style"
}

GROOM_DESC = {
    "Clean Shaven": "Smooth skin, perfectly groomed, no facial hair",
    "Light Stubble": "1-2 days of facial hair growth, faint shadow",
    "Medium Stubble": "3-4 days of growth, visible texture and grit",
    "Heavy Stubble": "5-7 days of dense facial hair growth, rugged look",
    "Short Beard": "Neatly trimmed, close to the face, professional",
    "Full Beard": "Thick, dense, well-kept full facial hair",
    "Long Beard": "Extended length, historic or aged look",
    "Unkempt / Dirty Beard": "Wild, untamed, survivor or historical styling",
    "Goatee": "Chin and mustache connection only",
    "Chevron Mustache": "Thick upper lip hair, retro/80s style",
    "Pencil Mustache": "Thin, refined and highly styled upper lip hair",
    "Patchy Beard": "Uneven growth, realistic imperfections and bald spots"
}

SFX_DESC = {
    "Sword Wound": "Clean, sharp blade laceration",
    "Glass Laceration": "Jagged cuts with micro-details",
    "Crush/Blunt Force Wound": "Swollen, uneven skin breakage",
    "3-Day Old Wound": "Partially scabbed, dark red/brown edges",
    "1-Week Old Scar": "Healing pinkish tissue, fresh scar",
    "1-Month Old Scar": "Settled scar tissue, slightly raised",
    "1-Year Old Keloid Scar": "Thick, raised, permanent keloid tissue",
    "5-Year Old Scar": "Faded, flat, pale scar integration",
    "Fresh Bruise (Immediate)": "Reddish/purple surface hematoma",
    "1-Day Old Bruise": "Deep purple and blue subdermal pooling",
    "3-Day Old Bruise": "Yellow and green edges, fading purple",
    "15-Day Fading Bruise": "Faint yellow/brown residual mark",
    "Acid Burn": "Melted, distorted skin texture",
    "1st Degree Burn": "Redness, inflamed epidermal layer",
    "2nd Degree Burn": "Blistering, severe dermal damage",
    "Katana Slash": "Deep, angled, highly precise slash wound"
}

ERA_DESC = {
    "Prehistoric / Stone Age": "Primitive, unkempt, prehistoric styling, weathered skin",
    "Ancient Rome / Greece": "Classical antiquity, togas, armor, traditional garments",
    "Pre-Islamic Middle East": "Ancient Arabian peninsula aesthetics, nomadic textures",
    "Medieval / Dark Ages": "Gritty, middle ages styling, chainmail, rustic materials",
    "Renaissance": "15th-16th century elegant styling, detailed fabrics",
    "Victorian Era (19th Century)": "19th century historical accuracy, Victorian/Qajar era",
    "1920s - Roaring Twenties": "1920s aesthetics, early modern styling, flapper/gangster",
    "1970s - Retro / Vintage": "1970s retro aesthetics, distinct color grading",
    "Contemporary / Present Day": "Modern day, current fashion and styling",
    "Cyberpunk / Distant Future": "Neon accents, synthetic materials, futuristic tech",
    "Post-Apocalyptic": "Wasteland survivor, scavenged gear, highly weathered"
}

NAT_DESC = {
    "Iranian/Persian": "Persian features, distinct bone structure",
    "Peninsular Arab (Saudi/Emirati)": "Peninsular Arab features, warm olive skin tones",
    "Levantine (Lebanese/Syrian)": "Eastern Mediterranean features",
    "Egyptian/North African": "North African features, warm skin tones",
    "Nordic/Scandinavian": "Fair skin, light features, structured jawline",
    "Mediterranean (Italian/Greek)": "Olive skin, Mediterranean facial structure",
    "Slavic/Eastern European": "Slavic facial structure, distinct cheekbones",
    "East Asian (Japanese/Korean)": "East Asian features, distinct eye shape",
    "South Asian (Indian/Pakistani)": "Desi features, rich brown skin tones",
    "Latin American": "Mestizo or Latin features, warm undertones"
}

CAM_DESC = {
    "85mm Lens (Standard Portrait)": "Standard portrait lens, minimal distortion, shallow depth of field",
    "100mm Macro (Extreme Detail)": "Extreme close-up, focusing on skin pores and SFX textures",
    "35mm Lens (Wider Context)": "Wider angle, empowering and dramatic perspective",
    "24mm Wide-Angle (Environmental)": "Wide view, incorporates background elements",
    "50mm Lens (Standard Human Eye)": "Human-eye perspective, neutral framing"
}

SIZE_LIST = [
    "4:5 (Standard Portrait)",
    "16:9 (Cinematic Widescreen)",
    "2.39:1 (Anamorphic Cinema)",
    "1:1 (Square)",
    "9:16 (Vertical Video)"
]

AGE_PROG_DESC = {
    "Stage 1: Subtle Aging": "Wait for final prompt from Master...",
    "Stage 2: Advanced Aging": "Wait for final prompt from Master..."
}

SFX_PROG_DESC = {
    "Stage 1: Fresh & Bleeding": "Wait for final prompt from Master...",
    "Stage 2: Healing & Bruised": "Wait for final prompt from Master..."
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
        "actor":"None", "gen":"", "age":"", "nat":"", "era":"", "h_col":"", 
        "h_tex":"", "sfx":"", "mat":"", "char":"", "groom":"", "cam":"", "light":"", "size":"",
        "age_prog":"", "sfx_prog":""
    }

def go_to(route): st.session_state.route = route; st.rerun()
def next_step(): st.session_state.step += 1; st.rerun()
def prev_step(): st.session_state.step -= 1; st.rerun()
def add_n(lst): return ["None"] + lst + ["Others"]

def smart_select(label, options, key, help_dict=None):
    opts = add_n(options)
    curr_val = st.session_state.draft.get(key, "")
    idx = 0
    if curr_val in opts: idx = opts.index(curr_val)
    elif curr_val and curr_val != "None": idx = len(opts) - 1
    
    if help_dict:
        c1, c2 = st.columns([11, 1])
        with c1:
            sel = st.selectbox(label, opts, index=idx, key=f"sel_{key}")
        with c2:
            with st.popover("❕"):
                help_html = f"""
                <div style="background-color: #000000 !important; margin: -1rem; padding: 1rem; min-height: 100px;">
                    <div style="color: #00f2ff; font-weight: 900; font-family: 'Cinzel', serif; margin-bottom: 10px; font-size: 0.9rem; border-bottom: 1px solid rgba(0,242,255,0.3); padding-bottom: 5px; text-transform: uppercase;">
                        EXCEL DICTIONARY: {label}
                    </div>
                    {"".join([f"<div style='color: #d0e0f0; font-family: Montserrat; font-size: 0.8rem; line-height: 1.8; margin-bottom: 4px;'><b style='color: #00f2ff;'>{k}:</b> {v}</div>" for k, v in help_dict.items()])}
                </div>
                """
                st.markdown(help_html, unsafe_allow_html=True)
    else:
        sel = st.selectbox(label, opts, index=idx, key=f"sel_{key}")
        
    if sel == "Others":
        custom = st.text_input(f"Type Custom {label}", value=curr_val if curr_val not in opts else "", key=f"txt_{key}")
        st.session_state.draft[key] = custom
    else:
        st.session_state.draft[key] = sel

def generate_prompt(draft):
    base_p = f"Professional cinematic portrait, beautifully framed composition, three-quarter profile angle, {draft['size']}, {draft['cam']}, {draft['light']}. "
    
    char_val = draft['char']
    char_desc = CONCEPTS.get(char_val, char_val)
    age_val = draft.get('age', 'Unknown Age')
    
    char_p = f"Subject: {draft['gen']}, {age_val}, {draft['nat']} from {draft['era']}. Concept: {char_desc}. "
    
    h_col_val = draft['h_col']
    h_desc = HAIR_COLORS.get(h_col_val, h_col_val)
    groom_p = f"Grooming: {draft['groom']}. Hair: {h_desc} ({draft['h_tex']}). "
    
    if draft['actor'] and draft['actor'] not in ["None", "No", ""]:
        base_p = f"Actor reference: {draft['actor']}. " + base_p

    age_prog_val = draft.get('age_prog', '')
    if age_prog_val and age_prog_val not in ["None", ""]:
        char_p += f"[APEX AGE PROGRESSION: {age_prog_val}] "

    sfx_p = ""
    if draft['sfx'] and draft['sfx'] not in ["None", ""]:
        sfx_p = f"[CINEMATIC MAKEUP TEST: Fake {draft['sfx']} prosthetic SFX applied using {draft['mat']}. "
        sfx_prog_val = draft.get('sfx_prog', '')
        if sfx_prog_val and sfx_prog_val not in ["None", ""]:
            sfx_p += f"APEX PROGRESSION STAGE: {sfx_prog_val}. "
        sfx_p += "Note: This is a safe simulation, artificial makeup.] "

    typo_p = f"Typography overlay: clearly written text '{age_val}' at the bottom margin of the image. " if age_val and age_val != "None" else ""
        
    return base_p + char_p + groom_p + sfx_p + typo_p + "8k resolution, raw photo, highly detailed."

ADMIN_USER = "sep"
ADMIN_PASS = "1386sy"

# ==========================================
# 4. موتور استایل (CSS Engine)
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

    /* 🔴 کد جادویی نابود کردن کادر دکمه لوگو */
    div.element-container:has(.logo-marker) + div.element-container button {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        min-height: 0 !important;
        height: auto !important;
        display: flex !important;
        justify-content: flex-start !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button:hover,
    div.element-container:has(.logo-marker) + div.element-container button:active,
    div.element-container:has(.logo-marker) + div.element-container button:focus {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button p {
        color: #00f2ff !important;
        font-family: 'Cinzel', serif !important;
        font-size: 1.5rem !important;
        font-weight: 900 !important;
        margin: 0 !important;
        padding: 0 !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button:hover p {
        color: #ffffff !important;
        text-shadow: 0 0 15px #00f2ff !important;
        transform: scale(1.02) !important;
    }
    /* پایان کدهای لوگو */

    .title-main { font-family: 'Cinzel'; color: #ffffff !important; font-size: 2.5rem; font-weight: 800; letter-spacing: 10px; margin: 0; text-shadow: 0 0 15px rgba(0, 242, 255, 0.5); }
    .subtitle { color: #00f2ff; font-family: 'Montserrat'; font-size: 0.8rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 30px;}

    label, .stMarkdown p { color: #00e5ff !important; font-family: 'Montserrat' !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.75rem !important; }

    div[data-baseweb="input"] > div { background-color: rgba(0, 20, 40, 0.9) !important; border: 1px solid rgba(0, 242, 255, 0.4) !important; border-radius: 10px !important; }
    div[data-baseweb="input"] input, div[data-baseweb="select"] { color: #ffffff !important; font-weight: bold !important; }

    .stButton > button {
        border: none !important; border-radius: 8px !important; font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; background-color: #00f2ff !important; color: #000000 !important;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.3);
    }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.02); box-shadow: 0 0 20px #00f2ff;}

    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 25px; backdrop-filter: blur(10px); margin-bottom: 20px; }
    
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 30px; color: #4a5d73; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 900; }
    .step-active { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }

    div[data-testid="stExpander"] { background: rgba(10, 25, 47, 0.6) !important; border: 1px solid rgba(0, 242, 255, 0.2) !important; border-radius: 12px !important; backdrop-filter: blur(10px); margin-bottom: 15px; transition: all 0.3s ease; }
    div[data-testid="stExpander"]:hover { border-color: rgba(0, 242, 255, 0.6) !important; box-shadow: 0 5px 20px rgba(0, 242, 255, 0.15); }
    div[data-testid="stExpander"] summary { padding: 15px !important; }
    div[data-testid="stExpander"] summary p { color: #ffffff !important; font-family: 'Cinzel', serif !important; font-size: 1.1rem !important; letter-spacing: 2px; font-weight: bold !important; }
    
    .stCodeBlock { background-color: #02060c !important; border-left: 4px solid #ff00aa !important; border-radius: 8px !important; box-shadow: inset 0 0 10px rgba(0,0,0,0.8); }
    .stCodeBlock code { color: #00e5ff !important; font-family: 'Courier New', Courier, monospace !important; line-height: 1.6 !important; font-size: 0.95rem !important; }
    
    div[data-testid="stPopover"] { padding-top: 26px; } 
    div[data-testid="stPopover"] > button {
        background: transparent !important; border: 1px solid #00f2ff !important; border-radius: 50% !important; width: 34px !important; height: 34px !important;
        color: #00f2ff !important; font-size: 1.1rem !important; font-weight: 900 !important; transition: 0.3s !important; display: flex; align-items: center; justify-content: center;
    }
    div[data-testid="stPopover"] > button:hover { background: rgba(0, 242, 255, 0.1) !important; color: #fff !important; box-shadow: 0 0 15px #00f2ff !important; }
    div[data-testid="stPopoverBody"], div[data-baseweb="popover"], div[data-baseweb="popover"] > div, [data-testid="stPopoverBody"] > div { 
        background-color: #000000 !important; background: #000000 !important; border-color: #00f2ff !important;
    }

    [data-testid="stImage"] img {
        border-radius: 12px !important;
        border: 2px solid #00f2ff !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.7), 0 0 35px rgba(0, 85, 255, 0.6) !important;
        transition: all 0.3s ease-in-out !important;
    }
    [data-testid="stImage"] img:hover {
        box-shadow: 0 0 25px rgba(0, 242, 255, 1), 0 0 50px rgba(0, 85, 255, 0.9) !important;
        transform: scale(1.02) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# ROUTE 1: ENTRY FLOW (LOGIN ONLY)
# ==========================================
if st.session_state.route == 'login':
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=280)
    with c2:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px; text-shadow: 0 0 15px #00f2ff;'>RESTRICTED ACCESS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#7b8ea8; font-family:Montserrat; font-size:0.8rem; margin-bottom:20px;'>Authorized Personnel Only. Please login to access UONA STUDIO.</p>", unsafe_allow_html=True)
        
        u_name = st.text_input("USERNAME", placeholder="Enter your credentials...")
        u_pass = st.text_input("PASSWORD", type="password", placeholder="Enter your password...")
        
        users = load_json(DB_FILE, {})
        
        if st.button("AUTHENTICATE", use_container_width=True):
            if u_name == ADMIN_USER and u_pass == ADMIN_PASS:
                st.session_state.auth = True
                st.session_state.user = u_name
                st.session_state.is_admin = True
                st.session_state.plan = "MASTER APEX"
                go_to('admin_panel')
            elif u_name in users:
                user_data = users[u_name]
                if isinstance(user_data, str):
                    db_pass = user_data
                    db_plan = "UONA Core"
                else:
                    db_pass = user_data.get("pass", "")
                    db_plan = user_data.get("plan", "UONA Core")
                
                if db_pass == u_pass:
                    st.session_state.auth = True
                    st.session_state.user = u_name
                    st.session_state.is_admin = False
                    st.session_state.plan = db_plan
                    go_to('dashboard')
                else:
                    st.error("ACCESS DENIED: Invalid Password.")
            else:
                st.error("ACCESS DENIED: Unregistered Account.")
    st.stop()

# ==========================================
# SHARED HEADER (WITH INVISIBLE BUTTON)
# ==========================================
if st.session_state.route != 'login':
    badge_color = "#ffaa00" if "Apex" in st.session_state.plan or "MASTER" in st.session_state.plan else "#00f2ff"
    
    c_head1, c_head2 = st.columns([1, 3])
    
    with c_head1:
        # مارکر نامرئی که به CSS می‌گوید دکمه بعدی را کاملا به متن تبدیل کند
        st.markdown('<span class="logo-marker"></span>', unsafe_allow_html=True)
        if st.button("UONA STUDIO", key="top_home_btn"):
            st.session_state.step = 1
            go_to('dashboard')
            
    with c_head2:
        st.markdown(f"""
            <div style="display: flex; justify-content: flex-end; align-items: center; height: 100%; padding-top: 10px;">
                <span style="color:{badge_color}; font-family:Cinzel; font-weight:bold; font-size:0.7rem; border:1px solid {badge_color}; padding:3px 8px; border-radius:4px; margin-right:15px; box-shadow: 0 0 8px rgba(0,0,0,0.5);">💎 {st.session_state.plan.upper()}</span>
                <span style="color:#ff00aa; font-weight:bold; font-family:Montserrat; font-size:0.7rem; margin-right:15px;">{'[MASTER ADMIN]' if st.session_state.is_admin else ''}</span>
                <span style="color:#fff; font-family:Montserrat; font-size:0.8rem;">USER: {st.session_state.user.upper()}</span>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<hr style='border-color: rgba(0,242,255,0.2); margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)

# ==========================================
# ROUTE: ADMIN PANEL
# ==========================================
if st.session_state.route == 'admin_panel':
    if not st.session_state.is_admin: go_to('dashboard')
    
    st.markdown("<h2 class='title-main' style='color:#ff00aa!important; text-shadow:0 0 15px #ff00aa;'>MASTER CONTROL PANEL</h2>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Manage Client Access & Subscriptions</div><br>", unsafe_allow_html=True)
    
    users = load_json(DB_FILE, {})
    
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>➕ Register New Client</h4>", unsafe_allow_html=True)
        new_u = st.text_input("New Client Username")
        new_p = st.text_input("New Client Password")
        new_plan = st.selectbox("Assign Subscription Tier", ["UONA Core", "UONA Apex"])
        
        if st.button("CREATE CLIENT ACCOUNT", use_container_width=True):
            if new_u and new_p:
                if new_u == ADMIN_USER:
                    st.error("Cannot use admin username.")
                else:
                    users[new_u] = {"pass": new_p, "plan": new_plan}
                    save_json(DB_FILE, users)
                    st.success(f"Client '{new_u}' successfully registered on {new_plan}.")
                    st.rerun()
            else:
                st.warning("Fill all fields.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>👥 Active Client Subscriptions</h4>", unsafe_allow_html=True)
        if not users:
            st.info("No active clients yet.")
        else:
            for usr, data in users.items():
                if isinstance(data, str): 
                    plan_val, pwd_val = "UONA Core", data
                else: 
                    plan_val, pwd_val = data.get("plan", "UONA Core"), data.get("pass", "")
                    
                col_name, col_plan, col_pass, col_btn = st.columns([2, 2, 2, 1])
                col_name.markdown(f"<span style='color:white; font-family:Montserrat; font-weight:bold;'>👤 {usr}</span>", unsafe_allow_html=True)
                col_plan.markdown(f"<span style='color:#00f2ff; font-family:Cinzel; font-size:0.8rem;'>{plan_val}</span>", unsafe_allow_html=True)
                col_pass.markdown(f"<span style='color:#888; font-family:monospace;'>pwd: {pwd_val}</span>", unsafe_allow_html=True)
                if col_btn.button("REVOKE", key=f"del_{usr}"):
                    del users[usr]
                    save_json(DB_FILE, users)
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 2: DASHBOARD FLOW
# ==========================================
elif st.session_state.route == 'dashboard':
    
    found_bg = find_bg_file()
    if found_bg:
        add_bg_from_local(found_bg)
    else:
        st.error("⚠️ هشدار سیستم: فایل بک‌گراند پیدا نشد.")
    
    st.markdown("<h2 style='color:#fff; font-family:Cinzel; text-align:center;'>CONTROL CENTER</h2><div class='subtitle' style='text-align:center;'>Select a module to begin</div>", unsafe_allow_html=True)
    
    if st.session_state.is_admin:
        if st.button("⚙️ RETURN TO ADMIN PANEL"): go_to('admin_panel')
        st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>🎬</h1><h3 class="module-title">NEW CHARACTER</h3><p style="color:#888; font-size:0.8rem;">Start Multi-Step Builder</p></div>', unsafe_allow_html=True)
        if st.button("START PROJECT", key="b1", use_container_width=True): st.session_state.step = 1; go_to('builder')
    with c2:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>📂</h1><h3 class="module-title" style="color:#777!important; text-shadow:none!important;">LIBRARY</h3><p style="color:#888; font-size:0.8rem;">Saved Looks & Presets</p></div>', unsafe_allow_html=True)
        if st.button("OPEN LIBRARY", key="b2", use_container_width=True): go_to('library')
    with c3:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>⚙️</h1><h3 class="module-title" style="color:#777!important; text-shadow:none!important;">SETTINGS</h3><p style="color:#888; font-size:0.8rem;">System Preferences</p></div>', unsafe_allow_html=True)
        if st.button("OPEN SETTINGS", key="b3", use_container_width=True): go_to('settings')

# ==========================================
# ROUTE: LIBRARY & SETTINGS
# ==========================================
elif st.session_state.route == 'library':
    st.markdown("<h2 class='title-main' style='text-align:center;'>PROJECT LIBRARY</h2>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle' style='text-align:center;'>Your Saved Cinematic Architectures</div><br>", unsafe_allow_html=True)
        
    projects = load_json(PROJ_FILE, [])
    my_projs = [p for p in projects if p.get("user") == st.session_state.user]
    
    if not my_projs:
        st.info("No projects saved yet.")
    else:
        for p in my_projs:
            with st.expander(f"📁 PROJECT LOG | {p['date']}"):
                st.markdown("<p style='color:#7b8ea8; font-size:0.75rem; letter-spacing:2px;'>GENERATED MASTER PROMPT:</p>", unsafe_allow_html=True)
                st.code(p['prompt'], language="markdown")

    st.markdown("<hr style='border-color: rgba(0,242,255,0.2);'>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='color:#00f2ff; font-family:Cinzel; margin-bottom:15px;'>REFERENCE GALLERY</h4>", unsafe_allow_html=True)
    l_c1, l_c2, l_c3, l_c4 = st.columns(4)
    with l_c1:
        if os.path.exists("desert_warn.jpg"): st.image("desert_warn.jpg", caption="Desert Warn")
    with l_c2:
        if os.path.exists("royal_clean.jpg"): st.image("royal_clean.jpg", caption="Royal Clean")
    with l_c3:
        if os.path.exists("dirty_combat.jpg"): st.image("dirty_combat.jpg", caption="Dirty Combat")
    with l_c4:
        if os.path.exists("urban_rebel.jpg"): st.image("urban_rebel.jpg", caption="Urban Rebel")

elif st.session_state.route == 'settings':
    st.markdown("<h2 class='title-main'>SYSTEM SETTINGS</h2>", unsafe_allow_html=True)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.selectbox("Default AI Engine", ["Midjourney V6", "Gemini Pro Vision", "Stable Diffusion XL"])
    st.selectbox("Theme Mode", ["Dark Cinematic", "Light Mode (Not Recommended)"])
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 3: CHARACTER BUILDER (MULTI-STEP)
# ==========================================
elif st.session_state.route == 'builder':
    st.markdown(f"""
        <div class="step-indicator">
            <span class="{'step-active' if st.session_state.step==1 else ''}">1. IDENTITY</span> ➔
            <span class="{'step-active' if st.session_state.step==2 else ''}">2. PHYSICAL</span> ➔
            <span class="{'step-active' if st.session_state.step==3 else ''}">3. GROOM/SFX</span> ➔
            <span class="{'step-active' if st.session_state.step==4 else ''}">4. TECHNICAL</span> ➔
            <span class="{'step-active' if st.session_state.step==5 else ''}">5. REVIEW</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    d = st.session_state.draft

    if st.session_state.step == 1:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 1: Core Identity</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            opts_act = ["None", "Yes", "No"]
            idx_act = opts_act.index(d['actor']) if d['actor'] in opts_act else 0
            d['actor'] = st.selectbox("Actor Reference", opts_act, index=idx_act)
            
            smart_select("Age Range", ["Elderly", "Middle-aged", "Young Adult", "Teenager", "Child", "Toddler"], 'age')
            
            if st.session_state.plan in ["UONA Apex", "MASTER APEX"]:
                st.markdown("<hr style='border-color: rgba(255, 170, 0, 0.3); margin: 10px 0;'>", unsafe_allow_html=True)
                smart_select("Age Progression Arc", list(AGE_PROG_DESC.keys()), 'age_prog', help_dict=AGE_PROG_DESC)

        with c2:
            smart_select("Gender", ["Male", "Female", "Androgynous", "Non-binary"], 'gen')
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col3.button("NEXT ➔"): next_step()

    elif st.session_state.step == 2:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 2: Physical Attributes</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            smart_select("Nationality", list(NAT_DESC.keys()), 'nat', help_dict=NAT_DESC)
            smart_select("Hair Color", list(HAIR_COLORS.keys()), 'h_col', help_dict=HAIR_COLORS)
        with c2:
            smart_select("Era / Period", list(ERA_DESC.keys()), 'era', help_dict=ERA_DESC)
            smart_select("Hair Texture", ["Straight (Silky)", "Wavy (S-shape)", "Curly (Ringlets)", "Afro (Coils)", "Matted (Weathered/Dirty)", "Bald / Shaved Head", "Thinning / Balding"], 'h_tex')
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("NEXT ➔"): next_step()

    elif st.session_state.step == 3:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 3: Grooming & SFX Trauma</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            smart_select("Grooming Style", list(GROOM_DESC.keys()), 'groom', help_dict=GROOM_DESC)
            smart_select("Material Finish", ["Silicone Prosthetic", "Matte Sealer", "Alcohol Palette", "Translucent Skin", "Gelatin Prosthetic", "Foam Latex", "Sweat/Grease FX"], 'mat')
        with c2:
            smart_select("Trauma / SFX", list(SFX_DESC.keys()), 'sfx', help_dict=SFX_DESC)
            
            if st.session_state.plan in ["UONA Apex", "MASTER APEX"]:
                st.markdown("<hr style='border-color: rgba(255, 170, 0, 0.3); margin: 10px 0;'>", unsafe_allow_html=True)
                smart_select("SFX Progression Arc", list(SFX_PROG_DESC.keys()), 'sfx_prog', help_dict=SFX_PROG_DESC)
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("NEXT ➔"): next_step()

    elif st.session_state.step == 4:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 4: Technical Specs</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            smart_select("Character Concept", list(CONCEPTS.keys()), 'char', help_dict=CONCEPTS)
            smart_select("Lighting Style", list(LIGHT_DESC.keys()), 'light', help_dict=LIGHT_DESC)
        with c2:
            smart_select("Camera & Lens", list(CAM_DESC.keys()), 'cam', help_dict=CAM_DESC)
            smart_select("Frame Size", SIZE_LIST, 'size')
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("REVIEW ➔"): next_step()

    elif st.session_state.step == 5:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 5: Final Review</h3>", unsafe_allow_html=True)
        
        preview_p = generate_prompt(d)
        st.info(preview_p)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1.5, 3, 2])
        if col1.button("⬅ EDIT (BACK)"): prev_step()
        if col3.button("🚀 PROCEED TO SIMULATION"): go_to('simulation')

        st.markdown("<br>", unsafe_allow_html=True)
        _, rev_c1, rev_c2, _ = st.columns([1, 2, 2, 1])
        with rev_c1:
            if os.path.exists("portrait_clean.PNG"): st.image("portrait_clean.PNG", caption="Visual Reference 1", use_container_width=True)
        with rev_c2:
            if os.path.exists("portrait_clean_2.jpg"): st.image("portrait_clean_2.jpg", caption="Visual Reference 2", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 4 & 5: SIMULATION AND ENGINE
# ==========================================
elif st.session_state.route == 'simulation':
    st.markdown("<h2 class='title-main'>VISUAL SIMULATION</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown('<div style="background:#0a192f; height:200px; border-radius:15px; border:1px dashed #00f2ff; display:flex; align-items:center; justify-content:center; flex-direction:column; margin-bottom:20px;"><h1 style="color:#00f2ff; opacity:0.5;">👁️</h1><p style="color:#00f2ff; opacity:0.7; font-family:Montserrat;">LIVE PREVIEW FEED</p></div>', unsafe_allow_html=True)
        
        sim_c1, sim_c2 = st.columns(2)
        with sim_c1:
            if os.path.exists("desert.jpg"): st.image("desert.jpg", caption="Desert Environment Test")
            if os.path.exists("night_neon.jpg"): st.image("night_neon.jpg", caption="Night Neon Test")
        with sim_c2:
            if os.path.exists("studio_portrait.jpg"): st.image("studio_portrait.jpg", caption="Studio Lighting Test")
            if os.path.exists("humidity_tester.jpg"): st.image("humidity_tester.jpg", caption="SFX Humidity Test")
            
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.selectbox("Render Engine Test", ["Preview Mode (Fast)", "High Fidelity"])
        if st.button("⬅ BACK TO BUILDER", use_container_width=True): go_to('builder')
        if st.button("⚡ GENERATE PROMPT", use_container_width=True): go_to('prompt_engine')
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.route == 'prompt_engine':
    st.markdown("<h2 class='title-main'>PROMPT ENGINE</h2>", unsafe_allow_html=True)
    
    final_p = generate_prompt(st.session_state.draft)

    c1, c2 = st.columns([2.5, 1])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.text_area("MASTER PROMPT (EDITABLE)", value=final_p, height=200)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        if st.button("💾 SAVE TO LIBRARY", use_container_width=True):
            projects = load_json(PROJ_FILE, [])
            projects.insert(0, {"user": st.session_state.user, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "prompt": final_p})
            save_json(PROJ_FILE, projects)
            st.success("Saved to Library!")
        if st.button("⬅ SIMULATION", use_container_width=True): go_to('simulation')
        st.markdown('</div>', unsafe_allow_html=True)
