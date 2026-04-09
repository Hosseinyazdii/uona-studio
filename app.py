import streamlit as st

# تنظیمات اصلی
st.set_page_config(page_title="UONA STUDIO", layout="wide")

# CSS حرفه‌ای برای دیزاین لوکس و دکمه کپی
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #0a192f 0%, #02060c 100%) !important; }
    .main-title { color: #d4af37; font-size: 2.5rem; font-weight: 900; text-align: center; text-shadow: 0 0 15px rgba(212, 175, 55, 0.5); margin-bottom: 30px; }
    .output-box { 
        background-color: #0d1b2a !important; border: 2px solid #00d4ff !important; 
        color: #00d4ff !important; padding: 20px !important; border-radius: 12px !important; 
        font-family: 'monospace' !important; font-size: 1.1rem !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2) !important;
    }
    .stButton>button {
        background: #d4af37 !important; color: #02060c !important;
        font-weight: bold !important; border-radius: 8px !important; width: 100% !important;
        border: none !important; height: 3.5rem !important; font-size: 1.1rem !important;
    }
    label p { color: #d4af37 !important; font-weight: bold !important; }
    div[data-baseweb="select"] > div { background-color: #0a1428 !important; border: 1px solid #d4af37 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">UONA STUDIO | CINEMATIC DESIGNER</p>', unsafe_allow_html=True)

# دیتابیس‌ها
nat_table = {"Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin", "Syrian": "Levantine features", "Saudi": "Peninsular Arab features", "Egyptian": "North African features", "Emirati": "Gulf Arab features", "Kuwaiti": "Northern Gulf features"}
era_table = {"Contemporary": "Current lighting, sharp details", "Ancient Era": "Ancient styling", "Medieval": "Gritty textures", "50 Years Ago": "Analog film look"}

# پنل مدیریت
c1, c2 = st.columns(2)
with c1:
    actor = st.selectbox("Actor Reference:", ["No", "Yes"])
    age = st.selectbox("Age:", ["Middle-aged", "Elderly", "Young Adult", "Child"])
    gender = st.selectbox("Gender:", ["Masculine / Male", "Feminine / Female"])
    nationality = st.selectbox("Nationality:", list(nat_table.keys()))
with c2:
    era = st.selectbox("Time Period:", list(era_table.keys()))
    char_style = st.selectbox("Character Style:", ["Heroic Warrior", "Ailing Character", "Royal"])
    grooming = st.selectbox("Grooming:", ["Pyramidal Moustache", "Viking Beard", "Clean Shaven"]) if gender == "Masculine / Male" else "None"
    canvas = st.selectbox("Canvas Size:", ["16:9", "4:3", "1:1"])

st.write("---")
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

final_prompt = f"A professional cinematic {canvas} portrait of a {age} {gender} {nationality}{nat_desc} from the {era} era{era_desc}. Style: {char_style}. Grooming: {grooming}. Hair: {hair}. {sfx_text}Finish: {material}. Technical: 8k, raw photography."

st.markdown("### 🚀 MASTER PROMPT READY")
st.markdown(f'<div class="output-box">{final_prompt}</div>', unsafe_allow_html=True)

# ایجاد فاصله بدون نیاز به کتابخانه خارجی
st.write("")

# دکمه کپی هوشمند
if st.button("🔥 CLICK TO COPY PROMPT"):
    st.components.v1.html(f"""
        <script>
        const el = document.createElement('textarea');
        el.value = "{final_prompt}";
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        alert("Prompt Copied to Clipboard!");
        </script>
    """, height=0)
    st.success("پرامپت با موفقیت به کلیپ‌بورد منتقل شد.")
