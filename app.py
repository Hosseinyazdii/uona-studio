import streamlit as st

# 1. تنظیمات اصلی
st.set_page_config(page_title="UONA STUDIO | AI DASHBOARD", layout="wide")

# 2. استایل اختصاصی (گرادینت سرمه‌ای تیره + متون فیروزه‌ای)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* گرادینت سرمه‌ای تیره برای کل صفحه */
    .stApp {
        background: linear-gradient(135deg, #0a192f 0%, #02060c 100%) !important;
        overflow-y: auto !important;
    }

    .header-box {
        background: rgba(0, 212, 255, 0.05); backdrop-filter: blur(10px);
        border-bottom: 2px solid #00d4ff; padding: 20px; margin-bottom: 30px; text-align: center;
    }
    .header-title {
        color: #00d4ff; font-family: 'Cinzel', serif; font-size: 2.5rem; letter-spacing: 8px;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5); margin: 0;
    }
    
    /* استایل لیبل‌ها و ستاره قرمز */
    .label-text { color: #00d4ff; font-family: 'Montserrat', sans-serif; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; margin-bottom: 5px; }
    .star { color: #ff4b4b; }

    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 12px; font-weight: 900; font-size: 1.4rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 25px; border-radius: 0 0 8px 8px; border-left: 10px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.1rem; line-height: 1.7; min-height: 520px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); user-select: all !important; }
    
    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO | PROMPT BUILDER</p></div>', unsafe_allow_html=True)

# 3. توابع کمکی برای مدیریت دیتا
def add_none(data):
    if isinstance(data, dict):
        new_dict = {"None": ""}
        new_dict.update(data)
        return new_dict
    return ["None"] + data

# --- دیتابیس کامل (۱۰۰٪ از شیت‌ها) ---
gender_data = add_none({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours", "Androgynous": "blend features"})
age_data = add_none({"Child / Pre-adolescent": "textureless skin", "Adolescent / Teenager": "oily skin texture", "Young Adult (Early 20s)": "peak elasticity", "Middle-aged (Late 40s)": "initial sagging", "Elderly / Senior": "collagen loss", "Ancient / Centenarian": "paper-thin skin"})
nat_data = add_none({"Iranian": "Indo-Aryan features, prominent nasal bridge", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Saudi": "Peninsular Arab features", "Kuwaiti": "Northern Gulf features", "Syrian": "Levantine features", "American": "Diverse features", "Indian": "South Asian features", "Chinese": "East Asian features", "African": "Sub-Saharan features", "European": "Caucasian features", "Turkish": "Eurasian features"})
era_data = add_none({"Stone Age / Prehistoric": "Primitive aesthetic", "BCE (Before Common Era)": "Ancient styling", "Pre-Islamic Era": "Traditional heritage", "Ancient Era (Hellenistic/Roman)": "Classical features", "Medieval / Dark Ages": "Gritty textures", "200 Years Ago": "Regency style", "150 Years Ago": "Victorian Era", "100 Years Ago": "Roaring 20s", "50 Years Ago": "1970s Retro", "Contemporary / Modern Day": "Current lighting", "Futuristic / Cyberpunk": "Neon accents", "Post-Apocalyptic": "Weathered textures"})
char_data = add_none({"Heroic Warrior": "Strong jawline", "Sinister Villain": "Harsh shadows", "Scholar / Intellectual": "Refined appearance", "Royal / Aristocratic": "Elegant posture", "Mercenary / Outlaw": "Rugged textures", "Mystic / Shaman": "Otherworldly look", "Corporate Executive / CEO": "Clean-cut", "Elite Athlete": "Defined muscularity", "Bohemian Artist": "Creative styling", "Average Citizen": "Naturalistic", "Blue-collar / Technician": "Grime", "Academic Student": "Youthful", "High-fashion Model": "Angular features", "Retiree / Grandparent": "Dignified aging", "Urban / Street Style": "Modern edge", "Rural / Outdoorsman": "Sun-damaged skin", "Red Carpet / Gala Guest": "Glamorous", "Ailing / Sickly Character": "Pale skin"})
groom_data = add_none({"Saudi Anchor Beard": "sharp angled", "Pyramidal Moustache": "wide base", "Clean Shaven": "smooth skin", "Light Stubble": "short even", "Heavy Stubble": "rough texture", "Designer Stubble": "trimmed edges", "Shadow Fade Beard": "faded sides", "Goatee (No Mustache)": "chin beard", "Classic Goatee": "connected", "Van Dyke": "pointed", "Anchor Beard": "thin defined", "Short Boxed Beard": "square edges", "Medium Boxed Beard": "clean appearance", "Long Full Beard": "natural growth", "Unkempt Beard": "messy", "Scruffy Beard": "patchy", "Wild Beard": "chaotic", "Bedouin Beard": "weathered", "Viking Beard": "braided", "Medieval Beard": "period growth", "Philosopher Beard": "soft", "Warrior Beard": "rugged", "Graying Patches": "gray strands", "Split Texture Beard": "dual-textured", "Short Sideburns": "above ear", "Mid-Ear Sideburns": "tragus level", "Long Sideburns": "ear lobe", "Extra-Long Sideburns": "pass lobe", "High Sideburns": "temple level", "Tapered Length": "faded", "Square Sideburns": "clean edges", "Pointed Sideburns": "triangle point", "Rounded Sideburns": "circular", "Pencil Sideburns": "thin line", "Flared Sideburns": "wide look", "Angled Sideburns": "slanted", "Mutton Chops": "wide full", "Friendly Mutton Chops": "connected", "Soul Patch": "below lip"})
sfx_data = add_none({"Fresh Katana Slash": "active bleeding", "Glass Laceration": "embedded glass", "Blunt Force Contusion": "swelling", "3-Day Old Wound": "scabbing", "1-Week Old Wound": "granulation", "1-Month Old Scar": "maturation", "1-Year Old Keloid Scar": "hypertrophic", "5-Year Old Atrophic Scar": "pale white", "Fresh Periorbital Hematoma": "bruising", "24-Hour Old Bruise": "deep purple", "3-Day Old Bruise": "greenish-yellow", "15-Day Old Fading Bruise": "fading spots", "Chemical Acid Burn": "melting tissue", "1st Degree Sunburn": "redness", "2nd Degree Burn": "blisters", "Bilateral Vitiligo": "white patches", "Diffuse Hyperpigmentation": "dark spots"})
aging_data = add_none({"Deep Nasolabial Folds": "smile lines", "Pronounced Crow's Feet": "eye wrinkles", "Hooded Eyelids / Ptosis": "sagging lids", "Dermal Crepiness": "paper skin", "Visible Liver Spots": "age spots", "Sagging Jowls": "loose skin", "Frontal Rhytids": "forehead ridges", "Periorbital Hollows": "sunken eyes", "Vertical Lip Lines": "mouth wrinkles", "Age-related Telangiectasia": "capillaries"})
hair_tex_data = add_none({"Afro-Textured": "structural coils", "Wavy (Type 2)": "S-shape", "Curly (Type 3)": "ringlets", "Straight (Sleek)": "linear", "Coarse & Wiry": "irregular graying", "Fine & Wispy": "translucent", "Disheveled & Matted": "weathered", "Braided / Cornrows": "interlocking"})
hair_col_data = add_none({"Jet black": "Jet black", "Deep espresso brown": "Espresso", "Light chestnut brown": "Sandy", "Ash blonde": "Cool blonde", "Golden blonde": "Warm blonde", "10% Salt & Pepper": "sparse grey", "30% Salt & Pepper": "mixed grey", "50% Salt & Pepper": "even grey", "70% Salt & Pepper": "mostly grey"})
light_data = add_none({"Rembrandt Lighting": "triangle light", "Cold Rim Lighting": "blue backlight", "Chiaroscuro": "contrast", "Teal and Orange": "cinematic", "Volumetric God Rays": "linear light", "Cinematic Golden Hour": "warm glow", "High-Key Studio": "bright", "Low-Key Moody": "mysterious", "Neon Cyberpunk": "edge light", "Hard Top Lighting": "harsh shadow", "Flickering Candlelight": "unsteady", "Soft Professional Softbox": "velvety"})
camera_data = add_none({"85mm Lens, Eye-Level Shot": "no distortion", "100mm Macro, Close-Up": "extreme detail", "50mm Lens, Dutch Angle": "tilted tension", "35mm Lens, Low-Angle": "hero shot", "24mm Wide-Angle, High-Angle": "thinning", "200mm Telephoto, Profile View": "compressed", "50mm Lens, Top-Down": "design focus", "85mm Lens, Three-Quarter View": "standard"})
pic_size_data = add_none(["Aspect Ratio 4:5 (Portrait)", "Aspect Ratio 16:9 (Widescreen)", "Aspect Ratio 2.39:1 (Anamorphic)", "Aspect Ratio 1:1 (Square)", "Aspect Ratio 9:16 (Vertical)"])
material_data = add_none(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin Finish", "Prosthetic Adhesive", "Matte Sealer", "Alcohol-activated Palette", "Granulation Tissue"])

# 4. بدنه داشبورد
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        st.markdown('<p class="label-text">Actor Reference <span class="star">*</span></p>', unsafe_allow_html=True)
        actor = st.selectbox("", ["None", "No", "Yes"], label_visibility="collapsed")
        st.markdown('<p class="label-text">Age Range <span class="star">*</span></p>', unsafe_allow_html=True)
        age_sel = st.selectbox("", list(age_data.keys()), label_visibility="collapsed")
    with r1c2:
        st.markdown('<p class="label-text">Gender <span class="star">*</span></p>', unsafe_allow_html=True)
        gender_sel = st.selectbox("", list(gender_data.keys()), label_visibility="collapsed")
        st.markdown('<p class="label-text">Nationality <span class="star">*</span></p>', unsafe_allow_html=True)
        nat_sel = st.selectbox("", list(nat_data.keys()), label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        st.markdown('<p class="label-text">Time Period</p>', unsafe_allow_html=True)
        era_sel = st.selectbox("", list(era_data.keys()), label_visibility="collapsed")
        st.markdown('<p class="label-text">Hair & Beard Color</p>', unsafe_allow_html=True)
        h_col = st.selectbox("", list(hair_col_data.keys()), label_visibility="collapsed")
    with r2c2:
        st.markdown('<p class="label-text">Character Type</p>', unsafe_allow_html=True)
        char_sel = st.selectbox("", list(char_data.keys()), label_visibility="collapsed")
        st.markdown('<p class="label-text">Grooming Style</p>', unsafe_allow_html=True)
        groom_sel = st.selectbox("", list(groom_data.keys()), label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        st.markdown('<p class="label-text">SFX Makeup / Trauma</p>', unsafe_allow_html=True)
        sfx_sel = st.selectbox("", list(sfx_data.keys()), label_visibility="collapsed")
        st.markdown('<p class="label-text">Aging Details</p>', unsafe_allow_html=True)
        aging_sel = st.selectbox("", list(aging_data.keys()), label_visibility="collapsed")
        st.markdown('<p class="label-text">Lighting Style</p>', unsafe_allow_html=True)
        light_sel = st.selectbox("", list(light_data.keys()), label_visibility="collapsed")
    with r3c2:
        st.markdown('<p class="label-text">Material Finish</p>', unsafe_allow_html=True)
        mat_sel = st.selectbox("", material_data, label_visibility="collapsed")
        st.markdown('<p class="label-text">Hair Texture</p>', unsafe_allow_html=True)
        h_tex = st.selectbox("", list(hair_tex_data.keys()), label_visibility="collapsed")
        st.markdown('<p class="label-text">Pic Size</p>', unsafe_allow_html=True)
        size_sel = st.selectbox("", pic_size_data, label_visibility="collapsed")
    
    st.markdown('<p class="label-text">Camera, Lens & Angle</p>', unsafe_allow_html=True)
    cam_sel = st.selectbox("", list(camera_data.keys()), label_visibility="collapsed")

# 5. منطق ساخت Master Prompt
def fmt(p, v, d=None):
    if v == "None" or not v: return ""
    desc = f" ({d[v]})" if d and v in d and d[v] else ""
    return f"{p}{v}{desc}"

p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
p_sfx = f" [SFX: {sfx_sel} ({sfx_data[sfx_sel]})]" if sfx_sel != "None" else ""
p_size = f" Aspect Ratio {size_sel}" if size_sel != "None" else ""

final_prompt = f"{p_actor}A professional cinematic {p_size} portrait of a {fmt('', gender_sel, gender_data)} {fmt('', age_sel, age_data)} {fmt('', nat_sel, nat_data)}{fmt(' from the ', era_sel, era_data)}. {fmt('Character: ', char_sel, char_data)}. {fmt('Grooming: ', groom_sel, groom_data)}. {fmt('Hair: ', h_col, hair_col_data)}{fmt(', Texture: ', h_tex, hair_tex_data)}. {fmt('Skin: ', aging_sel, aging_data)}.{p_sfx}. {fmt('Finish: ', mat_sel)}. {fmt('Technical Specs: ', light_sel, light_data)}{fmt(', ', cam_sel, camera_data)}, 8k, raw photography, subsurface scattering."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; color:#00d4ff; font-family:Tahoma; font-size:0.85rem; padding:10px;">لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>Please click on the text inside the box below to copy</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
