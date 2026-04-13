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

ADMIN_USER = "sep"
ADMIN_PASS = "1386sy"

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
# 2. دیتابیس مگا پرامپت (کامل)
# ==========================================

GENDER_LIST = ["Masculine / Male", "Feminine / Female", "Androgynous"]

AGE_LIST = [
    "Child / Pre-adolescent", 
    "Adolescent / Teenager", 
    "Young Adult (Early 20s)", 
    "Middle-aged (Late 40s)", 
    "Elderly / Senior", 
    "Ancient / Centenarian"
]

NAT_DESC = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure",
    "Syrian": "Levantine features, straight profile",
    "Turkish": "Eurasian features, strong facial contours, dark hair, medium olive skin",
    "Indian": "South Asian features, deep-set dark eyes, thick dark hair, rich warm undertones",
    "American": "Diverse North American features, broad range of skin tones, varied facial structures",
    "European": "Caucasian features, varied eye colors, prominent brow ridge, fair complexion",
    "African": "Sub-Saharan features, broad nasal structure, full lips, deep melanated skin",
    "Chinese": "East Asian features, epicanthic folds, high cheekbones, smooth skin texture"
}

ERA_DESC = {
    "Contemporary / Modern Day": "Current lighting, sharp details, digital photography look",
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures, survivalist look",
    "Before Common Era (BCE)": "Ancient civilization styling, rudimentary tools/makeup",
    "Pre-Islamic Era": "Traditional regional heritage, antique textures",
    "Ancient Era (Hellenistic/Roman)": "Classical features, draping, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures, atmospheric mood",
    "200 Years ago (Early 19th Century)": "Regency style, natural fiber textures, era-specific grooming",
    "150 years ago (Victorian Era)": "Formal, structured, refined textures, pale complexions",
    "100 Years ago (Roaring 20s)": "Vintage aesthetic, early 20th-century grooming/lighting",
    "50 Years ago (1970s Retro)": "Analog film look, warm hues, vintage hair styles",
    "Futuristic / Cyberpunk": "Neon accents, synthetic materials, high-tech glow",
    "Post-Apocalyptic": "Dirty, weathered, distressed textures, gritty survivalist"
}

CONCEPTS = {
    "Heroic Warrior": "Strong jawline, confident gaze, slight battle wear",
    "Sinister Villain": "Harsh shadows, menacing expression, sharp features",
    "Scholar / Intellectual": "Refined appearance, focused eyes, thoughtful pose",
    "Royal / Aristocratic": "Elegant posture, pristine skin, luxury textures",
    "Mercenary / Outlaw": "Rugged, weathered, scars, untamed grooming",
    "Mystic / Shaman": "Otherworldly look, spiritual paint, ethereal lighting",
    "Corporate Executive / CEO": "Clean-cut, authoritative, sharp professional lighting",
    "Elite Athlete / Fitness Pro": "Defined muscularity, healthy skin glow, sweat detail",
    "Bohemian Artist": "Creative styling, messy hair, expressive eyes",
    "Average Citizen": "Naturalistic, candid, everyday lighting",
    "Blue-collar / Technician": "Grime, work-worn skin, functional appearance",
    "Academic Student": "Youthful, inquisitive, natural-soft lighting",
    "High-fashion Model": "Angular features, studio lighting, flawless skin",
    "Retiree / Grandparent": "Dignified aging, soft textures, wisdom-filled gaze",
    "Urban / Street Style": "Modern edge, trendy accessories, natural city light",
    "Rural / Outdoorsman": "Sun-damaged skin, practical gear, natural daylight",
    "Red Carpet / Gala Guest": "Glamorous, high-contrast lighting, perfect grooming",
    "Ailing / Sickly Character": "Pale skin, dark circles, visible veins, weak posture"
}

GROOM_DESC = {
    "Clean Shaven": "Smooth skin, no stubble, close-cut grooming finish",
    "Saudi Anchor Beard": "Sharp and angular form connected to the chin",
    "Pyramidal Moustache": "Mustache with wide edges and a narrow top",
    "Light Stubble": "Very short, even stubble, uniform shade pattern",
    "Heavy Stubble": "Thicker, rough texture, darker shade, irregular growth",
    "Designer Stubble": "Precisely trimmed, clean sharp defined edges",
    "Shadow Fade Beard": "Faded sides, denser hair on chin, smooth gradient transition",
    "Classic Goatee": "Chin beard connected to mustache, smooth circular blend",
    "Short Boxed Beard": "Short, full beard, precise square defined edges",
    "Long Full Beard": "Long, thick, natural growth pattern, dense hair volume",
    "Unkempt Beard": "Messy natural growth, disheveled texture, random hair direction",
    "Warrior Beard": "Thick, rugged, battle-worn appearance, natural textures"
}

