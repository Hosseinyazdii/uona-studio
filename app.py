import streamlit as st

# تنظیمات اصلی صفحه با تم تیره
st.set_page_config(page_title="Uona Studio - Cinematic Designer", layout="wide")

# اعمال استایل "تم شماره ۱" (Luxury Cinematic)
st.markdown("""
    <style>
    .main { background-color: #050a15; color: #e0e0e0; }
    .stSelectbox label, .stTextInput label { color: #d4af37 !important; font-size: 18px; font-weight: bold; }
    .stButton>button { 
        background-color: #d4af37; color: #050a15; 
        font-weight: bold; border-radius: 8px; border: none; height: 3em;
    }
    .stButton>button:hover { background-color: #f1d592; color: #050a15; }
    .prompt-box { 
        background-color: #0a1428; border: 1px solid #d4af37; 
        padding: 20px; border-radius: 12px; color: #00d4ff; font-family: 'Courier New', monospace;
    }
    h1 { color: #d4af37; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 UONA STUDIO | Cinematic Character Designer")

# --- دیتابیس‌های VLOOKUP (ثبت شده در حافظه) ---
nat_table = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, almond-shaped eyes, olive skin tone",
    "Egyptian": "North African features, rounder face, dark expressive eyes, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, intense dark eyes, sun-kissed tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones, deep-set eyes, desert-gold skin tone",
    "Kuwaiti": "Northern Gulf features, refined facial structure, dark hair, light olive complexion",
    "Syrian": "Levantine features, straight profile, varying eye colors, fair to medium skin tone"
}

hair_table = {
    "Afro-Textured": "Kinky-coily patterns, high density, matte finish, tight structural coils",
    "Wavy (Type 2)": "Natural S-shape waves, effortless flow, soft luster, beachy texture",
    "Curly (Type 3)": "Defined ringlets, springy loops, voluminous structure, high frizz detail",
    "Straight (Sleek)": "Linear alignment, high specular highlights, silky smooth surface"
}

# --- بخش ورودی‌های اصلی (Dashborad Cells) ---
col1, col2 = st.columns(2)

with col1:
    actor = st.selectbox("Actor Reference (G7):", ["No", "Yes"])
    age = st.selectbox("Age (J7):", ["Middle-aged", "Elderly / Senior", "Young Adult", "Teen", "Child"])
    gender = st.selectbox("Gender (G9):", ["Masculine / Male", "Feminine / Female"])
    nationality = st.selectbox("Nationality (J9):", list(nat_table.keys()))

with col2:
    era = st.selectbox("Time Period (G12):", ["Contemporary", "Ancient Era", "Medieval", "50 Years Ago", "100 Years Ago"])
    char_style = st.selectbox("Character Style (J12):", ["Heroic Warrior", "Ailing / Sickly Character", "Scholar", "Elite Athlete"])
    
    # شرط هوشمند جنسیت
    if gender == "Masculine / Male":
        grooming = st.selectbox("Grooming Style (J14):", ["Pyramidal Moustache", "Viking Beard", "Clean Shaven", "Van Dyke"])
    else:
        grooming = "None"
        st.info("Grooming disabled for female character.")

# --- بخش گریم و متریال ---
st.write("---")
c3, c4, c5 = st.columns(3)

with c3:
    # شرط هوشمند سن برای SFX
    if age in ["Child", "Teen"]:
        sfx = "None"
        st.warning("SFX disabled for safety (Age Restriction).")
    else:
        sfx = st.selectbox("SFX Makeup (G17):", ["3-Day Old Wound", "Burn Scar", "Bruise", "None"])

with c4:
    hair_tex = st.selectbox("Hair Texture (J19):", list(hair_table.keys()))
    aging = st.text_input("Skin/Aging Details (G19):", "Frontal Rhytids")

with c5:
    material = st.selectbox("Material Finish (J17):", ["Matte Sealer", "Dried Blood & Dust", "Wet Look", "Silicon Finish"])

# --- بخش فنی ---
with st.expander("🎥 Technical Specifications (Camera & Lighting)"):
    canvas_size = st.selectbox("Canvas Size (J22):", ["Aspect Ratio 16:9", "Aspect Ratio 4:3", "Aspect Ratio 1:1"])
    lighting = st.selectbox("Lighting (G22):", ["Rembrandt Lighting", "Softbox", "Hard Sunlight", "Cinematic Rim Light"])
    lens = st.selectbox("Lens (G24):", ["85mm Lens", "35mm Wide", "50mm Prime"])

# --- منطق ساخت پرامپت (Master Prompt) ---
visual_guide = "[VISUAL GUIDE: Emulate facial structure of attached subject] " if actor == "Yes" else ""
nat_desc = f" ({nat_table[nationality]})" if nationality else ""
hair_desc = f"Hair Texture: {hair_table[hair_tex]}. " if hair_tex else ""
sfx_desc = f"[CINEMATIC PROSTHETIC STUDY: Apply {sfx} SFX]. " if sfx != "None" else ""

master_prompt = f"{visual_guide}A professional cinematic {canvas_size.replace('Aspect Ratio ', '')} portrait of a {age} {gender} {nationality}{nat_desc} from the {era} era. " \
                f"Character style: {char_style}. " \
                f"Grooming: {grooming}. " \
                f"{hair_desc}Skin: {aging}. {sfx_desc}" \
                f"Finish: {material}. " \
                f"Technical: Lighting: {lighting}, Lens: {lens}, 8k, subsurface scattering, raw photography, no-retouch."

# --- خروجی نهایی ---
st.write("---")
st.subheader("🚀 Master Prompt Output")
st.markdown(f'<div class="prompt-box">{master_prompt}</div>', unsafe_allow_html=True)

if st.button("📋 Copy to Clipboard"):
    st.info("Prompt ready to be copied from the box above!")