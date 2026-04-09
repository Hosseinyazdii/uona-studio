import streamlit as st

# تنظیمات پایه
st.set_page_config(page_title="UONA STUDIO", layout="wide")

# CSS حرفه‌ای برای ظاهر لوکس و هدر سه‌زبانه
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Montserrat:wght@100;400;900&display=swap');

    .stApp { background: radial-gradient(circle, #0a192f 0%, #02050a 100%) !important; }

    /* هدر اصلی */
    .header-container {
        text-align: center; padding: 40px 0; background: rgba(212, 175, 55, 0.03);
        border-radius: 20px; border: 1px solid rgba(212, 175, 55, 0.1);
        margin-bottom: 40px; box-shadow: inset 0 0 50px rgba(0,0,0,0.5);
    }
    .main-title {
        font-family: 'Playfair Display', serif !important; color: #d4af37 !important;
        font-size: 4.5rem !important; font-weight: 900 !important; letter-spacing: 5px !important;
        background: linear-gradient(to bottom, #f1d592 0%, #d4af37 50%, #8a6d3b 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(212, 175, 55, 0.4)); margin: 0 !important;
    }
    .sub-title {
        font-family: 'Montserrat', sans-serif !important; color: #ffffff !important;
        font-size: 1rem !important; letter-spacing: 12px !important; text-transform: uppercase;
        opacity: 0.7; margin-top: -10px !important;
    }

    /* بخش MASTER PROMPT READY */
    .master-ready {
        font-family: 'Montserrat', sans-serif !important; color: #00d4ff !important;
        font-size: 1.6rem !important; font-weight: 900 !important; letter-spacing: 5px !important;
        text-align: center; margin-top: 40px !important; text-shadow: 0 0 12px rgba(0, 212, 255, 0.6);
    }

    /* استایل راهنمای سه‌زبانه */
    .lang-guide {
        text-align: center; color: #d4af37; font-family: 'Tahoma', sans-serif;
        font-size: 0.9rem; margin-bottom: 15px; opacity: 0.9; line-height: 1.8;
    }

    /* کادر درخشان خروجی نهایی */
    .output-box { 
        background: rgba(13, 27, 42, 0.9) !important; border: 2px solid #00d4ff !important; 
        color: #00d4ff !important; padding: 30px !important; border-radius: 15px !important; 
        font-family: 'Courier New', monospace !important; font-size: 1.3rem !important;
        box-shadow: 0 0 40px rgba(0, 212, 255, 0.15) !important;
        line-height: 1.7; text-align: left; user-select: all !important; transition: 0.4s;
    }
    .output-box:hover { border-color: #d4af37 !important; box-shadow: 0 0 40px rgba(212, 175, 55, 0.3) !important; }

    label p { color: #d4af37 !important; font-weight: bold !important; font-family: 'Montserrat', sans-serif !important; }
    div[data-baseweb="select"] > div { background-color: #0a1428 !important; border: 1px solid rgba(212, 175, 55, 0.3) !important; color: white !important; }
    hr { border-top: 1px solid #d4af37 !important; opacity: 0.2; }
    </style>
    """, unsafe_allow_html=True)

# هدر
st.markdown("""
    <div class="header-container">
        <p class="main-title">UONA STUDIO</p>
        <p class="sub-title">CINEMATIC CHARACTER DESIGNER</p>
    </div>
    """, unsafe_allow_html=True)

# دیتابیس‌ها
nat_table = {"Iranian": "Indo-Aryan features, prominent nasal bridge", "Syrian": "Levantine features", "Saudi": "Peninsular Arab features", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Kuwaiti": "Northern Gulf features"}
era_table = {"Contemporary": "Current lighting", "Stone Age": "Primitive textures", "Medieval": "Gritty textures", "100 Years Ago": "Vintage film grain"}

# چیدمان ورودی‌ها
col1, col2 = st.columns(2)
with col1:
    actor = st.selectbox("Actor Reference:", ["No", "Yes"])
    age = st.selectbox("Age:", ["Middle-aged", "Elderly", "Young Adult", "Child"])
    gender = st.selectbox("Gender:", ["Masculine / Male", "Feminine / Female"])
    nationality = st.selectbox("Nationality:", list(nat_table.keys()))
with col2:
    era = st.selectbox("Time Period:", list(era_table.keys()))
    char_style = st.selectbox("Character Style:", ["Heroic Warrior", "Ailing Character", "Royal", "Scholar"])
    grooming = st.selectbox("Grooming:", ["Pyramidal Moustache", "Viking Beard", "Clean Shaven"]) if gender == "Masculine / Male" else "None"
    canvas = st.selectbox("Canvas Size:", ["16:9", "4:3", "1:1"])

st.markdown("---")
c3, c4, c5 = st.columns(3)
with c3:
    sfx = st.selectbox("SFX Makeup:", ["3-Day Old Wound", "Burn Scar", "None"]) if age not in ["Child", "Teen"] else "None"
with c4:
    hair = st.selectbox("Hair Texture:", ["Afro", "Wavy", "Curly", "Straight"])
with c5:
    material = st.selectbox("Material Finish:", ["Matte", "Dried Blood", "Wet Look"])

# ساخت پرامپت
nat_desc = f" ({nat_table[nationality]})"
era_desc = f" ({era_table[era]})"
sfx_text = f"[SFX: {sfx}]. " if sfx != "None" else ""
final_prompt = f"A professional cinematic {canvas} portrait of a {age} {gender} {nationality}{nat_desc} from the {era} era{era_desc}. Style: {char_style}. Grooming: {grooming}. Hair: {hair}. {sfx_text}Finish: {material}. Technical: 8k, raw photography, subsurface scattering."

# خروجی نهایی
st.markdown('<div class="master-ready">🚀 MASTER PROMPT READY 🚀</div>', unsafe_allow_html=True)

# راهنمای سه‌زبانه
st.markdown("""
    <div class="lang-guide">
        لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید<br>
        Please click on the text inside the box below to copy<br>
        يرجى الضغط على النص داخل المربع أدناه للنسخ
    </div>
    """, unsafe_allow_html=True)

st.markdown(f'<div class="output-box">{final_prompt}</div>', unsafe_allow_html=True)