HAIR_TEX_DESC = {
    "Straight (Sleek)": "Linear alignment, high specular highlights, silky smooth surface",
    "Wavy (Type 2)": "Natural S-shape waves, effortless flow, soft luster, beachy texture",
    "Curly (Type 3)": "Defined ringlets, springy loops, voluminous structure, high frizz detail",
    "Afro-Textured": "Kinky-coily patterns, high density, matte finish, tight structural coils",
    "Disheveled & Matted": "Tangled clumps, distressed cuticles, weathered look, realistic stray hairs"
}

HAIR_COLORS = {
    "Jet black / Natural black": "Jet black, deep and rich natural black",
    "Deep espresso brown": "Deep espresso brown with warm undertones",
    "Light chestnut / Sandy brown": "Light chestnut brown with honey or sandy tones",
    "Salt and pepper, 30% grey": "Black hair mixed with noticeable white strands",
    "Salt and pepper, 70% grey": "Mostly white hair mixed with scattered black strands",
    "Ash blonde / Golden blonde": "Ash blonde (cool tone) or golden blonde (warm tone)"
}

SFX_DESC = {
    "Fresh Katana/Sword Slash": "Deep sword wound, open edges, active bleeding",
    "Blunt Force Contusion": "Blunt force contusion, severe swelling, inflamed redness, no laceration",
    "1-Week old wound (Granulation)": "1-week old wound, pink granulation tissue, flaking skin",
    "1-Year Old Keloid Scar": "1-year old keloid scar, raised excess tissue, firm texture",
    "Fresh Periorbital Hematoma": "Fresh periorbital hematoma, purplish-red redness, severe inflammation",
    "24-Hour Old Bruise (Deep Purple)": "24-hour old bruise, deep purple and blue, cloudy tissue",
    "Chemical Acid Burn (Corrosive)": "Chemical acid burn, melted tissue, viscous and corroded texture",
    "2nd Degree Burn with Blisters": "2nd degree burn, fluid-filled blisters, shiny and peeling skin"
}

LIGHT_DESC = {
    "Rembrandt Lighting": "Classic cinematic light with a small triangle under the eye, highly elegant",
    "Chiaroscuro Lighting": "Severe contrast between shadow and light, dramatic facial volume",
    "Teal and Orange Lighting": "Classic cinematic mix of cool teal and warm orange tones",
    "Cinematic Golden Hour": "Warm and soft sunset light, highlighting natural skin tones",
    "High-Key Studio Lighting": "Flat and bright light with no shadows, revealing all details clearly",
    "Low-Key Moody Lighting": "Very low and dark light, revealing only specific parts of the face, mysterious mood",
    "Neon Cyberpunk Rim Light": "Colorful neon edge lights outlining the face, modern fantasy aesthetic"
}

CAM_DESC = {
    "85 mm Lens, Eye-Level Shot": "Classic portrait lens, perfect for showing skin texture without facial distortion",
    "100 mm Macro Lens, Extreme Close-Up": "Macro lens, specifically for stunning details like skin pores or SFX wound textures",
    "50 mm Lens, Dutch Angle": "Normal lens with tilted angle, creating suspense and dread",
    "35 mm Lens, Low-Angle (Hero Shot)": "Slightly wide, low-angle shot showing the character as powerful and heroic",
    "24 mm Wide-Angle, High-Angle": "Wide-angle lens from a high angle, making the face look slightly elongated or vulnerable"
}

SIZE_LIST = [
    "Aspect Ratio 16:9 (Widescreen)",
    "Aspect Ratio 4:5 (Portrait/Vertical)",
    "Aspect Ratio 5:4 (Portrait)",
    "Aspect Ratio 2.39:1 (Anamorphic / Cinemascope)",
    "Aspect Ratio 1:1 (Square)"
]

