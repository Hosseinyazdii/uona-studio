import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA STUDIO | FULL AI DASHBOARD", layout="wide")

# استایل سینماتیک و بک‌گراند اختصاصی
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
        background: rgba(5, 15, 26, 0.9); z-index: -1;
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
    
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 12px; font-weight: 900; font-size: 1.4rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 25px; border-radius: 0 0 8px 8px; border-left: 10px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.1rem; line-height: 1.7; min-height: 500px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); user-select: all !important; }
    
    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO | MASTER DASHBOARD</p></div>', unsafe_allow_html=True)

# --- استخراج کامل دیتای تمام شیت‌ها ---

genders = {"Masculine / Male": "strong bone structure, wide jawline", "Feminine / Female": "softer facial contours, high forehead", "Androgynous": "blend of masculine and feminine features"}

ages = {
    "Child / Pre-adolescent": "textureless skin, large eyes", "Adolescent / Teenager": "puberty changes, oily skin texture",
    "Young Adult (Early 20s)": "peak skin elasticity and radiance", "Middle-aged (Late 40s)": "initial fat loss and sagging",
    "Elderly / Senior": "complete collagen loss, deep wrinkles", "Ancient / Centenarian": "paper-thin skin, deep age spots"
}

nationalities = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin", "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin", "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure", "Syrian": "Levantine features, straight profile",
    "American": "Diverse North American features", "Indian": "South Asian features, deep-set dark eyes",
    "Chinese": "East Asian features, high cheekbones", "African": "Sub-Saharan features, deep melanated skin",
    "European": "Caucasian features, fair complexion", "Turkish": "Eurasian features, strong contours"
}

eras = {
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures", "BCE (Before Common Era)": "Ancient civilization styling",
    "Pre-Islamic Era": "Traditional regional heritage", "Ancient Era (Hellenistic/Roman)": "Classical features, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures", "200 Years Ago": "Regency style, era-specific grooming",
    "150 Years Ago": "Victorian Era, formal structured textures", "100 Years Ago": "Roaring 20s, vintage aesthetic",
    "50 Years Ago": "1970s Retro, analog film look", "Contemporary / Modern Day": "Current lighting, sharp details",
    "Futuristic / Cyberpunk": "Neon accents, high-tech glow", "Post-Apocalyptic": "Dirty, weathered textures"
}

char_types = {
    "Heroic Warrior": "Strong jawline, confident gaze", "Sinister Villain": "Harsh shadows, menacing expression",
    "Scholar / Intellectual": "Refined appearance, focused eyes", "Royal / Aristocratic": "Elegant posture, luxury textures",
    "Mercenary / Outlaw": "Rugged, weathered, scars", "Mystic / Shaman": "Otherworldly look, spiritual paint",
    "Corporate Executive / CEO": "Clean-cut, authoritative", "Elite Athlete": "Defined muscularity, sweat detail",
    "Bohemian Artist": "Creative styling, messy hair", "Average Citizen": "Naturalistic, candid",
    "Blue-collar / Technician": "Grime, work-worn skin", "Academic Student": "Youthful, inquisitive",
    "High-fashion Model": "Angular features, flawless skin", "Retiree / Grandparent": "Dignified aging",
    "Urban / Street Style": "Modern edge", "Rural / Outdoorsman": "Sun-damaged skin",
    "Red Carpet / Gala Guest": "Glamorous", "Ailing / Sickly": "Pale skin, dark circles"
}

grooming = {
    "Saudi Anchor Beard": "sharp angled form connected to chin", "Pyramidal Moustache": "wide base with narrow top",
    "Clean Shaven": "smooth skin, close-cut finish", "Light Stubble": "short even stubble",
    "Heavy Stubble": "thick rough texture", "Designer Stubble": "precisely trimmed edges",
    "Shadow Fade Beard": "faded sides, smooth gradient", "Goatee (No Mustache)": "chin beard only",
    "Classic Goatee": "chin beard connected to mustache", "Van Dyke": "pointed chin beard, disconnected mustache",
    "Anchor Beard": "pointed chin beard, thin defined mustache", "Short Boxed Beard": "precise square edges",
    "Medium Boxed Beard": "structured clean appearance", "Long Full Beard": "long thick natural growth",
    "Unkempt Beard": "messy growth, random direction", "Scruffy Beard": "patchy, rough, slightly dirty",
    "Medieval Beard": "period-authentic growth", "Philosopher Beard": "long soft texture",
    "Warrior Beard": "thick rugged battle-worn", "Short Sideburns": "above ear level",
    "Mid-Ear Sideburns": "level with tragus", "Long Sideburns": "ear lobe level",
    "Extra-Long Sideburns": "passes ear lobe", "Tapered Length": "gradient faded into skin",
    "Square Sideburns": "horizontal cut bottom", "Pointed Sideburns": "triangle point bottom",
    "Rounded Sideburns": "soft circular finish", "Pencil Sideburns": "ultra-thin line",
    "Flared Sideburns": "widens at base", "Angled Sideburns": "slanted cut bottom", "Mutton Chops": "wide full sideburns"
}

hair_textures = {
    "Afro-Textured": "Kinky-coily patterns, tight structural coils", "Wavy (Type 2)": "Natural S-shape waves, soft luster",
    "Curly (Type 3)": "Defined ringlets, voluminous structure", "Straight (Sleek)": "Linear alignment, silky surface",
    "Coarse & Wiry": "Thick strands, irregular graying", "Fine & Wispy": "Low density, translucent strands",
    "Disheveled & Matted": "Tangled clumps, weathered look", "Braided / Cornrows": "Intricate interlocking patterns"
}

