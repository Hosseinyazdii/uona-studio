import streamlit as st

# تنظیمات پایه برای حذف منوهای اضافه و تنظیم تم
st.set_page_config(page_title="Uona Studio | Cinematic Designer", layout="wide")

# تزریق CSS پیشرفته برای رسیدن به تم شماره ۱ (Luxury Cinematic)
st.markdown("""
    <style>
    /* کل صفحه */
    .stApp {
        background: radial-gradient(circle, #0a1428 0%, #050a15 100%) !important;
        color: #e0e0e0 !important;
    }
    
    /* هدر اصلی */
    h1 {
        color: #d4af37 !important;
        text-align: center !important;
        font-family: 'Playfair Display', serif !important;
        text-shadow: 0 0 20px rgba(212, 175, 55, 0.5) !important;
        border-bottom: 2px solid #d4af37 !important;
        padding-bottom: 20px !important;
        margin-bottom: 30px !important;
    }

    /* کادرهای انتخاب (Dropdowns) */
    div[data-baseweb="select"] > div {
        background-color: #0a1428 !important;
        border: 1px solid #d4af37 !important;
        border-radius: 8px !important;
        color: white !important;
    }
    
    /* لیبل‌ها (عنوان فیلدها) */
    label p {
        color: #d4af37 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        letter-spacing: 1px !important;
    }

    /* باکس نمایش پرامپت نهایی */
    .prompt-container {
        background: rgba(10, 20, 40, 0.8) !important;
        border: 2px solid #00d4ff !important;
        padding: 25px !important;
        border-radius: 15px !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3) !important;
        font-family: 'Courier New', monospace !important;
        color: #00d4ff !important;
        margin-top: 20px !important;
    }

    /* دکمه طلایی */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #f1d592 100%) !important;
        color: #050a15 !important;
        font-weight: 900 !important;
        border: none !important;
        padding: 15px !important;
        width: 100% !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 UONA STUDIO | Cinematic Character Designer")

# --- دیتابیس‌های VLOOKUP (بر اساس آخرین شیت‌های ارسالی تو) ---
nat_table = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure",
    "Syrian": "Levantine features, straight profile"
}

era_table = {
    "Stone Age": "Primitive aesthetic, raw textures",
    "BCE": "Ancient civilization styling, rudimentary tools",
    "Pre-Islamic": "Traditional regional heritage, antique textures",
    "Medieval": "Gritty, rustic, heavy textures",
    "100 Years Ago": "Vintage aesthetic, early 20th-century grooming",
    "Contemporary": "Current lighting, sharp details"
}

char_table = {
    "Heroic Warrior": "Strong jawline, battle-hardened gaze",
    "Sinister Villain": "Harsh shadows, menacing expression",
    "Royal": "Elegant posture, pristine skin",
    "Ailing Character": "Pale skin, dark circles, visible veins",
    "Bohemian Artist": "Creative styling, expressive eyes"
}

# --- چیدمان ورودی‌ها (Grid Layout) ---
col1, col2 = st.columns(2)

with col1:
    actor = st.selectbox("Actor Reference (G7):", ["No", "Yes"])
    age = st.selectbox("Age (J7):", ["Middle-aged", "Elderly / Senior", "Young Adult", "Teen", "Child"])
    gender = st.selectbox("Gender (G9):", ["Masculine / Male", "Feminine / Female"])
    nationality = st.selectbox("Nationality (J9):", list(nat_table.keys()))

with col2:
    era = st.selectbox("Time Period (G12):", list(era_table.keys()))
    char_style = st.selectbox("Character Style (J12):", list(char_table.keys()))
    
    # شرط هوشمند جنسیت برای ریش
    if gender == "Masculine / Male":
        grooming = st.selectbox("Grooming Style (J14):", ["Pyramidal Moustache", "Viking Beard", "Clean Shaven", "Heavy Stubble"])
    else:
        grooming = "None"
        st.info("Grooming disabled for female character.")

# --- بخش گریم و جزییات فنی ---
st.write("---")
c3, c4, c5 = st.columns(3)

with c3:
    if age in ["Child", "Teen"]:
        sfx = "None"
        st.warning("SFX Restricted for safety.")
    else:
        sfx = st.selectbox("SFX Makeup (G17):", ["3-Day Old Wound", "Encapsulated Silicone", "Burn Scar", "None"])

with c4:
    hair_tex = st.selectbox("Hair Texture (J19):", ["Afro-Textured", "Wavy", "Curly", "Straight"])
    aging = st.text_input("Skin/Aging Details (G19):", "Frontal Rhytids")

with c5:
    material = st.selectbox("Material Finish (J17):", ["Matte Sealer", "Dried Blood", "Wet Look", "Translucent Skin"])

# --- تنظیمات دوربین و ابعاد ---
with st.expander("🎥 Technical Specs (Lighting & Camera)"):
    canvas = st.selectbox("Canvas Size (J22):", ["16:9", "4:3", "1:1"])
    lighting = st.selectbox("Lighting (G22):", ["Rembrandt Lighting", "Cinematic Rim Light", "Softbox"])
    lens = st.selectbox("Lens (G24):", ["85mm Lens", "35mm Wide", "50mm Prime"])

# --- منطق ساخت Master Prompt ---
visual_guide = "[VISUAL GUIDE: Emulate facial structure] " if actor == "Yes" else ""
nat_desc = f" ({nat_table[nationality]})"
era_desc = f" ({era_table[era]})"
char_desc = f" ({char_table[char_style]})"
sfx_desc = f"[SFX STUDY: Apply {sfx}]. " if sfx != "None" else ""

final_prompt = f"{visual_guide}A professional cinematic {canvas} portrait of a {age} {gender} {nationality}{nat_desc} from the {era} era{era_desc}. " \
               f"Style: {char_style}{char_desc}. Grooming: {grooming}. " \
               f"Hair: {hair_tex}. Skin: {aging}. {sfx_desc}Finish: {material}. " \
               f"Technical: {lighting}, {lens}, 8k, raw photography."

# --- نمایش خروجی با استایل درخشان ---
st.write("---")
st.subheader("🚀 PROMPT MASTER OUTPUT")
st.markdown(f'<div class="prompt-container">{final_prompt}</div>', unsafe_allow_html=True)

if st.button("📋 COPY MASTER PROMPT"):
    st.success("Prompt generated successfully! Copy the text from the blue box.")