# ==========================================
# 3. مدیریت وضعیت (State Machine)
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'plan' not in st.session_state: st.session_state.plan = "UONA Core"
if 'route' not in st.session_state: st.session_state.route = 'login'

if 'draft' not in st.session_state: 
    st.session_state.draft = {
        "gen": "Masculine / Male", "age": "Young Adult (Early 20s)", "nat": "Iranian", 
        "char": "Average Citizen", "era": "Contemporary / Modern Day", "groom": "Clean Shaven", 
        "h_tex": "Straight (Sleek)", "h_col": "Jet black / Natural black",
        "cam": list(CAM_DESC.keys())[0], "light": list(LIGHT_DESC.keys())[0], "size": SIZE_LIST[0],
        "scenario_text": "", "arc_aging": "None", "arc_sfx": "None", "arc_pigment": "None",
        "bio_fatigue": False, "bio_lips": False
    }

def go_to(route): st.session_state.route = route; st.rerun()

# ==========================================
# 4. موتور پردازش هوشمند (Logic Engine)
# ==========================================
def generate_prompt(draft):
    # Baseline Specs
    baseline = f"Uona Studio Signature (Scientific Makeup Design). [Fixed Technical: {draft.get('cam')}, {draft.get('light')}, {draft.get('size')}]. "
    
    # Character DNA
    J9_desc = NAT_DESC.get(draft.get('nat'), "")
    G12_desc = ERA_DESC.get(draft.get('era'), "")
    identity = f"Character Identity: {draft.get('gen')}, Base Age {draft.get('age')}, Nationality: {draft.get('nat')} ({J9_desc}), Type: {draft.get('char')}, Era: {G12_desc}. "
    
    # Adaptive Appearance
    groom_val = draft.get('groom', 'Clean Shaven')
    groom_desc = GROOM_DESC.get(groom_val, "")
    appearance = f"Grooming/Appearance: {groom_val} ({groom_desc}), Hair Color: {draft.get('h_col')}, Texture: {draft.get('h_tex')}. "
    
    # Arc / Transformation Logic
    progression = ""
    is_arc_active = (draft.get('arc_aging', 'None') != "None") or (draft.get('arc_sfx', 'None') != "None") or (draft.get('arc_pigment', 'None') != "None")
    
    if is_arc_active:
        progression = f"HORIZONTAL TRIPTYCH ARC. Four stages divided by 1px separators. Scenario Context: [{draft.get('scenario_text', '')}]. "
        
        if draft.get('arc_aging', 'None') != "None":
            progression += f"SCIENTIFIC AGING LOGIC ({draft.get('arc_aging')}): Inject [Epidermal thinning, Bone density loss, Solar lentigines, Gravity-induced ptosis]. "
        
        if draft.get('arc_sfx', 'None') != "None":
            sfx_base = SFX_DESC.get(draft.get('arc_sfx'), draft.get('arc_sfx'))
            progression += f"SFX Trauma Arc: Base is {sfx_base}. SCIENTIFIC TRAUMA LOGIC: Apply Color Shift from wet crimson to dark scabbing, and Material Transformation to fibrous scar tissue. "
            
        if draft.get('arc_pigment', 'None') != "None":
            progression += f"Pigmentation Arc: {draft.get('arc_pigment')}. Apply progressive textural and dermal shift. "
        
        progression += f"PROGRESSION LABELS: Typography labels under each panel ('Initial' -> 'Spread' -> 'Damage' -> 'Final'). PROGRESS LINE ACTIVE. CRITICAL: Underlying facial identity MUST remain 100% identical across all panels. "
    else:
        progression += "Single Shot Portrait. "

    # Bio Details
    bio_layers = []
    if draft.get('bio_fatigue'): bio_layers.append("Chronic Fatigue & Sallow Skin")
    if draft.get('bio_lips'): bio_layers.append("Lips Volume Loss & Atrophy")
    if bio_layers:
        progression += f"Biological Detail Layers: {', '.join(bio_layers)}. "
    
    final_p = baseline + identity + appearance + progression + " 8k, hyper-realistic, subsurface scattering, focus on prosthetic makeup accuracy."
    return " ".join(final_p.split())

