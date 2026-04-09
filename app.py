import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA AI DASHBOARD", layout="wide")

# CSS حرفه‌ای برای شبیه‌سازی دقیق داشبورد اکسل و جلوگیری از به هم ریختگی
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    /* تنظیم پس‌زمینه کل صفحه به سرمه‌ای اکسل */
    .stApp { background-color: #0b1d2e !important; }

    /* هدر فیروزه‌ای */
    .header-box {
        background-color: #0d1b2a;
        border-bottom: 3px solid #00d4ff;
        padding: 15px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .header-title {
        color: #00d4ff;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8rem;
        font-weight: 900;
        text-transform: uppercase;
        margin: 0;
    }

    /* استایل لیبل‌ها با نقطه زرد */
    label p {
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.9rem !important;
    }
    .dot { color: #ffcc00; margin-right: 5px; font-size: 1.2rem; }

    /* کادر MASTER PROMPT مشابه اکسل */
    .master-header {
        background-color: #00f2ff;
        color: #000000;
        padding: 8px 15px;
        font-weight: 900;
        font-size: 1.3rem;
        border-radius: 4px 4px 0 0;
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Montserrat', sans-serif;
    }
    .master-box {
        background-color: #ffffff;
        color: #1a1a1a;
        padding: 20px;
        border-radius: 0 0 4px 4px;
        border-left: 2px solid #00f2ff;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
        min-height: 400px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* استایل ورودی‌ها (Selectboxes) */
    div[data-baseweb="select"] > div {
        background-color: #1a3a5a !important;
        border: 1px solid #00d4ff !important;
        color: white !important;
        height: 35px !important;
    }
    
    /* سایدبار آیکون‌ها در سمت چپ (تزیینی) */
    .icon-bar {
        border-right: 2px solid #00d4ff;
        padding-right: 15px;
        height: 100%;
    }

    /* تنظیم عرض ستون‌ها برای جلوگیری از به هم ریختگی در موبایل */
    [data-testid="column"] { min-width: 300px !important; }
    </style>
    """, unsafe_allow_html=True)

# هدر اصلی
st.markdown("""
    <div class="header-box">
        <span style="font-size: 2rem;">📟</span>
        <p class="header-title">PROMPT BUILDER</p>
    </div>
    """, unsafe_allow_html=True)

# دیتابیس‌ها
nat_table = {"Iranian": "Indo-Aryan features", "Syrian": "Levantine features", "Saudi": "Peninsular Arab features"}
era_table = {"Contemporary": "Current lighting", "Ancient Era": "Ancient textures"}

# چیدمان ستون اصلی و خروجی
col_form, col_gap, col_master = st.columns([1.5, 0.1, 1])

with col_form:
    # بخش اطلاعات پایه
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        actor = st.selectbox("🟡 Actore (G7):", ["No", "Yes"])
        age = st.selectbox("🟡 Age (J7):", ["Middle-aged", "Elderly / Senior", "Young Adult"])
    with r1c2:
        gender = st.selectbox("🟡 Gender (G9):", ["Masculine / Male", "Feminine / Female"])
        nationality = st.selectbox("🟡 Nationality (J9):", list(nat_table.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    
    # بخش زمان و استایل
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        era = st.selectbox("Time Period (G12):", list(era_table.keys()))
        hair_color = st.text_input("Hair & Beard Color:", "Black / Salt & Pepper")
    with r2c2:
        char_style = st.selectbox("Character Type (J12):", ["Heroic Warrior", "Ailing", "Royal"])
        grooming = st.selectbox("Grooming Style (J14):", ["Viking Beard", "Pyramidal Moustache"])

    st.markdown("<br>", unsafe_allow_html=True)

    # بخش SFX و جزییات فنی
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        sfx = st.selectbox("SFX Makeup (G17):", ["3-Day Old Wound", "Burn Scar", "None"])
        aging = st.text_input("Aging Details (G19):", "Frontal Rhytids")
        lighting = st.selectbox("Lighting (G22):", ["Rembrandt Lighting", "Rim Light"])
    with r3c2:
        material = st.text_input("Material:", "Matte Sealer")
        hair_tex = st.selectbox("Hair Texture (J19):", ["Afro", "Wavy", "Straight"])
        canvas = st.selectbox("Bible Size (J22):", ["Aspect Ratio 16:9", "1:1"])

# ساخت پرامپت
nat_desc = f" ({nat_table[nationality]})"
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
final_prompt = f"{visual_guide}A professional cinematic {canvas} portrait of a {gender} {age} {nationality}{nat_desc} from the {era} era. " \
               f"Character style: {char_style}. Grooming: {grooming}. Hair: {hair_color}, Texture: {hair_tex}. " \
               f"Skin: {aging}. SFX: {sfx}. Material: {material}. Technical: {lighting}, 8k, raw photography."

with col_master:
    st.markdown('<div class="master-header">📖 MASTER PROMT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="master-box">{final_prompt}</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; color: #00d4ff; font-size: 0.8rem; margin-top: 15px; font-family: Montserrat;'>
            لطفاً برای کپی کردن، متن داخل کادر سفید را انتخاب کنید<br>
            Please select the text inside the white box to copy
        </div>
        """, unsafe_allow_html=True)
