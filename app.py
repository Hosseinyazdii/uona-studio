import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA STUDIO | PROMPT BUILDER", layout="wide")

# استایل تخصصی (Luxury Cinematic + Excel Dashboard Style)
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
        color: #00d4ff; font-family: 'Cinzel', serif; font-size: 2.5rem; letter-spacing: 6px;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5); margin: 0;
    }
    label p { color: #00d4ff !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; text-transform: uppercase !important; }
    
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 12px; font-weight: 900; font-size: 1.4rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 25px; border-radius: 0 0 8px 8px; border-left: 10px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.1rem; line-height: 1.7; min-height: 500px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); user-select: all !important; }
    
    .lang-guide { text-align: center; color: #00d4ff !important; font-family: 'Tahoma', sans-serif; font-size: 0.85rem; margin-bottom: 15px; opacity: 0.8; line-height: 1.6; text-shadow: 0 0 5px rgba(0, 212, 255, 0.3); }

    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO | MASTER DASHBOARD</p></div>', unsafe_allow_html=True)

# --- دیتابیس جامع استخراج شده از تمام ۱۵ شیت اکسل ---

nationalities = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure",
    "Syrian": "Levantine features, straight profile",
    "American": "Diverse North American features, broad range of skin tones",
    "Indian": "South Asian features, deep-set dark eyes, rich warm undertones",
    "Chinese": "East Asian features, high cheekbones, smooth skin",
    "African": "Sub-Saharan features, broad nasal structure, deep melanated skin",
    "European": "Caucasian features, fair complexion",
    "Turkish": "Eurasian features, strong contours, medium olive skin"
}

eras = {
    "Contemporary / Modern Day": "Current lighting, sharp details",
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures",
    "BCE (Before Common Era)": "Ancient civilization styling",
    "Pre-Islamic Era": "Traditional regional heritage",
    "Ancient Era (Hellenistic/Roman)": "Classical features, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures",
    "200 Years Ago (Early 19th Century)": "Regency style, era-specific grooming",
    "150 Years Ago (Victorian Era)": "Formal structured textures, pale complexions",
    "100 Years Ago (Roaring 20s)": "Vintage aesthetic, early 20th-century grooming",
    "50 Years Ago (1970s Retro)": "Analog film look, warm hues",
    "Futuristic / Cyberpunk": "Neon accents, high-tech glow",
    "Post-Apocalyptic": "Dirty, weathered, distressed textures"
}

char_types = {
    "Heroic Warrior": "Strong jawline, confident gaze",
    "Sinister Villain": "Harsh shadows, menacing expression",
    "Scholar / Intellectual": "Refined appearance, focused eyes",
    "Royal / Aristocratic": "Elegant posture, luxury textures",
    "Mercenary / Outlaw": "Rugged, weathered, scars",
    "Mystic / Shaman": "Otherworldly look, spiritual paint",
    "Corporate Executive / CEO": "Clean-cut, authoritative",
    "Elite Athlete / Fitness Pro": "Defined muscularity, sweat detail",
    "Bohemian Artist": "Creative styling, messy hair",
    "Average Citizen": "Naturalistic, candid",
    "Blue-collar / Technician": "Grime, work-worn skin",
    "Academic Student": "Youthful, inquisitive",
    "High-fashion Model": "Angular features, flawless skin",
    "Retiree / Grandparent": "Dignified aging",
    "Urban / Street Style": "Modern edge",
    "Rural / Outdoorsman": "Sun-damaged skin",
    "Red Carpet / Gala Guest": "Glamorous",
    "Ailing / Sickly Character": "Pale skin, dark circles, visible veins"
}