# ==========================================
# 5. موتور استایل (CSS Engine)
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
        background-color: transparent !important; border: none !important; box-shadow: none !important;
        padding: 0 !important; min-height: 0 !important; height: auto !important; display: flex !important; justify-content: flex-start !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button p {
        color: #00f2ff !important; font-family: 'Cinzel', serif !important; font-size: 1.5rem !important;
        font-weight: 900 !important; margin: 0 !important; padding: 0 !important; text-transform: uppercase !important; transition: all 0.3s ease !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button:hover p {
        color: #ffffff !important; text-shadow: 0 0 15px #00f2ff !important; transform: scale(1.02) !important;
    }

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
    
    div[data-testid="stExpander"] { background: rgba(10, 25, 47, 0.6) !important; border: 1px solid rgba(0, 242, 255, 0.2) !important; border-radius: 12px !important; backdrop-filter: blur(10px); margin-bottom: 15px; transition: all 0.3s ease; }
    div[data-testid="stExpander"]:hover { border-color: rgba(0, 242, 255, 0.6) !important; box-shadow: 0 5px 20px rgba(0, 242, 255, 0.15); }
    div[data-testid="stExpander"] summary { padding: 15px !important; }
    div[data-testid="stExpander"] summary p { color: #ffffff !important; font-family: 'Cinzel', serif !important; font-size: 1.1rem !important; letter-spacing: 2px; font-weight: bold !important; }
    
    [data-testid="stImage"] img { border-radius: 12px !important; border: 2px solid #00f2ff !important; box-shadow: 0 0 15px rgba(0, 242, 255, 0.7) !important; }
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
# SHARED HEADER
# ==========================================
if st.session_state.route != 'login':
    badge_color = "#ffaa00" if "Apex" in st.session_state.plan or "MASTER" in st.session_state.plan else "#00f2ff"
    c_head1, c_head2 = st.columns([1, 3])
    with c_head1:
        st.markdown('<span class="logo-marker"></span>', unsafe_allow_html=True)
        if st.button("UONA STUDIO", key="top_home_btn"): go_to('dashboard')
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
                if new_u != ADMIN_USER:
                    users[new_u] = {"pass": new_p, "plan": new_plan}
                    save_json(DB_FILE, users)
                    st.success(f"Client '{new_u}' successfully registered.")
                    st.rerun()
            else: st.warning("Fill all fields.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>👥 Active Client Subscriptions</h4>", unsafe_allow_html=True)
        if not users: st.info("No active clients yet.")
        else:
            for usr, data in users.items():
                if isinstance(data, str): plan_val, pwd_val = "UONA Core", data
                else: plan_val, pwd_val = data.get("plan", "UONA Core"), data.get("pass", "")
                col_name, col_plan, col_pass, col_btn = st.columns([2, 2, 2, 1])
                col_name.markdown(f"<span style='color:white; font-family:Montserrat; font-weight:bold;'>👤 {usr}</span>", unsafe_allow_html=True)
                col_plan.markdown(f"<span style='color:#00f2ff; font-family:Cinzel; font-size:0.8rem;'>{plan_val}</span>", unsafe_allow_html=True)
                col_pass.markdown(f"<span style='color:#888; font-family:monospace;'>pwd: {pwd_val}</span>", unsafe_allow_html=True)
                if col_btn.button("REVOKE", key=f"del_{usr}"):
                    del users[usr]; save_json(DB_FILE, users); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 2: DASHBOARD FLOW
# ==========================================
elif st.session_state.route == 'dashboard':
    bg = find_bg_file()
    if bg: add_bg_from_local(bg)
    
    st.markdown("<h2 style='color:#fff; font-family:Cinzel; text-align:center;'>CONTROL CENTER</h2><div class='subtitle' style='text-align:center;'>Select a module to begin</div>", unsafe_allow_html=True)
    if st.session_state.is_admin:
        if st.button("⚙️ RETURN TO ADMIN PANEL"): go_to('admin_panel')
        st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>🎬</h1><h3 class="module-title">NEW CHARACTER</h3><p style="color:#888; font-size:0.8rem;">Start Cinematic UI Builder</p></div>', unsafe_allow_html=True)
        if st.button("START PROJECT", key="b1", use_container_width=True): go_to('builder')
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
    projects = load_json(PROJ_FILE, [])
    my_projs = [p for p in projects if p.get("user") == st.session_state.user]
    if not my_projs: st.info("No projects saved yet.")
    else:
        for p in my_projs:
            with st.expander(f"📁 PROJECT LOG | {p['date']}"):
                st.code(p['prompt'], language="markdown")
    st.markdown("<hr style='border-color: rgba(0,242,255,0.2);'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#00f2ff; font-family:Cinzel;'>REFERENCE GALLERY</h4>", unsafe_allow_html=True)
    l_c1, l_c2, l_c3, l_c4 = st.columns(4)
    with l_c1:
        if os.path.exists("desert_warn.jpg"): st.image("desert_warn.jpg", caption="Desert Warn")
    with l_c2:
        if os.path.exists("royal_clean.jpg"): st.image("royal_clean.jpg", caption="Royal Clean")

elif st.session_state.route == 'settings':
    st.markdown("<h2 class='title-main'>SYSTEM SETTINGS</h2>", unsafe_allow_html=True)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.selectbox("Default AI Engine", ["Midjourney V6", "Gemini Pro Vision", "Stable Diffusion XL"])
    st.selectbox("Theme Mode", ["Dark Cinematic", "Light Mode (Not Recommended)"])
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 🔴 ROUTE 3: CHARACTER BUILDER (NEW UX/UI DASHBOARD) 🔴
# ==========================================
elif st.session_state.route == 'builder':
    st.markdown("<h2 class='title-main' style='text-align:center; font-size:2rem; margin-bottom: 25px;'>IDENTITY ENGINE / CHARACTER LAB</h2>", unsafe_allow_html=True)
    d = st.session_state.draft

    # --- System UX Logic Verification ---
    age_val = d.get('age', AGE_LIST[2])
    age_idx = AGE_LIST.index(age_val) if age_val in AGE_LIST else 0
    is_under_22 = age_idx < 2  # Checks if "Child" or "Adolescent"
    gen_val = d.get('gen', GENDER_LIST[0])
    is_female = gen_val in ["Feminine / Female", "Female"]

    # --- 3-Column Visual Layout (Desktop First) ---
    c_left, c_center, c_right = st.columns([3, 4.5, 2.5], gap="medium")

    # ----- 1. LEFT PANEL: CHARACTER DNA (30%) -----
    with c_left:
        st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%;">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff; margin-bottom:15px; font-family:Cinzel;'><span style='font-size:1.2rem;'>🔒</span> CHARACTER DNA</h4>", unsafe_allow_html=True)
        
        d['gen'] = st.radio("GENDER (BIOMETRIC LOCK)", GENDER_LIST, index=GENDER_LIST.index(gen_val) if gen_val in GENDER_LIST else 0)
        st.markdown("<br>", unsafe_allow_html=True)
        d['age'] = st.select_slider("BASE AGE", options=AGE_LIST, value=age_val)
        st.markdown("<br>", unsafe_allow_html=True)
        d['nat'] = st.selectbox("NATIONALITY", list(NAT_DESC.keys()), index=list(NAT_DESC.keys()).index(d.get('nat', 'Iranian')) if d.get('nat') in NAT_DESC else 0)
        d['char'] = st.selectbox("CHARACTER TYPE", list(CONCEPTS.keys()), index=list(CONCEPTS.keys()).index(d.get('char', 'Average Citizen')) if d.get('char') in CONCEPTS else 0)
        
        st.markdown("<div style='margin-top: 25px; padding: 12px; background: rgba(0, 242, 255, 0.05); border-left: 3px solid #00f2ff; color: #00f2ff; font-family: Montserrat; font-size: 0.75rem; text-transform:uppercase;'>🔒 Identity Locked. Base Parameters Preserved.</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ----- 2. CENTER STAGE: LIVE PREVIEW (45%) -----
    with c_center:
        st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%; display: flex; flex-direction: column;">', unsafe_allow_html=True)
        
        # Hero Frame
        st.markdown("<div style='flex-grow: 1; border: 1px solid rgba(0,242,255,0.3); border-radius: 10px; background: #02060c; position:relative; overflow: hidden; display:flex; justify-content:center; align-items:center; min-height: 400px;'>", unsafe_allow_html=True)
        st.markdown("<div style='position:absolute; top: 10px; left: 15px; color:#00f2ff; font-size:0.7rem; font-family:Montserrat; background: rgba(0,0,0,0.5); padding: 5px 10px; border-radius: 4px; border: 1px solid rgba(0,242,255,0.2);'>🟢 Prosthetic Makeup Simulation Active</div>", unsafe_allow_html=True)
        
        if os.path.exists("portrait_clean.PNG"):
            st.image("portrait_clean.PNG", use_container_width=True)
        else:
            st.markdown("<h3 style='color:rgba(255,255,255,0.1); font-family:Cinzel;'>[ 4:5 LIVE PORTRAIT FRAME ]</h3>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Cinematic Timeline Bar
        st.markdown("""
        <div style='display: flex; justify-content: space-between; align-items: center; margin-top: 20px; padding: 15px; background: rgba(0, 242, 255, 0.05); border-radius: 8px; border: 1px solid rgba(0,242,255,0.2);'>
            <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.8rem; font-weight:bold;'>STAGE 1</span><br><span style='color:#888; font-size:0.6rem; text-transform:uppercase;'>Initial</span></div>
            <div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(0,242,255,0.5) 0%, rgba(255,255,255,0.2) 100%); margin: 0 15px;'></div>
            <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.8rem; font-weight:bold;'>STAGE 2</span><br><span style='color:#888; font-size:0.6rem; text-transform:uppercase;'>Spread</span></div>
            <div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(0,242,255,0.5) 0%, rgba(255,255,255,0.2) 100%); margin: 0 15px;'></div>
            <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.8rem; font-weight:bold;'>STAGE 3</span><br><span style='color:#888; font-size:0.6rem; text-transform:uppercase;'>Damage</span></div>
            <div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(0,242,255,0.5) 0%, rgba(255,255,255,0.2) 100%); margin: 0 15px;'></div>
            <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.8rem; font-weight:bold;'>STAGE 4</span><br><span style='color:#888; font-size:0.6rem; text-transform:uppercase;'>Final</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚡ GENERATE CINEMATIC SEQUENCE", use_container_width=True): go_to('prompt_engine')
        st.markdown('</div>', unsafe_allow_html=True)

    # ----- 3. RIGHT PANEL: TRANSFORMATION ENGINE (25%) -----
    with c_right:
        st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%;">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#ffaa00; margin-bottom:15px; font-family:Cinzel;'><span style='font-size:1.2rem;'>⚙️</span> DYNAMIC CONTROL</h4>", unsafe_allow_html=True)
        
        with st.expander("A. ADAPTIVE PARAMETERS", expanded=True):
            d['era'] = st.selectbox("TIME PERIOD", list(ERA_DESC.keys()), index=list(ERA_DESC.keys()).index(d.get('era', list(ERA_DESC.keys())[0])) if d.get('era') in ERA_DESC else 0)
            
            # Female Constraint Logic
            if is_female:
                st.markdown("<div style='margin: 10px 0; padding: 8px; background: rgba(255, 0, 0, 0.1); border-left: 3px solid red; color: #aaa; font-family: Montserrat; font-size: 0.75rem;'>🔒 Grooming Locked (Biological Constraint)</div>", unsafe_allow_html=True)
                d['groom'] = "Clean Shaven"
            else:
                d['groom'] = st.selectbox("GROOMING", list(GROOM_DESC.keys()), index=list(GROOM_DESC.keys()).index(d.get('groom', "Clean Shaven")) if d.get('groom') in GROOM_DESC else 0)

            d['h_tex'] = st.selectbox("HAIR TEXTURE", list(HAIR_TEX_DESC.keys()), index=list(HAIR_TEX_DESC.keys()).index(d.get('h_tex', list(HAIR_TEX_DESC.keys())[0])) if d.get('h_tex') in HAIR_TEX_DESC else 0)
            d['h_col'] = st.selectbox("HAIR & BEARD COLOR", list(HAIR_COLORS.keys()), index=list(HAIR_COLORS.keys()).index(d.get('h_col', list(HAIR_COLORS.keys())[0])) if d.get('h_col') in HAIR_COLORS else 0)

        with st.expander("B. ADVANCED MODULES (ARC)", expanded=True):
            # 🔴 فیکس مهم: بستن دسترسی اکانت‌های Core به ماژول‌های Arc 🔴
            if st.session_state.plan == "UONA Core":
                st.markdown("""
                <div style='margin: 10px 0; padding: 15px; background: rgba(255, 170, 0, 0.05); border: 1px solid rgba(255, 170, 0, 0.3); border-radius: 8px; text-align: center;'>
                    <span style='font-size: 2rem;'>🔒</span><br>
                    <b style='color: #ffaa00; font-family: Montserrat; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;'>Premium Feature</b>
                    <p style='color: #888; font-size: 0.7rem; margin-top: 5px;'>Arc Modules (Aging, SFX, Pigmentation) require an Apex or Master subscription.</p>
                </div>
                """, unsafe_allow_html=True)
                
                d['arc_aging'] = "None"
                d['arc_sfx'] = "None"
                d['arc_pigment'] = "None"
                d['bio_fatigue'] = False
                d['bio_lips'] = False
                d['scenario_text'] = ""
                
            else:
                d['arc_aging'] = st.selectbox("AGING ENGINE", ["None", "Wrinkles", "Volume & Sagging", "Skin Texture & Pigmentation", "Hair & Brows"], index=0)
                
                # Age < 22 SFX Constraint Logic
                if is_under_22:
                    st.markdown("<div style='margin: 10px 0; padding: 8px; background: rgba(255, 0, 0, 0.1); border-left: 3px solid red; color: #aaa; font-family: Montserrat; font-size: 0.75rem;'>🔒 SFX Locked (Age Constraint: ≥ 22)</div>", unsafe_allow_html=True)
                    d['arc_sfx'] = "None"
                else:
                    sfx_opts = ["None"] + list(SFX_DESC.keys())
                    d['arc_sfx'] = st.selectbox("SFX & TRAUMA ENGINE", sfx_opts, index=0)
                    
                d['arc_pigment'] = st.selectbox("SKIN PIGMENTATION", ["None", "Vitiligo", "Melasma & Hyperpigmentation", "Freckles"], index=0)
                
                st.markdown("<p style='color:#00f2ff; font-size: 0.7rem; margin-top: 15px; text-transform:uppercase;'>Biological Detail Layers</p>", unsafe_allow_html=True)
                d['bio_fatigue'] = st.checkbox("Fatigue & Illness", value=d.get('bio_fatigue', False))
                d['bio_lips'] = st.checkbox("Lips Volume Loss", value=d.get('bio_lips', False))
                
                d['scenario_text'] = st.text_input("SCENARIO DESCRIPTION", value=d.get('scenario_text', ''), placeholder="e.g. A slash wound oxidizing over time...")

        # System Feedback Bar
        if d['arc_sfx'] != "None" and d['arc_aging'] != "None":
            feedback, f_color = "⚠️ Arc Conflict (Hybrid Mode)", "#ffcc00"
        elif is_female or is_under_22:
            feedback, f_color = "🔒 Constraints Safely Enforced", "#00f2ff"
        else:
            feedback, f_color = "✅ Continuity Preserved", "#00ffaa"
            
        st.markdown(f"<div style='margin-top: 15px; padding: 12px; background: rgba(0, 0, 0, 0.5); border-left: 3px solid {f_color}; color: {f_color}; font-family: Montserrat; font-size: 0.75rem; text-transform:uppercase;'>{feedback}</div>", unsafe_allow_html=True)
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
        with sim_c2:
            if os.path.exists("studio_portrait.jpg"): st.image("studio_portrait.jpg", caption="Studio Lighting Test")
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.selectbox("Render Engine Test", ["Preview Mode (Fast)", "High Fidelity"])
        if st.button("⬅ BACK TO BUILDER", use_container_width=True): go_to('builder')
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.route == 'prompt_engine':
    st.markdown("<h2 class='title-main'>PROMPT ENGINE</h2>", unsafe_allow_html=True)
    final_p = generate_prompt(st.session_state.draft)

    c1, c2 = st.columns([2.5, 1])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.text_area("MASTER PROMPT (SCIENTIFIC LOGIC)", value=final_p, height=200)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        if st.button("💾 SAVE TO LIBRARY", use_container_width=True):
            projects = load_json(PROJ_FILE, [])
            projects.insert(0, {"user": st.session_state.user, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "prompt": final_p})
            save_json(PROJ_FILE, projects)
            st.success("Saved to Library!")
        if st.button("⬅ BACK TO LAB", use_container_width=True): go_to('builder')
        st.markdown('</div>', unsafe_allow_html=True)
