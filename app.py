import streamlit as st
from datetime import datetime
import os
import json

# ==========================================
# 1. تنظیمات پلتفرم و دیتابیس (تغییر آیکون تب مرورگر)
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

# ==========================================
# 2. دیتابیس هوشمند اکسل (توضیحات پرامپت انگلیسی)
# ==========================================
HAIR_COLORS = {
    "Jet Black": "Jet black / Natural black",
    "Espresso Brown": "Deep espresso brown / Dark chocolate",
    "Ash Blonde": "Ash blonde (Cool tone)",
    "Salt & Pepper": "Salt and pepper, varying grey hair percentage",
    "Silver / Grey": "Silver / Grey hair",
    "White": "Pure white hair"
}

CONCEPTS = {
    "Heroic Warrior": "Strong jawline, confident gaze, slight battle wear",
    "Sinister Villain": "Harsh shadows, menacing expression, sharp features",
    "Scholar": "Refined appearance, focused eyes, thoughtful pose",
    "Royal": "Elegant posture, pristine skin, luxury textures",
    "Peasant / Commoner": "Naturalistic, everyday lighting, unpolished look",
    "Cybernetic Enhanced": "Sci-fi elements, subtle synthetic integration",
    "Undead / Zombie": "Pale skin, dark circles, hollowed features"
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
    "Stone Age": "Primitive, unkempt, prehistoric styling, weathered skin",
    "Before Christ (BC)": "Ancient antiquity, classical era styling",
    "Pre-Islamic Era": "Ancient Arabian peninsula aesthetics, nomadic textures",
    "200 Years Ago": "19th century historical accuracy, Victorian/Qajar era",
    "150 Years Ago": "Late 19th century, industrial revolution grit",
    "100 Years Ago": "1920s aesthetics, early modern styling",
    "50 Years Ago": "1970s retro aesthetics, distinct color grading",
    "Contemporary": "Modern day, current fashion and styling",
    "Cyberpunk / Future": "Neon accents, synthetic materials, futuristic"
}

NAT_DESC = {
    "Iranian": "Persian features, distinct bone structure",
    "Saudi (Peninsular Arab)": "Peninsular Arab features, warm olive skin tones",
    "Levantine": "Eastern Mediterranean features",
    "North African": "Amazigh or Arab-African blend",
    "European (Caucasian)": "Classic Caucasian features, varying pale to light skin",
    "African (Sub-Saharan)": "Deep rich skin tones, prominent structural features",
    "East Asian": "East Asian features, distinct facial structure",
    "South Asian": "Desi features, rich brown skin tones",
    "Latin American": "Mestizo or Latin features, warm undertones"
}

GROOM_DESC = {
    "Clean Shaven": "Smooth skin, perfectly groomed",
    "Light Stubble": "1-2 days of facial hair growth",
    "Heavy Stubble": "3-5 days of dense facial hair growth",
    "Full Beard": "Well-kept, dense full facial hair",
    "Long Beard (Dirty Look)": "Unkempt, wild, historically accurate long beard",
    "Goatee": "Chin and mustache connection",
    "Moustache Only": "Isolated upper lip hair",
    "Patchy Beard": "Uneven growth, realistic imperfections"
}

CAM_DESC = {
    "85mm Eye-Level (Portrait)": "Standard portrait lens, minimal distortion, shallow depth of field",
    "100mm Macro (Extreme Detail)": "Extreme close-up, focusing on skin pores and SFX textures",
    "35mm Low-Angle (Hero Shot)": "Wider angle looking up, empowering and dramatic",
    "50mm Standard": "Human-eye perspective, neutral framing",
    "24mm Wide-Angle (Environmental)": "Wide view, incorporates background elements"
}

LIGHT_DESC = {
    "Rembrandt": "Classic portrait lighting, triangle of light on the cheek",
    "Teal & Orange": "Hollywood blockbuster color grading",
    "Neon / Cyberpunk": "Vibrant, high-contrast artificial lighting",
    "Softbox / Studio": "Even, flattering, commercial-grade lighting",
    "Chiaroscuro (High Contrast)": "Dramatic interplay of deep shadows and bright highlights",
    "Cinematic Backlight": "Subject separated from background via rim light",
    "Harsh Midday Sun": "Hard shadows, realistic outdoor daytime",
    "Overcast / Diffused": "Soft, shadowless natural lighting"
}

