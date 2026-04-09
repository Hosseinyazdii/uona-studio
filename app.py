import streamlit as st

# 1. تنظیمات پایه و تم سینماتیک
st.set_page_config(page_title="UONA STUDIO | PRO DASHBOARD", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        /* بک‌گراند با بافت پوست ماکرو و نورپردازی دراماتیک برای ایجاد عمق */
        background-image: url("https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=2542");
        background-size: cover; background-attachment: fixed;
        overflow-y: auto !important;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        /* لایه تیره برای تمرکز روی فرم و ایجاد اتمسفر سینمایی عمیق */
        background: radial-gradient(circle, rgba(5, 10, 20, 0.85) 0%, rgba(2, 5, 10, 0.98) 100%);
        z-index: -1;
    }
    .header-box {
        background: rgba(0, 212, 255, 0.03); backdrop-filter: blur(15px);
        border-bottom: 1px solid rgba(0, 212, 255, 0.3); padding: 30px; margin-bottom: 40px; text-align: center;
    }
    .header-title {
        color: #00d4ff; font-family: 'Cinzel', serif; font-size: 2.8rem; letter-spacing: 10px;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.4); margin: 0;
    }
    
    label p { color: #00d4ff !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.85rem !important; }
    
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 15px; font-weight: 900; font-size: 1.4rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 35px; border-radius: 0 0 8px 8px; border-left: 12px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.8; min-height: 550px; box-shadow: 0 30px 60px rgba(0,0,0,0.9); user-select: all !important; }
    
    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(10, 20, 35, 0.7) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.2) !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO</p></div>', unsafe_allow_html=True)

# 2. توابع کمکی برای مدیریت None
def add_none(data_list): return ["None"] + data_list
def add_none_dict(data_dict):
    new_dict = {"None": ""}
    new_dict.update(data_dict)
    return new_dict