grooming = {
    "Saudi Anchor Beard": "sharp angled form connected to chin", "Pyramidal Moustache": "wide base with narrow top",
    "Clean Shaven": "smooth skin, no stubble", "Light Stubble": "short even stubble",
    "Heavy Stubble": "thick rough texture", "Designer Stubble": "precisely trimmed edges",
    "Shadow Fade Beard": "faded sides, denser hair on chin", "Goatee (No Mustache)": "chin beard only",
    "Classic Goatee": "chin beard connected to mustache", "Van Dyke": "pointed chin beard, disconnected mustache",
    "Anchor Beard": "pointed chin beard, thin defined mustache", "Short Boxed Beard": "precise square edges",
    "Medium Boxed Beard": "structured clean appearance", "Long Full Beard": "long thick natural growth",
    "Unkempt Beard": "messy growth, random direction", "Scruffy Beard": "patchy, rough texture",
    "Wild Beard": "long chaotic untamed texture", "Bedouin Beard": "natural sun-exposed texture",
    "Viking Beard": "long thick braided strands", "Medieval Beard": "period-authentic growth",
    "Philosopher Beard": "long soft texture", "Warrior Beard": "thick rugged battle-worn",
    "Graying Patches": "natural gray mixed-tone patches", "Split Texture Beard": "smooth chin, rough sides",
    "Short Sideburns": "above ear level", "Mid-Ear Sideburns": "level with tragus",
    "Long Sideburns": "ear lobe level", "Extra-Long Sideburns": "passes ear lobe",
    "High Sideburns": "temple level", "Tapered Length": "gradient faded into skin",
    "Square Sideburns": "horizontal cut bottom", "Pointed Sideburns": "triangle point bottom",
    "Rounded Sideburns": "soft circular finish", "Pencil Sideburns": "ultra-thin line",
    "Flared Sideburns": "widens at base", "Angled Sideburns": "slanted cut bottom",
    "Mutton Chops": "wide full sideburns", "Friendly Mutton Chops": "connected via mustache", "Soul Patch": "small patch below lower lip"
}

sfx_trauma = {
    "None": "No trauma", "Fresh Katana/Sword Slash": "Deep open edges, active bleeding", 
    "Glass Laceration with Shards": "Irregular edges, embedded glass", "Blunt Force Contusion": "Severe swelling, inflammation",
    "3-Day Old Wound (Scabbing)": "Scabbing, pink edges", "1-Week Old Wound (Granulation)": "Granulation tissue, peeling skin",
    "1-Month Old Scar (Maturation)": "Fibrous tissue, maturation", "1-Year Old Keloid Scar": "Raised hypertrophic tissue",
    "5-Year Old Atrophic Scar": "Pale white, level with skin", "Fresh Periorbital Hematoma": "Purple-red bruising, inflammation",
    "24-Hour Old Bruise (Deep Purple)": "Deep purple and blue", "3-Day Old Bruise (Greenish-Yellow)": "Greenish-yellow tint",
    "15-Day Old Fading Bruise": "Fading yellow spots", "Chemical Acid Burn (Corrosive)": "Melting tissue texture",
    "1st Degree Sunburn/Erythema": "Uniform redness", "2nd Degree Burn with Blisters": "Liquid-filled blisters",
    "Bilateral Vitiligo Depigmentation": "White patches with defined borders", "Diffuse Hyperpigmentation": "Irregular brown spots"
}

aging = {
    "None": "No aging", "Deep Nasolabial Folds": "deep smile lines", "Pronounced Crow's Feet": "radial eye wrinkles",
    "Hooded Eyelids / Ptosis": "sagging upper lids", "Dermal Crepiness": "paper-thin skin texture",
    "Visible Liver Spots (Lentigines)": "age-related pigment spots", "Sagging Jowls & Loose Skin": "loose jawline skin",
    "Frontal Rhytids (Forehead Furrows)": "deep forehead ridges", "Periorbital Hollows & Eye Bags": "sunken eyes",
    "Vertical Lip Lines (Smoker's Lines)": "fine vertical mouth wrinkles", "Age-related Telangiectasia": "broken capillaries"
}

hair_textures = {
    "Afro-Textured": "Tight structural coils, matte finish", "Wavy (Type 2)": "Natural S-shape waves",
    "Curly (Type 3)": "Defined ringlets, voluminous loops", "Straight (Sleek)": "Linear alignment, silky surface",
    "Coarse & Wiry": "Thick diameter, irregular graying", "Fine & Wispy": "Low density, translucent strands",
    "Disheveled & Matted": "Tangled clumps, weathered look", "Braided / Cornrows": "Intricate interlocking patterns"
}

hair_colors = {
    "Jet black": "Jet black", "Deep espresso brown": "Dark chocolate", "Light chestnut brown": "Sandy brown",
    "Ash blonde": "Cool blonde", "Golden blonde": "Warm blonde", "10% Salt & Pepper": "sparse grey",
    "30% Salt & Pepper": "mixed grey", "50% Salt & Pepper": "even grey mix", "70% Salt & Pepper": "mostly grey"
}

