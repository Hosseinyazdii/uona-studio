import streamlit as st
from datetime import datetime

# 1. تنظیمات پایه و مخفی‌سازی UI سیستم
st.set_page_config(page_title="UONA STUDIO | AI DASHBOARD", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* مخفی کردن منوهای پیش‌فرض استریم‌لیت برای یوزرها */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* تنظیم گرادینت سرمه‌ای تیره عمیق */
    .stApp {
        background: radial-gradient(circle, #0a192f 0%, #02060c 100%) !important;
        overflow-y: auto !important;
    }

    .header-box {
        background: rgba(0, 212, 255, 0.05); backdrop-filter: blur(10px);
        border-bottom: 2px solid #00d4ff; padding: 25px; margin-bottom: 35px; text-align: center;
    }
    .header-title {
        color: #00d4ff; font-family: 'Cinzel', serif; font-size: 2.5rem; letter-spacing: 10px;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5); margin: 0;
    }
    
    .label-text { color: #00d4ff; font-family: 'Montserrat', sans-serif; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; margin-top: 15px; margin-bottom: 5px; }
    .star { color: #ff4b4b; font-weight: bold; }

    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 12px; font-weight: 900; font-size: 1.4rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat', sans-serif; }
    .master-box { background-color: #ffffff; color: #111; padding: 30px; border-radius: 0 0 8px 8px; border-left: 10px solid #00f2ff; font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.8; min-height: 520px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); user-select: all !important; }
    
    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 8px !important; }

    .footer {
        width: 100%; color: #556a8b; text-align: center; padding: 30px 0; font-family: 'Montserrat', sans-serif;
        border-top: 1px solid rgba(0, 212, 255, 0.1); margin-top: 60px;
    }
    .footer-rights { color: #00d4ff; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO</p></div>', unsafe_allow_html=True)

# 2. دیتابیس کامل (۱۰۰٪ دیتای اکسل)
def get_list(data): return ["None"] + data
def get_dict(data):
    d = {"None": ""}
    d.update(data)
    return d

gender_d = get_dict({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours", "Androgynous": "blend features"})
age_d = get_dict({"Child / Pre-adolescent": "textureless skin", "Adolescent / Teenager": "oily skin texture", "Young Adult (Early 20s)": "peak elasticity", "Middle-aged (Late 40s)": "initial sagging", "Elderly / Senior": "collagen loss", "Ancient / Centenarian": "paper-thin skin"})
nat_d = get_dict({"Iranian": "Indo-Aryan features, prominent nasal bridge", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Saudi": "Peninsular Arab features", "Kuwaiti": "Northern Gulf features", "Syrian": "Levantine features", "American": "Diverse North American features", "Indian": "South Asian features", "Chinese": "East Asian features", "African": "Sub-Saharan features", "European": "Caucasian features", "Turkish": "Eurasian features"})
era_d = get_dict({"Stone Age / Prehistoric": "Primitive aesthetic", "BCE (Before Common Era)": "Ancient civilization styling", "Pre-Islamic Era": "Traditional heritage", "Ancient Era (Hellenistic/Roman)": "Classical features", "Medieval / Dark Ages": "Gritty textures", "200 Years Ago": "Regency style", "150 Years Ago": "Victorian Era", "100 Years Ago": "Roaring 20s", "50 Years Ago": "1970s Retro", "Contemporary / Modern Day": "Current lighting", "Futuristic / Cyberpunk": "Neon accents", "Post-Apocalyptic": "Weathered textures"})
char_d = get_dict({"Heroic Warrior": "Strong jawline", "Sinister Villain": "Harsh shadows", "Scholar / Intellectual": "Refined appearance", "Royal / Aristocratic": "Elegant posture", "Mercenary / Outlaw": "Rugged textures", "Mystic / Shaman": "Otherworldly look", "Corporate Executive / CEO": "Clean-cut", "Elite Athlete": "Defined muscularity", "Bohemian Artist": "Creative styling", "Average Citizen": "Naturalistic", "Blue-collar / Technician": "Grime", "Academic Student": "Youthful", "High-fashion Model": "Angular features", "Retiree / Grandparent": "Dignified aging", "Urban / Street Style": "Modern edge", "Rural / Outdoorsman": "Sun-damaged skin", "Red Carpet / Gala Guest": "Glamorous", "Ailing / Sickly Character": "Pale skin"})
groom_d = get_dict({"Saudi Anchor Beard": "sharp angled", "Pyramidal Moustache": "wide base", "Clean Shaven": "smooth skin", "Light Stubble": "short even", "Heavy Stubble": "rough texture", "Designer Stubble": "trimmed edges", "Shadow Fade Beard": "faded sides", "Goatee (No Mustache)": "chin beard", "Classic Goatee": "connected", "Van Dyke": "pointed", "Anchor Beard": "thin defined", "Short Boxed Beard": "square edges", "Medium Boxed Beard": "clean appearance", "Long Full Beard": "natural growth", "Unkempt Beard": "messy", "Scruffy Beard": "patchy", "Wild Beard": "chaotic", "Bedouin Beard": "weathered", "Viking Beard": "braided", "Medieval Beard": "period growth", "Philosopher Beard": "soft", "Warrior Beard": "rugged", "Graying Patches": "gray strands", "Split Texture Beard": "dual-textured", "Short Sideburns": "above ear", "Mid-Ear Sideburns": "tragus level", "Long Sideburns": "ear lobe", "Extra-Long Sideburns": "pass lobe", "High Sideburns": "temple level", "Tapered Length": "faded", "Square Sideburns": "clean edges", "Pointed Sideburns": "triangle point", "Rounded Sideburns": "circular", "Pencil Sideburns": "thin line", "Flared Sideburns": "wide look", "Angled Sideburns": "slanted", "Mutton Chops": "wide full", "Friendly Mutton Chops": "connected", "Soul Patch": "below lip"})
sfx_d = get_dict({"Fresh Katana Slash": "active bleeding", "Glass Laceration": "embedded glass", "Blunt Force Contusion": "swelling", "3-Day Old Wound": "scabbing", "1-Week Old Wound": "granulation", "1-Month Old Scar": "maturation", "1-Year Old Keloid Scar": "hypertrophic", "5-Year Old Atrophic Scar": "pale white", "Fresh Periorbital Hematoma": "bruising", "24-Hour Old Bruise": "deep purple", "3-Day Old Bruise": "greenish-yellow", "15-Day Old Fading Bruise": "fading spots", "Chemical Acid Burn": "melting tissue", "1st Degree Sunburn": "redness", "2nd Degree Burn": "blisters", "Bilateral Vitiligo": "white patches", "Diffuse Hyperpigmentation": "dark spots"})
aging_d = get_dict({"Deep Nasolabial Folds": "smile lines", "Pronounced Crow's Feet": "eye wrinkles", "Hooded Eyelids / Ptosis": "sagging lids", "Dermal Crepiness": "paper skin", "Visible Liver Spots": "age spots", "Sagging Jowls": "loose skin", "Frontal Rhytids": "forehead ridges", "Periorbital Hollows": "sunken eyes", "Vertical Lip Lines": "mouth wrinkles", "Age-related Telangiectasia": "capillaries"})
hair_tex_d = get_dict({"Afro-Textured": "structural coils", "Wavy (Type 2)": "S-shape", "Curly (Type 3)": "ringlets", "Straight (Sleek)": "linear", "Coarse & Wiry": "irregular graying", "Fine & Wispy": "translucent", "Disheveled & Matted": "weathered", "Braided / Cornrows": "interlocking"})
hair_col_d = get_dict({"Jet black": "Jet black", "Deep espresso brown": "Espresso", "Light chestnut brown": "Sandy", "Ash blonde": "Cool blonde", "Golden blonde": "Warm blonde", "10% Salt & Pepper": "sparse grey", "30% Salt & Pepper": "mixed grey", "50% Salt & Pepper": "even grey", "70% Salt & Pepper": "mostly grey"})
light_d = get_dict({"Rembrandt Lighting": "triangle light", "Cold Rim Lighting": "blue backlight", "Chiaroscuro": "contrast", "Teal and Orange": "cinematic", "Volumetric God Rays": "linear light", "Cinematic Golden Hour": "warm glow", "High-Key Studio": "bright", "Low-Key Moody": "mysterious", "Neon Cyberpunk": "edge light", "Hard Top Lighting": "harsh shadow", "Flickering Candlelight": "unsteady", "Soft Professional Softbox": "velvety"})
camera_d = get_dict({"85mm Lens, Eye-Level Shot": "no distortion", "100mm Macro, Close-Up": "extreme detail", "50mm Lens, Dutch Angle": "tilted tension", "35mm Lens, Low-Angle": "hero shot", "24mm Wide-Angle, High-Angle": "thinning", "200mm Telephoto, Profile View": "compressed", "50mm Lens, Top-Down": "design focus", "85mm Lens, Three-Quarter View": "standard"})
size_list = get_list(["Aspect Ratio 4:5 (Portrait)", "Aspect Ratio 16:9 (Widescreen)", "Aspect Ratio 2.39:1 (Anamorphic)", "Aspect Ratio 1:1 (Square)", "Aspect Ratio 9:16 (Vertical)"])
mat_list = get_list(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin Finish", "Prosthetic Adhesive", "Matte Sealer", "Alcohol Palette", "Granulation Tissue"])

# 3. بدنه اصلی
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        st.markdown('<p class="label-text">Actor Reference <span class="star">*</span></p>', unsafe_allow_html=True)
        actor = st.selectbox("", ["None", "No", "Yes"], key="actor", label_visibility="collapsed")
        st.markdown('<p class="label-text">Age Range <span class="star">*</span></p>', unsafe_allow_html=True)
        age_sel = st.selectbox("", list(age_d.keys()), key="age", label_visibility="collapsed")
    with r1c2:
        st.markdown('<p class="label-text">Gender <span class="star">*</span></p>', unsafe_allow_html=True)
        gender_sel = st.selectbox("", list(gender_d.keys()), key="gender", label_visibility="collapsed")
        st.markdown('<p class="label-text">Nationality <span class="star">*</span></p>', unsafe_allow_html=True)
        nat_sel = st.selectbox("", list(nat_d.keys()), key="nat", label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        st.markdown('<p class="label-text">Time Period</p>', unsafe_allow_html=True)
        era_sel = st.selectbox("", list(era_d.keys()), key="era", label_visibility="collapsed")
        st.markdown('<p class="label-text">Hair & Beard Color</p>', unsafe_allow_html=True)
        h_col = st.selectbox("", list(hair_col_data.keys() if 'hair_col_data' in locals() else hair_col_d.keys()), key="h_col", label_visibility="collapsed")
    with r2c2:
        st.markdown('<p class="label-text">Character Type</p>', unsafe_allow_html=True)
        char_sel = st.selectbox("", list(char_d.keys()), key="char", label_visibility="collapsed")
        st.markdown('<p class="label-text">Grooming Style</p>', unsafe_allow_html=True)
        groom_sel = st.selectbox("", list(groom_d.keys()), key="groom", label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        st.markdown('<p class="label-text">SFX Makeup / Trauma</p>', unsafe_allow_html=True)
        sfx_sel = st.selectbox("", list(sfx_d.keys()), key="sfx", label_visibility="collapsed")
        st.markdown('<p class="label-text">Aging Details</p>', unsafe_allow_html=True)
        aging_sel = st.selectbox("", list(aging_d.keys()), key="aging", label_visibility="collapsed")
        st.markdown('<p class="label-text">Lighting Style</p>', unsafe_allow_html=True)
        light_sel = st.selectbox("", list(light_d.keys()), key="light", label_visibility="collapsed")
    with r3c2:
        st.markdown('<p class="label-text">Material Finish</p>', unsafe_allow_html=True)
        mat_sel = st.selectbox("", mat_list, key="mat", label_visibility="collapsed")
        st.markdown('<p class="label-text">Hair Texture</p>', unsafe_allow_html=True)
        h_tex = st.selectbox("", list(hair_tex_d.keys()), key="htex", label_visibility="collapsed")
        st.markdown('<p class="label-text">Pic Size</p>', unsafe_allow_html=True)
        size_sel = st.selectbox("", size_list, key="size", label_visibility="collapsed")
    
    st.markdown('<p class="label-text">Camera, Lens & Angle</p>', unsafe_allow_html=True)
    cam_sel = st.selectbox("", list(camera_d.keys()), key="cam", label_visibility="collapsed")

# 4. منطق ساخت Master Prompt
def fmt(p, v, d=None):
    if v == "None" or not v: return ""
    desc = f" ({d[v]})" if d and v in d and d[v] else ""
    return f"{p}{v}{desc}"

p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
p_sfx = f" [SFX STUDY: Apply {sfx_sel} ({sfx_d[sfx_sel]}) SFX as a makeup layer]." if sfx_sel != "None" else ""
p_size = f" Aspect Ratio {size_sel}" if size_sel != "None" else ""

final_prompt = f"{p_actor}A professional cinematic {p_size} portrait of a {fmt('', gender_sel, gender_d)} {fmt('', age_sel, age_d)} {fmt('', nat_sel, nat_d)}{fmt(' from the ', era_sel, era_d)}. {fmt('Character: ', char_sel, char_d)}. {fmt('Grooming: ', groom_sel, groom_d)}. {fmt('Hair: ', h_col, hair_col_d)}{fmt(', Texture: ', h_tex, hair_tex_d)}. {fmt('Skin: ', aging_sel, aging_d)}.{p_sfx} {fmt('Finish Material: ', mat_sel)}. {fmt('Technical Specs: ', light_sel, light_d)}{fmt(', ', cam_sel, camera_d)}, 8k, raw photography, subsurface scattering, focus on prosthetic makeup accuracy."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; color:#00d4ff; font-family:Tahoma; font-size:0.85rem; padding:10px;">لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>Please click on the text inside the box below to copy</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)

# 5. فوتر اختصاصی
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} <span class="footer-rights">UONA GROUP</span>. ALL RIGHTS RESERVED. <br>
        PROFESSIONAL CINEMATIC CHARACTER DESIGN AI SYSTEM | EST. 2024
    </div>
    """, unsafe_allow_html=True)