# --- دیتابیس کامل ---
gender_data = add_none_dict({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours", "Androgynous": "blend features"})
age_data = add_none_dict({"Child / Pre-adolescent": "textureless skin", "Adolescent / Teenager": "oily skin", "Young Adult (Early 20s)": "skin elasticity", "Middle-aged (Late 40s)": "fat loss", "Elderly / Senior": "collagen loss", "Ancient / Centenarian": "paper-thin skin"})
nat_data = add_none_dict({"Iranian": "Indo-Aryan features", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Saudi": "Peninsular Arab features", "Kuwaiti": "Northern Gulf features", "Syrian": "Levantine features", "American": "Diverse features", "Indian": "South Asian features", "Chinese": "East Asian features", "African": "Sub-Saharan features", "European": "Caucasian features", "Turkish": "Eurasian features"})
era_data = add_none_dict({"Stone Age / Prehistoric": "Primitive aesthetic", "BCE (Before Common Era)": "Ancient styling", "Pre-Islamic Era": "Traditional heritage", "Ancient Era (Hellenistic/Roman)": "Historical accuracy", "Medieval / Dark Ages": "Gritty textures", "200 Years Ago": "Regency style", "150 Years Ago": "Victorian Era", "100 Years Ago": "Roaring 20s", "50 Years Ago": "1970s Retro", "Contemporary / Modern Day": "Current lighting", "Futuristic / Cyberpunk": "Neon accents", "Post-Apocalyptic": "Weathered textures"})
char_data = add_none_dict({"Heroic Warrior": "Strong jawline", "Sinister Villain": "Harsh shadows", "Scholar / Intellectual": "Refined appearance", "Royal / Aristocratic": "Elegant posture", "Mercenary / Outlaw": "Rugged textures", "Mystic / Shaman": "Otherworldly look", "Corporate Executive / CEO": "Clean-cut", "Elite Athlete": "Defined muscularity", "Bohemian Artist": "Creative styling", "Average Citizen": "Naturalistic", "Blue-collar / Technician": "Grime", "Academic Student": "Youthful", "High-fashion Model": "Angular features", "Retiree / Grandparent": "Dignified aging", "Urban / Street Style": "Modern edge", "Rural / Outdoorsman": "Sun-damaged skin", "Red Carpet / Gala Guest": "Glamorous", "Ailing / Sickly Character": "Pale skin"})
groom_data = add_none_dict({"Saudi Anchor Beard": "sharp angled", "Pyramidal Moustache": "wide base", "Clean Shaven": "smooth skin", "Light Stubble": "short even", "Heavy Stubble": "rough texture", "Designer Stubble": "trimmed edges", "Shadow Fade Beard": "faded sides", "Goatee (No Mustache)": "chin beard", "Classic Goatee": "connected", "Van Dyke": "pointed", "Anchor Beard": "thin defined", "Short Boxed Beard": "square edges", "Medium Boxed Beard": "clean appearance", "Long Full Beard": "natural growth", "Unkempt Beard": "messy", "Scruffy Beard": "patchy", "Wild Beard": "chaotic", "Bedouin Beard": "weathered", "Viking Beard": "braided", "Medieval Beard": "period growth", "Philosopher Beard": "soft", "Warrior Beard": "rugged", "Graying Patches": "gray strands", "Split Texture Beard": "dual-textured", "Short Sideburns": "above ear", "Mid-Ear Sideburns": "tragus level", "Long Sideburns": "ear lobe", "Extra-Long Sideburns": "pass lobe", "High Sideburns": "temple level", "Tapered Length": "faded", "Square Sideburns": "clean edges", "Pointed Sideburns": "triangle point", "Rounded Sideburns": "circular", "Pencil Sideburns": "thin line", "Flared Sideburns": "wide look", "Angled Sideburns": "slanted", "Mutton Chops": "wide full", "Friendly Mutton Chops": "connected", "Soul Patch": "below lip"})
sfx_data = add_none_dict({"Fresh Katana Slash": "active bleeding", "Glass Laceration": "embedded glass", "Blunt Force Contusion": "swelling", "3-Day Old Wound": "scabbing", "1-Week Old Wound": "granulation", "1-Month Old Scar": "maturation", "1-Year Old Keloid Scar": "hypertrophic", "5-Year Old Atrophic Scar": "pale white", "Fresh Periorbital Hematoma": "bruising", "24-Hour Old Bruise": "deep purple", "3-Day Old Bruise": "greenish-yellow", "15-Day Old Fading Bruise": "fading spots", "Chemical Acid Burn": "melting tissue", "1st Degree Sunburn": "redness", "2nd Degree Burn": "blisters", "Bilateral Vitiligo": "white patches", "Diffuse Hyperpigmentation": "dark spots"})
aging_data = add_none_dict({"Deep Nasolabial Folds": "smile lines", "Pronounced Crow's Feet": "eye wrinkles", "Hooded Eyelids / Ptosis": "sagging lids", "Dermal Crepiness": "paper skin", "Visible Liver Spots": "age spots", "Sagging Jowls": "loose skin", "Frontal Rhytids": "forehead ridges", "Periorbital Hollows": "sunken eyes", "Vertical Lip Lines": "mouth wrinkles", "Age-related Telangiectasia": "capillaries"})
hair_tex_data = add_none_dict({"Afro-Textured": "structural coils", "Wavy (Type 2)": "S-shape", "Curly (Type 3)": "ringlets", "Straight (Sleek)": "linear", "Coarse & Wiry": "irregular graying", "Fine & Wispy": "translucent", "Disheveled & Matted": "weathered", "Braided / Cornrows": "interlocking"})
hair_col_data = add_none_dict({"Jet black": "Jet black", "Deep espresso brown": "Espresso", "Light chestnut brown": "Sandy", "Ash blonde": "Cool blonde", "Golden blonde": "Warm blonde", "10% Salt & Pepper": "sparse grey", "30% Salt & Pepper": "mixed grey", "50% Salt & Pepper": "even grey", "70% Salt & Pepper": "mostly grey"})
light_data = add_none_dict({"Rembrandt Lighting": "triangle light", "Cold Rim Lighting": "blue backlight", "Chiaroscuro": "contrast", "Teal and Orange": "cinematic", "Volumetric God Rays": "linear light", "Cinematic Golden Hour": "warm glow", "High-Key Studio": "bright", "Low-Key Moody": "mysterious", "Neon Cyberpunk": "edge light", "Hard Top Lighting": "harsh shadow", "Flickering Candlelight": "unsteady", "Soft Professional Softbox": "velvety"})
camera_data = add_none_dict({"85mm Lens, Eye-Level": "no distortion", "100mm Macro, Close-Up": "extreme detail", "50mm Lens, Dutch Angle": "tilted tension", "35mm Lens, Low-Angle": "hero shot", "24mm Wide-Angle, High-Angle": "thinning", "200mm Telephoto, Profile View": "compressed", "50mm Lens, Top-Down": "design focus", "85mm Lens, Three-Quarter": "standard"})
pic_size_data = add_none(["Aspect Ratio 4:5", "Aspect Ratio 16:9", "Aspect Ratio 2.39:1", "Aspect Ratio 1:1", "Aspect Ratio 9:16"])
material_data = add_none(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin", "Prosthetic Adhesive", "Matte Sealer", "Alcohol Palette", "Granulation Tissue"])

# 3. بدنه داشبورد
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("Actor Reference <span class='required-star'>*</span>", ["None", "No", "Yes"], unsafe_allow_html=True)
        age_sel = st.selectbox("Age Range <span class='required-star'>*</span>", list(age_data.keys()), unsafe_allow_html=True)
    with r1c2:
        gender_sel = st.selectbox("Gender <span class='required-star'>*</span>", list(gender_data.keys()), unsafe_allow_html=True)
        nat_sel = st.selectbox("Nationality <span class='required-star'>*</span>", list(nat_data.keys()), unsafe_allow_html=True)

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

# 4. منطق ساخت Master Prompt
def fmt(p, v, d=None):
    if v == "None" or not v: return ""
    desc = f" ({d[v]})" if d and v in d and d[v] else ""
    return f"{p}{v}{desc}"

p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
p_sfx = f" [SFX: {sfx_sel} ({sfx_data[sfx_sel]})]" if sfx_sel != "None" else ""
p_size = f" Aspect Ratio {size_sel}" if size_sel != "None" else ""

final_prompt = f"{p_actor}A professional cinematic {p_size} portrait of a {fmt('', gender_sel, gender_data)} {fmt('', age_sel, age_data)} {fmt('', nat_sel, nat_data)}{fmt(' from the ', era_sel, era_data)}. {fmt('Character: ', char_sel, char_data)}. {fmt('Grooming: ', groom_sel, groom_data)}. {fmt('Hair: ', h_col, hair_col_data)}{fmt(', Texture: ', h_tex, hair_tex_data)}. {fmt('Skin: ', aging_sel, aging_data)}.{p_sfx}. {fmt('Finish: ', mat_sel)}. {fmt('Technical: ', light_sel, light_data)}{fmt(', ', cam_sel, camera_data)}, 8k, raw photography, subsurface scattering."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown('<div class="lang-guide">لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>Please click on the text inside the box to copy<br>يرجى الضغط على النص داخل المربع أدناه للنسخ</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
