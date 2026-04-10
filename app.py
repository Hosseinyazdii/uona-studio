import streamlit as st
from datetime import datetime
import os
import json

# ==========================================
# 1. تنظیمات پلتفرم و مدیریت دیتابیس
# ==========================================
st.set_page_config(page_title="UONA STUDIO | AI SaaS", layout="wide", initial_sidebar_state="collapsed")

DB_FILE = ".users_db.json"
PROJ_FILE = ".projects_db.json"

def load_json(file, default):
    if not os.path.exists(file):
        with open(file, "w") as f: json.dump(default, f)
    with open(file, "r") as f: return json.load(f)

def save_json(file, data):
    with open(file, "w") as f: json.dump(data, f)

# ==========================================
# 2. مدیریت وضعیت (State Machine)
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'route' not in st.session_state: st.session_state.route = 'login'
if 'step' not in st.session_state: st.session_state.step = 1
# دیتای پیش‌نویس کاراکتر
if 'draft' not in st.session_state: 
    st.session_state.draft = {
        "gen":"", "age":"", "actor":"", "nat":"", "era":"", "h_col":"", 
        "h_tex":"", "sfx":"", "mat":"", "char":"", "groom":"", "cam":"", "light":"", "size":""
    }

# توابع مسیریابی
def go_to(route): st.session_state.route = route; st.rerun()
def next_step(): st.session_state.step += 1; st.rerun()
def prev_step(): st.session_state.step -= 1; st.rerun()