lighting = {
    "Rembrandt Lighting": "triangle light on cheek", "Cold Rim Lighting": "blue backlight separation",
    "Chiaroscuro": "high contrast shadows", "Teal and Orange Lighting": "cinematic color contrast",
    "Volumetric God Rays": "linear light through fog", "Cinematic Golden Hour": "warm soft light",
    "High-Key Studio Lighting": "bright, shadowless", "Low-Key Moody Lighting": "dark, mysterious",
    "Neon Cyberpunk Rim Light": "colorful edge light", "Hard Top Lighting": "harsh overhead shadows",
    "Flickering Candlelight": "unsteady soft shadows", "Soft Professional Softbox": "velvety even light"
}

cameras = {
    "85mm Lens, Eye-Level Shot": "no distortion portrait", "100mm Macro Lens, Extreme Close-Up": "skin pore detail",
    "50mm Lens, Dutch Angle": "tilted tension view", "35mm Lens, Low-Angle (Hero Shot)": "powerful low perspective",
    "24mm Wide-Angle, High-Angle": "thinning high perspective", "200mm Telephoto, Profile View": "compressed semi-profile",
    "50mm Lens, Top-Down (Bird's Eye)": "vertical hair design focus", "85mm Lens, Three-Quarter View": "standard contouring"
}

# --- ساختار فرم ---
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actor Reference:", ["No", "Yes"])
        age_sel = st.selectbox("🟡 Age Range:", list(ages.keys()))
    with r1c2:
        gender_sel = st.selectbox("🟡 Gender:", ["Masculine / Male", "Feminine / Female", "Androgynous"])
        nat_sel = st.selectbox("🟡 Nationality:", list(nationalities.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era_sel = st.selectbox("Time Period:", list(eras.keys()))
        h_col = st.selectbox("Hair & Beard Color:", list(hair_colors.keys()))
    with r2c2:
        char_sel = st.selectbox("Character Type:", list(char_types.keys()))
        groom_sel = st.selectbox("Grooming Style:", list(grooming.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx_sel = st.selectbox("SFX Makeup / Trauma:", list(sfx_trauma.keys()))
        aging_sel = st.selectbox("Aging Details:", list(aging.keys()))
        light_sel = st.selectbox("Lighting Style:", list(lighting.keys()))
    with r3c2:
        mat_sel = st.selectbox("Material Finish:", ["Encapsulated Silicone", "Matte Sealer", "Translucent Skin", "Prosthetic Adhesive"])
        h_tex = st.selectbox("Hair Texture:", list(hair_textures.keys()))
        size_sel = st.selectbox("Pic Size:", ["16:9 (Widescreen)", "1:1 (Square)", "2.39:1 (Anamorphic)", "4:5 (Portrait)"])

    cam_sel = st.selectbox("Camera & Lens:", list(cameras.keys()))

# --- فرمول نهایی پرامپت ---
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
sfx_desc = f"[CINEMATIC PROSTHETIC STUDY: Apply {sfx_sel} ({sfx_trauma[sfx_sel]})]. " if sfx_sel != "None" else ""

final_prompt = f"{visual_guide}A professional cinematic Aspect Ratio {size_sel} portrait of a {gender_sel} {age_sel} {nat_sel} ({nationalities[nat_sel]}) " \
               f"from the {era_sel} ({eras[era_sel]}). Character style: {char_sel} ({char_types[char_sel]}). Grooming: {groom_sel} ({grooming[groom_sel]}). " \
               f"Hair: {h_col} ({hair_colors[h_col]}), Texture: {h_tex} ({hair_textures[h_tex]}). " \
               f"Skin Aging: {aging_sel} ({aging[aging_sel]}). {sfx_desc}Finish Material: {mat_sel}. " \
               f"Technical Specs: {light_sel}, {cam_sel}, 8k, subsurface scattering, raw photography."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    
    st.markdown("""<div class="lang-guide">لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>
        Please click on the text inside the box below to copy<br>
        يرجى الضغط على النص داخل المربع أدناه للنسخ</div>""", unsafe_allow_html=True)
    
    st.markdown(f'<div class="output-box">{final_prompt}</div>', unsafe_allow_html=True)
