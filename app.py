import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA AI DASHBOARD", layout="wide")

# CSS حرفه‌ای برای استایل سینماتیک و رفع مشکل اسکرول
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;400;700;900&family=Playfair+Display:ital,wght@1,900&display=swap');

    /* رفع مشکل اسکرول و تنظیم پس‌زمینه */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0b1d2e !important;
        overflow-y: auto !important;
    }

    /* هدر فیروزه‌ای لاکچری */
    .header-box {
        background-color: #050f1a;
        border-bottom: 2px solid #00d4ff;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .header-title {
        color: #00d4ff;
        font-family: 'Cinzel', serif;
        font-size: 2.2rem;
        letter-spacing: 6px;
        margin: 0;
        text-align: center;
    }

    /* استایل لیبل‌ها - قدرتمند و سینماتیک */
    label p {
        color: #00d4ff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    /* نشانه اجباری (دایره زرد) */
    .req-mark { color: #ffcc00; margin-right: 8px; font-size: 1.1rem; }

    /* استایل فیلدهای ورودی متنی */
    .stTextInput>div>div>input {
        background-color: #1a3a5a !important;
        color: #ffffff !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* کادر MASTER PROMPT (دقیقاً مشابه اکسل) */
    .master-header {
        background-color: #00f2ff;
        color: #000000;
        padding: 12px;
        font-weight: 900;
        font-size: 1.4rem;
        border-radius: 4px 4px 0 0;
        font-family: 'Montserrat', sans-serif;
        text-align: center;
        box-shadow: 0 -5px 15px rgba(0, 212, 255, 0.2);
    }
    .master-box {
        background-color: #ffffff;
        color: #111111;
        padding: 30px;
        border-radius: 0 0 4px 4px;
        border-left: 5px solid #00f2ff;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2rem;
        line-height: 1.8;
        min-height: 450px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }

    /* جداکننده سینماتیک */
    hr { border-top: 1px solid rgba(0, 212, 255, 0.2) !important; margin: 40px 0 !important; }
    </style>
    """, unsafe_allow_html=True)

# هدر اصلی
st.markdown("""
    <div class="header-box">
        <p class="header-title">UONA STUDIO | PROMPT BUILDER</p>
    </div>
    """, unsafe_allow_html=True)

# دیتابیس‌ها
nat_table = {"Iranian": "Indo-Aryan features", "Syrian": "Levantine features", "Saudi": "Peninsular Arab features"}
era_table = {"Contemporary": "Current lighting", "Ancient Era": "Ancient textures"}

# بدنه اصلی
col_form, col_gap, col_master = st.columns([1.6, 0.1, 1])

with col_form:
    # بخش اول: پایه (اجباری با دایره زرد)
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actore:", ["No", "Yes"])
        age = st.selectbox("🟡 Age:", ["Middle-aged", "Elderly / Senior", "Young Adult"])
    with r1c2:
        gender = st.selectbox("🟡 Gender:", ["Masculine / Male", "Feminine / Female"])
        nationality = st.selectbox("🟡 Nationality:", list(nat_table.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    
    # بخش دوم: استایل و زمان
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era = st.selectbox("Time Period:", list(era_table.keys()))
        hair_color = st.text_input("Hair & Beard Color:", placeholder="Enter color (e.g. Salt & Pepper)")
    with r2c2:
        char_style = st.selectbox("Character Type:", ["Heroic Warrior", "Ailing", "Royal"])
        grooming = st.selectbox("Grooming Style:", ["Viking Beard", "Pyramidal Moustache"])

    st.markdown("<br>", unsafe_allow_html=True)

    # بخش سوم: فنی و SFX
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx = st.selectbox("SFX Makeup:", ["3-Day Old Wound", "Burn Scar", "None"])
        aging = st.text_input("Aging Details:", placeholder="Enter details (e.g. Forehead Furrows)")
        lighting = st.selectbox("Lighting:", ["Rembrandt Lighting", "Rim Light"])
    with r3c2:
        material = st.text_input("Material:", placeholder="Enter material (e.g. Matte Sealer)")
        hair_tex = st.selectbox("Hair Texture:", ["Afro", "Wavy", "Straight"])
        canvas = st.selectbox("Bible Size:", ["Aspect Ratio 16:9", "1:1"])

# ساخت پرامپت نهایی
nat_desc = f" ({nat_table[nationality]})"
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
final_prompt = f"{visual_guide}A professional cinematic {canvas} portrait of a {gender} {age} {nationality}{nat_desc} from the {era} era. " \
               f"Character style: {char_style}. Grooming: {grooming}. Hair Color: {hair_color}, Texture: {hair_tex}. " \
               f"Skin: {aging}. SFX: {sfx}. Material: {material}. Technical: {lighting}, 8k, raw photography, subsurface scattering."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMPT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; color: #00d4ff; font-family: Montserrat; padding-top: 20px;'>
            <p style='font-size: 0.9rem; opacity: 0.8;'>لطفاً برای کپی کردن، متن داخل کادر سفید را انتخاب کنید</p>
            <p style='font-size: 0.8rem; letter-spacing: 1px;'>CLICK INSIDE THE BOX TO SELECT ALL</p>
        </div>
        """, unsafe_allow_html=True)
