import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA STUDIO | AI DASHBOARD", layout="wide")

# استایل سینماتیک، بک‌گراند و رفع اسکرول
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?q=80&w=2342");
        background-size: cover; background-attachment: fixed;
        overflow-y: auto !important;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(5, 15, 26, 0.88); z-index: -1;
    }
    .header-box {
        background: rgba(0, 212, 255, 0.05); backdrop-filter: blur(10px);
        border-bottom: 2px solid #00d4ff; padding: 25px; margin-bottom: 35px; text-align: center;
    }
    .header-title {
        color: #00d4ff; font-family: 'Cinzel', serif; font-size: 2.5rem; letter-spacing: 8px;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5); margin: 0;
    }
    label p { color: #00d4ff !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; text-transform: uppercase !important; }
    
    /* کادر سفید Master Prompt */
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 15px; font-weight: 900; font-size: 1.5rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 30px; border-radius: 0 0 8px 8px; border-left: 10px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.2rem; line-height: 1.8; min-height: 500px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); user-select: all !important; }
    
    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO | PROMPT BUILDER</p></div>', unsafe_allow_html=True)

# --- دیتابیس‌های استخراج شده از شیت‌های اکسل (Full Data) ---

# شیت Nationality
nationalities = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure",
    "Syrian": "Levantine features, straight profile",
    "American": "Diverse North American features, varied facial structures",
    "Indian": "South Asian features, deep-set dark eyes, rich warm undertones",
    "Chinese": "East Asian features, high cheekbones, smooth skin",
    "African": "Sub-Saharan features, broad nasal structure, deep melanated skin",
    "European": "Caucasian features, varied eye colors, fair complexion",
    "Turkish": "Eurasian features, strong facial contours, medium olive skin"
}

# شیت Time Period
eras = {
    "Contemporary / Modern Day": "Current lighting, sharp details",
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures",
    "BCE (Before Common Era)": "Ancient civilization styling",
    "Pre-Islamic Era": "Traditional regional heritage, antique textures",
    "Ancient Era (Hellenistic/Roman)": "Classical features, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures",
    "200 Years Ago": "Regency style, era-specific grooming",
    "150 Years Ago": "Formal, structured, refined textures",
    "100 Years Ago": "Vintage aesthetic, early 20th-century grooming",
    "50 Years Ago": "Analog film look, warm hues",
    "Futuristic / Cyberpunk": "Neon accents, high-tech glow",
    "Post-Apocalyptic": "Dirty, weathered, distressed textures"
}

# شیت Character Type
char_types = {
    "Heroic Warrior": "Strong jawline, confident gaze",
    "Sinister Villain": "Harsh shadows, menacing expression",
    "Scholar / Intellectual": "Refined appearance, focused eyes",
    "Royal / Aristocratic": "Elegant posture, pristine skin",
    "Mercenary / Outlaw": "Rugged, weathered, scars",
    "Mystic / Shaman": "Otherworldly look, spiritual paint",
    "Elite Athlete": "Defined muscularity, sweat detail",
    "Bohemian Artist": "Creative styling, messy hair",
    "High-fashion Model": "Angular features, flawless skin",
    "Retiree / Grandparent": "Dignified aging, wisdom-filled gaze"
}

# شیت Grooming
grooming_styles = {
    "Saudi Anchor Beard": "sharp and angled form connected to chin",
    "Pyramidal Moustache": "wide base with narrow top mustache",
    "Clean Shaven": "smooth skin, no stubble",
    "Light Stubble": "very short even stubble",
    "Heavy Stubble": "thicker rough texture",
    "Designer Stubble": "precisely trimmed sharp edges",
    "Viking Beard": "long, thick, braided or wild growth",
    "Van Dyke": "pointed chin beard, disconnected mustache",
    "Goatee": "chin beard only",
    "Mutton Chops": "wide full sideburns connected to mustache"
}

# شیت SFX & Trauma
sfx_options = {
    "None": "None",
    "Fresh Katana/Sword Slash": "Deep, open edges, active bleeding",
    "Glass Laceration with Shards": "Irregular edges, embedded glass particles",
    "Blunt Force Contusion": "Severe swelling, inflamed redness",
    "3-Day Old Wound (Scabbing)": "Scab formation, dark pink edges",
    "1-Week Old Wound (Granulation)": "Pink tissue, peeling skin",
    "1-Month Old Scar (Maturation)": "Fibrous tissue, recessed area",
    "1-Year Old Keloid Scar": "Raised hypertrophic tissue",
    "Fresh Periorbital Hematoma": "Purple-red bruising, intense inflammation",
    "3-Day Old Bruise (Greenish-Yellow)": "Hemoglobin degradation tones"
}

