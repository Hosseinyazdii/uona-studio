import streamlit as st
from datetime import datetime

# 1. تنظیمات سیستمی و حذف اسکرول
st.set_page_config(page_title="UONA STUDIO | AI SYSTEM", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* تنظیم تم و حذف اسکرول */
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%) !important;
        height: 100vh;
        overflow: hidden !important;
        color: white;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    /* هدر مقتدر و خوانا */
    .nav-bar {
        display: flex; align-items: center; padding: 15px 50px;
        background: rgba(2, 6, 12, 0.8); border-bottom: 1px solid rgba(0, 242, 255, 0.2);
        justify-content: space-between;
    }
    .title-main {
        font-family: 'Cinzel'; color: #ffffff; font-size: 3.5rem; font-weight: 800; 
        letter-spacing: 10px; margin: 0; text-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
    }
    .slogan-main { font-family: 'Montserrat'; color: #00f2ff; font-size: 0.8rem; letter-spacing: 6px; text-transform: uppercase; }

    /* پورتال ورودی */
    .module-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 20px; padding: 30px; text-align: center; transition: 0.4s; backdrop-filter: blur(10px);
    }
    .module-card:hover { border-color: #00f2ff; background: rgba(0, 242, 255, 0.08); transform: translateY(-10px); }
    .icon-vector { font-size: 60px; margin-bottom: 20px; display: block; }
    
    /* استایل فرم و انتخاب‌ها */
    .label-text { color: #00d4ff; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; font-size: 0.75rem; margin-bottom: 3px; }
    .star { color: #ff4b4b; }
    div[data-baseweb="select"] > div { background-color: rgba(26, 58, 90, 0.7) !important; color: white !important; border-radius: 8px !important; border: 1px solid rgba(0, 242, 255, 0.3) !important; }

    /* کادر خروجی نهایی */
    .master-header { background: linear-gradient(90deg, #00f2ff, #0088ff); color: #000; padding: 10px; font-weight: 900; font-size: 1.2rem; border-radius: 8px 8px 0 0; text-align: center; font-family: 'Montserrat'; }
    .master-box { 
        background-color: #ffffff; color: #111; padding: 25px; border-radius: 0 0 8px 8px; 
        border-left: 10px solid #00f2ff; font-family: 'Montserrat'; font-size: 1.05rem; 
        line-height: 1.7; height: 420px; overflow-y: auto; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; padding: 20px; border-top: 1px solid rgba(0, 242, 255, 0.1); background: rgba(0,0,0,0.4); }
    .uona-tag { color: #00f2ff; font-weight: 900; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

# مدیریت ناوبری
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- هدر ثابت ---
h_col1, h_col2 = st.columns([1, 6])
with h_col1:
    try: st.image("image.png", width=100)
    except: st.markdown("<div style='width:90px; height:90px; background:#00f2ff; border-radius:12px;'></div>", unsafe_allow_html=True)
with h_col2:
    st.markdown('<h1 class="title-main">UONA STUDIO</h1><div class="slogan-main">The Art of Cinematic Transformation</div>', unsafe_allow_html=True)

# --- صفحه پورتال ---
if st.session_state.page == 'home':
    st.markdown("<br><br><h2 style='text-align:center; color:white; font-family:Cinzel; letter-spacing:5px;'>SELECT YOUR MODULE</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="module-card"><span class="icon-vector">🎬</span><h3>CINEMATIC</h3><p style="font-size:0.7rem; opacity:0.6;">Feature Films & VFX</p></div>', unsafe_allow_html=True)
        if st.button("ENTER MODULE", key="cine"): st.session_state.page = 'cinematic'; st.rerun()
    with c2:
        st.markdown('<div class="module-card"><span class="icon-vector">📺</span><h3>TV SERIES</h3><p style="font-size:0.7rem; opacity:0.6;">Episodic Production</p></div>', unsafe_allow_html=True)
        if st.button("ENTER MODULE", key="series"): st.session_state.page = 'cinematic'; st.rerun()
    with c3:
        st.markdown('<div class="module-card" style="opacity:0.5;"><span class="icon-vector">🎭</span><h3>THEATER</h3><p style="color:#ff4b4b; font-size:0.7rem;">COMING SOON</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="module-card" style="opacity:0.5;"><span class="icon-vector">👠</span><h3>FASHION</h3><p style="color:#ff4b4b; font-size:0.7rem;">COMING SOON</p></div>', unsafe_allow_html=True)

# --- بخش Cinematic (فول دیتا) ---
elif st.session_state.page == 'cinematic':
    if st.button("← BACK TO PORTAL"): st.session_state.page = 'home'; st.rerun()
    
    # 2. دیتابیس کامل استخراج شده (۱۰۰٪ شیت ها)
    def add_n(d): 
        if isinstance(d, dict): return {**{"None": ""}, **d}
        return ["None"] + d

    gender_d = add_n({"Masculine / Male": "strong bone structure, wide jawline", "Feminine / Female": "softer facial contours", "Androgynous": "blend of features"})
    age_d = add_n({"Child / Pre-adolescent": "textureless skin", "Adolescent / Teenager": "oily skin", "Young Adult (Early 20s)": "peak elasticity", "Middle-aged (Late 40s)": "initial fat loss", "Elderly / Senior": "collagen loss", "Ancient / Centenarian": "paper-thin skin"})
    nat_d = add_n({"Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Saudi": "Peninsular Arab features", "Kuwaiti": "Northern Gulf features", "Syrian": "Levantine features", "American": "Diverse North American features", "Indian": "South Asian features", "Chinese": "East Asian features", "African": "Sub-Saharan features", "European": "Caucasian features", "Turkish": "Eurasian features"})
    era_d = add_n({"Stone Age / Prehistoric": "Primitive aesthetic", "BCE (Before Common Era)": "Ancient styling", "Pre-Islamic Era": "Traditional heritage", "Ancient Era (Hellenistic/Roman)": "Classical features", "Medieval / Dark Ages": "Gritty, rustic textures", "200 Years Ago": "Regency style", "150 Years Ago": "Victorian Era", "100 Years Ago": "Roaring 20s", "50 Years Ago": "1970s Retro", "Contemporary / Modern Day": "Current lighting", "Futuristic / Cyberpunk": "Neon accents", "Post-Apocalyptic": "Weathered textures"})
    char_d = add_n({"Heroic Warrior": "Strong jawline", "Sinister Villain": "Harsh shadows", "Scholar / Intellectual": "Refined appearance", "Royal / Aristocratic": "Elegant posture", "Mercenary / Outlaw": "Rugged, weathered", "Mystic / Shaman": "Otherworldly look", "Corporate Executive / CEO": "Clean-cut", "Elite Athlete": "Defined muscularity", "Bohemian Artist": "Creative styling", "Average Citizen": "Naturalistic", "Blue-collar / Technician": "Grime", "Academic Student": "Youthful", "High-fashion Model": "Angular features", "Retiree / Grandparent": "Dignified aging", "Urban / Street Style": "Modern edge", "Rural / Outdoorsman": "Sun-damaged skin", "Red Carpet / Gala Guest": "Glamorous", "Ailing / Sickly Character": "Pale skin"})
    groom_d = add_n({"Saudi Anchor Beard": "sharp angled", "Pyramidal Moustache": "wide base", "Clean Shaven": "smooth skin", "Light Stubble": "short even", "Heavy Stubble": "rough texture", "Designer Stubble": "trimmed edges", "Shadow Fade Beard": "faded sides", "Goatee (No Mustache)": "chin beard", "Classic Goatee": "connected", "Van Dyke": "pointed", "Anchor Beard": "thin defined", "Short Boxed Beard": "square edges", "Medium Boxed Beard": "clean appearance", "Long Full Beard": "natural growth", "Unkempt Beard": "messy", "Scruffy Beard": "patchy", "Wild Beard": "chaotic", "Bedouin Beard": "weathered", "Viking Beard": "braided", "Medieval Beard": "period growth", "Philosopher Beard": "soft", "Warrior Beard": "rugged", "Graying Patches": "gray strands", "Split Texture Beard": "dual-textured", "Short Sideburns": "above ear", "Mid-Ear Sideburns": "tragus level", "Long Sideburns": "ear lobe", "Extra-Long Sideburns": "pass lobe", "High Sideburns": "temple level", "Tapered Length": "faded", "Square Sideburns": "clean edges", "Pointed Sideburns": "triangle point", "Rounded Sideburns": "circular", "Pencil Sideburns": "thin line", "Flared Sideburns": "wide look", "Angled Sideburns": "slanted", "Mutton Chops": "wide full", "Friendly Mutton Chops": "connected", "Soul Patch": "below lip"})
    
    # ۳. طبقه‌بندی تخصصی SFX
    sfx_cats = {
        "Acute Trauma (جراحت حاد)": ["Fresh Katana/Sword Slash", "Glass Laceration with Shards", "Blunt Force Contusion", "Chemical Acid Burn (Corrosive)"],
        "Healing Stages (مراحل بهبودی)": ["3-Day Old Wound (Scabbing)", "1-Week Old Wound (Granulation)", "1-Month Old Scar (Maturation)", "1-Year Old Keloid Scar", "5-Year Old Atrophic Scar"],
        "Bruising (کبودی)": ["Fresh Periorbital Hematoma", "24-Hour Old Bruise (Deep Purple)", "3-Day Old Bruise (Greenish-Yellow)", "15-Day Old Fading Bruise"],
        "Skin Conditions (مشکلات پوستی)": ["1st Degree Sunburn/Erythema", "2nd Degree Burn with Blisters", "Bilateral Vitiligo Depigmentation", "Diffuse Hyperpigmentation & Melasma"]
    }
    
    aging_d = add_n({"Deep Nasolabial Folds": "smile lines", "Pronounced Crow's Feet": "eye wrinkles", "Hooded Eyelids / Ptosis": "sagging lids", "Dermal Crepiness": "paper skin", "Visible Liver Spots": "age spots", "Sagging Jowls": "loose skin", "Frontal Rhytids": "forehead ridges", "Periorbital Hollows": "sunken eyes", "Vertical Lip Lines": "mouth wrinkles", "Age-related Telangiectasia": "capillaries"})
    h_tex_d = add_n({"Afro-Textured": "structural coils", "Wavy (Type 2)": "S-shape waves", "Curly (Type 3)": "defined ringlets", "Straight (Sleek)": "linear", "Coarse & Wiry": "irregular graying", "Fine & Wispy": "translucent", "Disheveled & Matted": "weathered", "Braided / Cornrows": "interlocking"})
    h_col_d = add_n({"Jet black": "Jet black", "Deep espresso brown": "Espresso", "Light chestnut brown": "Sandy", "Ash blonde": "Cool blonde", "Golden blonde": "Warm blonde", "10% Salt & Pepper": "sparse grey", "30% Salt & Pepper": "mixed grey", "50% Salt & Pepper": "even grey", "70% Salt & Pepper": "mostly grey"})
    light_d = add_n({"Rembrandt Lighting": "triangle light", "Cold Rim Lighting": "blue backlight", "Chiaroscuro": "contrast", "Teal and Orange": "cinematic", "Volumetric God Rays": "linear light", "Cinematic Golden Hour": "warm glow", "High-Key Studio": "bright", "Low-Key Moody": "mysterious", "Neon Cyberpunk": "edge light", "Hard Top Lighting": "harsh shadow", "Flickering Candlelight": "unsteady", "Soft Professional Softbox": "velvety"})
    cam_d = add_n({"85mm Lens, Eye-Level Shot": "no distortion", "100mm Macro, Close-Up": "extreme detail", "50mm Lens, Dutch Angle": "tilted tension", "35mm Lens, Low-Angle": "hero shot", "24mm Wide-Angle, High-Angle": "thinning", "200mm Telephoto, Profile View": "compressed", "50mm Lens, Top-Down": "design focus", "85mm Lens, Three-Quarter View": "standard"})
    size_l = add_n(["4:5 (Portrait)", "16:9 (Widescreen)", "2.39:1 (Anamorphic)", "1:1 (Square)", "9:16 (Vertical)"])
    mat_l = add_n(["Encapsulated Silicone", "Feathered Edges", "Translucent Skin", "Prosthetic Adhesive", "Matte Sealer", "Alcohol Palette", "Granulation Tissue"])

    c_form, c_master = st.columns([1.8, 1])
    with c_form:
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            st.markdown('<p class="label-text">Actor Reference <span class="star">*</span></p>', unsafe_allow_html=True)
            actor = st.selectbox("", ["None", "No", "Yes"], key="act", label_visibility="collapsed")
            st.markdown('<p class="label-text">Gender <span class="star">*</span></p>', unsafe_allow_html=True)
            gen = st.selectbox("", list(gender_d.keys()), key="gen", label_visibility="collapsed")
            st.markdown('<p class="label-text">SFX Category (طبقه‌بندی جراحت)</p>', unsafe_allow_html=True)
            s_cat = st.selectbox("", ["None"] + list(sfx_cats.keys()), key="scat", label_visibility="collapsed")
        with r1c2:
            st.markdown('<p class="label-text">Age Range <span class="star">*</span></p>', unsafe_allow_html=True)
            age = st.selectbox("", list(age_d.keys()), key="age", label_visibility="collapsed")
            st.markdown('<p class="label-text">Nationality <span class="star">*</span></p>', unsafe_allow_html=True)
            nat = st.selectbox("", list(nat_d.keys()), key="nat", label_visibility="collapsed")
            st.markdown('<p class="label-text">Specific Trauma (انتخاب جراحت)</p>', unsafe_allow_html=True)
            s_type = st.selectbox("", sfx_cats[s_cat] if s_cat != "None" else ["None"], key="stype", label_visibility="collapsed")

        r2c1, r2c2 = st.columns(2)
        with r2c1:
            st.markdown('<p class="label-text">Time Period / Era</p>', unsafe_allow_html=True)
            era = st.selectbox("", list(era_d.keys()), key="era", label_visibility="collapsed")
            st.markdown('<p class="label-text">Character Type</p>', unsafe_allow_html=True)
            char = st.selectbox("", list(char_d.keys()), key="char", label_visibility="collapsed")
            st.markdown('<p class="label-text">Lighting & Camera</p>', unsafe_allow_html=True)
            light = st.selectbox("", list(light_d.keys()), key="light", label_visibility="collapsed")
        with r2c2:
            st.markdown('<p class="label-text">Grooming Style</p>', unsafe_allow_html=True)
            groom = st.selectbox("", list(groom_d.keys()), key="groom", label_visibility="collapsed")
            st.markdown('<p class="label-text">Skin Aging & Texture</p>', unsafe_allow_html=True)
            aging = st.selectbox("", list(aging_d.keys()), key="aging", label_visibility="collapsed")
            cam = st.selectbox("", list(cam_d.keys()), key="cam", label_visibility="collapsed")

    # منطق پرامپت
    def f(p, v, d=None):
        if v == "None" or not v: return ""
        desc = f" ({d[v]})" if d and v in d and d[v] else ""
        return f"{p}{v}{desc}"

    p_actor = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
    p_sfx = f" [SFX STUDY: Apply {s_type} SFX as a makeup layer]." if s_type != "None" else ""
    
    final_prompt = f"{p_actor}A professional cinematic portrait of a {f('', gen, gender_d)} {f('', age, age_d)} {f('', nat, nat_d)}{f(' from the ', era, era_d)}. {f('Concept: ', char, char_d)}. {f('Grooming: ', groom, groom_d)}. {f('Hair: ', h_col_d[list(h_col_d.keys())[0]], h_col_d)}. {f('Skin: ', aging, aging_d)}.{p_sfx} Technical: {f('', light, light_d)}, {f('', cam, cam_d)}, 8k, raw photography."

    with c_master:
        st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)

# 4. فوتر
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} <span class="uona-tag">UONA GROUP</span>. ALL RIGHTS RESERVED. <br>
        PROFESSIONAL CHARACTER DESIGN AI PLATFORM | V 2.0
    </div>
    """, unsafe_allow_html=True)