# ==========================================
# 3. مدیریت وضعیت (State Machine) و توابع
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'route' not in st.session_state: st.session_state.route = 'login'
if 'step' not in st.session_state: st.session_state.step = 1

if 'draft' not in st.session_state: 
    st.session_state.draft = {
        "actor":"None", "gen":"", "age":"", "nat":"", "era":"", "h_col":"", 
        "h_tex":"", "sfx":"", "mat":"", "char":"", "groom":"", "cam":"", "light":"", "size":""
    }

def go_to(route): st.session_state.route = route; st.rerun()
def next_step(): st.session_state.step += 1; st.rerun()
def prev_step(): st.session_state.step -= 1; st.rerun()
def add_n(lst): return ["None"] + lst + ["Others"]

# تابع فرم‌ساز اختصاصی با Tooltip تعاملی و شیشه‌ای
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
                st.markdown(f"<div class='tooltip-title'>EXCEL DICTIONARY: {label.upper()}</div>", unsafe_allow_html=True)
                help_html = "".join([f"<div class='tooltip-text'><b style='color:#00f2ff;'>{k}:</b> {v}</div>" for k, v in help_dict.items()])
                st.markdown(help_html, unsafe_allow_html=True)
    else:
        sel = st.selectbox(label, opts, index=idx, key=f"sel_{key}")
        
    if sel == "Others":
        custom = st.text_input(f"Type Custom {label}", value=curr_val if curr_val not in opts else "", key=f"txt_{key}")
        st.session_state.draft[key] = custom
    else:
        st.session_state.draft[key] = sel

# --- تابع تولید پرامپت استاتیک و هوشمند (جایگذاری فرمول‌های اکسل) ---
def generate_prompt(draft):
    base_p = f"Professional cinematic portrait, {draft['size']}, {draft['cam']}, {draft['light']}. "
    
    char_val = draft['char']
    char_desc = CONCEPTS.get(char_val, char_val)
    char_p = f"Subject: {draft['gen']}, {draft['age']}, {draft['nat']} from {draft['era']}. Concept: {char_desc}. "
        
    h_col_val = draft['h_col']
    h_desc = HAIR_COLORS.get(h_col_val, h_col_val)
    groom_p = f"Grooming: {draft['groom']}. Hair: {h_desc} ({draft['h_tex']}). "
    
    if draft['sfx'] and draft['sfx'] not in ["None", ""]:
        sfx_p = f"[CINEMATIC MAKEUP TEST: Fake {draft['sfx']} prosthetic SFX applied using {draft['mat']}. Note: This is a safe simulation, artificial makeup.] "
    else:
        sfx_p = ""
        
    return base_p + char_p + groom_p + sfx_p + "8k resolution, raw photo, highly detailed."

# 📌 اطلاعات ورود پنل ادمین
ADMIN_USER = "admin"
ADMIN_PASS = "1234"

