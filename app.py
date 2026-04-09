import streamlit as st

# تنظیمات اصلی برای حذف حاشیه‌های پیش‌فرض
st.set_page_config(page_title="Uona Studio | Professional Cinematic Designer", layout="wide")

# تزریق CSS پیشرفته برای اورراید کردن کامل ظاهر استریم‌لیت
st.markdown("""
    <style>
    /* مخفی کردن منوهای اضافه استریم‌لیت */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* تنظیم پس‌زمینه اصلی با گرادینت سرمه‌ای تیره */
    .stApp {
        background: radial-gradient(circle, #0a192f 0%, #02060c 100%) !important;
    }

    /* طراحی کارت‌های اصلی */
    .stSelectbox, .stTextInput {
        background-color: rgba(10, 25, 47, 0.7) !important;
        border: 1px solid #d4af37 !important;
        border-radius: 10px !important;
        padding: 5px !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.1) !important;
    }

    /* استایل متن لیبل‌ها (طلایی نئونی) */
    label p {
        color: #d4af37 !important;
        font-family: 'Tahoma', sans-serif !important;
        font-size: 1rem !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        text-shadow: 0 0 5px rgba(212, 175, 55, 0.5) !important;
    }

    /* استایل تیتر اصلی */
    .main-title {
        color: #d4af37;
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        text-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
        border-bottom: 3px solid #d4af37;
        margin-bottom: 40px;
        padding-bottom: 10px;
    }

    /* باکس درخشان خروجی پرامپت (Cyan Glow) */
    .output-box {
        background-color: #0d1b2a !important;
        border: 2px solid #00d4ff !important;
        color: #00d4ff !important;
        padding: 25px !important;
        border-radius: 15px !important;
        font-family: 'Courier New', monospace !important;
        font-size: 1.1rem !important;
        box-shadow: 0 0 25px rgba(0, 212, 255, 0.2) !important;
        line-height: 1.6 !important;
    }

    /* دکمه طلایی لوکس */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #d4af37 0%, #f1d592 100%) !important;
        color: #02060c !important;
        border: none !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        padding: 15px 30px !important;
        border-radius: 12px !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">UONA STUDIO | PRO DESIGNER</p>', unsafe_allow_html=True)

# --- دیتابیس‌ها ---
# (همان جداول قبلی با دقت بالا)
nat_table = {"Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin", "Syrian": "Levantine features, fair to medium skin", "Saudi": "Peninsular Arab features, high cheekbones"}
era_table = {"Contemporary": "Current lighting, sharp details", "Ancient Era": "Ancient civilization styling", "Medieval": "Gritty, rustic textures"}
char_table = {"Heroic Warrior": "Strong jawline, battle-hardened gaze", "Ailing Character": "Pale skin, dark circles"}

# --- ساختار داشبورد ---
col1, col2 = st.columns(2)

with col1:
    actor = st.selectbox("Actor Reference:", ["No", "Yes"])
    age = st.selectbox("Age:", ["Middle-aged", "Elderly", "Young Adult", "Child"])
    gender = st.selectbox("Gender:", ["Masculine / Male", "Feminine / Female"])
    nationality = st.selectbox("Nationality:", list(nat_table.keys()))

with col2:
    era = st.selectbox("Time Period:", list(era_table.keys()))
    char_style = st.selectbox("Character Style:", list(char_table.keys()))
    if gender == "Masculine / Male":
        grooming = st.selectbox("Grooming:", ["Pyramidal Moustache", "Viking Beard", "Clean Shaven"])
    else:
        grooming = "None"
    
    canvas = st.selectbox("Canvas Size:", ["16:9", "4:3", "1:1"])

st.write("---")
c3, c4, c5 = st.columns(3)
with c3:
    sfx = st.selectbox("SFX Makeup:", ["3-Day Old Wound", "Burn Scar", "None"]) if age not in ["Child", "Teen"] else "None"
with c4:
    hair = st.selectbox("Hair Texture:", ["Afro", "Wavy", "Curly", "Straight"])
with c5:
    material = st.selectbox("Material Finish:", ["Matte", "Dried Blood", "Wet Look"])

# --- ساخت پرامپت ---
nat_desc = f" ({nat_table[nationality]})"
era_desc = f" ({era_table[era]})"
sfx_desc = f"[SFX: {sfx}]. " if sfx != "None" else ""

prompt = f"A professional cinematic {canvas} portrait of a {age} {gender} {nationality}{nat_desc} from the {era} era{era_desc}. Style: {char_style}. Grooming: {grooming}. Hair: {hair}. {sfx_desc}Finish: {material}. Technical: 8k, raw photography."

st.write("### 🚀 MASTER PROMPT READY")
st.markdown(f'<div class="output-box">{prompt}</div>', unsafe_allow_html=True)

# دکمه کپی به روش استریم‌لیت (نمایش کد قابل کپی)
st.write("")
if st.button("🔥 GENERATE & PREPARE FOR COPY"):
    st.text_area("کد زیر را کپی کنید:", value=prompt, height=100)
    st.success("پرامپت با موفقیت آماده شد. متن داخل کادر بالا را کپی کنید.")