# ==========================================
# 3. موتور استایل (CSS Engine)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh; overflow-x: hidden;
    }
    #MainMenu, footer, header {visibility: hidden;}

    .title-main { font-family: 'Cinzel'; color: #ffffff !important; font-size: 2.5rem; font-weight: 800; letter-spacing: 10px; margin: 0; text-shadow: 0 0 15px rgba(0, 242, 255, 0.5); }
    .subtitle { color: #00f2ff; font-family: 'Montserrat'; font-size: 0.8rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 30px;}

    label, .stMarkdown p { color: #00e5ff !important; font-family: 'Montserrat' !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.75rem !important; }

    /* دکمه‌های اصلی */
    .stButton > button {
        border: none !important; border-radius: 8px !important;
        font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px; transition: 0.3s;
        background-color: #00f2ff !important; color: #000000 !important;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.3);
    }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.02); box-shadow: 0 0 20px #00f2ff;}

    /* پنل‌ها و کارت‌ها */
    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 25px; backdrop-filter: blur(10px); margin-bottom: 20px; }
    
    /* Progress Bar اختصاصی */
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 30px; color: #4a5d73; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 900; }
    .step-active { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }

    .nav-top { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(0, 242, 255, 0.2); padding-bottom: 10px; margin-bottom: 20px; }
    
    .module-title { font-family: 'Cinzel'; color: #008b8b !important; text-shadow: 0 0 12px rgba(255, 215, 0, 0.8) !important; letter-spacing: 3px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

def add_n(d): return ["None"] + d + ["Others"]

# ==========================================
# ROUTE 1: ENTRY FLOW (LOGIN)
# ==========================================
if st.session_state.route == 'login':
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=250)
    with c2:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px;'>UONA ACCESS</h1>", unsafe_allow_html=True)
        mode = st.radio("ENTRY", ["Login", "Register"], horizontal=True)
        u_name = st.text_input("USERNAME")
        u_pass = st.text_input("PASSWORD", type="password")
        
        users = load_json(DB_FILE, {"hossein": "1234"})
        if mode == "Login":
            if st.button("AUTHENTICATE"):
                if u_name in users and users[u_name] == u_pass:
                    st.session_state.auth = True; st.session_state.user = u_name; go_to('dashboard')
                else: st.error("Access Denied")
        else:
            if st.button("CREATE ACCOUNT"):
                if u_name and u_pass:
                    users[u_name] = u_pass; save_json(DB_FILE, users); st.success("Account created!")

# ==========================================
# SHARED HEADER (برای بقیه صفحات)
# ==========================================
if st.session_state.route != 'login':
    st.markdown(f"""
        <div class="nav-top">
            <div><span style="color:#00f2ff; font-family:Cinzel; font-size:1.5rem; font-weight:900;">UONA STUDIO</span></div>
            <div>
                <span style="color:#fff; font-family:Montserrat; font-size:0.8rem;">USER: {st.session_state.user.upper()}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# ROUTE 2: DASHBOARD FLOW
# ==========================================
if st.session_state.route == 'dashboard':
    st.markdown("<h2 style='color:#fff; font-family:Cinzel; text-align:center;'>CONTROL CENTER</h2><div class='subtitle' style='text-align:center;'>Select a module to begin</div>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>🎬</h1><h3 class="module-title">NEW CHARACTER</h3><p style="color:#888; font-size:0.8rem;">Start Multi-Step Builder</p></div>', unsafe_allow_html=True)
        if st.button("START PROJECT", key="b1", use_container_width=True): 
            st.session_state.step = 1; go_to('builder')
    with c2:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>📂</h1><h3 class="module-title" style="color:#777!important; text-shadow:none!important;">LIBRARY</h3><p style="color:#888; font-size:0.8rem;">Saved Looks & Presets</p></div>', unsafe_allow_html=True)
        st.button("OPEN LIBRARY", disabled=True, use_container_width=True)
    with c3:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>⚙️</h1><h3 class="module-title" style="color:#777!important; text-shadow:none!important;">SETTINGS</h3><p style="color:#888; font-size:0.8rem;">System Preferences</p></div>', unsafe_allow_html=True)
        st.button("OPEN SETTINGS", disabled=True, use_container_width=True)

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
    
    d = st.session_state.draft # رفرنس کوتاه

    # --- STEP 1 ---
    if st.session_state.step == 1:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 1: Core Identity</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        d['actor'] = c1.selectbox("Actor Reference", ["None", "Yes", "No"], index=["None", "Yes", "No"].index(d['actor']) if d['actor'] else 0)
        d['gen'] = c2.selectbox("Gender", ["Male", "Female", "Androgynous"], index=["Male", "Female", "Androgynous"].index(d['gen']) if d['gen'] else 0)
        d['age'] = c1.selectbox("Age Range", ["Elderly", "Middle-aged", "Young Adult", "Child"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("EXIT"): go_to('dashboard')
        if col3.button("NEXT ➔"): next_step()

    # --- STEP 2 ---
    elif st.session_state.step == 2:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 2: Physical Attributes</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        d['nat'] = c1.selectbox("Nationality", ["Iranian", "Saudi", "European", "African", "Asian"])
        d['era'] = c2.selectbox("Era / Period", ["Ancient", "Medieval", "100 Years Ago", "Contemporary"])
        d['h_col'] = c1.selectbox("Hair Color", ["Jet Black", "Espresso", "Ash Blonde", "Salt & Pepper"])
        d['h_tex'] = c2.selectbox("Hair Texture", ["Afro", "Wavy", "Curly", "Straight", "Matted"])
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("NEXT ➔"): next_step()

    # --- STEP 3 ---
    elif st.session_state.step == 3:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 3: Grooming & SFX Trauma</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        d['groom'] = c1.selectbox("Grooming Style", ["Clean Shaven", "Full Beard", "Stubble", "Goatee"])
        d['sfx'] = c2.selectbox("Trauma / SFX", ["None", "Katana Slash", "Bruise", "Glass Wound", "Burn"])
        d['mat'] = c1.selectbox("Material Finish", ["Silicone", "Matte Sealer", "Alcohol Palette"])
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("NEXT ➔"): next_step()

    # --- STEP 4 ---
    elif st.session_state.step == 4:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 4: Technical Specs</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        d['char'] = c1.selectbox("Character Concept", ["Warrior", "Villain", "Scholar", "Royal"])
        d['cam'] = c2.selectbox("Camera & Lens", ["85mm", "100mm Macro", "35mm Low-Angle"])
        d['light'] = c1.selectbox("Lighting Style", ["Rembrandt", "Teal & Orange", "Neon"])
        d['size'] = c2.selectbox("Frame Size", ["4:5", "16:9", "2.39:1", "1:1"])
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("REVIEW ➔"): next_step()

    # --- STEP 5 (REVIEW) ---
    elif st.session_state.step == 5:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 5: Final Review</h3>", unsafe_allow_html=True)
        st.info(f"**Identity:** {d['gen']}, {d['age']} | **Physical:** {d['nat']}, {d['era']} | **Hair:** {d['h_col']} ({d['h_tex']}) \n\n **Concept:** {d['char']}, {d['groom']} | **SFX:** {d['sfx']} ({d['mat']}) \n\n **Tech:** {d['cam']}, {d['light']}, {d['size']}")
        
        col1, col2, col3 = st.columns([1.5, 3, 2])
        if col1.button("⬅ EDIT (BACK)"): prev_step()
        if col3.button("🚀 PROCEED TO SIMULATION"): go_to('simulation')

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 4: VISUAL SIMULATION
# ==========================================
elif st.session_state.route == 'simulation':
    st.markdown("<h2 style='color:#fff; font-family:Cinzel;'>VISUAL SIMULATION</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div style="background:#0a192f; height:350px; border-radius:15px; border:1px dashed #00f2ff; display:flex; align-items:center; justify-content:center; flex-direction:column;">
            <h1 style="color:#00f2ff; opacity:0.5;">👁️</h1>
            <p style="color:#00f2ff; opacity:0.7; font-family:Montserrat;">LIVE PREVIEW FEED (AWAITING ENGINE RENDER)</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>Environment Tweaks</h4>", unsafe_allow_html=True)
        st.selectbox("Render Engine Test", ["Preview Mode (Fast)", "High Fidelity"])
        st.slider("Atmospheric Density", 0, 100, 50)
        st.markdown("<hr>", unsafe_allow_html=True)
        if st.button("⬅ BACK TO BUILDER", use_container_width=True): go_to('builder')
        if st.button("⚡ GENERATE PROMPT", use_container_width=True): go_to('prompt_engine')
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 5: PROMPT ENGINE
# ==========================================
elif st.session_state.route == 'prompt_engine':
    st.markdown("<h2 style='color:#fff; font-family:Cinzel;'>PROMPT ENGINE</h2>", unsafe_allow_html=True)
    
    d = st.session_state.draft
    final_p = f"Professional cinematic portrait, {d['size']}, {d['gen']}, {d['age']}, {d['nat']} from {d['era']}. Concept: {d['char']}, {d['groom']}. Hair: {d['h_col']} ({d['h_tex']}). SFX: {d['sfx']}. Material: {d['mat']}. Tech: {d['cam']}, {d['light']}, 8k raw photo, Unreal Engine 5 render style."

    c1, c2 = st.columns([2.5, 1])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.text_area("MASTER PROMPT (EDITABLE)", value=final_p, height=200)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.selectbox("Target AI", ["Midjourney V6", "Gemini Pro", "Stable Diffusion XL"])
        st.selectbox("Detail Level", ["Standard", "Hyper-Realistic", "Concept Art"])
        if st.button("💾 SAVE TO PROJECT", use_container_width=True):
            projects = load_json(PROJ_FILE, [])
            projects.insert(0, {"user": st.session_state.user, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "prompt": final_p})
            save_json(PROJ_FILE, projects)
            st.success("Project Saved!")
        if st.button("⬅ SIMULATION", use_container_width=True): go_to('simulation')
        if st.button("🏠 DASHBOARD", use_container_width=True): go_to('dashboard')
        st.markdown('</div>', unsafe_allow_html=True)
