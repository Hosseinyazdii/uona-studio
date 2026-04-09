import streamlit as st

# 1. تنظیمات اصلی و تم سینماتیک
st.set_page_config(page_title="UONA STUDIO | MASTER DASHBOARD", layout="wide")

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
    /* استایل لیبل‌ها و ستاره قرمز */
    label p { 
        color: #00d4ff !important; 
        font-family: 'Montserrat', sans-serif !important; 
        font-weight: 700 !important; 
        text-transform: uppercase !important;
        font-size: 0.85rem !important;
    }
    .required-star { color: #ff4b4b; font-weight: bold; margin-left: 3px; }

    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 15px; font-weight: 900; font-size: 1.4rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 30px; border-radius: 0 0 8px 8px; border-left: 10px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.8; min-height: 550px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); user-select: all !important; }
    
    .lang-guide { text-align: center; color: #00d4ff !important; font-family: 'Tahoma', sans-serif; font-size: 0.85rem; margin-bottom: 15px; opacity: 0.8; line-height: 1.6; }

    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO | PROMPT BUILDER</p></div>', unsafe_allow_html=True)

# 2. تعریف دیتابیس کامل (۱۰۰٪ از شیت‌ها) با اضافه شدن گزینه None

def add_none(data_list):
    return ["None"] + data_list

def add_none_dict(data_dict):
    new_dict = {"None": ""}
    new_dict.update(data_dict)
    return new_dict

gender_data = add_none_dict({
    "Masculine / Male": "strong bone structure, wide jawline",
    "Feminine / Female": "softer facial contours, high forehead",
    "Androgynous": "blend of masculine and feminine features"
})

age_data = add_none_dict({
    "Child / Pre-adolescent": "textureless skin, large eyes",
    "Adolescent / Teenager": "puberty changes, oily skin texture",
    "Young Adult (Early 20s)": "peak skin elasticity and radiance",
    "Middle-aged (Late 40s)": "initial fat loss and sagging",
    "Elderly / Senior": "complete collagen loss, deep wrinkles",
    "Ancient / Centenarian": "paper-thin skin, deep age spots"
})

nat_data = add_none_dict({
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
})

era_data = add_none_dict({
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
})

char_data = add_none_dict({
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
})

groom_data = add_none_dict({
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
    "Graying Patches": "Natural gray strands, mixed-tone patches",
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
})

sfx_data = add_none_dict({
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
    "3-Day Old Bruise (Greenish-Yellow)": "greenish-yellow tint from blood degradation",
    "15-Day Old Fading Bruise": "fading yellow spots",
    "Chemical Acid Burn (Corrosive)": "melting tissue, slimy corroded texture",
    "1st Degree Sunburn/Erythema": "uniform redness, no blisters",
    "2nd Degree Burn with Blisters": "liquid-filled blisters, peeling skin",
    "Bilateral Vitiligo Depigmentation": "white patches with defined borders",
    "Diffuse Hyperpigmentation & Melasma": "irregular dark brown spots"
})

aging_data = add_none_dict({
    "Deep Nasolabial Folds": "deep smile lines from nose to mouth",
    "Pronounced Crow's Feet": "radial wrinkles around eyes",
    "Hooded Eyelids / Ptosis": "sagging upper eyelid skin",
    "Dermal Crepiness": "fine paper-like skin texture",
    "Visible Liver Spots (Lentigines)": "sun-related age spots",
    "Sagging Jowls & Loose Skin": "loss of jawline definition",
    "Frontal Rhytids (Forehead Furrows)": "deep horizontal forehead ridges",
    "Periorbital Hollows & Eye Bags": "sunken eyes and puffiness",
    "Vertical Lip Lines (Smoker's Lines)": "fine vertical mouth wrinkles",
    "Age-related Telangiectasia": "broken capillaries on nose and cheeks"
})

hair_tex_data = add_none_dict({
    "Afro-Textured": "tight structural coils, matte finish",
    "Wavy (Type 2)": "natural S-shape waves, soft luster",
    "Curly (Type 3)": "defined ringlets, springy loops",
    "Straight (Sleek)": "linear alignment, silky surface",
    "Coarse & Wiry": "thick strands, irregular graying",
    "Fine & Wispy": "low density, translucent thin strands",
    "Disheveled & Matted": "tangled clumps, weathered look",
    "Braided / Cornrows": "intricate interlocking patterns"
})

hair_col_data = add_none_dict({
    "Jet black": "Jet black",
    "Deep espresso brown": "Dark chocolate brown",
    "Light chestnut brown": "Sandy honey brown",
    "Ash blonde": "Cool toned blonde",
    "Golden blonde": "Warm blonde",
    "10% Salt & Pepper": "sparse white strands",
    "30% Salt & Pepper": "mixed white strands",
    "50% Salt & Pepper": "even grey mix",
    "70% Salt & Pepper": "predominantly grey hair"
})

light_data = add_none_dict({
    "Rembrandt Lighting": "classic triangle light on cheek",
    "Cold Rim Lighting": "blue backlight separation",
    "Chiaroscuro": "high contrast shadows",
    "Teal and Orange Lighting": "cinematic color contrast",
    "Volumetric God Rays": "linear light through fog",
    "Cinematic Golden Hour": "warm soft sunset glow",
    "High-Key Studio Lighting": "bright and shadowless",
    "Low-Key Moody Lighting": "dark and mysterious shadows",
    "Neon Cyberpunk Rim Light": "neon edge lighting",
    "Hard Top Lighting": "harsh overhead shadows",
    "Flickering Candlelight": "unsteady soft warm shadows",
    "Soft Professional Softbox": "velvety even light"
})

camera_data = add_none_dict({
    "85mm Lens, Eye-Level Shot": "no distortion portrait",
    "100mm Macro Lens, Extreme Close-Up": "extreme texture detail",
    "50mm Lens, Dutch Angle": "tilted tension view",
    "35mm Lens, Low-Angle (Hero Shot)": "powerful low perspective",
    "24mm Wide-Angle, High-Angle": "thinning high perspective",
    "200mm Telephoto, Profile View": "compressed bokeh profile",
    "50mm Lens, Top-Down (Bird's Eye)": "vertical design focus",
    "85mm Lens, Three-Quarter View": "standard contouring view"
})

pic_size_data = add_none(["Aspect Ratio 4:5", "Aspect Ratio 16:9", "Aspect Ratio 2.39:1", "Aspect Ratio 1:1", "Aspect Ratio 9:16"])
material_data = add_none(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin Finish", "Prosthetic Adhesive", "Matte Sealer", "Alcohol Palette", "Granulation Tissue"])

# 3. بدنه داشبورد
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    # پایه (اجباری با ستاره قرمز)
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("Actor Reference *", ["None", "No", "Yes"])
        age_sel = st.selectbox("Age Range *", list(age_data.keys()))
    with r1c2:
        gender_sel = st.selectbox("Gender *", list(gender_data.keys()))
        nat_sel = st.selectbox("Nationality *", list(nat_data.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era_sel = st.selectbox("Time Period", list(era_data.keys()))
        h_col = st.selectbox("Hair & Beard Color", list(hair_col_data.keys()))
    with r2c2:
        char_sel = st.selectbox("Character Type", list(char_data.keys()))
        groom_sel = st.selectbox("Grooming Style", list(groom_data.keys()))

    st.markdown("<br>", unsafe_allow_html=True)

    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx_sel = st.selectbox("SFX Makeup / Trauma", list(sfx_data.keys()))
        aging_sel = st.selectbox("Aging Details", list(aging_data.keys()))
        light_sel = st.selectbox("Lighting Style", list(light_data.keys()))
    with r3c2:
        mat_sel = st.selectbox("Material Finish", material_data)
        h_tex = st.selectbox("Hair Texture", list(hair_tex_data.keys()))
        size_sel = st.selectbox("Pic Size", pic_size_data)

    cam_sel = st.selectbox("Camera, Lens & Angle", list(camera_data.keys()))

# 4. ساخت پرامپت (حذف None از متن نهایی)
def format_part(prefix, val, desc_dict=None):
    if val == "None" or not val: return ""
    desc = f" ({desc_dict[val]})" if desc_dict and val in desc_dict and desc_dict[val] else ""
    return f"{prefix}{val}{desc}"

p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
p_gender = format_part("", gender_sel, gender_data)
p_age = format_part("", age_sel, age_data)
p_nat = format_part("", nat_sel, nat_data)
p_era = format_part(" from the ", era_sel, era_data)
p_char = format_part(" Character Concept: ", char_sel, char_data)
p_groom = format_part(" Grooming: ", groom_sel, groom_data)
p_h_col = format_part(" Hair Color: ", h_col, hair_col_data)
p_h_tex = format_part(", Texture: ", h_tex, hair_tex_data)
p_age_det = format_part(" Skin: ", aging_sel, aging_data)
p_sfx = f" [SFX: {sfx_sel} ({sfx_data[sfx_sel]})]" if sfx_sel != "None" else ""
p_mat = format_part(" Finish: ", mat_sel)
p_light = format_part(" Technical: ", light_sel, light_data)
p_cam = format_part(", ", cam_sel, camera_data)
p_size = f" Aspect Ratio {size_sel}" if size_sel != "None" else ""

final_prompt = f"{p_actor}A professional cinematic {p_size} portrait of a {p_gender} {p_age} {p_nat}{p_era}. {p_char}.{p_groom}.{p_h_col}{p_h_tex}.{p_age_det}.{p_sfx}.{p_mat}.{p_light}{p_cam}, 8k, raw photography, subsurface scattering."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown("""<div class="lang-guide">لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>
        Please click on the text inside the box below to copy<br>
        يرجى الضغط على النص داخل المربع أدناه للنسخ</div>""", unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
