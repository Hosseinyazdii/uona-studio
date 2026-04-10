import streamlit as st

# --- CONFIGURATION & STYLING ---
st.set_page_config(page_title="UONA Studio", layout="wide")

st.markdown("""
    <style>
    /* تنظیم فونت و استایل کلی */
    @import url('https://fonts.googleapis.com/css2?family=Bender&display=swap');
    
    .main { background-color: #0e1117; }
    
    /* هدر اختصاصی UONA */
    .header-container {
        display: flex;
        align-items: center;
        background-color: #001f3f; /* سرمه‌ای Carbine Blue */
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 25px;
        border: 1px solid #003366;
    }
    
    .header-title {
        color: #ffffff;
        font-family: 'Bender', serif;
        font-size: 32px;
        text-shadow: 2px 2px 4px #000000;
        margin-left: 20px;
    }

    /* استایل فوتر و آیکون‌ها */
    .footer-container {
        display: flex;
        justify-content: space-around;
        background: rgba(0,0,0,0.4);
        padding: 25px;
        border-top: 1px solid #333;
        margin-top: 50px;
    }
    
    .footer-icon {
        font-family: 'Bender', serif;
        font-size: 20px;
        color: white;
        text-shadow: 2px 2px 8px #000000;
        text-align: center;
    }
    </style>
""", unsafe_allow_safe=True)

# --- HEADER SECTION ---
logo_url = "https://raw.githubusercontent.com/Hosseinyazdii/uona-studio/main/logo.png"
st.markdown(f"""
    <div class="header-container">
        <img src="{logo_url}" width="70">
        <div class="header-title">UONA Group | <span style="font-weight: 200; font-size: 24px;">Cinematic Character Designer</span></div>
    </div>
""", unsafe_allow_safe=True)

# --- HELPER FUNCTION FOR 'OTHERS' OPTION ---
def select_with_others(label, options, key):
    selected = st.selectbox(label, options + ["Others..."], key=key)
    if selected == "Others...":
        return st.text_input(f"Type custom {label}:", key=f"input_{key}")
    return selected

# --- UI LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    actor_ref = st.selectbox("Actor Reference (G7):", ["No", "Yes"])
    age = select_with_others("Age (J7):", ["Young Adult", "Middle-aged", "Elderly / Senior"], "age")
    gender = st.selectbox("Gender (G9):", ["Masculine / Male", "Feminine / Female"])
    nationality = select_with_others("Nationality (J9):", ["Iranian", "Saudi", "British", "African"], "nat")

with col2:
    era = select_with_others("Time Period (G12):", ["Contemporary", "Ancient Era", "100 Years Ago"], "era")
    style = select_with_others("Character Style (J12):", ["Heroic Warrior", "Academic Student", "Villain"], "style")
    grooming = select_with_others("Grooming Style (J14):", ["Pyramidal Moustache", "Clean Shaven", "Full Beard"], "groom")

st.divider()

col3, col4 = st.columns(2)
with col3:
    sfx = select_with_others("SFX Makeup (G17):", ["3-Day Old Wound", "Hematoma", "Vitiligo"], "sfx")
    hair = select_with_others("Hair Texture (J19):", ["Afro-Textured", "Straight", "Wavy"], "hair")

with col4:
    finish = select_with_others("Material Finish (J17):", ["Matte Sealer", "Glossy", "Satin"], "finish")
    skin = st.text_input("Skin/Aging Details (G19):", value="Frontal Rhytids")

# --- PROMPT GENERATION LOGIC (V14) ---
consistency_msg = "[STRICT CONSISTENCY MODE: Maintain identity...]: " if actor_ref == "Yes" else ""
sfx_header = "[PROFESSIONAL SFX ARTISTRY: Detailed prosthetic showing]: " if sfx else ""

prompt = (
    f"{consistency_msg}A cinematic portrait of a {age} {gender} {nationality} from the {era} era. "
    f"Character archetype: {style}. Grooming: {grooming}. Hair: {hair}. "
    f"Skin: {skin}. {sfx_header}{sfx}. Material: {finish}. "
    f"Technical: 8k resolution, subsurface scattering, cinematic light physics, raw photography, no-retouch."
)

st.subheader("Master Prompt Output")
st.text_area("Copy this to Gemini:", value=prompt, height=150)

if st.button("📋 Copy Prompt"):
    st.write("Prompt ready to copy! (Use Cmd+C on your Mac)")

# --- FOOTER SECTION ---
st.markdown("""
    <div class="footer-container">
        <div class="footer-icon">🎬<br>Series</div>
        <div class="footer-icon">🎞️<br>Movie</div>
        <div class="footer-icon">🏛️<br>Theater</div>
        <div class="footer-icon">🎥<br>Production</div>
    </div>
""", unsafe_allow_safe=True)
