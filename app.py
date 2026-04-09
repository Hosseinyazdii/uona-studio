import streamlit as st

# تنظیمات پایه
st.set_page_config(page_title="UONA STUDIO | AI DASHBOARD", layout="wide")

# استایل سینماتیک و بک‌گراند اختصاصی
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700;900&display=swap');
    
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?q=80&w=2342");
        background-size: cover; background-attachment: fixed;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(5, 15, 26, 0.88); z-index: -1;
    }
    .header-box {
        background: rgba(0, 212, 255, 0.05); backdrop-filter: blur(10px);
        border-bottom: 2px solid #00d4ff; padding: 20px; margin-bottom: 30px; text-align: center;
    }
    .header-title {
        color: #00d4ff; font-family: 'Cinzel', serif; font-size: 2.2rem; letter-spacing: 6px;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5); margin: 0;
    }
    label p { color: #00d4ff !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; text-transform: uppercase !important; }
    
    /* کادر سفید Master Prompt مشابه اکسل */
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 12px; font-weight: 900; font-size: 1.4rem; border-radius: 8px 8px 0 0; text-align: center; }
    .master-box { background-color: #ffffff; color: #111; padding: 25px; border-radius: 0 0 8px 8px; border-left: 8px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.7; min-height: 450px; box-shadow: 0 15px 40px rgba(0,0,0,0.5); }
    
    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO | AI DASHBOARD</p></div>', unsafe_allow_html=True)

# --- دیتابیس‌های استخراج شده از اکسل ---
nationalities = {
    "Iranian": "standard features", "Egyptian": "North African features", "Emirati": "Gulf Arab features", 
    "Saudi": "Peninsular Arab features", "Kuwaiti": "Northern Gulf features", "Syrian": "Levantine features",
    "American": "Diverse North American features", "Indian": "South Asian features", "Chinese": "East Asian features",
    "African": "Sub-Saharan features", "European": "Caucasian features", "Turkish": "Eurasian features"
}

eras = {
    "Contemporary / Modern Day": "Current lighting", "Stone Age / Prehistoric": "Primitive textures", 
    "BCE (Before Common Era)": "Ancient civilization styling", "Ancient Era (Hellenistic/Roman)": "Classical features",
    "Medieval / Dark Ages": "Gritty textures", "100 Years Ago (Roaring 20s)": "Vintage aesthetic"
}

# --- چیدمان داشبورد ---
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actor Reference:", ["No", "Yes"])
        age = st.selectbox("🟡 Age:", ["Elderly / Senior", "Middle-aged", "Young Adult", "Adolescent / Teenager", "Child / Pre-adolescent"])
    with r1c2:
        gender = st.selectbox("🟡 Gender:", ["Masculine / Male", "Feminine / Female", "Androgynous"])
        nat_choice = st.selectbox("🟡 Nationality:", list(nationalities.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era_choice = st.selectbox("Time Period:", list(eras.keys()))
        hair_color = st.text_input("Hair & Beard Color:", "Black / Salt & Pepper")
    with r2c2:
        char_type = st.selectbox("Character Type:", ["Heroic Warrior", "Sinister Villain", "Royal / Aristocratic", "Scholar / Intellectual"])
        grooming = st.selectbox("Grooming Style:", ["Viking Beard", "Saudi Anchor Beard", "Pyramidal Moustache", "Clean Shaven", "Heavy Stubble"])

    st.markdown("<br>", unsafe_allow_html=True)

    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx = st.selectbox("SFX Makeup:", ["3-Day Old Wound (Scabbing)", "Fresh Katana/Sword Slash", "Burn Scar", "None"])
        aging = st.text_input("Aging Details:", "Frontal Rhytids (Forehead Furrows)")
        lighting = st.selectbox("Lighting:", ["Rembrandt Lighting", "Cinematic Golden Hour", "Cinematic Rim Light"])
    with r3c2:
        material = st.text_input("Material:", "Matte Sealer")
        hair_tex = st.selectbox("Hair Texture:", ["Coarse & Wiry", "Afro-Textured", "Wavy (Type 2)", "Straight (Sleek)"])
        canvas = st.selectbox("Bible Size:", ["Aspect Ratio 16:9 (Widescreen)", "Aspect Ratio 1:1 (Square)", "Aspect Ratio 2.39:1 (Anamorphic)"])

    camera = st.selectbox("Camera & Lens:", ["85mm Lens, Three-Quarter View", "100mm Macro Lens, Extreme Close-Up", "50mm Lens, Dutch Angle"])

# --- منطق ساخت Master Prompt (دقیقاً طبق فرمول اکسل تو) ---
nat_desc = nationalities[nat_choice]
era_desc = eras[era_choice]
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
sfx_desc = f"[CINEMATIC PROSTHETIC STUDY: Apply {sfx} SFX as a makeup layer]. " if sfx != "None" else ""

final_prompt = f"{visual_guide}A professional cinematic {canvas} portrait of a {gender} {age} {nat_choice} ({nat_desc}) from the {era_choice} ({era_desc}) era. " \
               f"Character style: {char_type}. Grooming: {grooming}. Hair Texture: {hair_tex}. " \
               f"Skin: {aging}. {sfx_desc}Technical: Lighting: {lighting}, Lens: {camera}, 8k, subsurface scattering, raw photography, no-retouch, focus on prosthetic makeup accuracy."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00d4ff; font-size:0.8rem; margin-top:10px;'>لطفاً برای کپی کردن، متن داخل کادر سفید را انتخاب کنید</p>", unsafe_allow_html=True)
