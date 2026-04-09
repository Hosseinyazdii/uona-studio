import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA STUDIO | AI Dashboard", layout="wide")

# تزریق CSS برای شبیه‌سازی دقیق تم اکسل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Montserrat:wght@400;700&display=swap');

    .stApp { background-color: #0b1d2e !important; }

    /* هدر اصلی مشابه اکسل */
    .header-box {
        background-color: #0a1428;
        border-bottom: 3px solid #00d4ff;
        padding: 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    .main-title {
        font-family: 'Playfair Display', serif;
        color: #ffffff;
        font-size: 3rem;
        letter-spacing: 3px;
        margin: 0;
    }

    /* استایل لیبل‌ها و نشان اجباری */
    label p {
        color: #00d4ff !important;
        font-weight: bold !important;
        font-family: 'Montserrat', sans-serif !important;
    }
    .required { color: #ff4b4b; margin-left: 5px; }

    /* کادر خروجی مشابه MASTER PROMPT اکسل */
    .master-box {
        background-color: #ffffff;
        color: #000000;
        padding: 25px;
        border-radius: 5px;
        border-left: 10px solid #00d4ff;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
        min-height: 300px;
    }
    .master-header {
        background-color: #00d4ff;
        color: #000000;
        padding: 10px;
        font-weight: 900;
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 0;
        border-radius: 5px 5px 0 0;
    }

    /* استایل ورودی‌ها */
    div[data-baseweb="select"] > div {
        background-color: #1a3a5a !important;
        border: 1px solid #00d4ff !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# هدر
st.markdown('<div class="header-box"><p class="main-title">🎬 UONA STUDIO | PROMPT BUILDER</p></div>', unsafe_allow_html=True)

# دیتابیس‌ها
nat_table = {"Iranian": "Indo-Aryan features, prominent nasal bridge", "Syrian": "Levantine features", "Saudi": "Peninsular Arab features", "Egyptian": "North African features", "Emirati": "Gulf Arab features"}
era_table = {"Contemporary": "Current lighting", "Ancient Era": "Ancient textures", "Medieval": "Gritty textures"}

# بدنه اصلی - چیدمان بر اساس داشبورد اکسل
col_main, col_output = st.columns([1.5, 1])

with col_main:
    # بخش اول: اطلاعات پایه (اجباری)
    st.subheader("📍 Basic Info")
    r1_c1, r1_c2 = st.columns(2)
    with r1_c1:
        actor = st.selectbox("Actor Reference (G7) *", ["No", "Yes"])
        age = st.selectbox("Age (J7) *", ["Middle-aged", "Elderly / Senior", "Young Adult", "Child"])
    with r1_c2:
        gender = st.selectbox("Gender (G9) *", ["Masculine / Male", "Feminine / Female"])
        nationality = st.selectbox("Nationality (J9) *", list(nat_table.keys()))

    st.markdown("---")
    
    # بخش دوم: سبک و زمان (آپشنال)
    st.subheader("⏳ Style & Era")
    r2_c1, r2_c2 = st.columns(2)
    with r2_c1:
        era = st.selectbox("Time Period (G12):", list(era_table.keys()))
        hair_color = st.text_input("Hair & Beard Color:", "Black / Salt & Pepper")
    with r2_c2:
        char_style = st.selectbox("Character Type (J12):", ["Heroic Warrior", "Ailing Character", "Royal"])
        grooming = st.selectbox("Grooming Style (J14):", ["Viking Beard", "Pyramidal Moustache", "Clean Shaven"])

    st.markdown("---")

    # بخش سوم: جزییات گریم و فنی
    st.subheader("🎨 SFX & Technical")
    r3_c1, r3_c2 = st.columns(2)
    with r3_c1:
        sfx = st.selectbox("SFX Makeup (G17):", ["3-Day Old Wound", "Burn Scar", "None"])
        aging = st.text_input("Aging Details (G19):", "Frontal Rhytids")
        lighting = st.selectbox("Lighting (G22):", ["Rembrandt Lighting", "Cinematic Rim Light"])
    with r3_c2:
        material = st.text_input("Material (J17):", "Matte Sealer")
        hair_tex = st.selectbox("Hair Texture (J19):", ["Afro", "Wavy", "Curly", "Straight"])
        canvas = st.selectbox("Canvas Size (J22):", ["16:9 (Widescreen)", "4:3", "1:1"])

# ساخت پرامپت
nat_desc = f" ({nat_table[nationality]})"
sfx_desc = f"[CINEMATIC PROSTHETIC STUDY: Apply {sfx}]. " if sfx != "None" else ""
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""

final_prompt = f"{visual_guide}A professional cinematic {canvas} portrait of a {gender} {age} {nationality}{nat_desc} from the {era} era. " \
               f"Character style: {char_style}. Grooming: {grooming}. Hair Color: {hair_color}, Texture: {hair_tex}. " \
               f"Skin: {aging}. {sfx_desc}Material: {material}. " \
               f"Technical: {lighting}, 8k, raw photography, subsurface scattering."

with col_output:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; color: #00d4ff; font-size: 0.8rem; margin-top: 10px;'>
            لطفاً متن داخل کادر سفید را برای کپی انتخاب کنید<br>
            Please select the text inside the white box to copy
        </div>
        """, unsafe_allow_html=True)