# شیت Aging
aging_options = [
    "None", "Frontal Rhytids (Forehead Furrows)", "Deep Nasolabial Folds", 
    "Pronounced Crow's Feet", "Hooded Eyelids / Ptosis", "Dermal Crepiness",
    "Visible Liver Spots", "Sagging Jowls & Loose Skin", "Periorbital Hollows", "Age-related Telangiectasia"
]

# شیت Lighting
lighting_styles = [
    "Rembrandt Lighting", "Cinematic Golden Hour", "Chiaroscuro", 
    "Volumetric God Rays", "High-Key Studio Lighting", "Low-Key Moody Lighting",
    "Neon Cyberpunk Rim Light", "Hard Top Lighting", "Teal and Orange Lighting"
]

# شیت Camera & Lens
camera_options = [
    "85mm Lens, Eye-Level Shot", "100mm Macro Lens, Extreme Close-Up", 
    "50mm Lens, Dutch Angle", "35mm Lens, Low-Angle (Hero Shot)", 
    "200mm Telephoto, Profile View", "85mm Lens, Three-Quarter View"
]

# --- چیدمان داشبورد ---
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    # پایه (اجباری)
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actore Reference:", ["No", "Yes"])
        age_choice = st.selectbox("🟡 Age Range:", ["Elderly / Senior", "Middle-aged", "Young Adult", "Adolescent", "Child"])
    with r1c2:
        gender_choice = st.selectbox("🟡 Gender:", ["Masculine / Male", "Feminine / Female", "Androgynous"])
        nat_choice = st.selectbox("🟡 Nationality:", list(nationalities.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    
    # سبک و زمان
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era_choice = st.selectbox("Time Period:", list(eras.keys()))
        hair_color = st.text_input("Hair & Beard Color:", placeholder="Enter color (e.g. 30% Salt and Pepper)")
    with r2c2:
        char_choice = st.selectbox("Character Type:", list(char_types.keys()))
        groom_choice = st.selectbox("Grooming Style:", list(grooming_styles.keys()))

    st.markdown("<br>", unsafe_allow_html=True)

    # فنی و SFX
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx_choice = st.selectbox("SFX Makeup / Trauma:", list(sfx_options.keys()))
        aging_choice = st.selectbox("Aging Details:", aging_options)
        lighting_choice = st.selectbox("Lighting Style:", lighting_styles)
    with r3c2:
        material = st.text_input("Material Finish:", placeholder="e.g. Encapsulated Silicone")
        hair_tex = st.selectbox("Hair Texture:", ["Afro-Textured", "Wavy (Type 2)", "Curly (Type 3)", "Straight", "Coarse & Wiry"])
        canvas = st.selectbox("Bible Size (Aspect Ratio):", ["Aspect Ratio 16:9", "Aspect Ratio 1:1", "Aspect Ratio 2.39:1", "Aspect Ratio 4:5"])

    camera_choice = st.selectbox("Camera, Lens & Angle:", camera_options)

# --- منطق ساخت Master Prompt (فرمول نهایی) ---
nat_desc = nationalities[nat_choice]
era_desc = eras[era_choice]
char_desc = char_types[char_choice]
groom_desc = grooming_styles[groom_choice]
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
sfx_desc = f"[CINEMATIC PROSTHETIC STUDY: Apply {sfx_choice} ({sfx_options[sfx_choice]}) SFX as a makeup layer]. " if sfx_choice != "None" else ""

final_prompt = f"{visual_guide}A professional cinematic {canvas} portrait of a {gender_choice} {age_choice} {nat_choice} ({nat_desc}) from the {era_choice} ({era_desc}). " \
               f"Character Concept: {char_choice} ({char_desc}). Grooming: {groom_choice} ({groom_desc}). Hair Color: {hair_color}, Texture: {hair_tex}. " \
               f"Skin Aging: {aging_choice}. {sfx_desc}Finish Material: {material}. " \
               f"Technical Specs: {lighting_choice}, {camera_choice}, 8k, raw photography, subsurface scattering, extreme detail on prosthetic edges."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; color: #00d4ff; font-family: Montserrat; padding-top: 20px;'>
            <p style='font-size: 0.9rem; opacity: 0.8;'>لطفاً برای کپی کردن، متن داخل کادر سفید را انتخاب کنید</p>
            <p style='font-size: 0.8rem; letter-spacing: 1px;'>CLICK INSIDE THE BOX TO SELECT ALL</p>
        </div>
        """, unsafe_allow_html=True)
