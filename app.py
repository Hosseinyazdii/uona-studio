import streamlit as st

# 1. تنظیمات پایه
st.set_page_config(page_title="UONA STUDIO | MASTER DASHBOARD", layout="wide")

# 2. تزریق CSS برای استایل سینماتیک، بک‌گراند و رفع اسکرول
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
        background: rgba(5, 15, 26, 0.92); z-index: -1;
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
    
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 15px; font-weight: 900; font-size: 1.5rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 30px; border-radius: 0 0 8px 8px; border-left: 10px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.8; min-height: 520px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); user-select: all !important; }
    
    .lang-guide { text-align: center; color: #00d4ff !important; font-family: 'Tahoma', sans-serif; font-size: 0.85rem; margin-bottom: 15px; opacity: 0.8; line-height: 1.6; }

    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO | PROMPT BUILDER</p></div>', unsafe_allow_html=True)

# 3. دیتابیس کامل (۱۰۰٪ دیتای اکسل)

gender_data = {
    "Masculine / Male": "strong bone structure, wide jawline",
    "Feminine / Female": "softer facial contours, high forehead",
    "Androgynous": "blend of masculine and feminine features"
}

age_data = {
    "Child / Pre-adolescent": "textureless skin, large eyes",
    "Adolescent / Teenager": "puberty changes, oily skin texture",
    "Young Adult (Early 20s)": "peak skin elasticity and radiance",
    "Middle-aged (Late 40s)": "initial fat loss and sagging",
    "Elderly / Senior": "complete collagen loss, deep wrinkles",
    "Ancient / Centenarian": "paper-thin skin, deep age spots"
}

nat_data = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure",
    "Syrian": "Levantine features, straight profile",
    "American": "Diverse North American features, broad range of skin tones",
    "Indian": "South Asian features, deep-set dark eyes, rich warm undertones",
    "Chinese": "East Asian features, high cheekbones, smooth skin texture",
    "African": "Sub-Saharan features, broad nasal structure, deep melanated skin",
    "European": "Caucasian features, fair complexion",
    "Turkish": "Eurasian features, strong contours, medium olive skin"
}

era_data = {
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures",
    "BCE (Before Common Era)": "Ancient civilization styling",
    "Pre-Islamic Era": "Traditional regional heritage, antique textures",
    "Ancient Era (Hellenistic/Roman)": "Classical features, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures",
    "200 Years Ago (Early 19th Century)": "Regency style, era-specific grooming",
    "150 Years Ago (Victorian Era)": "Formal, structured, refined textures",
    "100 Years Ago (Roaring 20s)": "Vintage aesthetic, early 20th-century grooming",
    "50 Years Ago (1970s Retro)": "Analog film look, warm hues",
    "Contemporary / Modern Day": "Current lighting, sharp details",
    "Futuristic / Cyberpunk": "Neon accents, high-tech glow",
    "Post-Apocalyptic": "Dirty, weathered, distressed textures"
}

