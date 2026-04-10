import streamlit as st
from datetime import datetime

# 1. تنظیمات پایه و امنیت بصری
st.set_page_config(page_title="UONA STUDIO | AI DESIGN SYSTEM", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@200;400;700;900&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}

    /* تم سرمه‌ای عمیق غول‌های فناوری */
    .stApp {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        overflow-x: hidden;
    }

    /* هدر مدرن با لوگو و تایتل درخشان */
    .nav-bar {
        display: flex;
        align-items: center;
        padding: 25px 60px;
        background: rgba(2, 6, 12, 0.7);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(0, 242, 255, 0.2);
        justify-content: space-between;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    .logo-container { display: flex; align-items: center; gap: 20px; }
    .nav-title-ultra { 
        font-family: 'Cinzel'; color: #00f2ff; font-size: 3.5rem; font-weight: 900; 
        letter-spacing: 8px; margin: 0; text-shadow: 0 0 25px rgba(0, 242, 255, 0.6);
        line-height: 1;
    }
    .nav-slogan { font-family: 'Montserrat'; color: #ffffff; font-size: 0.8rem; letter-spacing: 6px; opacity: 0.7; text-transform: uppercase; margin-top: 5px; }

    /* استایل کارت‌های پورتال ورودی */
    .portal-container { padding: 80px 10%; text-align: center; }
    .portal-headline { color: white; font-family: 'Cinzel'; font-size: 2.2rem; letter-spacing: 5px; margin-bottom: 60px; opacity: 0.9; }
    
    .module-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 25px;
        padding: 50px 20px;
        text-align: center;
        transition: all 0.5s cubic-bezier(0.2, 1, 0.3, 1);
        backdrop-filter: blur(15px);
        min-height: 320px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .module-card:hover {
        background: rgba(0, 242, 255, 0.08);
        border-color: #00f2ff;
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0, 242, 255, 0.15);
    }
    .icon-box {
        width: 100px; height: 100px;
        background: rgba(0, 242, 255, 0.05);
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 25px;
        font-size: 45px;
        border: 1px solid rgba(0, 242, 255, 0.2);
    }
    .module-name { font-family: 'Cinzel'; color: white; font-size: 1.6rem; letter-spacing: 3px; margin-bottom: 10px; }
    .module-desc { font-family: 'Montserrat'; color: #556a8b; font-size: 0.75rem; letter-spacing: 1px; text-transform: uppercase; }
    .status-badge { color: #ff4b4b; font-size: 0.7rem; font-weight: 900; letter-spacing: 2px; margin-top: 15px; text-transform: uppercase; border: 1px solid #ff4b4b; padding: 2px 10px; border-radius: 4px; }

    /* دکمه‌های استریم‌لیت در صفحه پورتال */
    .stButton > button {
        background: transparent !important; color: #00f2ff !important;
        border: 1px solid #00f2ff !important; border-radius: 50px !important;
        font-family: 'Montserrat' !important; font-weight: 700 !important;
        transition: all 0.3s !important; text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton > button:hover { background: #00f2ff !important; color: #000 !important; box-shadow: 0 0 20px #00f2ff; }

    /* فرمول پرامپت نهایی */
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 15px; font-weight: 900; font-size: 1.4rem; border-radius: 12px 12px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { background-color: #ffffff; color: #111; padding: 35px; border-radius: 0 0 12px 12px; border-left: 12px solid #00f2ff; font-family: 'Montserrat'; font-size: 1.15rem; line-height: 1.8; min-height: 520px; box-shadow: 0 30px 60px rgba(0,0,0,0.5); user-select: all !important; }
    
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; margin-top: 15px; }
    .star { color: #ff4b4b; font-weight: bold; }
    
    div[data-baseweb="select"] > div, .stTextInput>div>div>input { background-color: rgba(26, 58, 90, 0.6) !important; color: white !important; border: 1px solid rgba(0, 212, 255, 0.4) !important; border-radius: 10px !important; }

    .footer { width: 100%; color: #ffffff; text-align: center; padding: 50px 0; font-family: 'Montserrat'; border-top: 1px solid rgba(0, 242, 255, 0.1); margin-top: 100px; background: rgba(0,0,0,0.3); }
    .footer-rights { color: #00f2ff; font-weight: 900; font-size: 1.3rem; text-shadow: 0 0 10px rgba(0, 242, 255, 0.5); letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

# مدیریت ناوبری اپلیکیشن
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- هدر ثابت (غول فناوری) ---
logo_col1, logo_col2 = st.columns([1, 4])
with logo_col1:
    try:
        st.image("image.png", width=120)
    except:
        st.markdown("<div style='width:100px; height:100px; background:#00f2ff; border-radius:15px; display:flex; align-items:center; justify-content:center; color:black; font-weight:900;'>UONA</div>", unsafe_allow_html=True)

with logo_col2:
    st.markdown("""
        <div style='padding-top:10px;'>
            <h1 class="nav-title-ultra">UONA STUDIO</h1>
            <div class="nav-slogan">The Art of Cinematic Transformation</div>
        </div>
        """, unsafe_allow_html=True)

# --- صفحه پورتال (Landing Page) ---
if st.session_state.page == 'home':
    st.markdown("<div class='portal-container'>", unsafe_allow_html=True)
    st.markdown("<p class='portal-headline'>SELECT YOUR DESIGN MODULE</p>", unsafe_allow_html=True)
    
    p_col1, p_col2, p_col3, p_col4 = st.columns(4)
    
    with p_col1:
        st.markdown('<div class="module-card"><div class="icon-box">🎬</div><div class="module-name">CINEMATIC</div><div class="module-desc">Feature Films & VFX</div></div>', unsafe_allow_html=True)
        if st.button("OPEN MODULE", key="btn_cine"):
            st.session_state.page = 'cinematic'
            st.rerun()

    with p_col2:
        st.markdown('<div class="module-card"><div class="icon-box">📺</div><div class="module-name">TV SERIES</div><div class="module-desc">Episodic Character Design</div></div>', unsafe_allow_html=True)
        if st.button("OPEN MODULE", key="btn_series"):
            st.session_state.page = 'cinematic' # به دیتابیس فعلی وصل می‌شود
            st.rerun()

    with p_col3:
        st.markdown('<div class="module-card"><div class="icon-box">🎭</div><div class="module-name">THEATER</div><div class="module-desc">Stage & Live Performance</div><div class="status-badge">Coming Soon</div></div>', unsafe_allow_html=True)
        st.button("LOCKED", disabled=True, key="btn_theater")

    with p_col4:
        st.markdown('<div class="module-card"><div class="icon-box">👠</div><div class="module-name">FASHION</div><div class="module-desc">Editorial & High-Fashion</div><div class="status-badge">Coming Soon</div></div>', unsafe_allow_html=True)
        st.button("LOCKED", disabled=True, key="btn_fashion")
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- ماژول Cinematic (دیتابیس کامل) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK TO PORTAL"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("<h2 style='color:#00f2ff; font-family:Cinzel; letter-spacing:4px; margin-top:20px;'>🎞️ CINEMATIC DESIGN MODULE</h2>", unsafe_allow_html=True)

    # دیتابیس جامع ۱۰۰٪
    def add_none(data):
        if isinstance(data, dict):
            d = {"None": ""}; d.update(data); return d
        return ["None"] + data

    gender_d = add_none({"Masculine / Male": "strong bone structure", "Feminine / Female": "softer facial contours", "Androgynous": "blend features"})
    age_d = add_none({"Child / Pre-adolescent": "textureless skin", "Adolescent / Teenager": "oily skin texture", "Young Adult (Early 20s)": "peak elasticity", "Middle-aged (Late 40s)": "initial sagging", "Elderly / Senior": "collagen loss", "Ancient / Centenarian": "paper-thin skin"})
    nat_d = add_none({"Iranian": "Indo-Aryan features, prominent nasal bridge", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Saudi": "Peninsular Arab features", "Kuwaiti": "Northern Gulf features", "Syrian": "Levantine features", "American": "Diverse features", "Indian": "South Asian features", "Chinese": "East Asian features", "African": "Sub-Saharan features", "European": "Caucasian features", "Turkish": "Eurasian features"})
    era_d = add_none({"Stone Age / Prehistoric": "Primitive aesthetic", "BCE (Before Common Era)": "Ancient styling", "Pre-Islamic Era": "Traditional heritage", "Ancient Era (Hellenistic/Roman)": "Classical features", "Medieval / Dark Ages": "Gritty textures", "200 Years Ago": "Regency style", "150 Years Ago": "Victorian Era", "100 Years Ago": "Roaring 20s", "50 Years Ago": "1970s Retro", "Contemporary / Modern Day": "Current lighting", "Futuristic / Cyberpunk": "Neon accents", "Post-Apocalyptic": "Weathered textures"})
    char_d = add_none({"Heroic Warrior": "Strong jawline", "Sinister Villain": "Harsh shadows", "Scholar / Intellectual": "Refined appearance", "Royal / Aristocratic": "Elegant posture", "Mercenary / Outlaw": "Rugged textures", "Mystic / Shaman": "Otherworldly look", "Corporate Executive / CEO": "Clean-cut", "Elite Athlete": "Defined muscularity", "Bohemian Artist": "Creative styling", "Average Citizen": "Naturalistic", "Blue-collar / Technician": "Grime", "Academic Student": "Youthful", "High-fashion Model": "Angular features", "Retiree / Grandparent": "Dignified aging", "Urban / Street Style": "Modern edge", "Rural / Outdoorsman": "Sun-damaged skin", "Red Carpet / Gala Guest": "Glamorous", "Ailing / Sickly Character": "Pale skin"})
    groom_d = add_none({"Saudi Anchor Beard": "sharp angled", "Pyramidal Moustache": "wide base", "Clean Shaven": "smooth skin", "Light Stubble": "short even", "Heavy Stubble": "rough texture", "Designer Stubble": "trimmed edges", "Shadow Fade Beard": "faded sides", "Goatee (No Mustache)": "chin beard", "Classic Goatee": "connected", "Van Dyke": "pointed", "Anchor Beard": "thin defined", "Short Boxed Beard": "square edges", "Medium Boxed Beard": "clean appearance", "Long Full Beard": "natural growth", "Unkempt Beard": "messy", "Scruffy Beard": "patchy", "Wild Beard": "chaotic", "Bedouin Beard": "weathered", "Viking Beard": "braided", "Medieval Beard": "period growth", "Philosopher Beard": "soft", "Warrior Beard": "rugged", "Graying Patches": "gray strands", "Split Texture Beard": "dual-textured", "Short Sideburns": "above ear", "Mid-Ear Sideburns": "tragus level", "Long Sideburns": "ear lobe", "Extra-Long Sideburns": "pass lobe", "High Sideburns": "temple level", "Tapered Length": "faded", "Square Sideburns": "clean edges", "Pointed Sideburns": "triangle point", "Rounded Sideburns": "circular", "Pencil Sideburns": "thin line", "Flared Sideburns": "wide look", "Angled Sideburns": "slanted", "Mutton Chops": "wide full", "Friendly Mutton Chops": "connected", "Soul Patch": "below lip"})
    sfx_d = add_none({"Fresh Katana Slash": "active bleeding", "Glass Laceration": "embedded glass", "Blunt Force Contusion": "swelling", "3-Day Old Wound": "scabbing", "1-Week Old Wound": "granulation", "1-Month Old Scar": "maturation", "1-Year Old Keloid Scar": "hypertrophic", "5-Year Old Atrophic Scar": "pale white", "Fresh Periorbital Hematoma": "bruising", "24-Hour Old Bruise": "deep purple", "3-Day Old Bruise": "greenish-yellow", "15-Day Old Fading Bruise": "fading spots", "Chemical Acid Burn": "melting tissue", "1st Degree Sunburn": "redness", "2nd Degree Burn": "blisters", "Bilateral Vitiligo": "white patches", "Diffuse Hyperpigmentation": "dark spots"})
    aging_d = add_none({"Deep Nasolabial Folds": "smile lines", "Pronounced Crow's Feet": "eye wrinkles", "Hooded Eyelids / Ptosis": "sagging lids", "Dermal Crepiness": "paper skin", "Visible Liver Spots": "age spots", "Sagging Jowls": "loose skin", "Frontal Rhytids": "forehead ridges", "Periorbital Hollows": "sunken eyes", "Vertical Lip Lines": "mouth wrinkles", "Age-related Telangiectasia": "capillaries"})
    hair_tex_d = add_none({"Afro-Textured": "structural coils", "Wavy (Type 2)": "S-shape", "Curly (Type 3)": "ringlets", "Straight (Sleek)": "linear", "Coarse & Wiry": "irregular graying", "Fine & Wispy": "translucent", "Disheveled & Matted": "weathered", "Braided / Cornrows": "interlocking"})
    hair_col_d = add_none({"Jet black": "Jet black", "Deep espresso brown": "Espresso", "Light chestnut brown": "Sandy", "Ash blonde": "Cool blonde", "Golden blonde": "Warm blonde", "10% Salt & Pepper": "sparse grey", "30% Salt & Pepper": "mixed grey", "50% Salt & Pepper": "even grey", "70% Salt & Pepper": "mostly grey"})
    light_d = add_none({"Rembrandt Lighting": "triangle light", "Cold Rim Lighting": "blue backlight", "Chiaroscuro": "contrast", "Teal and Orange": "cinematic", "Volumetric God Rays": "linear light", "Cinematic Golden Hour": "warm glow", "High-Key Studio": "bright", "Low-Key Moody": "mysterious", "Neon Cyberpunk": "edge light", "Hard Top Lighting": "harsh shadow", "Flickering Candlelight": "unsteady", "Soft Professional Softbox": "velvety"})
    camera_d = add_none({"85mm Lens, Eye-Level Shot": "no distortion", "100mm Macro, Close-Up": "extreme detail", "50mm Lens, Dutch Angle": "tilted tension", "35mm Lens, Low-Angle": "hero shot", "24mm Wide-Angle, High-Angle": "thinning", "200mm Telephoto, Profile View": "compressed", "50mm Lens, Top-Down": "design focus", "85mm Lens, Three-Quarter View": "standard"})
    size_list = add_none(["Aspect Ratio 4:5 (Portrait)", "Aspect Ratio 16:9 (Widescreen)", "Aspect Ratio 2.39:1 (Anamorphic)", "Aspect Ratio 1:1 (Square)", "Aspect Ratio 9:16 (Vertical)"])
    mat_list = add_none(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin Finish", "Prosthetic Adhesive", "Matte Sealer", "Alcohol Palette", "Granulation Tissue"])

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
            h_col = st.selectbox("", list(hair_col_d.keys()), key="hcol", label_visibility="collapsed")
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

    # منطق ساخت پرامپت
    def fmt(p, v, d=None):
        if v == "None" or not v: return ""
        desc = f" ({d[v]})" if d and v in d and d[v] else ""
        return f"{p}{v}{desc}"

    p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
    p_sfx = f" [SFX STUDY: Apply {sfx_sel} ({sfx_d[sfx_sel]}) SFX as a makeup layer]." if sfx_sel != "None" else ""
    p_size = f" Aspect Ratio {size_sel}" if size_sel != "None" else ""

    final_prompt = f"{p_actor}A professional cinematic {p_size} portrait of a {fmt('', gender_sel, gender_d)} {fmt('', age_sel, age_d)} {fmt('', nat_sel, nat_d)}{fmt(' from the ', era_sel, era_d)}. {fmt('Character Concept: ', char_sel, char_d)}. {fmt('Grooming: ', groom_sel, groom_d)}. {fmt('Hair Color: ', h_col, hair_col_d)}{fmt(', Texture: ', h_tex, hair_tex_d)}. {fmt('Skin: ', aging_sel, aging_d)}.{p_sfx} {fmt('Finish Material: ', mat_sel)}. {fmt('Technical Specs: ', light_sel, light_d)}{fmt(', ', cam_sel, camera_d)}, 8k, raw photography, subsurface scattering, focus on prosthetic makeup accuracy."

    with col_master:
        st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center; color:#00d4ff; font-family:Tahoma; font-size:0.85rem; padding:10px;">لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>Please click on the text inside the box below to copy</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)

# 6. فوتر حرفه‌ای
st.markdown(f"""
    <div class="footer">
        <div class="footer-content">
            © {datetime.now().year} <span class="footer-rights">UONA GROUP</span>. ALL RIGHTS RESERVED. <br>
            PREMIUM CINEMATIC DESIGN SYSTEM | POWERED BY AI TECHNOLOGY
        </div>
    </div>
    """, unsafe_allow_html=True)