# ==========================================
# 4. موتور استایل (CSS Engine)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh; overflow-x: hidden;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    .title-main { font-family: 'Cinzel'; color: #ffffff !important; font-size: 2.5rem; font-weight: 800; letter-spacing: 10px; margin: 0; text-shadow: 0 0 15px rgba(0, 242, 255, 0.5); }
    .subtitle { color: #00f2ff; font-family: 'Montserrat'; font-size: 0.8rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 30px;}

    label, .stMarkdown p { color: #00e5ff !important; font-family: 'Montserrat' !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.75rem !important; }

    div[data-baseweb="input"] > div { background-color: rgba(0, 20, 40, 0.9) !important; border: 1px solid rgba(0, 242, 255, 0.4) !important; border-radius: 10px !important; }
    div[data-baseweb="input"] input { color: #ffffff !important; font-weight: bold !important; }

    .stButton > button {
        border: none !important; border-radius: 8px !important; font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; background-color: #00f2ff !important; color: #000000 !important;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.3);
    }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.02); box-shadow: 0 0 20px #00f2ff;}

    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 25px; backdrop-filter: blur(10px); margin-bottom: 20px; }
    
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 30px; color: #4a5d73; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 900; }
    .step-active { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }

    .nav-top { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(0, 242, 255, 0.2); padding-bottom: 10px; margin-bottom: 20px; }
    .module-title { font-family: 'Cinzel'; color: #008b8b !important; text-shadow: 0 0 12px rgba(255, 215, 0, 0.8) !important; letter-spacing: 3px; font-weight: 900; }

    div[data-testid="stExpander"] { background: rgba(10, 25, 47, 0.6) !important; border: 1px solid rgba(0, 242, 255, 0.2) !important; border-radius: 12px !important; backdrop-filter: blur(10px); margin-bottom: 15px; transition: all 0.3s ease; }
    div[data-testid="stExpander"]:hover { border-color: rgba(0, 242, 255, 0.6) !important; box-shadow: 0 5px 20px rgba(0, 242, 255, 0.15); }
    div[data-testid="stExpander"] summary { padding: 15px !important; }
    div[data-testid="stExpander"] summary p { color: #ffffff !important; font-family: 'Cinzel', serif !important; font-size: 1.1rem !important; letter-spacing: 2px; font-weight: bold !important; }
    
    .stCodeBlock { background-color: #02060c !important; border-left: 4px solid #ff00aa !important; border-radius: 8px !important; box-shadow: inset 0 0 10px rgba(0,0,0,0.8); }
    .stCodeBlock code { color: #00e5ff !important; font-family: 'Courier New', Courier, monospace !important; line-height: 1.6 !important; font-size: 0.95rem !important; }
    
    /* 🔴 استایل‌های اختصاصی Tooltip تعاملی با بک‌گراند مشکی */
    div[data-testid="stPopover"] { padding-top: 26px; } 
    div[data-testid="stPopover"] > button {
        background: transparent !important; border: 1px solid #00f2ff !important;
        border-radius: 50% !important; width: 34px !important; height: 34px !important;
        color: #00f2ff !important; font-size: 1.1rem !important; font-weight: 900 !important;
        transition: 0.3s !important; display: flex; align-items: center; justify-content: center;
    }
    div[data-testid="stPopover"] > button:hover { background: rgba(0, 242, 255, 0.1) !important; color: #fff !important; box-shadow: 0 0 15px #00f2ff !important; }
    
    /* تغییر رنگ پس‌زمینه به مشکی خالص */
    div[data-testid="stPopoverBody"] { 
        background: #000000 !important; 
        border: 1px solid #00f2ff !important; 
        border-radius: 12px !important; 
        box-shadow: 0 10px 30px rgba(0,242,255,0.4) !important; 
        padding: 15px; width: 350px !important;
    }
    
    .tooltip-title { color: #00f2ff; font-weight: 900; font-family: 'Cinzel'; margin-bottom: 10px; font-size: 0.9rem; border-bottom: 1px solid rgba(0,242,255,0.3); padding-bottom: 5px;}
    .tooltip-text { color: #d0e0f0; font-family: 'Montserrat'; font-size: 0.8rem; line-height: 1.8; margin-bottom: 4px;}
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
                go_to('admin_panel')
            elif u_name in users and users[u_name] == u_pass:
                st.session_state.auth = True
                st.session_state.user = u_name
                st.session_state.is_admin = False
                go_to('dashboard')
            else:
                st.error("ACCESS DENIED: Invalid Credentials or Unregistered Account.")
    st.stop()

# ==========================================
# SHARED HEADER
# ==========================================
if st.session_state.route != 'login':
    st.markdown(f"""
        <div class="nav-top">
            <div><span style="color:#00f2ff; font-family:Cinzel; font-size:1.5rem; font-weight:900;">UONA STUDIO</span></div>
            <div>
                <span style="color:#ff00aa; font-weight:bold; font-family:Montserrat; font-size:0.7rem; margin-right:15px;">{'[MASTER ADMIN]' if st.session_state.is_admin else ''}</span>
                <span style="color:#fff; font-family:Montserrat; font-size:0.8rem;">USER: {st.session_state.user.upper()}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# ROUTE: ADMIN PANEL
# ==========================================
if st.session_state.route == 'admin_panel':
    if not st.session_state.is_admin: go_to('dashboard')
    
    st.markdown("<h2 class='title-main' style='color:#ff00aa!important; text-shadow:0 0 15px #ff00aa;'>MASTER CONTROL PANEL</h2>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Manage Client Access & Subscriptions</div><br>", unsafe_allow_html=True)
    
    if st.button("⬅ ENTER MAIN STUDIO (APP)"): go_to('dashboard')
    
    users = load_json(DB_FILE, {})
    
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>➕ Register New Client</h4>", unsafe_allow_html=True)
        new_u = st.text_input("New Client Username")
        new_p = st.text_input("New Client Password")
        if st.button("CREATE CLIENT ACCOUNT", use_container_width=True):
            if new_u and new_p:
                if new_u == ADMIN_USER:
                    st.error("Cannot use admin username.")
                else:
                    users[new_u] = new_p
                    save_json(DB_FILE, users)
                    st.success(f"Client '{new_u}' successfully registered.")
                    st.rerun()
            else:
                st.warning("Fill both fields.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>👥 Active Client Subscriptions</h4>", unsafe_allow_html=True)
        if not users:
            st.info("No active clients yet.")
        else:
            for usr in list(users.keys()):
                col_name, col_pass, col_btn = st.columns([2, 2, 1])
                col_name.markdown(f"<span style='color:white; font-family:Montserrat; font-weight:bold;'>👤 {usr}</span>", unsafe_allow_html=True)
                col_pass.markdown(f"<span style='color:#888; font-family:monospace;'>pwd: {users[usr]}</span>", unsafe_allow_html=True)
                if col_btn.button("REVOKE", key=f"del_{usr}"):
                    del users[usr]
                    save_json(DB_FILE, users)
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 2: DASHBOARD FLOW
# ==========================================
elif st.session_state.route == 'dashboard':
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
    
    c_btn, _ = st.columns([1, 4])
    with c_btn:
        if st.button("⬅ BACK TO DASHBOARD", use_container_width=True): go_to('dashboard')
    st.markdown("<hr style='border-color: rgba(0,242,255,0.2);'>", unsafe_allow_html=True)
    
    projects = load_json(PROJ_FILE, [])
    my_projs = [p for p in projects if p.get("user") == st.session_state.user]
    
    if not my_projs:
        st.info("No projects saved yet.")
    else:
        for p in my_projs:
            with st.expander(f"📁 PROJECT LOG | {p['date']}"):
                st.markdown("<p style='color:#7b8ea8; font-size:0.75rem; letter-spacing:2px;'>GENERATED MASTER PROMPT:</p>", unsafe_allow_html=True)
                st.code(p['prompt'], language="markdown")

elif st.session_state.route == 'settings':
    st.markdown("<h2 class='title-main'>SYSTEM SETTINGS</h2>", unsafe_allow_html=True)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.selectbox("Default AI Engine", ["Midjourney V6", "Gemini Pro Vision", "Stable Diffusion XL"])
    st.selectbox("Theme Mode", ["Dark Cinematic", "Light Mode (Not Recommended)"])
    if st.button("⬅ BACK TO DASHBOARD"): go_to('dashboard')
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
        with c2:
            smart_select("Gender", ["Male", "Female", "Androgynous", "Non-binary"], 'gen')
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("EXIT"): go_to('dashboard')
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
            smart_select("Frame Size", ["4:5", "16:9", "2.39:1", "1:1"], 'size')
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("REVIEW ➔"): next_step()

    elif st.session_state.step == 5:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 5: Final Review</h3>", unsafe_allow_html=True)
        
        preview_p = generate_prompt(d)
        st.info(preview_p)
        
        col1, col2, col3 = st.columns([1.5, 3, 2])
        if col1.button("⬅ EDIT (BACK)"): prev_step()
        if col3.button("🚀 PROCEED TO SIMULATION"): go_to('simulation')

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 4 & 5: SIMULATION AND ENGINE
# ==========================================
elif st.session_state.route == 'simulation':
    st.markdown("<h2 class='title-main'>VISUAL SIMULATION</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown('<div style="background:#0a192f; height:350px; border-radius:15px; border:1px dashed #00f2ff; display:flex; align-items:center; justify-content:center; flex-direction:column;"><h1 style="color:#00f2ff; opacity:0.5;">👁️</h1><p style="color:#00f2ff; opacity:0.7; font-family:Montserrat;">LIVE PREVIEW FEED</p></div>', unsafe_allow_html=True)
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
        if st.button("🏠 DASHBOARD", use_container_width=True): go_to('dashboard')
        st.markdown('</div>', unsafe_allow_html=True)
