import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA STUDIO", layout="wide")

# CSS حرفه‌ای برای دیزاین لوکس و کادر درخشان
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #0a192f 0%, #02060c 100%) !important; }
    .main-title { color: #d4af37; font-size: 2.8rem; font-weight: 900; text-align: center; text-shadow: 0 0 15px rgba(212, 175, 55, 0.5); margin-bottom: 20px; }
    
    /* کادر درخشان پرامپت نهایی */
    .output-box { 
        background-color: #0d1b2a !important; border: 2px solid #d4af37 !important; 
        color: #00d4ff !important; padding: 25px !important; border-radius: 12px !important; 
        font-family: 'Courier New', monospace !important; font-size: 1.2rem !important;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.2) !important;
        line-height: 1.6;
        text-align: left;
        user-select: all !important; /* این خط باعث میشه با یک کلیک کل متن انتخاب بشه */
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #d4af37, #f1d592) !important; color: #02060c !important;
        font-weight: bold !important; border-radius: 10px !important; width: 100% !important;
        border: none !important; height: 3.5rem !important; font-size: 1.1rem !important;
    }
    
    label p { color: #d4af37 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    div[data-baseweb="select"] > div { background-color: #0a1428 !important; border: 1px solid #d4af37 !important; color: white !important; }
    hr { border-top: 1px solid #d4af37 !important; opacity: 0.3; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">UONA STUDIO | CINEMATIC DESIGNER</p>', unsafe_allow_html=True)

# دیتابیس‌ها
nat_table = {"Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin", "Syrian": "Levantine features", "Saudi": "Peninsular Arab features", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Kuwaiti": "Northern Gulf features"}
era_table = {"Contemporary": "Current lighting, sharp details", "Stone Age": "Primitive textures", "Medieval": "Gritty textures", "100 Years Ago": "Vintage film grain"}

# پنل مدیریت
c1, c2 = st.columns(2)
with c1:
    actor = st.selectbox("Actor Reference:", ["No", "Yes"])
    age = st.selectbox("Age:", ["Middle-aged", "Elderly", "Young Adult", "Child"])
    gender = st.selectbox("Gender:", ["Masculine / Male", "Feminine / Female"])
    nationality = st.selectbox("Nationality:", list(nat_table.keys()))
with c2:
    era = st.selectbox("Time Period:", list(era_table.keys()))
    char_style = st.selectbox("Character Style:", ["Heroic Warrior", "Ailing Character", "Royal", "Scholar"])
    grooming = st.selectbox("Grooming:", ["Pyramidal Moustache", "Viking Beard", "Clean Shaven"]) if gender == "Masculine / Male" else "None"
    canvas = st.selectbox("Canvas Size:", ["16:9", "4:3", "1:1"])

st.markdown("---")
c3, c4, c5 = st.columns(3)
with c3:
    sfx = st.selectbox("SFX Makeup:", ["3-Day Old Wound", "Burn Scar", "Bruise", "None"]) if age not in ["Child", "Teen"] else "None"
with c4:
    hair = st.selectbox("Hair Texture:", ["Afro", "Wavy", "Curly", "Straight"])
with c5:
    material = st.selectbox("Material Finish:", ["Matte", "Dried Blood", "Wet Look", "Translucent Skin"])

# ساخت پرامپت
nat_desc = f" ({nat_table[nationality]})"
era_desc = f" ({era_table[era]})"
sfx_text = f"[SFX: {sfx}]. " if sfx != "None" else ""

final_prompt = f"A professional cinematic {canvas} portrait of a {age} {gender} {nationality}{nat_desc} from the {era} era{era_desc}. Style: {char_style}. Grooming: {grooming}. Hair: {hair}. {sfx_text}Finish: {material}. Technical: 8k, raw photography, subsurface scattering."

st.markdown("### 🚀 MASTER PROMPT READY")
st.info("لطفاً متن داخل کادر زیر را کپی کنید:")
st.markdown(f'<div class="output-box">{final_prompt}</div>', unsafe_allow_html=True)

st.write("") 

if st.button("🔥 GENERATE PROMPT"):
    st.success("پرامپت با موفقیت ساخته شد. حالا متن آبی کادر بالا را کپی و در جمینای پیست کنید.")
