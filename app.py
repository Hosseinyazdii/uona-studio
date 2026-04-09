import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA AI DASHBOARD", layout="wide")

# CSS حرفه‌ای با بک‌گراند تصویری و افکت‌های نوری
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700;900&display=swap');

    /* تنظیم بک‌گراند کل صفحه */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?ixlib=rb-4.0.3&auto=format&fit=crop&w=2342&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* لایه تیره روی بک‌گراند برای خوانایی بیشتر */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(5, 15, 26, 0.85); /* تاریک کردن بک‌گراند */
        z-index: -1;
    }

    /* هدر سینماتیک */
    .header-box {
        background: rgba(0, 212, 255, 0.05);
        backdrop-filter: blur(10px);
        border-bottom: 2px solid #00d4ff;
        padding: 25px;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    }
    .header-title {
        color: #00d4ff;
        font-family: 'Cinzel', serif;
        font-size: 2.5rem;
        letter-spacing: 8px;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        margin: 0;
    }

    /* کادرهای ورودی شیشه‌ای */
    div[data-baseweb="select"] > div, .stTextInput>div>div>input {
        background-color: rgba(26, 58, 90, 0.6) !important;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(0, 212, 255, 0.4) !important;
        color: white !important;
        border-radius: 8px !important;
    }

    label p {
        color: #00d4ff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
    }

    /* کادر MASTER PROMPT اکسل */
    .master-header {
        background: linear-gradient(90deg, #00f2ff, #0088ff);
        color: #000000;
        padding: 15px;
        font-weight: 900;
        font-size: 1.5rem;
        border-radius: 8px 8px 0 0;
        font-family: 'Montserrat', sans-serif;
        text-align: center;
    }
    .master-box {
        background-color: #ffffff;
        color: #111111;
        padding: 30px;
        border-radius: 0 0 8px 8px;
        border-left: 8px solid #00f2ff;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.25rem;
        line-height: 1.8;
        min-height: 480px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }

    /* نوار اسکرول زیبا */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #050f1a; }
    ::-webkit-scrollbar-thumb { background: #00d4ff; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# هدر
st.markdown('<div class="header-box"><p class="header-title">UONA STUDIO</p></div>', unsafe_allow_html=True)

# دیتابیس‌ها
nat_table = {"Iranian": "Indo-Aryan features", "Syrian": "Levantine features", "Saudi": "Peninsular Arab features"}
era_table = {"Contemporary": "Current lighting", "Ancient Era": "Ancient textures"}

# بدنه اصلی
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actore:", ["No", "Yes"])
        age = st.selectbox("🟡 Age:", ["Middle-aged", "Elderly / Senior", "Young Adult"])
    with r1c2:
        gender = st.selectbox("🟡 Gender:", ["Masculine / Male", "Feminine / Female"])
        nationality = st.selectbox("🟡 Nationality:", list(nat_table.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era = st.selectbox("Time Period:", list(era_table.keys()))
        hair_color = st.text_input("Hair & Beard Color:", placeholder="e.g. Salt & Pepper")
    with r2c2:
        char_style = st.selectbox("Character Type:", ["Heroic Warrior", "Ailing", "Royal"])
        grooming = st.selectbox("Grooming Style:", ["Viking Beard", "Pyramidal Moustache"])

    st.markdown("<br>", unsafe_allow_html=True)

    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx = st.selectbox("SFX Makeup:", ["3-Day Old Wound", "Burn Scar", "None"])
        aging = st.text_input("Aging Details:", placeholder="e.g. Forehead Furrows")
        lighting = st.selectbox("Lighting:", ["Rembrandt Lighting", "Rim Light"])
    with r3c2:
        material = st.text_input("Material:", placeholder="e.g. Matte Sealer")
        hair_tex = st.selectbox("Hair Texture:", ["Afro", "Wavy", "Straight"])
        canvas = st.selectbox("Bible Size:", ["Aspect Ratio 16:9", "1:1"])

# ساخت پرامپت
nat_desc = f" ({nat_table[nationality]})"
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
final_prompt = f"{visual_guide}A professional cinematic {canvas} portrait of a {gender} {age} {nationality}{nat_desc} from the {era} era. Character style: {char_style}. Grooming: {grooming}. Hair Color: {hair_color}, Texture: {hair_tex}. Skin: {aging}. SFX: {sfx}. Material: {material}. Technical: {lighting}, 8k, raw photography."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
