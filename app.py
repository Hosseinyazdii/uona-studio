import streamlit as st

# تنظیمات پایه و حذف منوهای استاندارد استریم‌لیت
st.set_page_config(page_title="UONA STUDIO | Cinematic Designer", layout="wide")

# تزریق CSS پیشرفته برای ظاهر لوکس و هدر سفارشی
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Montserrat:wght@100;400;900&display=swap');

    /* تنظیم پس‌زمینه کل اپلیکیشن */
    .stApp { 
        background: radial-gradient(circle, #0a192f 0%, #02050a 100%) !important; 
    }

    /* طراحی هدر لوکس */
    .header-container {
        text-align: center;
        padding: 40px 0;
        background: rgba(212, 175, 55, 0.03);
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.1);
        margin-bottom: 40px;
        box-shadow: inset 0 0 50px rgba(0,0,0,0.5);
    }

    .main-title {
        font-family: 'Playfair Display', serif !important;
        color: #d4af37 !important;
        font-size: 4.5rem !important;
        font-weight: 900 !important;
        margin-bottom: 0px !important;
        letter-spacing: 5px !important;
        text-transform: uppercase;
        background: linear-gradient(to bottom, #f1d592 0%, #d4af37 50%, #8a6d3b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(212, 175, 55, 0.4));
    }

    .sub-title {
        font-family: 'Montserrat', sans-serif !important;
        color: #ffffff !important;
        font-size: 1rem !important;
        font-weight: 100 !important;
        letter-spacing: 12px !important;
        text-transform: uppercase;
        opacity: 0.7;
        margin-top: -10px !important;
    }

    /* استایل بخش MASTER PROMPT READY */
    .master-ready {
        font-family: 'Montserrat', sans-serif !important;
        color: #00d4ff !important;
        font-size: 1.6rem !important;
        font-weight: 900 !important;
        letter-spacing: 5px !important;
        text-transform: uppercase;
        text-align: center;
        margin-top: 40px !important;
        margin-bottom: 15px !important;
        text-shadow: 0 0 12px rgba(0, 212, 255, 0.6);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
    }

    /* کادر درخشان خروجی نهایی */
    .output-box { 
        background: rgba(13, 27, 42, 0.9) !important; 
        border: 2px solid #00d4ff !important; 
        color: #00d4ff !important; 
        padding: 30px !important; 
        border-radius: 15px !important; 
        font-family: 'Courier New', monospace !important; 
        font-size: 1.3rem !important;
        box-shadow: 0 0 40px rgba(0, 212, 255, 0.15) !important;
        line-height: 1.7;
        text-align: left;
        user-select: all !important;
        transition: 0.4s;
    }
    .output-box:hover {
        border-color: #d4af37 !important;
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.3) !important;
        color: #ffffff !important;
    }

    /* تنظیمات المان‌های ورودی */
    label p { 
        color: #d4af37 !important; 
        font-weight: bold !important; 
        font-family: 'Montserrat', sans-serif !important;
        font-size: 1.1rem !important;
    }
    
    div[data-baseweb="select"] > div { 
        background-color: #0a1428 !important; 
        border: 1px solid rgba(212, 175, 55, 0.3) !important; 
        color: white !important; 
        border-radius: 10px !important;
    }

    .stButton>button {
        background: linear-gradient(45deg, #d4af37, #8a6d3b) !important; 
        color: #000 !important;
        font-weight: 900 !important; 
        border-radius: 10px !important; 
        width: 100% !important;
        border: none !important; 
        height: 4rem !important; 
        letter-spacing: 2px;
        font-family: 'Montserrat', sans-serif !important;
        transition: 0.4s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.6) !important;
        transform: translateY(-3px);
    }
    
    hr { border-top: 1px solid #d4af37 !important; opacity: 0.2; }
    </style>
    """, unsafe_allow_html=True)

# نمایش هدر اختصاصی
st.markdown("""
    <div class="header-container">
        <p class="main-title">UONA STUDIO</p>
        <p class="sub-title">CINEMATIC CHARACTER DESIGNER</p>
    </div>
    """, unsafe_allow_html=True)

# --- دیتابیس‌های منطق طراحی ---
nat_table = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin tone",
    "Syrian": "Levantine features, straight profile, fair to medium skin",
    "Saudi": "Peninsular Arab features, high cheekbones, deep-set eyes",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, sun-kissed tanned skin",
    "Kuwaiti": "Northern Gulf features, refined facial structure"
}

era_table = {
    "Contemporary": "Current lighting, ultra-sharp details",
    "Stone Age": "Primitive textures, raw aesthetic, natural lighting",
    "Medieval": "Gritty, rustic, heavy textures",
    "100 Years Ago": "Vintage aesthetic, early 20th-century film grain",
    "Ancient Era": "Ancient civilization styling, sun-drenched textures"
}

# --- پنل مدیریت ورودی‌ها (Layout) ---
col1, col2 = st.columns(2)

with col1:
    actor = st.selectbox("Actor Reference (G7):", ["No", "Yes"])
    age = st.selectbox("Age (J7):", ["Middle-aged", "Elderly / Senior", "Young Adult", "Teen", "Child"])
    gender = st.selectbox("Gender (G9):", ["Masculine / Male", "Feminine / Female"])
    nationality = st.selectbox("Nationality (J9):", list(nat_table.keys()))

with col2:
    era = st.selectbox("Time Period (G12):", list(era_table.keys()))
    char_style = st.selectbox("Character Style (J12):", ["Heroic Warrior", "Ailing Character", "Royal", "Scholar", "Sinister Villain"])
    # شرط هوشمند جنسیت برای ریش
    if gender == "Masculine / Male":
        grooming = st.selectbox("Grooming (J14):", ["Pyramidal Moustache", "Viking Beard", "Clean Shaven", "Heavy Stubble"])
    else:
        grooming = "None"
        st.info("Grooming disabled for female character.")
    canvas = st.selectbox("Canvas Size (J22):", ["16:9", "4:3", "1:1"])

st.markdown("---")

# ردیف سوم جزییات گریم
c3, c4, c5 = st.columns(3)
with c3:
    if age in ["Child", "Teen"]:
        sfx = "None"
        st.warning("SFX restricted for safety.")
    else:
        sfx = st.selectbox("SFX Makeup (G17):", ["3-Day Old Wound", "Burn Scar", "Bruise", "None"])

with c4:
    hair = st.selectbox("Hair Texture (J19):", ["Afro-Textured", "Wavy", "Curly", "Straight"])

with c5:
    material = st.selectbox("Material Finish (J17):", ["Matte Sealer", "Dried Blood", "Wet Look", "Translucent Skin"])

# --- ساخت Master Prompt ---
nat_desc = f" ({nat_table[nationality]})"
era_desc = f" ({era_table[era]})"
sfx_text = f"[SFX STUDY: Apply {sfx}]. " if sfx != "None" else ""

final_prompt = f"A professional cinematic {canvas} portrait of a {age} {gender} {nationality}{nat_desc} from the {era} era{era_desc}. " \
               f"Character style: {char_style}. Grooming: {grooming}. Hair texture: {hair}. " \
               f"{sfx_text}Finish: {material}. Technical: 8k, raw photography, subsurface scattering, cinematic rim light."

# --- نمایش خروجی با استایل جدید ---
st.markdown('<div class="master-ready"><span>🚀</span> MASTER PROMPT READY <span>🚀</span></div>', unsafe_allow_html=True)

# راهنمای کپی برای کاربر
st.info("لطفاً برای کپی کردن، روی متن داخل کادر زیر کلیک کنید:")

st.markdown(f'<div class="output-box">{final_prompt}</div>', unsafe_allow_html=True)

st.write("") # فاصله بصری

if st.button("🔥 GENERATE PROMPT"):
    st.success("پرامپت با موفقیت ساخته شد. متن در کادر آبی بالا آماده کپی است.")