char_data = {
    "Heroic Warrior": "Strong jawline, confident gaze",
    "Sinister Villain": "Harsh shadows, menacing expression",
    "Scholar / Intellectual": "Refined appearance, focused eyes",
    "Royal / Aristocratic": "Elegant posture, pristine skin",
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

groom_data = {
    "Saudi Anchor Beard": "sharp angled form connected to chin",
    "Pyramidal Moustache": "wide base with narrow top",
    "Clean Shaven": "Smooth skin, no stubble",
    "Light Stubble": "Very short, even stubble",
    "Heavy Stubble": "Thicker, rough texture",
    "Designer Stubble": "Precisely trimmed edges",
    "Shadow Fade Beard": "Faded sides, smooth gradient",
    "Goatee (No Mustache)": "Chin beard only, clean shaven cheeks",
    "Classic Goatee": "Chin beard connected to mustache",
    "Van Dyke": "Pointed chin beard, disconnected mustache",
    "Anchor Beard": "Pointed chin beard, thin defined mustache",
    "Short Boxed Beard": "Short, full beard, precise square edges",
    "Medium Boxed Beard": "Medium length, structured clean appearance",
    "Long Full Beard": "Long, thick, natural growth pattern",
    "Unkempt Beard": "Messy natural growth, disheveled texture",
    "Scruffy Beard": "Patchy, rough texture",
    "Wild Beard": "Long, chaotic, untamed texture",
    "Bedouin Beard": "Natural sun-exposed texture",
    "Viking Beard": "Long, thick, braided strands",
    "Medieval Beard": "Natural, period-authentic growth",
    "Philosopher Beard": "Long, soft texture, intellectual",
    "Warrior Beard": "Thick, rugged, battle-worn",
    "Graying Patches": "Natural gray strands, mixed-tone",
    "Split Texture Beard": "Smooth on chin, rough on sides",
    "Short Sideburns": "Above ear level",
    "Mid-Ear Sideburns": "Level with tragus",
    "Long Sideburns": "Ear lobe level",
    "Extra-Long Sideburns": "Passes ear lobe",
    "High Sideburns": "Temple level",
    "Tapered Length": "Gradient length, faded into skin",
    "Square Sideburns": "Horizontal cut bottom",
    "Pointed Sideburns": "Triangle point bottom",
    "Rounded Sideburns": "Soft circular finish",
    "Pencil Sideburns": "Ultra-thin line",
    "Flared Sideburns": "Widens at base",
    "Angled Sideburns": "Slanted cut bottom",
    "Mutton Chops": "Wide full sideburns",
    "Friendly Mutton Chops": "Mutton chops connected via mustache",
    "Soul Patch": "Small patch below lower lip"
}

sfx_data = {
    "None": "no trauma",
    "Fresh Katana/Sword Slash": "deep, open edges, active bleeding",
    "Glass Laceration with Shards": "irregular edges, embedded glass particles",
    "Blunt Force Contusion": "severe swelling, inflamed redness",
    "3-Day Old Wound (Scabbing)": "scab formation, dark pink edges",
    "1-Week Old Wound (Granulation)": "pink tissue, peeling skin",
    "1-Month Old Scar (Maturation)": "fibrous tissue, recessed area",
    "1-Year Old Keloid Scar": "raised hypertrophic tissue",
    "5-Year Old Atrophic Scar": "pale white, level with skin",
    "Fresh Periorbital Hematoma": "purple-red bruising, intense inflammation",
    "24-Hour Old Bruise (Deep Purple)": "deep purple and blue tones",
    "3-Day Old Bruise (Greenish-Yellow)": "greenish-yellow tint from hemoglobin degradation",
    "15-Day Old Fading Bruise": "fading yellow spots",
    "Chemical Acid Burn (Corrosive)": "melting tissue, slimy corroded texture",
    "1st Degree Sunburn/Erythema": "uniform redness, no blisters",
    "2nd Degree Burn with Blisters": "liquid-filled blisters, peeling skin",
    "Bilateral Vitiligo Depigmentation": "white patches with defined borders",
    "Diffuse Hyperpigmentation & Melasma": "irregular dark brown spots"
}

aging_data = {
    "None": "no visible aging",
    "Deep Nasolabial Folds": "deep smile lines from nose to mouth",
    "Pronounced Crow's Feet": "radial wrinkles around eyes",
    "Hooded Eyelids / Ptosis": "sagging upper eyelid skin",
    "Dermal Crepiness": "fine paper-like skin texture",
    "Visible Liver Spots (Lentigines)": "sun-related age spots",
    "Sagging Jowls & Loose Skin": "loss of jawline definition",
    "Frontal Rhytids (Forehead Furrows)": "deep horizontal forehead ridges",
    "Periorbital Hollows & Eye Bags": "sunken eyes and under-eye puffiness",
    "Vertical Lip Lines (Smoker's Lines)": "fine vertical mouth wrinkles",
    "Age-related Telangiectasia": "broken capillaries on nose and cheeks"
}

hair_tex_data = {
    "Afro-Textured": "tight structural coils, matte finish",
    "Wavy (Type 2)": "natural S-shape waves, soft luster",
    "Curly (Type 3)": "defined ringlets, springy loops",
    "Straight (Sleek)": "linear alignment, silky surface",
    "Coarse & Wiry": "thick strands, irregular graying",
    "Fine & Wispy": "low density, translucent thin strands",
    "Disheveled & Matted": "tangled clumps, weathered look",
    "Braided / Cornrows": "intricate interlocking patterns"
}

hair_col_data = {
    "Jet black": "Jet black",
    "Deep espresso brown": "Dark chocolate brown",
    "Light chestnut brown": "Sandy honey brown",
    "Ash blonde": "Cool toned blonde",
    "Golden blonde": "Warm blonde",
    "10% Salt & Pepper": "sparse white strands",
    "30% Salt & Pepper": "mixed white strands",
    "50% Salt & Pepper": "even grey mix",
    "70% Salt & Pepper": "predominantly grey hair"
}

light_data = {
    "Rembrandt Lighting": "classic triangle light on cheek",
    "Cold Rim Lighting": "blue backlight separation",
    "Chiaroscuro": "high contrast between light and dark",
    "Teal and Orange Lighting": "cinematic color contrast",
    "Volumetric God Rays": "linear light through fog",
    "Cinematic Golden Hour": "warm soft sunset glow",
    "High-Key Studio Lighting": "bright and shadowless",
    "Low-Key Moody Lighting": "dark and mysterious shadows",
    "Neon Cyberpunk Rim Light": "colorful neon edge lighting",
    "Hard Top Lighting": "harsh overhead shadows",
    "Flickering Candlelight": "unsteady soft warm shadows",
    "Soft Professional Softbox": "velvety even light"
}

camera_data = {
    "85mm Lens, Eye-Level Shot": "no distortion portrait",
    "100mm Macro Lens, Extreme Close-Up": "extreme pore and texture detail",
    "50mm Lens, Dutch Angle": "tilted tension view",
    "35mm Lens, Low-Angle (Hero Shot)": "powerful low perspective",
    "24mm Wide-Angle, High-Angle": "thinning high perspective",
    "200mm Telephoto, Profile View": "compressed bokeh profile",
    "50mm Lens, Top-Down (Bird's Eye)": "vertical hair design focus",
    "85mm Lens, Three-Quarter View": "standard contouring view"
}

pic_size_data = [
    "Aspect Ratio 4:5 (Portrait)",
    "Aspect Ratio 16:9 (Widescreen)",
    "Aspect Ratio 2.39:1 (Anamorphic / Cinemascope)",
    "Aspect Ratio 1:1 (Square)",
    "Aspect Ratio 9:16 (Vertical / Stories)"
]

material_data = [
    "Encapsulated Silicone",
    "Feathered Edges",
    "Translucent Skin Finish",
    "Prosthetic Adhesive",
    "Matte Sealer",
    "Alcohol-activated Palette",
    "Granulation Tissue"
]

# 4. بدنه اصلی داشبورد (چیدمان ستونی)
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    # بخش پایه (🟡 اجباری)
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actor Reference:", ["No", "Yes"])
        age_sel = st.selectbox("🟡 Age Range:", list(age_data.keys()))
    with r1c2:
        gender_sel = st.selectbox("🟡 Gender:", list(gender_data.keys()))
        nat_sel = st.selectbox("🟡 Nationality:", list(nat_data.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    
    # بخش استایل و زمان
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era_sel = st.selectbox("Time Period:", list(era_data.keys()))
        h_col = st.selectbox("Hair & Beard Color:", list(hair_col_data.keys()))
    with r2c2:
        char_sel = st.selectbox("Character Type:", list(char_data.keys()))
        groom_sel = st.selectbox("Grooming Style:", list(groom_data.keys()))

    st.markdown("<br>", unsafe_allow_html=True)

    # بخش SFX و جزییات فنی
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx_sel = st.selectbox("SFX Makeup / Trauma:", list(sfx_data.keys()))
        aging_sel = st.selectbox("Aging Details:", list(aging_data.keys()))
        light_sel = st.selectbox("Lighting Style:", list(light_data.keys()))
    with r3c2:
        mat_sel = st.selectbox("Material Finish:", material_data)
        h_tex = st.selectbox("Hair Texture:", list(hair_tex_data.keys()))
        size_sel = st.selectbox("Pic Size:", pic_size_data)

    cam_sel = st.selectbox("Camera, Lens & Angle:", list(camera_data.keys()))

# 5. منطق ساخت Master Prompt
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
sfx_desc = f"[CINEMATIC PROSTHETIC STUDY: Apply {sfx_sel} ({sfx_data[sfx_sel]}) SFX as a makeup layer]. " if sfx_sel != "None" else ""

final_prompt = f"{visual_guide}A professional cinematic {size_sel} portrait of a {gender_sel} ({gender_data[gender_sel]}) " \
               f"{age_sel} ({age_data[age_sel]}) {nat_sel} ({nat_data[nat_sel]}) from the {era_sel} ({era_data[era_sel]}). " \
               f"Character Concept: {char_sel} ({char_data[char_sel]}). Grooming: {groom_sel} ({groom_data[groom_sel]}). " \
               f"Hair: {h_col} ({hair_col_data[h_col]}), Texture: {h_tex} ({hair_tex_data[h_tex]}). " \
               f"Skin: {aging_sel} ({aging_data[aging_sel]}). {sfx_desc}Finish Material: {mat_sel}. " \
               f"Technical Specs: {light_sel}, {cam_sel}, 8k, subsurface scattering, raw photography, no-retouch, focus on prosthetic makeup accuracy."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    
    st.markdown("""<div class="lang-guide">لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>
        Please click on the text inside the box below to copy<br>
        يرجى الضغط على النص داخل المربع أدناه للنسخ</div>""", unsafe_allow_html=True)
    
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
