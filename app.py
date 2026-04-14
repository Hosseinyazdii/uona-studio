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
        if os.path.exists(name): return name
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
        """, unsafe_allow_html=True
    )

# ==========================================
# 2. دیتابیس مگا پرامپت (V2.0)
# ==========================================# --- Phase 2: ARC CONFIG ---
    elif st.session_state.step == 2:
        age_val = d.get('age', AGE_LIST[2])
        is_under_22 = AGE_LIST.index(age_val) < 2 if age_val in AGE_LIST else False
        is_female = d.get('gen') in ["Feminine / Female", "Female"]

        c_left, c_center, c_right = st.columns([3, 4.5, 2.5], gap="medium")

        # 1. پنل چپ: DNA قفل شده
        with c_left:
            st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%;">', unsafe_allow_html=True)
            st.markdown("<h4 style='color:#00f2ff; font-family:Cinzel;'>🔒 CHARACTER DNA</h4>", unsafe_allow_html=True)
            st.info(f"**Gender:** {d.get('gen')}\n\n**Age:** {d.get('age')}\n\n**Nat:** {d.get('nat')}\n\n**Type:** {d.get('char')}")
            st.markdown("<div style='padding: 10px; background: rgba(0,242,255,0.1); border-left: 3px solid #00f2ff; color: #00f2ff; font-size: 0.75rem;'>🔒 Identity Locked.<br>Base parameters are preserved for continuous execution.</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 2. پنل وسط: پیش‌نمایش
        with c_center:
            st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%; display: flex; flex-direction: column;">', unsafe_allow_html=True)
            st.markdown("<div style='flex-grow: 1; border: 1px solid rgba(0,242,255,0.3); border-radius: 10px; background: #02060c; position:relative; overflow: hidden; display:flex; justify-content:center; align-items:center; min-height: 350px;'>", unsafe_allow_html=True)
            
            st.markdown("""
            <div style='position:absolute; top: 10px; left: 15px; display: flex; flex-direction: column; gap: 5px;'>
                <span style='color:#00f2ff; font-size:0.65rem; background: rgba(0,0,0,0.6); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(0,242,255,0.3);'>🟢 Identity Engine Active</span>
                <span style='color:#00f2ff; font-size:0.65rem; background: rgba(0,0,0,0.6); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(0,242,255,0.3);'>🔒 Biometric Continuity Locked</span>
                <span style='color:#00f2ff; font-size:0.65rem; background: rgba(0,0,0,0.6); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(0,242,255,0.3);'>⚡ Material Simulation Running</span>
            </div>
            """, unsafe_allow_html=True)

            # لود کردن عکس arc.jpg به جای باکس مشکی
            if os.path.exists("arc.jpg"): st.image("arc.jpg", use_container_width=True)
            elif os.path.exists("portrait_clean.PNG"): st.image("portrait_clean.PNG", use_container_width=True)
            else: st.markdown("<div style='min-height:350px; display:flex; align-items:center; justify-content:center;'><h3 style='color:rgba(255,255,255,0.1);'>[ 4:5 LIVE PORTRAIT FRAME ]</h3></div>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # تایم‌لاین داینامیک بر اساس تعداد استیج‌های انتخاب شده یا نوشته شده
            stages_count_ui = d.get('arc_stages', 4)
            if d.get('scenario_text', '').strip():
                # اگر متن نوشته بود، تعداد استیج رو از متن میخونه
                stages_count_ui, _ = ai_narrative_parser(d['scenario_text'], stages_count_ui)
                
            timeline_html = "<div style='display: flex; justify-content: space-between; align-items: center; margin-top: 15px; padding: 10px; background: rgba(0,242,255,0.05); border-radius: 8px;'>"
            for i in range(stages_count_ui):
                timeline_html += f"<div style='text-align:center;'><span style='color:#00f2ff; font-size:0.7rem; font-weight:bold;'>STAGE {i+1}</span></div>"
                if i < stages_count_ui - 1:
                    timeline_html += "<div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(0,242,255,0.5) 0%, rgba(255,255,255,0.2) 100%); margin: 0 5px;'></div>"
                    timeline_html += "<div style='color:#00f2ff; font-size:0.8rem;'>➔</div>"
                    timeline_html += "<div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(255,255,255,0.2) 0%, rgba(0,242,255,0.5) 100%); margin: 0 5px;'></div>"
            timeline_html += "</div>"
            st.markdown(timeline_html, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            c_btn1, c_btn2 = st.columns(2)
            if c_btn1.button("⬅ BACK", use_container_width=True): prev_step()
            if c_btn2.button("NEXT: REVIEW ➔", use_container_width=True): next_step()
            st.markdown('</div>', unsafe_allow_html=True)

        # 3. پنل راست: دیتابیس‌های تخصصی
        with c_right:
            st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%; overflow-y: auto;">', unsafe_allow_html=True)
            st.markdown("<h4 style='color:#ffaa00; font-family:Cinzel;'>⚙️ TRANSFORMATION ENGINE</h4>", unsafe_allow_html=True)
            
            if st.session_state.plan == "UONA Core":
                st.markdown("""
                <div style='margin-top: 20px; padding: 15px; background: rgba(255, 170, 0, 0.05); border: 1px solid rgba(255, 170, 0, 0.3); border-radius: 8px; text-align: center;'>
                    <span style='font-size: 2rem;'>🔒</span><br>
                    <b style='color: #ffaa00; font-size: 0.85rem; text-transform: uppercase;'>Premium Feature</b>
                    <p style='color: #888; font-size: 0.7rem;'>Arc Modules require Apex tier.</p>
                </div>
                """, unsafe_allow_html=True)
                d['arc_stages'] = 4
                d['arc_aging'] = "None"; d['arc_sfx'] = "None"; d['arc_pigment'] = "None"; d['bio_fatigue'] = False; d['bio_lips'] = False; d['scenario_text'] = ""
            else:
                d['arc_stages'] = st.slider("NUMBER OF STAGES", 2, 5, d.get('arc_stages', 4))
                
                with st.expander("A. AGING ENGINE", expanded=True):
                    d['arc_aging'] = st.selectbox("Aging Categories", ["None", "Wrinkles", "Volume & Sagging", "Skin Texture & Pigmentation", "Hair & Brows"])
                    if d['arc_aging'] != "None":
                        aging_stages = AGING_STAGES.get(d['arc_aging'], ["Stage 1", "Stage 2", "Stage 3", "Stage 4"])
                        d['arc_aging_stage'] = st.selectbox("Select Stage", ["All Stages (Progression Arc)"] + aging_stages)
                
                with st.expander("B. SFX & TRAUMA ENGINE", expanded=True):
                    if is_under_22:
                        st.markdown("<div style='padding: 5px; border-left: 3px solid red; color: #aaa; font-size: 0.7rem;'>🔒 SFX Locked (Age Constraint)</div>", unsafe_allow_html=True)
                        d['arc_sfx'] = "None"
                    else:
                        sfx_v2_opts = ["None", "Bruises", "Contusions", "Abrasions", "First & Second Degree Burns", "Chemical Burns (Acid-Type Simulation)", "Keloids (Fibrotic Overgrowth)"]
                        d['arc_sfx'] = st.selectbox("Trauma Simulation", sfx_v2_opts)
                        if d['arc_sfx'] != "None":
                            sfx_stages = SFX_STAGES.get(d['arc_sfx'], ["Stage 1", "Stage 2", "Stage 3", "Stage 4"])
                            d['arc_sfx_stage'] = st.selectbox("Select Stage", ["All Stages (Progression Arc)"] + sfx_stages)
                        
                with st.expander("C. PIGMENTATION ARC", expanded=True):
                    pigment_opts = ["None", "Vitiligo", "Melasma & Hyperpigmentation", "Freckles"]
                    d['arc_pigment'] = st.selectbox("Skin Pigmentation", pigment_opts)
                    if d['
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
        "actor": "None", "gen": "Masculine / Male", "age": "Young Adult (Early 20s)", "nat": "Iranian", 
        "char": "Average Citizen", "era": "Contemporary / Modern Day", "groom": "Clean Shaven", 
        "h_tex": "Straight (Sleek)", "h_col": "Jet black / Natural black", "mat": "None", "sfx": "None",
        "cam": list(CAM_DESC.keys())[0], "light": list(LIGHT_DESC.keys())[0], "size": SIZE_LIST[0],
        "scenario_text": "", "arc_stages": 4, "arc_aging": "None", "arc_sfx": "None", "arc_pigment": "None",
        "arc_aging_stage": "All Stages (Progression Arc)", "arc_sfx_stage": "All Stages (Progression Arc)", "arc_pigment_stage": "All Stages (Progression Arc)",
        "bio_fatigue": False, "bio_lips": False
    }

def go_to(route): st.session_state.route = route; st.rerun()
def next_step(): st.session_state.step += 1; st.rerun()
def prev_step(): st.session_state.step -= 1; st.rerun()
# ==========================================
# 4. موتور پارسر هوشمند (AI Narrative Parser)
# ==========================================
def ai_narrative_parser(text, default_stages):
    text = text.lower()
    extracted_data = []
    
    # 🔴 FIX: اگر در متن عددی نبود، از همان عدد منوی UI (default_stages) استفاده می‌کند
    stages = default_stages
    if "2" in text or "two" in text or "۲" in text: stages = 2
    elif "3" in text or "three" in text or "۳" in text: stages = 3
    elif "5" in text or "five" in text or "۵" in text: stages = 5

    # 🔴 FIX: اضافه شدن کلمات فینگلیش برای تشخیص دقیق
    if "acid" in text or "chemical" in text or "اسید" in text or "asid" in text:
        extracted_data.append(("SFX ARC [Chemical Burns]", SFX_STAGES["Chemical Burns (Acid-Type Simulation)"]))
    elif "burn" in text or "fire" in text or "سوختگی" in text or "آتش" in text or "sukhtegi" in text or "atash" in text:
        extracted_data.append(("SFX ARC [First & Second Degree Burns]", SFX_STAGES["First & Second Degree Burns"]))
    elif "bruise" in text or "punch" in text or "کبودی" in text or "مشت" in text or "kabudi" in text or "mosht" in text:
        extracted_data.append(("SFX ARC [Bruises]", SFX_STAGES["Bruises"]))
    elif "sword" in text or "slash" in text or "cut" in text or "شمشیر" in text or "زخم" in text or "zakhm" in text:
        extracted_data.append(("SFX ARC [Abrasions]", SFX_STAGES["Abrasions"]))

    if "age" in text or "old" in text or "years" in text or "پیر" in text or "سن" in text or "pir" in text or "sen" in text:
        extracted_data.append(("AGING ARC [Volume & Sagging]", AGING_STAGES["Volume & Sagging"]))

    if "vitiligo" in text or "پیسی" in text or "pisi" in text:
        extracted_data.append(("PIGMENTATION ARC [Vitiligo]", PIGMENT_STAGES["Vitiligo"]))
    elif "freckle" in text or "کک" in text or "مک" in text or "kak" in text or "mak" in text:
        extracted_data.append(("PIGMENTATION ARC [Freckles]", PIGMENT_STAGES["Freckles"]))
        
    return stages, extracted_data
# ==========================================
# 5. موتور پردازش نهایی پرامپت (Strict Formula Mode)
# ==========================================
def generate_prompt(draft):
    uona_signature = "Uona Studio Signature (Scientific Makeup Design)."
    tech_specs = f"[Fixed Technical: {draft.get('cam')}, {draft.get('light')}, {draft.get('size')}]."
    
    act_str = "VISUAL GUIDE: Use facial structure of attached subject. " if draft.get('actor') == "Yes" else ""
    nat_desc = NAT_DESC.get(draft.get('nat'), "")
    era_desc = ERA_DESC.get(draft.get('era'), "")
    groom_val = draft.get('groom', 'Clean Shaven')
    groom_desc = GROOM_DESC.get(groom_val, "")
    
    identity = f"Character Identity: {draft.get('gen')}, Base Age {draft.get('age')}, Nationality: {draft.get('nat')} ({nat_desc}), Type: {draft.get('char')}, Era: {era_desc}. "
    appearance = f"Grooming/Appearance: {groom_val} ({groom_desc}), Hair Color: {draft.get('h_col')}, Texture: {draft.get('h_tex')}. "
    mat_finish = f"Material Finish: {MAT_DESC.get(draft.get('mat'), '')}. " if draft.get('mat') != "None" else ""
    
    char_base = f"[{act_str}{identity}{appearance}{mat_finish}]"
    
    dynamic_stage = ""
    scenario = draft.get('scenario_text', '').strip()
    is_ui_active = (draft.get('arc_aging', 'None') != "None") or (draft.get('arc_sfx', 'None') != "None") or (draft.get('arc_pigment', 'None') != "None")
    
    ui_stages = draft.get('arc_stages', 4) 
    
    if scenario:
        parsed_stages, extracted_db = ai_narrative_parser(scenario, ui_stages)
        
        if extracted_db:
            dynamic_stage = f"[HORIZONTAL SEQUENCE ARC. {parsed_stages} stages separated by 1px white line. "
            for arc_title, arc_details in extracted_db:
                sliced_details = arc_details[:parsed_stages] if len(arc_details) >= parsed_stages else arc_details
                dynamic_stage += f"SYSTEM APPLIED {arc_title}: " + ", ".join([f"Stage {i+1} ({d})" for i, d in enumerate(sliced_details)]) + ". "
            
            # 🔴 FIX: اضافه کردن خط زمانی داستان کاربر به استیج‌های دیتابیس برای SFX و زمان‌بندی
            dynamic_stage += f"NARRATIVE TIMELINE CONTEXT: Evolve the physical traits and SFX strictly based on this chronological timeline: '{scenario}'. "
            dynamic_stage += "CRITICAL: Underlying facial identity MUST remain 100% identical across all panels.]"
        else:
            dynamic_stage = f"[HORIZONTAL SEQUENCE ARC. {parsed_stages} stages separated by 1px white line. NARRATIVE TRANSFORMATION: '{scenario}'. Extract biological aging, SFX evolution, and grooming dynamically based on this narrative. CRITICAL: Underlying facial identity MUST remain 100% identical across all panels.]"
            
    elif is_ui_active:
        stages_count = ui_stages
        dynamic_stage = f"[HORIZONTAL SEQUENCE ARC. {stages_count} stages separated by 1px white line. "
        
        if draft.get('arc_aging', 'None') != "None":
            aging_arr = AGING_STAGES.get(draft.get('arc_aging'), [])
            sliced = aging_arr[:stages_count] if aging_arr else []
            dynamic_stage += f"SCIENTIFIC AGING LOGIC: {draft.get('arc_aging')} (" + ", ".join(sliced) + "). "
        if draft.get('arc_sfx', 'None') != "None":
            sfx_arr = SFX_STAGES.get(draft.get('arc_sfx'), [])
            sliced = sfx_arr[:stages_count] if sfx_arr else []
            dynamic_stage += f"SFX TRAUMA ARC: {draft.get('arc_sfx')} (" + ", ".join(sliced) + "). "
        if draft.get('arc_pigment', 'None') != "None":
            pig_arr = PIGMENT_STAGES.get(draft.get('arc_pigment'), [])
            sliced = pig_arr[:stages_count] if pig_arr else []
            dynamic_stage += f"PIGMENTATION ARC: {draft.get('arc_pigment')} (" + ", ".join(sliced) + "). "
            
        dynamic_stage += "CRITICAL: Underlying facial identity MUST remain 100% identical across all panels.]"
        
    else:
        base_sfx = SFX_DESC.get(draft.get('sfx'), draft.get('sfx')) if draft.get('sfx') != "None" else ""
        dynamic_stage = f"[Single Shot Portrait. CINEMATIC PROSTHETIC STUDY: Apply {base_sfx} as a makeup layer.]" if base_sfx else "[Single Shot Portrait.]"

    final_prompt = f"{uona_signature} {tech_specs} {char_base} {dynamic_stage} 8k, hyper-realistic, subsurface scattering, focus on prosthetic makeup accuracy."
    return " ".join(final_prompt.split())
# ==========================================
# 6. موتور استایل (CSS Engine)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%); height: 100vh; overflow-x: hidden; }
    #MainMenu, footer, header {visibility: hidden;} .stDeployButton {display:none;}
    div.element-container:has(.logo-marker) + div.element-container button { background-color: transparent !important; border: none !important; box-shadow: none !important; padding: 0 !important; height: auto !important; display: flex !important; justify-content: flex-start !important; }
    div.element-container:has(.logo-marker) + div.element-container button p { color: #00f2ff !important; font-family: 'Cinzel', serif !important; font-size: 1.5rem !important; font-weight: 900 !important; margin: 0 !important; padding: 0 !important; text-transform: uppercase !important; transition: all 0.3s ease !important; }
    div.element-container:has(.logo-marker) + div.element-container button:hover p { color: #ffffff !important; text-shadow: 0 0 15px #00f2ff !important; transform: scale(1.02) !important; }
    .title-main { font-family: 'Cinzel'; color: #ffffff !important; font-size: 2.5rem; font-weight: 800; letter-spacing: 10px; margin: 0; text-shadow: 0 0 15px rgba(0, 242, 255, 0.5); }
    .subtitle { color: #00f2ff; font-family: 'Montserrat'; font-size: 0.8rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 30px;}
    label, .stMarkdown p { color: #00e5ff !important; font-family: 'Montserrat' !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.75rem !important; }
    div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div { background-color: rgba(0, 20, 40, 0.9) !important; border: 1px solid rgba(0, 242, 255, 0.4) !important; border-radius: 10px !important; }
    div[data-baseweb="input"] input, div[data-baseweb="select"], div[data-baseweb="slider"], textarea { color: #ffffff !important; font-weight: bold !important; font-family: 'Montserrat', sans-serif !important; }
    .stButton > button { border: none !important; border-radius: 8px !important; font-family: 'Cinzel', serif !important; font-weight: 900 !important; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; background-color: #00f2ff !important; color: #000000 !important; box-shadow: 0 0 10px rgba(0, 242, 255, 0.3); }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.02); box-shadow: 0 0 20px #00f2ff;}
    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 25px; backdrop-filter: blur(10px); margin-bottom: 20px; }
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 30px; color: #4a5d73; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 900; }
    .step-active { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }
    div[data-testid="stExpander"] { background: rgba(10, 25, 47, 0.6) !important; border: 1px solid rgba(0, 242, 255, 0.2) !important; border-radius: 12px !important; backdrop-filter: blur(10px); margin-bottom: 15px; transition: all 0.3s ease; }
    div[data-testid="stExpander"] summary { padding: 15px !important; }
    div[data-testid="stExpander"] summary p { color: #ffffff !important; font-family: 'Montserrat' !important; font-size: 0.9rem !important; letter-spacing: 1px; font-weight: bold !important; text-transform: uppercase !important; }
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
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px;'>RESTRICTED ACCESS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#7b8ea8; font-family:Montserrat; font-size:0.8rem; margin-bottom:20px;'>Authorized Personnel Only. Please login to access UONA STUDIO.</p>", unsafe_allow_html=True)
        
        u_name = st.text_input("USERNAME", placeholder="Enter your credentials...")
        u_pass = st.text_input("PASSWORD", type="password", placeholder="Enter your password...")
        users = load_json(DB_FILE, {})
        
        if st.button("AUTHENTICATE", use_container_width=True):
            if u_name == ADMIN_USER and u_pass == ADMIN_PASS:
                st.session_state.auth = True; st.session_state.user = u_name; st.session_state.is_admin = True; st.session_state.plan = "MASTER APEX"
                go_to('admin_panel')
            elif u_name in users:
                user_data = users[u_name]
                db_pass = user_data if isinstance(user_data, str) else user_data.get("pass", "")
                db_plan = "UONA Core" if isinstance(user_data, str) else user_data.get("plan", "UONA Core")
                
                if db_pass == u_pass:
                    st.session_state.auth = True; st.session_state.user = u_name; st.session_state.is_admin = False; st.session_state.plan = db_plan
                    go_to('dashboard')
                else: st.error("ACCESS DENIED: Invalid Password.")
            else: st.error("ACCESS DENIED: Unregistered Account.")
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
# ROUTES: ADMIN, DASHBOARD, LIBRARY, SETTINGS
# ==========================================
if st.session_state.route == 'admin_panel':
    if not st.session_state.is_admin: go_to('dashboard')
    st.markdown("<h2 class='title-main' style='color:#ff00aa!important;'>MASTER CONTROL PANEL</h2>", unsafe_allow_html=True)
    users = load_json(DB_FILE, {})
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        new_u = st.text_input("New Client Username")
        new_p = st.text_input("New Client Password")
        new_plan = st.selectbox("Assign Subscription Tier", ["UONA Core", "UONA Apex"])
        if st.button("CREATE CLIENT ACCOUNT", use_container_width=True):
            if new_u and new_p and new_u != ADMIN_USER:
                users[new_u] = {"pass": new_p, "plan": new_plan}; save_json(DB_FILE, users); st.success("Created!"); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        for usr, data in users.items():
            plan_val = "UONA Core" if isinstance(data, str) else data.get("plan", "UONA Core")
            col_name, col_plan, col_btn = st.columns([2, 2, 1])
            col_name.write(f"👤 {usr}"); col_plan.write(f"💎 {plan_val}")
            if col_btn.button("REVOKE", key=f"del_{usr}"): del users[usr]; save_json(DB_FILE, users); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.route == 'dashboard':
    bg = find_bg_file()
    if bg: add_bg_from_local(bg)
    st.markdown("<h2 style='color:#fff; font-family:Cinzel; text-align:center;'>CONTROL CENTER</h2><div class='subtitle' style='text-align:center;'>Select a module to begin</div>", unsafe_allow_html=True)
    if st.session_state.is_admin:
        if st.button("⚙️ RETURN TO ADMIN PANEL"): go_to('admin_panel')
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>🎬</h1><h3>NEW CHARACTER</h3></div>', unsafe_allow_html=True)
        if st.button("START PROJECT", key="b1", use_container_width=True): st.session_state.step = 1; go_to('builder')
    with c2:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>📂</h1><h3>LIBRARY</h3></div>', unsafe_allow_html=True)
        if st.button("OPEN LIBRARY", key="b2", use_container_width=True): go_to('library')
    with c3:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>⚙️</h1><h3>SETTINGS</h3></div>', unsafe_allow_html=True)
        if st.button("OPEN SETTINGS", key="b3", use_container_width=True): go_to('settings')

elif st.session_state.route == 'library':
    st.markdown("<h2 class='title-main'>PROJECT LIBRARY</h2>", unsafe_allow_html=True)
    projects = load_json(PROJ_FILE, [])
    for p in [p for p in projects if p.get("user") == st.session_state.user]:
        with st.expander(f"📁 PROJECT LOG | {p['date']}"): st.code(p['prompt'], language="markdown")

elif st.session_state.route == 'settings':
    st.markdown("<h2 class='title-main'>SYSTEM SETTINGS</h2>", unsafe_allow_html=True)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.selectbox("Default AI Engine", ["Midjourney V6", "Gemini Pro Vision", "Stable Diffusion XL"])
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 🔴 ROUTE 3: CHARACTER BUILDER 🔴
# ==========================================
elif st.session_state.route == 'builder':
    st.markdown(f"""
        <div class="step-indicator">
            <span class="{'step-active' if st.session_state.step==1 else ''}">1. FULL BASELINE</span> ➔
            <span class="{'step-active' if st.session_state.step==2 else ''}">2. ARC CONFIG (V2.0 SYSTEM)</span> ➔
            <span class="{'step-active' if st.session_state.step==3 else ''}">3. REVIEW</span>
        </div>
    """, unsafe_allow_html=True)
    
    d = st.session_state.draft

    # --- Phase 1: FULL BASELINE ---
    if st.session_state.step == 1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>Phase 1: Complete Baseline Architecture</h3>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<p style='color:#ffaa00;'>💠 IDENTITY & CORE</p>", unsafe_allow_html=True)
            d['actor'] = st.selectbox("Actor Reference", ["None", "Yes", "No"], index=["None", "Yes", "No"].index(d.get('actor', "None")))
            d['gen'] = st.selectbox("GENDER", GENDER_LIST, index=GENDER_LIST.index(d.get('gen', GENDER_LIST[0])) if d.get('gen') in GENDER_LIST else 0)
            d['age'] = st.selectbox("BASE AGE", AGE_LIST, index=AGE_LIST.index(d.get('age', AGE_LIST[0])) if d.get('age') in AGE_LIST else 0)
            d['nat'] = st.selectbox("NATIONALITY", list(NAT_DESC.keys()), index=list(NAT_DESC.keys()).index(d.get('nat', 'Iranian')) if d.get('nat') in NAT_DESC else 0)
            d['era'] = st.selectbox("ERA / PERIOD", list(ERA_DESC.keys()), index=list(ERA_DESC.keys()).index(d.get('era', list(ERA_DESC.keys())[0])) if d.get('era') in ERA_DESC else 0)

        with c2:
            st.markdown("<p style='color:#ffaa00;'>💠 APPEARANCE & STYLING</p>", unsafe_allow_html=True)
            d['char'] = st.selectbox("CHARACTER TYPE", list(CONCEPTS.keys()), index=list(CONCEPTS.keys()).index(d.get('char', 'Average Citizen')) if d.get('char') in CONCEPTS else 0)
            d['groom'] = st.selectbox("GROOMING", list(GROOM_DESC.keys()), index=list(GROOM_DESC.keys()).index(d.get('groom', "Clean Shaven")) if d.get('groom') in GROOM_DESC else 0)
            d['h_col'] = st.selectbox("HAIR COLOR", list(HAIR_COLORS.keys()), index=list(HAIR_COLORS.keys()).index(d.get('h_col', list(HAIR_COLORS.keys())[0])) if d.get('h_col') in HAIR_COLORS else 0)
            d['h_tex'] = st.selectbox("HAIR TEXTURE", list(HAIR_TEX_DESC.keys()), index=list(HAIR_TEX_DESC.keys()).index(d.get('h_tex', list(HAIR_TEX_DESC.keys())[0])) if d.get('h_tex') in HAIR_TEX_DESC else 0)
            d['mat'] = st.selectbox("MATERIAL FINISH", list(MAT_DESC.keys()), index=list(MAT_DESC.keys()).index(d.get('mat', 'None')) if d.get('mat') in MAT_DESC else 0)

        with c3:
            st.markdown("<p style='color:#ffaa00;'>💠 BASE SFX & TECHNICAL</p>", unsafe_allow_html=True)
            sfx_opts = ["None"] + list(SFX_DESC.keys())
            d['sfx'] = st.selectbox("BASE TRAUMA / SFX", sfx_opts, index=sfx_opts.index(d.get('sfx', "None")) if d.get('sfx') in sfx_opts else 0)
            d['cam'] = st.selectbox("CAMERA LENS", list(CAM_DESC.keys()), index=list(CAM_DESC.keys()).index(d.get('cam', list(CAM_DESC.keys())[0])) if d.get('cam') in CAM_DESC else 0)
            d['light'] = st.selectbox("CINEMATIC LIGHTING", list(LIGHT_DESC.keys()), index=list(LIGHT_DESC.keys()).index(d.get('light', list(LIGHT_DESC.keys())[0])) if d.get('light') in LIGHT_DESC else 0)
            d['size'] = st.selectbox("ASPECT RATIO", SIZE_LIST, index=SIZE_LIST.index(d.get('size', SIZE_LIST[0])) if d.get('size') in SIZE_LIST else 0)
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("NEXT: ARC CONFIGURATION ➔", use_container_width=True): next_step()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Phase 2: ARC CONFIG ---
    elif st.session_state.step == 2:
        age_val = d.get('age', AGE_LIST[2])
        is_under_22 = AGE_LIST.index(age_val) < 2 if age_val in AGE_LIST else False
        is_female = d.get('gen') in ["Feminine / Female", "Female"]

        c_left, c_center, c_right = st.columns([3, 4.5, 2.5], gap="medium")

        # 1. پنل چپ: DNA قفل شده
        with c_left:
            st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%;">', unsafe_allow_html=True)
            st.markdown("<h4 style='color:#00f2ff; font-family:Cinzel;'>🔒 CHARACTER DNA</h4>", unsafe_allow_html=True)
            st.info(f"**Gender:** {d.get('gen')}\n\n**Age:** {d.get('age')}\n\n**Nat:** {d.get('nat')}\n\n**Type:** {d.get('char')}")
            st.markdown("<div style='padding: 10px; background: rgba(0,242,255,0.1); border-left: 3px solid #00f2ff; color: #00f2ff; font-size: 0.75rem;'>🔒 Identity Locked.<br>Base parameters are preserved for continuous execution.</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 2. پنل وسط: پیش‌نمایش
        with c_center:
            st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%; display: flex; flex-direction: column;">', unsafe_allow_html=True)
            st.markdown("<div style='flex-grow: 1; border: 1px solid rgba(0,242,255,0.3); border-radius: 10px; background: #02060c; position:relative; overflow: hidden; display:flex; justify-content:center; align-items:center; min-height: 350px;'>", unsafe_allow_html=True)
            
            st.markdown("""
            <div style='position:absolute; top: 10px; left: 15px; display: flex; flex-direction: column; gap: 5px;'>
                <span style='color:#00f2ff; font-size:0.65rem; background: rgba(0,0,0,0.6); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(0,242,255,0.3);'>🟢 Identity Engine Active</span>
                <span style='color:#00f2ff; font-size:0.65rem; background: rgba(0,0,0,0.6); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(0,242,255,0.3);'>🔒 Biometric Continuity Locked</span>
                <span style='color:#00f2ff; font-size:0.65rem; background: rgba(0,0,0,0.6); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(0,242,255,0.3);'>⚡ Material Simulation Running</span>
            </div>
            """, unsafe_allow_html=True)

            if os.path.exists("portrait_clean.PNG"): st.image("portrait_clean.PNG", use_container_width=True)
            else: st.markdown("<h3 style='color:rgba(255,255,255,0.1);'>[ 4:5 LIVE PORTRAIT FRAME ]</h3>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("""
            <div style='display: flex; justify-content: space-between; align-items: center; margin-top: 15px; padding: 10px; background: rgba(0,242,255,0.05); border-radius: 8px;'>
                <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.7rem; font-weight:bold;'>INITIAL</span></div>
                <div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(0,242,255,0.5) 0%, rgba(255,255,255,0.2) 100%); margin: 0 10px;'></div>
                <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.7rem; font-weight:bold;'>SPREAD</span></div>
                <div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(0,242,255,0.5) 0%, rgba(255,255,255,0.2) 100%); margin: 0 10px;'></div>
                <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.7rem; font-weight:bold;'>DAMAGE</span></div>
                <div style='flex-grow: 1; height: 2px; background: linear-gradient(90deg, rgba(0,242,255,0.5) 0%, rgba(255,255,255,0.2) 100%); margin: 0 10px;'></div>
                <div style='text-align:center;'><span style='color:#00f2ff; font-size:0.7rem; font-weight:bold;'>FINAL</span></div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            c_btn1, c_btn2 = st.columns(2)
            if c_btn1.button("⬅ BACK", use_container_width=True): prev_step()
            if c_btn2.button("NEXT: REVIEW ➔", use_container_width=True): next_step()
            st.markdown('</div>', unsafe_allow_html=True)

        # 3. پنل راست: دیتابیس‌های تخصصی
        with c_right:
            st.markdown('<div class="glass-panel" style="padding: 20px; height: 100%; overflow-y: auto;">', unsafe_allow_html=True)
            st.markdown("<h4 style='color:#ffaa00; font-family:Cinzel;'>⚙️ TRANSFORMATION ENGINE</h4>", unsafe_allow_html=True)
            
            if st.session_state.plan == "UONA Core":
                st.markdown("""
                <div style='margin-top: 20px; padding: 15px; background: rgba(255, 170, 0, 0.05); border: 1px solid rgba(255, 170, 0, 0.3); border-radius: 8px; text-align: center;'>
                    <span style='font-size: 2rem;'>🔒</span><br>
                    <b style='color: #ffaa00; font-size: 0.85rem; text-transform: uppercase;'>Premium Feature</b>
                    <p style='color: #888; font-size: 0.7rem;'>Arc Modules require Apex tier.</p>
                </div>
                """, unsafe_allow_html=True)
                d['arc_stages'] = 4
                d['arc_aging'] = "None"; d['arc_sfx'] = "None"; d['arc_pigment'] = "None"; d['bio_fatigue'] = False; d['bio_lips'] = False; d['scenario_text'] = ""
            else:
                d['arc_stages'] = st.slider("NUMBER OF STAGES", 2, 5, d.get('arc_stages', 4))
                
                with st.expander("A. AGING ENGINE", expanded=True):
                    d['arc_aging'] = st.selectbox("Aging Categories", ["None", "Wrinkles", "Volume & Sagging", "Skin Texture & Pigmentation", "Hair & Brows"])
                    if d['arc_aging'] != "None":
                        aging_stages = AGING_STAGES.get(d['arc_aging'], ["Stage 1", "Stage 2", "Stage 3", "Stage 4"])
                        d['arc_aging_stage'] = st.selectbox("Select Stage", ["All Stages (Progression Arc)"] + aging_stages)
                
                with st.expander("B. SFX & TRAUMA ENGINE", expanded=True):
                    if is_under_22:
                        st.markdown("<div style='padding: 5px; border-left: 3px solid red; color: #aaa; font-size: 0.7rem;'>🔒 SFX Locked (Age Constraint)</div>", unsafe_allow_html=True)
                        d['arc_sfx'] = "None"
                    else:
                        sfx_v2_opts = ["None", "Bruises", "Contusions", "Abrasions", "First & Second Degree Burns", "Chemical Burns (Acid-Type Simulation)", "Keloids (Fibrotic Overgrowth)"]
                        d['arc_sfx'] = st.selectbox("Trauma Simulation", sfx_v2_opts)
                        if d['arc_sfx'] != "None":
                            sfx_stages = SFX_STAGES.get(d['arc_sfx'], ["Stage 1", "Stage 2", "Stage 3", "Stage 4"])
                            d['arc_sfx_stage'] = st.selectbox("Select Stage", ["All Stages (Progression Arc)"] + sfx_stages)
                        
                with st.expander("C. PIGMENTATION ARC", expanded=True):
                    pigment_opts = ["None", "Vitiligo", "Melasma & Hyperpigmentation", "Freckles"]
                    d['arc_pigment'] = st.selectbox("Skin Pigmentation", pigment_opts)
                    if d['arc_pigment'] != "None":
                        pig_stages = PIGMENT_STAGES.get(d['arc_pigment'], ["Stage 1", "Stage 2", "Stage 3", "Stage 4"])
                        d['arc_pigment_stage'] = st.selectbox("Select Stage", ["All Stages (Progression Arc)"] + pig_stages)
                    
                with st.expander("D. BIOLOGICAL DETAILS", expanded=False):
                    d['bio_fatigue'] = st.checkbox("Fatigue & Sallow Skin", value=d.get('bio_fatigue', False))
                    d['bio_lips'] = st.checkbox("Lips Volume Loss", value=d.get('bio_lips', False))
                
                d['scenario_text'] = st.text_area("NARRATIVE (OPTIONAL)", value=d.get('scenario_text', ''), placeholder="e.g. A 40-year-old man with a deep wound, aging to 80...")

            if is_female or is_under_22: 
                f_text = "🔒 Constraints Safely Enforced"
                f_color = "#00f2ff"
            elif d['arc_sfx'] != "None" and d['arc_aging'] != "None":
                f_text = "⚠️ Arc Conflict Detected"
                f_color = "#ffaa00"
            else: 
                f_text = "✅ Continuity Preserved"
                f_color = "#00ffaa"
                
            st.markdown(f"<div style='margin-top: 15px; padding: 10px; border-left: 3px solid {f_color}; color: {f_color}; font-size: 0.7rem;'>{f_text}</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- Phase 3: REVIEW ---
    elif st.session_state.step == 3:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>Phase 3: Logic Engine Output</h3>", unsafe_allow_html=True)
        final_prompt = generate_prompt(d)
        st.info(final_prompt)
        
        st.markdown("<br>", unsafe_allow_html=True)
        c_btn1, c_btn2 = st.columns(2)
        if c_btn1.button("⬅ EDIT PARAMETERS", use_container_width=True): prev_step()
        if c_btn2.button("PROCEED TO SIMULATION 🚀", use_container_width=True): go_to('simulation')
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 4 & 5: SIMULATION AND ENGINE
# ==========================================
elif st.session_state.route == 'simulation':
    st.markdown("<h2 class='title-main'>VISUAL SIMULATION</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown('<div style="background:#0a192f; height:200px; border-radius:15px; border:1px dashed #00f2ff; display:flex; align-items:center; justify-content:center; flex-direction:column; margin-bottom:20px;"><h1 style="color:#00f2ff; opacity:0.5;">👁️</h1><p style="color:#00f2ff; opacity:0.7; font-family:Montserrat;">LIVE PREVIEW FEED</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        if st.button("⬅ BACK TO BUILDER", use_container_width=True): go_to('builder')
        if st.button("⚡ GENERATE PROMPT", use_container_width=True): go_to('prompt_engine')
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.route == 'prompt_engine':
    st.markdown("<h2 class='title-main'>PROMPT ENGINE</h2>", unsafe_allow_html=True)
    final_p = generate_prompt(st.session_state.draft)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.text_area("MASTER PROMPT", value=final_p, height=200)
    c1, c2 = st.columns(2)
    if c1.button("⬅ BACK TO SIMULATION", use_container_width=True): go_to('simulation')
    if c2.button("💾 SAVE TO LIBRARY", use_container_width=True):
        projects = load_json(PROJ_FILE, [])
        projects.insert(0, {"user": st.session_state.user, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "prompt": final_p})
        save_json(PROJ_FILE, projects)
        st.success("Saved to Library!")
    st.markdown('</div>', unsafe_allow_html=True)