hair_colors = {
    "Jet black": "Jet black beard, natural black", "Deep espresso": "Dark chocolate brown",
    "Light chestnut": "Sandy brown, honey tones", "Ash blonde": "Cool blonde", "Golden blonde": "Warm blonde",
    "10% Salt & Pepper": "sparse white strands", "30% Salt & Pepper": "mixed white strands",
    "50% Salt & Pepper": "even grey mix", "70% Salt & Pepper": "predominantly grey"
}

sfx_trauma = {
    "None": "No trauma", "Fresh Katana Slash": "Deep open edges, active bleeding", "Glass Laceration": "Irregular edges, glass shards",
    "Blunt Force Contusion": "Severe swelling, inflammation", "3-Day Old Wound": "Scabbing, pink edges",
    "1-Week Old Wound": "Granulation tissue, peeling skin", "1-Month Old Scar": "Fibrous tissue, maturation",
    "1-Year Old Keloid Scar": "Raised hypertrophic tissue", "5-Year Old Atrophic Scar": "Pale white, level with skin",
    "Fresh Periorbital Hematoma": "Purple-red bruising, intense inflammation", "24-Hour Old Bruise": "Deep purple and blue",
    "3-Day Old Bruise": "Greenish-yellow tint"
}

aging_details = {
    "None": "no aging", "Deep Nasolabial Folds": "deep smile lines", "Pronounced Crow's Feet": "radial eye wrinkles",
    "Hooded Eyelids": "ptosis, sagging upper lids", "Dermal Crepiness": "paper-like skin texture",
    "Visible Liver Spots": "age-related lentigines", "Sagging Jowls": "loose jawline skin",
    "Frontal Rhytids": "deep forehead furrows", "Periorbital Hollows": "sunken eyes, eye bags",
    "Vertical Lip Lines": "smoker's lines", "Telangiectasia": "visible broken capillaries"
}

lighting = {
    "Rembrandt Lighting": "classic triangle light on cheek", "Cold Rim Lighting": "blue backlight separation",
    "Chiaroscuro": "high contrast shadows", "Teal and Orange": "cinematic color contrast",
    "Volumetric God Rays": "linear light through fog", "Golden Hour": "warm soft sunset light",
    "High-Key Studio": "bright, no shadow", "Low-Key Moody": "dark, mysterious shadows",
    "Neon Cyberpunk": "colorful rim light", "Hard Top Lighting": "harsh shadows under eyes"
}

cameras = {
    "85mm Lens, Eye-Level": "classic portrait, no distortion", "100mm Macro, Close-Up": "extreme skin pore detail",
    "50mm Lens, Dutch Angle": "tilted angle, tension", "35mm Lens, Low-Angle": "hero shot, powerful view",
    "24mm Wide-Angle": "high-angle, distorted features", "200mm Telephoto": "bokeh background, compressed face",
    "50mm Lens, Top-Down": "bird's eye, hair design focus", "85mm Lens, Three-Quarter": "standard contouring view"
}

pic_sizes = ["4:5 (Portrait)", "16:9 (Widescreen)", "2.39:1 (Anamorphic)", "1:1 (Square)", "9:16 (Vertical)"]

materials = ["Encapsulated Silicone", "Feathered Edges", "Translucent Skin Finish", "Prosthetic Adhesive", "Matte Sealer", "Alcohol-activated Palette", "Granulation Tissue"]

# --- ساخت داشبورد ---
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actor Reference:", ["No", "Yes"])
        age_c = st.selectbox("🟡 Age Range:", list(ages.keys()))
    with r1c2:
        gender_c = st.selectbox("🟡 Gender:", list(genders.keys()))
        nat_c = st.selectbox("🟡 Nationality:", list(nationalities.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era_c = st.selectbox("Time Period:", list(eras.keys()))
        h_color = st.selectbox("Hair & Beard Color:", list(hair_colors.keys()))
    with r2c2:
        char_c = st.selectbox("Character Type:", list(char_types.keys()))
        groom_c = st.selectbox("Grooming Style:", list(grooming.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx_c = st.selectbox("SFX Makeup / Trauma:", list(sfx_trauma.keys()))
        aging_c = st.selectbox("Aging Details:", list(aging_details.keys()))
        light_c = st.selectbox("Lighting Style:", list(lighting.keys()))
    with r3c2:
        mat_c = st.selectbox("Material Finish:", materials)
        h_tex = st.selectbox("Hair Texture:", list(hair_textures.keys()))
        size_c = st.selectbox("Pic Size:", pic_sizes)

    cam_c = st.selectbox("Camera & Lens:", list(cameras.keys()))

# --- فرمول نهایی ---
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
sfx_desc = f"[CINEMATIC PROSTHETIC STUDY: Apply {sfx_c} ({sfx_trauma[sfx_c]})]. " if sfx_c != "None" else ""

final_prompt = f"{visual_guide}A professional cinematic Aspect Ratio {size_c} portrait of a {gender_c} ({genders[gender_c]}) {age_c} ({ages[age_c]}) {nat_c} ({nationalities[nat_c]}) " \
               f"from the {era_c} ({eras[era_c]}). Character Concept: {char_c} ({char_types[char_c]}). Grooming: {groom_c}. " \
               f"Hair: {h_color} ({hair_colors[h_color]}), Texture: {h_tex} ({hair_textures[h_tex]}). " \
               f"Skin: {aging_c} ({aging_details[aging_c]}). {sfx_desc}Finish Material: {mat_c}. " \
               f"Technical Specs: {light_c}, {cam_c}, 8k, subsurface scattering, raw photography."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00d4ff; font-family:Montserrat; padding-top:20px;'>لطفاً برای کپی کردن، متن داخل کادر سفید را انتخاب کنید</p>", unsafe_allow_html=True)
