import streamlit as st
from datetime import datetime
import os
import json
import base64

# ==========================================
# 1. تنظیمات پلتفرم و دیتابیس
# ==========================================
st.set_page_config(
    page_title="UONA STUDIO | AI SAAS", 
    page_icon="logo.PNG", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

DB_FILE = ".users_db.json"
PROJ_FILE = ".projects_db.json"

def load_json(file, default):
    if not os.path.exists(file):
        with open(file, "w") as f: json.dump(default, f)
    with open(file, "r") as f: return json.load(f)

def save_json(file, data):
    with open(file, "w") as f: json.dump(data, f)

def find_bg_file():
    possible_names = ["background.jpg", "background.jpeg", "background.png", "Background.jpg", "BACKGROUND.JPG"]
    for name in possible_names:
        if os.path.exists(name):
            return name
    return None

def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    
    mime_type = "image/png" if image_file.lower().endswith('.png') else "image/jpeg"
    
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"], .stApp {{
            background: linear-gradient(rgba(2,6,12,0.85), rgba(10,25,47,0.85)), url(data:{mime_type};base64,{encoded_string}) !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# 2. دیتابیس مگا پرامپت (بهینه‌سازی شده)
# ==========================================

GENDER_LIST = ["Masculine / Male", "Feminine / Female", "Androgynous"]

AGE_LIST = [
    "Child / Pre-adolescent", 
    "Adolescent / Teenager", 
    "Young Adult (Early 20s)", 
    "Middle-aged (Late 40s)", 
    "Elderly / Senior", 
    "Ancient / Centenarian"
]

NAT_DESC = {
    "Iranian": "Indo-Aryan features, prominent nasal bridge, olive skin",
    "Egyptian": "North African features, warm bronze skin tone",
    "Emirati": "Gulf Arab features, sharp jawline, tanned skin",
    "Saudi": "Peninsular Arab features, high cheekbones",
    "Kuwaiti": "Northern Gulf features, refined structure",
    "Syrian": "Levantine features, straight profile",
    "Turkish": "Eurasian features, strong facial contours, dark hair, medium olive skin",
    "Indian": "South Asian features, deep-set dark eyes, thick dark hair, rich warm undertones",
    "American": "Diverse North American features, broad range of skin tones, varied facial structures",
    "European": "Caucasian features, varied eye colors, prominent brow ridge, fair complexion",
    "African": "Sub-Saharan features, broad nasal structure, full lips, deep melanated skin",
    "Chinese": "East Asian features, epicanthic folds, high cheekbones, smooth skin texture"
}

ERA_DESC = {
    "Contemporary / Modern Day": "Current lighting, sharp details, digital photography look",
    "Stone Age / Prehistoric": "Primitive aesthetic, raw textures, survivalist look",
    "Before Common Era (BCE)": "Ancient civilization styling, rudimentary tools/makeup",
    "Pre-Islamic Era": "Traditional regional heritage, antique textures",
    "Ancient Era (Hellenistic/Roman)": "Classical features, draping, historical accuracy",
    "Medieval / Dark Ages": "Gritty, rustic, heavy textures, atmospheric mood",
    "200 Years ago (Early 19th Century)": "Regency style, natural fiber textures, era-specific grooming",
    "150 years ago (Victorian Era)": "Formal, structured, refined textures, pale complexions",
    "100 Years ago (Roaring 20s)": "Vintage aesthetic, early 20th-century grooming/lighting",
    "50 Years ago (1970s Retro)": "Analog film look, warm hues, vintage hair styles",
    "Futuristic / Cyberpunk": "Neon accents, synthetic materials, high-tech glow",
    "Post-Apocalyptic": "Dirty, weathered, distressed textures, gritty survivalist"
}

CONCEPTS = {
    "Heroic Warrior": "Strong jawline, confident gaze, slight battle wear",
    "Sinister Villain": "Harsh shadows, menacing expression, sharp features",
    "Scholar / Intellectual": "Refined appearance, focused eyes, thoughtful pose",
    "Royal / Aristocratic": "Elegant posture, pristine skin, luxury textures",
    "Mercenary / Outlaw": "Rugged, weathered, scars, untamed grooming",
    "Mystic / Shaman": "Otherworldly look, spiritual paint, ethereal lighting",
    "Corporate Executive / CEO": "Clean-cut, authoritative, sharp professional lighting",
    "Elite Athlete / Fitness Pro": "Defined muscularity, healthy skin glow, sweat detail",
    "Bohemian Artist": "Creative styling, messy hair, expressive eyes",
    "Average Citizen": "Naturalistic, candid, everyday lighting",
    "Blue-collar / Technician": "Grime, work-worn skin, functional appearance",
    "Academic Student": "Youthful, inquisitive, natural-soft lighting",
    "High-fashion Model": "Angular features, studio lighting, flawless skin",
    "Retiree / Grandparent": "Dignified aging, soft textures, wisdom-filled gaze",
    "Urban / Street Style": "Modern edge, trendy accessories, natural city light",
    "Rural / Outdoorsman": "Sun-damaged skin, practical gear, natural daylight",
    "Red Carpet / Gala Guest": "Glamorous, high-contrast lighting, perfect grooming",
    "Ailing / Sickly Character": "Pale skin, dark circles, visible veins, weak posture"
}

GROOM_DESC = {
    "Saudi Anchor Beard": "Sharp and angular form connected to the chin",
    "Pyramidal Moustache": "Mustache with wide edges and a narrow top",
    "Clean Shaven": "Smooth skin, no stubble, close-cut grooming finish",
    "Light Stubble": "Very short, even stubble, uniform shade pattern",
    "Heavy Stubble": "Thicker, rough texture, darker shade, irregular growth",
    "Designer Stubble": "Precisely trimmed, clean sharp defined edges",
    "Shadow Fade Beard": "Faded sides, denser hair on chin, smooth gradient transition",
    "Goatee (No Mustache)": "Chin beard only, completely clean shaven cheeks and upper lip",
    "Classic Goatee": "Chin beard connected to mustache, smooth circular blend",
    "Van Dyke": "Pointed chin beard, disconnected floating mustache, sharp detail",
    "Anchor Beard": "Pointed chin beard, thin defined floating mustache",
    "Short Boxed Beard": "Short, full beard, precise square defined edges",
    "Medium Boxed Beard": "Medium length, full, structured clean appearance",
    "Long Full Beard": "Long, thick, natural growth pattern, dense hair volume",
    "Unkempt Beard": "Messy natural growth, disheveled texture, random hair direction",
    "Scruffy Beard": "Patchy, rough texture, slightly dirty, abandoned grooming",
    "Wild Beard": "Long, chaotic, untamed texture, tangled strands",
    "Bedouin Beard": "Long, natural sun-exposed texture, weathered appearance",
    "Viking Beard": "Long, thick, braided beard strands, rugged texture",
    "Medieval Beard": "Natural, period-authentic growth, no sharp trimming",
    "Philosopher Beard": "Long, soft texture, intellectual appearance, flowing hair",
    "Warrior Beard": "Thick, rugged, battle-worn appearance, natural textures",
    "Graying Patches": "Natural gray strands, mixed-tone patches, mature appearance",
    "Split Texture Beard": "Smooth on chin, rough on sides, dual-textured growth",
    "Short Sideburns": "Above the ear level, clean shaven cheeks",
    "Mid-Ear Sideburns": "Level with the tragus, standard length",
    "Long Sideburns": "Reaches the ear lobe level",
    "Extra-Long Sideburns": "Passes the ear lobe, extended length",
    "High Sideburns": "Reaches the temple level, very short",
    "Tapered Length": "Gradient length, smoothly faded into skin",
    "Square Sideburns": "Horizontal cut bottom, clean edges",
    "Pointed Sideburns": "Triangle point bottom, defined shape",
    "Rounded Sideburns": "Soft, circular finish bottom",
    "Pencil Sideburns": "Ultra-thin line, high detail trimming",
    "Flared Sideburns": "Widens at the base, classic wide look",
    "Angled Sideburns": "Slanted cut bottom, geometric defined shape",
    "Mutton Chops": "Wide full sideburns connected to mustache, clean chin",
    "Friendly Mutton Chops": "Mutton chops connected via mustache, soft blend",
    "Soul Patch": "Small patch below the lower lip, defined connection"
}

HAIR_TEX_DESC = {
    "Afro-Textured": "Kinky-coily patterns, high density, matte finish, tight structural coils",
    "Wavy (Type 2)": "Natural S-shape waves, effortless flow, soft luster, beachy texture",
    "Curly (Type 3)": "Defined ringlets, springy loops, voluminous structure, high frizz detail",
    "Straight (Sleek)": "Linear alignment, high specular highlights, silky smooth surface",
    "Coarse & Wiry": "Thick diameter strands, rough cuticle texture, irregular graying patterns",
    "Fine & Wispy": "Low density, translucent thin strands, sensitive to wind/motion",
    "Disheveled & Matted": "Tangled clumps, distressed cuticles, weathered look, realistic stray hairs",
    "Braided / Cornrows": "Intricate interlocking patterns, scalp tension detail, tight woven texture"
}

HAIR_COLORS = {
    "Salt and pepper beard, 10% grey hair": "Black hair mixed with scattered white strands",
    "Salt and pepper beard, 30% grey hair": "Black hair mixed with noticeable white strands",
    "Salt and pepper beard, 50% grey hair": "Even mix of black and white hair strands",
    "Salt and pepper beard, 70% grey hair": "Mostly white hair mixed with scattered black strands",
    "Jet black beard / Natural black": "Jet black, deep and rich natural black",
    "Deep espresso brown / Dark chocolate": "Deep espresso brown with warm undertones",
    "Light chestnut brown / Sandy brown": "Light chestnut brown with honey or sandy tones",
    "Ash blonde / Golden blonde beard": "Ash blonde (cool tone) or golden blonde (warm tone)"
}

SFX_DESC = {
    "Fresh Katana/Sword Slash": "Deep sword wound, open edges, active bleeding",
    "Glass Laceration with Shards": "Glass laceration, irregular edges, glass shards embedded in the tissue",
    "Blunt Force Contusion": "Blunt force contusion, severe swelling, inflamed redness, no laceration",
    "3-Day old wound (Scabbing)": "3-day old wound, beginning to scab, dark pink edges",
    "1-Week old wound (Granulation)": "1-week old wound, pink granulation tissue, flaking skin",
    "1-Month old Old Scar (Maturation)": "1-month old scar, fibrous tissue, reduced redness, slight indentation",
    "1-Year Old Keloid Scar": "1-year old keloid scar, raised excess tissue, firm texture",
    "5-Years Old Atrophic Scar": "5-year old atrophic scar, pale, white, flush with the skin",
    "Fresh Periorbital Hematoma": "Fresh periorbital hematoma, purplish-red redness, severe inflammation",
    "24-Hour Old Bruise (Deep Purple)": "24-hour old bruise, deep purple and blue, cloudy tissue",
    "3-Days Old Bruise (Greenish-Yellow)": "3-day old bruise, starting to turn yellow, greenish edges",
    "15-Days Old Fading Bruise": "15-day old fading bruise, very faint yellow spots, healing",
    "Chemical Acid Burn (Corrosive)": "Chemical acid burn, melted tissue, viscous and corroded texture",
    "1st Degree Sunburn/Erythema": "1st degree burn, uniform redness, no blisters, sensitive skin",
    "2nd Degree Burn with Blisters": "2nd degree burn, fluid-filled blisters, shiny and peeling skin",
    "Bilateral Vitiligo Depigmentation": "Vitiligo, completely white patches with distinct borders, no raised texture",
    "Diffuse Hyperpigmentation & Melasma": "Hyperpigmentation, irregular dark brown spots, melasma pattern"
}

MAT_DESC = {
    "Encapsulated Silicone": "Realistic skin-like translucency, blended edges",
    "Feathered Edges": "Seamless transition between prosthetic and skin",
    "Translucent Skin Finish": "Layers of depth, natural light absorption",
    "Prosthetic Adhesive": "Texture of professional bonding, visible seal",
    "Matte Sealer": "Non-reflective surface, velvety skin texture",
    "Alcohol-activated Palette": "Translucent color washes, realistic bruising/veins",
    "Granulation Tissue": "Raw, healing tissue texture, high detail"
}

AGE_PROG_DESC = {
    "Deep Nasolabial Folds": "Deep nasolabial folds from the side of the nose to the corner of the lips",
    "Pronounced Crow's Feet": "Radial wrinkles around the eyes",
    "Hooded Eyelids / Ptosis": "Hooded eyelids, sagging skin on the upper eyelids",
    "Dermal Crepiness": "Crepey skin texture, very fine and delicate wrinkles on the skin surface",
    "Visible Liver Spots (Lentigines)": "Visible liver spots, brown pigmentation due to sun and age",
    "Sagging Jowls & Loose Skin": "Sagging jowls and jawline, loose skin on the sides of the face",
    "Frontal Rhytids (Forehead Furrows)": "Deep horizontal furrows on the forehead",
    "Periorbital Hollows & Eye Bags": "Periorbital hollows and under-eye bags, fat depletion and extreme fatigue appearance",
    "Vertical Lip Lines (Smoker's Lines)": "Vertical lip lines, realistic aging details",
    "Age-related Telangiectasia": "Visible blood vessels, fine red capillaries on the cheeks and nose"
}

SFX_PROG_DESC = {
    "Stage 1: Fresh & Bleeding": "Wait for final prompt from Master...",
    "Stage 2: Healing & Bruised": "Wait for final prompt from Master..."
}

LIGHT_DESC = {
    "Rembrandt Lighting": "Classic cinematic light with a small triangle under the eye, highly elegant",
    "Cold Rim Lighting": "Cold blue rim light separating the character from the background",
    "Chiaroscuro": "Very high contrast between darkness and light",
    "Teal and Orange Lighting": "Classic cinematic mix of cool teal and warm orange tones",
    "Bokeh Background": "Shallow depth of field, subject separated with blurred bokeh background",
    "Chiaroscuro Lighting": "Severe contrast between shadow and light, dramatic facial volume",
    "Volumetric God Rays": "Linear light rays passing through fog or dust, creating a spiritual or eerie atmosphere",
    "Cinematic Golden Hour": "Warm and soft sunset light, highlighting natural skin tones",
    "High-Key Studio Lighting": "Flat and bright light with no shadows, revealing all details clearly",
    "Low-Key Moody Lighting": "Very low and dark light, revealing only specific parts of the face, mysterious mood",
    "Neon Cyberpunk Rim Light": "Colorful neon edge lights outlining the face, modern fantasy aesthetic",
    "Hard Top Lighting": "Harsh overhead light, creating strong shadows under the eyes and cheekbones",
    "Flickering Candlelight": "Flickering candlelight, creating soft and dynamic shadows, historical classic vibe",
    "Soft Professional Softbox": "Standard professional photography light, making the skin look velvety and even"
}

CAM_DESC = {
    "85 mm Lens, Eye-Level Shot": "Classic portrait lens, perfect for showing skin texture without facial distortion",
    "100 mm Macro Lens, Extreme Close-Up": "Macro lens, specifically for stunning details like skin pores or SFX wound textures",
    "50 mm Lens, Dutch Angle": "Normal lens with tilted angle, creating suspense and dread",
    "35 mm Lens, Low-Angle (Hero Shot)": "Slightly wide, low-angle shot showing the character as powerful and heroic",
    "24 mm Wide-Angle, High-Angle": "Wide-angle lens from a high angle, making the face look slightly elongated or vulnerable",
    "200 mm Telephoto, Profile View": "Telephoto lens, completely blurring the background to focus entirely on the jawline from the profile",
    "50 mm Lens, Top-Down (Bird's Eye)": "Completely vertical top-down view, excellent for overhead design details",
    "85 mm Lens, Three-Quarter View": "Three-quarter angle, standard for showing facial volume contouring and professional shading"
}

SIZE_LIST = [
    "Aspect Ratio 4:5 (Portrait/Vertical)",
    "Aspect Ratio 5:4 (Portrait)",
    "Aspect Ratio 16:9 (Widescreen)",
    "Aspect Ratio 9:16 (Vertical / Stories)",
    "Aspect Ratio 2.39:1 (Anamorphic / Cinemascope)",
    "Aspect Ratio 1:1 (Square)"
]

# ==========================================
# 3. مدیریت وضعیت (State Machine)
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'plan' not in st.session_state: st.session_state.plan = "UONA Core"
if 'route' not in st.session_state: st.session_state.route = 'login'
if 'step' not in st.session_state: st.session_state.step = 1

if 'draft' not in st.session_state: 
    st.session_state.draft = {
        "actor":"None", "gen":"", "age":"", "nat":"", "era":"", "h_col":"", 
        "h_tex":"", "sfx":"", "mat":"", "char":"", "groom":"", "cam":"", "light":"", "size":"",
        "age_prog":"None", "sfx_prog":"None"
    }

def go_to(route): st.session_state.route = route; st.rerun()
def next_step(): st.session_state.step += 1; st.rerun()
def prev_step(): st.session_state.step -= 1; st.rerun()
def add_n(lst): return ["None"] + lst + ["Others"]

def smart_select(label, options, key, help_dict=None):
    opts = add_n(options)
    curr_val = st.session_state.draft.get(key, "")
    idx = 0
    if curr_val in opts: idx = opts.index(curr_val)
    elif curr_val and curr_val != "None": idx = len(opts) - 1
    
    if help_dict:
        c1, c2 = st.columns([11, 1])
        with c1:
            sel = st.selectbox(label, opts, index=idx, key=f"sel_{key}")
        with c2:
            with st.popover("❕"):
                help_html = f"""
                <div style="background-color: #000000 !important; margin: -1rem; padding: 1rem; min-height: 100px;">
                    <div style="color: #00f2ff; font-weight: 900; font-family: 'Cinzel', serif; margin-bottom: 10px; font-size: 0.9rem; border-bottom: 1px solid rgba(0,242,255,0.3); padding-bottom: 5px; text-transform: uppercase;">
                        EXCEL DICTIONARY: {label}
                    </div>
                    {"".join([f"<div style='color: #d0e0f0; font-family: Montserrat; font-size: 0.8rem; line-height: 1.8; margin-bottom: 4px;'><b style='color: #00f2ff;'>{k}:</b> {v}</div>" for k, v in help_dict.items()])}
                </div>
                """
                st.markdown(help_html, unsafe_allow_html=True)
    else:
        sel = st.selectbox(label, opts, index=idx, key=f"sel_{key}")
        
    if sel == "Others":
        custom = st.text_input(f"Type Custom {label}", value=curr_val if curr_val not in opts else "", key=f"txt_{key}")
        st.session_state.draft[key] = custom
    else:
        st.session_state.draft[key] = sel

def generate_prompt(draft):
    G7 = draft.get('actor', '')
    J22 = "" 
    J7 = draft.get('age', '') if draft.get('age') != "None" else ""
    G9 = draft.get('gen', '') if draft.get('gen') != "None" else ""
    
    J9_key = draft.get('nat', '') if draft.get('nat') != "None" else ""
    G12_key = draft.get('era', '') if draft.get('era') != "None" else ""
    J12_key = draft.get('char', '') if draft.get('char') != "None" else ""
    J14_key = draft.get('groom', '') if draft.get('groom') != "None" else ""
    
    h_col_key = draft.get('h_col', '') if draft.get('h_col') != "None" else ""
    h_tex_key = draft.get('h_tex', '') if draft.get('h_tex') != "None" else ""
    
    G17_key = draft.get('sfx', '') if draft.get('sfx') != "None" else ""
    J17_key = draft.get('mat', '') if draft.get('mat') != "None" else ""
    G22_key = draft.get('light', '') if draft.get('light') != "None" else ""
    G24_key = draft.get('cam', '') if draft.get('cam') != "None" else ""
    
    age_prog_key = draft.get('age_prog', 'None')
    sfx_prog_key = draft.get('sfx_prog', 'None')

    is_arc_active = (age_prog_key != "None") or (sfx_prog_key != "None")

    J9_desc = NAT_DESC.get(J9_key, "standard features") if J9_key else ""
    G12_desc = ERA_DESC.get(G12_key, G12_key) if G12_key else ""
    J12_desc = CONCEPTS.get(J12_key, J12_key) if J12_key else ""
    J14_desc = GROOM_DESC.get(J14_key, J14_key) if J14_key else ""
    
    col_desc = HAIR_COLORS.get(h_col_key, h_col_key)
    tex_desc = HAIR_TEX_DESC.get(h_tex_key, h_tex_key)
    J19_desc = f"{col_desc} {tex_desc}".strip()
    
    G17_desc = SFX_DESC.get(G17_key, G17_key) if G17_key else ""
    J17_desc = MAT_DESC.get(J17_key, J17_key) if J17_key else ""
    G22_desc = LIGHT_DESC.get(G22_key, G22_key) if G22_key else ""
    G24_desc = CAM_DESC.get(G24_key, G24_key) if G24_key else ""

    prompt = ""
    if G7 == "Yes":
        prompt += "[VISUAL GUIDE: Emulate the facial structure and proportions of the attached subject. Use the photo as a likeness reference only. Apply the following design]: "

    prompt += "A professional cinematic "
    if J22: prompt += J22 + " "
    prompt += "portrait of a "
    
    if J7: prompt += f"{J7} "
    if G9: prompt += f"{G9} "
    
    if J9_key: prompt += f"{J9_key} ({J9_desc}) "
        
    if G12_desc: prompt += f"from the {G12_desc} era. "
    else: prompt += ". "
        
    if J12_desc: prompt += f"Character style: {J12_desc}. "
        
    if G9 not in ["Feminine / Female", "Female", "Feminine"] and J14_desc:
        prompt += f"Grooming: {J14_desc}. "
        
    if J19_desc: prompt += f"Hair Texture: {J19_desc}. "
        
    prompt += "Skin: standard. " 
        
    if "Child" not in J7 and "Teen" not in J7 and G17_desc:
        prompt += f"[CINEMATIC PROSTHETIC STUDY: Apply {G17_desc} SFX as a makeup layer]. "
        
    if J17_desc: prompt += f"Finish: {J17_desc}. "
        
    prompt += "Technical: "
    if G22_desc: prompt += f"Lighting: {G22_desc}, "
    if G24_desc: prompt += f"Lens: {G24_desc}, "
    
    size = draft.get('size', '')
    if size and size != "None": prompt += f"Frame: {size}, "
    
    # 🔴 منطق جدید آرک با جداکننده نئونی و دستور هوش مصنوعی 🔴
    if is_arc_active:
        prompt += "Layout: Create a horizontal triptych composition (three equal panels side-by-side). Separate each panel with a glowing neon vertical line divider. All panels must maintain identical professional cinematic realism, raw photography, subsurface scattering, no-retouch, focus on prosthetic makeup accuracy, beautifully framed three-quarter profile angle. "
        
        if age_prog_key != "None":
            arc_desc = AGE_PROG_DESC.get(age_prog_key, age_prog_key)
            prompt += f"Subject Progression: [APEX AGE ARC: {arc_desc}]. "
            prompt += "Dynamic AI Instruction: Use your high-end cinematic creativity to organically age the character across the panels. Dynamically evolve and adjust the hair style, beard, mustache, skin texture, and any SFX trauma to realistically match the specific age progression in each panel. "
            
            if "Deep Nasolabial Folds" in age_prog_key:
                prompt += "Panel 1 (Left): age 30. Panel 2 (Middle): age 40. Panel 3 (Right): age 50. Ensure each panel is clearly labeled with text at the bottom margin: 'Age 30', 'Age 40', 'Age 50' respectively. "
            elif "Pronounced Crow's Feet" in age_prog_key:
                 prompt += "Panel 1 (Left): minor wrinkles. Panel 2 (Middle): pronounced crow's feet. Panel 3 (Right): advanced wrinkles. Clearly label: 'Minor', 'Pronounced', 'Advanced'. "
            else:
                prompt += "Panel 1 (Left): base age. Panel 2 (Middle): +10 years older. Panel 3 (Right): +20 years older. Ensure each panel is clearly labeled with text at the bottom margin with the respective age. "

        elif sfx_prog_key != "None":
            arc_desc = SFX_PROG_DESC.get(sfx_prog_key, sfx_prog_key)
            prompt += f"Makeup Progression: [APEX SFX ARC: {arc_desc}]. "
            if "Fresh Katana/Sword Slash" in sfx_prog_key:
                prompt += "Panel 1 (Left): fresh slash with bleeding. Panel 2 (Middle): partially scabbed (3 days old). Panel 3 (Right): fading scar (1 year old). Clearly label: 'Fresh', 'Scabbed', 'Faded'. "
            else:
                prompt += "Panel 1 (Left): fresh trauma. Panel 2 (Middle): healing stage. Panel 3 (Right): fully healed scar. Clearly label each stage at the bottom margin. "
            
    else:
        prompt += "Layout: single cinematic raw photography portrait. beautifully framed composition, three-quarter profile angle, subsurface scattering, no-retouch. "
        if J7: prompt += f" Typography overlay: clearly written text '{J7}' at the bottom margin of the image. "

    prompt += "8k, focus on prosthetic makeup accuracy."

    return " ".join(prompt.split())

ADMIN_USER = "sep"
ADMIN_PASS = "1386sy"

# ==========================================
# 4. موتور استایل (CSS Engine)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Montserrat:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0a192f 0%, #02060c 100%);
        height: 100vh; overflow-x: hidden;
    }

    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}

    div.element-container:has(.logo-marker) + div.element-container button {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        min-height: 0 !important;
        height: auto !important;
        display: flex !important;
        justify-content: flex-start !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button:hover,
    div.element-container:has(.logo-marker) + div.element-container button:active,
    div.element-container:has(.logo-marker) + div.element-container button:focus {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button p {
        color: #00f2ff !important;
        font-family: 'Cinzel', serif !important;
        font-size: 1.5rem !important;
        font-weight: 900 !important;
        margin: 0 !important;
        padding: 0 !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
    }
    div.element-container:has(.logo-marker) + div.element-container button:hover p {
        color: #ffffff !important;
        text-shadow: 0 0 15px #00f2ff !important;
        transform: scale(1.02) !important;
    }

    .title-main { font-family: 'Cinzel'; color: #ffffff !important; font-size: 2.5rem; font-weight: 800; letter-spacing: 10px; margin: 0; text-shadow: 0 0 15px rgba(0, 242, 255, 0.5); }
    .subtitle { color: #00f2ff; font-family: 'Montserrat'; font-size: 0.8rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 30px;}

    label, .stMarkdown p { color: #00e5ff !important; font-family: 'Montserrat' !important; font-weight: 700 !important; text-transform: uppercase !important; font-size: 0.75rem !important; }

    div[data-baseweb="input"] > div { background-color: rgba(0, 20, 40, 0.9) !important; border: 1px solid rgba(0, 242, 255, 0.4) !important; border-radius: 10px !important; }
    div[data-baseweb="input"] input, div[data-baseweb="select"] { color: #ffffff !important; font-weight: bold !important; }

    .stButton > button {
        border: none !important; border-radius: 8px !important; font-family: 'Cinzel', serif !important; font-weight: 900 !important;
        text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; background-color: #00f2ff !important; color: #000000 !important;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.3);
    }
    .stButton > button:hover { background-color: #ffffff !important; transform: scale(1.02); box-shadow: 0 0 20px #00f2ff;}

    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 25px; backdrop-filter: blur(10px); margin-bottom: 20px; }
    
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 30px; color: #4a5d73; font-family: 'Montserrat'; font-size: 0.7rem; font-weight: 900; }
    .step-active { color: #00f2ff; text-shadow: 0 0 8px #00f2ff; }

    div[data-testid="stExpander"] { background: rgba(10, 25, 47, 0.6) !important; border: 1px solid rgba(0, 242, 255, 0.2) !important; border-radius: 12px !important; backdrop-filter: blur(10px); margin-bottom: 15px; transition: all 0.3s ease; }
    div[data-testid="stExpander"]:hover { border-color: rgba(0, 242, 255, 0.6) !important; box-shadow: 0 5px 20px rgba(0, 242, 255, 0.15); }
    div[data-testid="stExpander"] summary { padding: 15px !important; }
    div[data-testid="stExpander"] summary p { color: #ffffff !important; font-family: 'Cinzel', serif !important; font-size: 1.1rem !important; letter-spacing: 2px; font-weight: bold !important; }
    
    .stCodeBlock { background-color: #02060c !important; border-left: 4px solid #ff00aa !important; border-radius: 8px !important; box-shadow: inset 0 0 10px rgba(0,0,0,0.8); }
    .stCodeBlock code { color: #00e5ff !important; font-family: 'Courier New', Courier, monospace !important; line-height: 1.6 !important; font-size: 0.95rem !important; }
    
    div[data-testid="stPopover"] { padding-top: 26px; } 
    div[data-testid="stPopover"] > button {
        background: transparent !important; border: 1px solid #00f2ff !important; border-radius: 50% !important; width: 34px !important; height: 34px !important;
        color: #00f2ff !important; font-size: 1.1rem !important; font-weight: 900 !important; transition: 0.3s !important; display: flex; align-items: center; justify-content: center;
    }
    div[data-testid="stPopover"] > button:hover { background: rgba(0, 242, 255, 0.1) !important; color: #fff !important; box-shadow: 0 0 15px #00f2ff !important; }
    div[data-testid="stPopoverBody"], div[data-baseweb="popover"], div[data-baseweb="popover"] > div, [data-testid="stPopoverBody"] > div { 
        background-color: #000000 !important; background: #000000 !important; border-color: #00f2ff !important;
    }

    [data-testid="stImage"] img {
        border-radius: 12px !important;
        border: 2px solid #00f2ff !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.7), 0 0 35px rgba(0, 85, 255, 0.6) !important;
        transition: all 0.3s ease-in-out !important;
    }
    [data-testid="stImage"] img:hover {
        box-shadow: 0 0 25px rgba(0, 242, 255, 1), 0 0 50px rgba(0, 85, 255, 0.9) !important;
        transform: scale(1.02) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# ROUTE 1: ENTRY FLOW (LOGIN ONLY)
# ==========================================
if st.session_state.route == 'login':
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.PNG"): st.image("logo.PNG", width=280)
    with c2:
        st.markdown("<h1 style='color:#ffffff; font-family:Cinzel; margin-top:80px; text-shadow: 0 0 15px #00f2ff;'>RESTRICTED ACCESS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#7b8ea8; font-family:Montserrat; font-size:0.8rem; margin-bottom:20px;'>Authorized Personnel Only. Please login to access UONA STUDIO.</p>", unsafe_allow_html=True)
        
        u_name = st.text_input("USERNAME", placeholder="Enter your credentials...")
        u_pass = st.text_input("PASSWORD", type="password", placeholder="Enter your password...")
        
        users = load_json(DB_FILE, {})
        
        if st.button("AUTHENTICATE", use_container_width=True):
            if u_name == ADMIN_USER and u_pass == ADMIN_PASS:
                st.session_state.auth = True
                st.session_state.user = u_name
                st.session_state.is_admin = True
                st.session_state.plan = "MASTER APEX"
                go_to('admin_panel')
            elif u_name in users:
                user_data = users[u_name]
                if isinstance(user_data, str):
                    db_pass = user_data
                    db_plan = "UONA Core"
                else:
                    db_pass = user_data.get("pass", "")
                    db_plan = user_data.get("plan", "UONA Core")
                
                if db_pass == u_pass:
                    st.session_state.auth = True
                    st.session_state.user = u_name
                    st.session_state.is_admin = False
                    st.session_state.plan = db_plan
                    go_to('dashboard')
                else:
                    st.error("ACCESS DENIED: Invalid Password.")
            else:
                st.error("ACCESS DENIED: Unregistered Account.")
    st.stop()

# ==========================================
# SHARED HEADER (WITH INVISIBLE BUTTON)
# ==========================================
if st.session_state.route != 'login':
    badge_color = "#ffaa00" if "Apex" in st.session_state.plan or "MASTER" in st.session_state.plan else "#00f2ff"
    
    c_head1, c_head2 = st.columns([1, 3])
    
    with c_head1:
        st.markdown('<span class="logo-marker"></span>', unsafe_allow_html=True)
        if st.button("UONA STUDIO", key="top_home_btn"):
            st.session_state.step = 1
            go_to('dashboard')
            
    with c_head2:
        st.markdown(f"""
            <div style="display: flex; justify-content: flex-end; align-items: center; height: 100%; padding-top: 10px;">
                <span style="color:{badge_color}; font-family:Cinzel; font-weight:bold; font-size:0.7rem; border:1px solid {badge_color}; padding:3px 8px; border-radius:4px; margin-right:15px; box-shadow: 0 0 8px rgba(0,0,0,0.5);">💎 {st.session_state.plan.upper()}</span>
                <span style="color:#ff00aa; font-weight:bold; font-family:Montserrat; font-size:0.7rem; margin-right:15px;">{'[MASTER ADMIN]' if st.session_state.is_admin else ''}</span>
                <span style="color:#fff; font-family:Montserrat; font-size:0.8rem;">USER: {st.session_state.user.upper()}</span>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<hr style='border-color: rgba(0,242,255,0.2); margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)

# ==========================================
# ROUTE: ADMIN PANEL
# ==========================================
if st.session_state.route == 'admin_panel':
    if not st.session_state.is_admin: go_to('dashboard')
    
    st.markdown("<h2 class='title-main' style='color:#ff00aa!important; text-shadow:0 0 15px #ff00aa;'>MASTER CONTROL PANEL</h2>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Manage Client Access & Subscriptions</div><br>", unsafe_allow_html=True)
    
    users = load_json(DB_FILE, {})
    
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>➕ Register New Client</h4>", unsafe_allow_html=True)
        new_u = st.text_input("New Client Username")
        new_p = st.text_input("New Client Password")
        new_plan = st.selectbox("Assign Subscription Tier", ["UONA Core", "UONA Apex"])
        
        if st.button("CREATE CLIENT ACCOUNT", use_container_width=True):
            if new_u and new_p:
                if new_u == ADMIN_USER:
                    st.error("Cannot use admin username.")
                else:
                    users[new_u] = {"pass": new_p, "plan": new_plan}
                    save_json(DB_FILE, users)
                    st.success(f"Client '{new_u}' successfully registered on {new_plan}.")
                    st.rerun()
            else:
                st.warning("Fill all fields.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00f2ff;'>👥 Active Client Subscriptions</h4>", unsafe_allow_html=True)
        if not users:
            st.info("No active clients yet.")
        else:
            for usr, data in users.items():
                if isinstance(data, str): 
                    plan_val, pwd_val = "UONA Core", data
                else: 
                    plan_val, pwd_val = data.get("plan", "UONA Core"), data.get("pass", "")
                    
                col_name, col_plan, col_pass, col_btn = st.columns([2, 2, 2, 1])
                col_name.markdown(f"<span style='color:white; font-family:Montserrat; font-weight:bold;'>👤 {usr}</span>", unsafe_allow_html=True)
                col_plan.markdown(f"<span style='color:#00f2ff; font-family:Cinzel; font-size:0.8rem;'>{plan_val}</span>", unsafe_allow_html=True)
                col_pass.markdown(f"<span style='color:#888; font-family:monospace;'>pwd: {pwd_val}</span>", unsafe_allow_html=True)
                if col_btn.button("REVOKE", key=f"del_{usr}"):
                    del users[usr]
                    save_json(DB_FILE, users)
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 2: DASHBOARD FLOW
# ==========================================
elif st.session_state.route == 'dashboard':
    
    found_bg = find_bg_file()
    if found_bg:
        add_bg_from_local(found_bg)
    else:
        st.error("⚠️ هشدار سیستم: فایل بک‌گراند پیدا نشد.")
    
    st.markdown("<h2 style='color:#fff; font-family:Cinzel; text-align:center;'>CONTROL CENTER</h2><div class='subtitle' style='text-align:center;'>Select a module to begin</div>", unsafe_allow_html=True)
    
    if st.session_state.is_admin:
        if st.button("⚙️ RETURN TO ADMIN PANEL"): go_to('admin_panel')
        st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>🎬</h1><h3 class="module-title">NEW CHARACTER</h3><p style="color:#888; font-size:0.8rem;">Start Multi-Step Builder</p></div>', unsafe_allow_html=True)
        if st.button("START PROJECT", key="b1", use_container_width=True): st.session_state.step = 1; go_to('builder')
    with c2:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>📂</h1><h3 class="module-title" style="color:#777!important; text-shadow:none!important;">LIBRARY</h3><p style="color:#888; font-size:0.8rem;">Saved Looks & Presets</p></div>', unsafe_allow_html=True)
        if st.button("OPEN LIBRARY", key="b2", use_container_width=True): go_to('library')
    with c3:
        st.markdown('<div class="glass-panel" style="text-align:center;"><h1>⚙️</h1><h3 class="module-title" style="color:#777!important; text-shadow:none!important;">SETTINGS</h3><p style="color:#888; font-size:0.8rem;">System Preferences</p></div>', unsafe_allow_html=True)
        if st.button("OPEN SETTINGS", key="b3", use_container_width=True): go_to('settings')

# ==========================================
# ROUTE: LIBRARY & SETTINGS
# ==========================================
elif st.session_state.route == 'library':
    st.markdown("<h2 class='title-main' style='text-align:center;'>PROJECT LIBRARY</h2>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle' style='text-align:center;'>Your Saved Cinematic Architectures</div><br>", unsafe_allow_html=True)
        
    projects = load_json(PROJ_FILE, [])
    my_projs = [p for p in projects if p.get("user") == st.session_state.user]
    
    if not my_projs:
        st.info("No projects saved yet.")
    else:
        for p in my_projs:
            with st.expander(f"📁 PROJECT LOG | {p['date']}"):
                st.markdown("<p style='color:#7b8ea8; font-size:0.75rem; letter-spacing:2px;'>GENERATED MASTER PROMPT:</p>", unsafe_allow_html=True)
                st.code(p['prompt'], language="markdown")

    st.markdown("<hr style='border-color: rgba(0,242,255,0.2);'>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='color:#00f2ff; font-family:Cinzel; margin-bottom:15px;'>REFERENCE GALLERY</h4>", unsafe_allow_html=True)
    l_c1, l_c2, l_c3, l_c4 = st.columns(4)
    with l_c1:
        if os.path.exists("desert_warn.jpg"): st.image("desert_warn.jpg", caption="Desert Warn")
    with l_c2:
        if os.path.exists("royal_clean.jpg"): st.image("royal_clean.jpg", caption="Royal Clean")
    with l_c3:
        if os.path.exists("dirty_combat.jpg"): st.image("dirty_combat.jpg", caption="Dirty Combat")
    with l_c4:
        if os.path.exists("urban_rebel.jpg"): st.image("urban_rebel.jpg", caption="Urban Rebel")

elif st.session_state.route == 'settings':
    st.markdown("<h2 class='title-main'>SYSTEM SETTINGS</h2>", unsafe_allow_html=True)
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.selectbox("Default AI Engine", ["Midjourney V6", "Gemini Pro Vision", "Stable Diffusion XL"])
    st.selectbox("Theme Mode", ["Dark Cinematic", "Light Mode (Not Recommended)"])
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 3: CHARACTER BUILDER (MULTI-STEP)
# ==========================================
elif st.session_state.route == 'builder':
    st.markdown(f"""
        <div class="step-indicator">
            <span class="{'step-active' if st.session_state.step==1 else ''}">1. IDENTITY</span> ➔
            <span class="{'step-active' if st.session_state.step==2 else ''}">2. PHYSICAL</span> ➔
            <span class="{'step-active' if st.session_state.step==3 else ''}">3. GROOM/SFX</span> ➔
            <span class="{'step-active' if st.session_state.step==4 else ''}">4. TECHNICAL</span> ➔
            <span class="{'step-active' if st.session_state.step==5 else ''}">5. REVIEW</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    d = st.session_state.draft

    if st.session_state.step == 1:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 1: Core Identity</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            opts_act = ["None", "Yes", "No"]
            idx_act = opts_act.index(d['actor']) if d['actor'] in opts_act else 0
            d['actor'] = st.selectbox("Actor Reference", opts_act, index=idx_act)
            
            smart_select("Age Range", AGE_LIST, 'age')
            
            if st.session_state.plan in ["UONA Apex", "MASTER APEX"]:
                st.markdown("<hr style='border-color: rgba(255, 170, 0, 0.3); margin: 10px 0;'>", unsafe_allow_html=True)
                smart_select("Age Progression Arc", list(AGE_PROG_DESC.keys()), 'age_prog', help_dict=AGE_PROG_DESC)

        with c2:
            smart_select("Gender", GENDER_LIST, 'gen')
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col3.button("NEXT ➔"): next_step()

    elif st.session_state.step == 2:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 2: Physical Attributes</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            smart_select("Nationality", list(NAT_DESC.keys()), 'nat', help_dict=NAT_DESC)
            smart_select("Hair Color", list(HAIR_COLORS.keys()), 'h_col', help_dict=HAIR_COLORS)
        with c2:
            smart_select("Era / Period", list(ERA_DESC.keys()), 'era', help_dict=ERA_DESC)
            smart_select("Hair Texture", list(HAIR_TEX_DESC.keys()), 'h_tex', help_dict=HAIR_TEX_DESC)
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("NEXT ➔"): next_step()

    elif st.session_state.step == 3:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 3: Grooming & SFX Trauma</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            smart_select("Grooming Style", list(GROOM_DESC.keys()), 'groom', help_dict=GROOM_DESC)
            smart_select("Material Finish", list(MAT_DESC.keys()), 'mat', help_dict=MAT_DESC)
        with c2:
            smart_select("Trauma / SFX", list(SFX_DESC.keys()), 'sfx', help_dict=SFX_DESC)
            
            if st.session_state.plan in ["UONA Apex", "MASTER APEX"]:
                st.markdown("<hr style='border-color: rgba(255, 170, 0, 0.3); margin: 10px 0;'>", unsafe_allow_html=True)
                smart_select("SFX Progression Arc", list(SFX_PROG_DESC.keys()), 'sfx_prog', help_dict=SFX_PROG_DESC)
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("NEXT ➔"): next_step()

    elif st.session_state.step == 4:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 4: Technical Specs</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            smart_select("Character Concept", list(CONCEPTS.keys()), 'char', help_dict=CONCEPTS)
            smart_select("Lighting Style", list(LIGHT_DESC.keys()), 'light', help_dict=LIGHT_DESC)
        with c2:
            smart_select("Camera & Lens", list(CAM_DESC.keys()), 'cam', help_dict=CAM_DESC)
            smart_select("Frame Size", SIZE_LIST, 'size')
        
        col1, col2, col3 = st.columns([1, 4, 1])
        if col1.button("⬅ BACK"): prev_step()
        if col3.button("REVIEW ➔"): next_step()

    elif st.session_state.step == 5:
        st.markdown("<h3 style='color:#00f2ff; font-family:Cinzel;'>STEP 5: Final Review</h3>", unsafe_allow_html=True)
        
        preview_p = generate_prompt(d)
        st.info(preview_p)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1.5, 3, 2])
        if col1.button("⬅ EDIT (BACK)"): prev_step()
        if col3.button("🚀 PROCEED TO SIMULATION"): go_to('simulation')

        st.markdown("<br>", unsafe_allow_html=True)
        _, rev_c1, rev_c2, _ = st.columns([1, 2, 2, 1])
        with rev_c1:
            if os.path.exists("portrait_clean.PNG"): st.image("portrait_clean.PNG", caption="Visual Reference 1", use_container_width=True)
        with rev_c2:
            if os.path.exists("portrait_clean_2.jpg"): st.image("portrait_clean_2.jpg", caption="Visual Reference 2", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 4 & 5: SIMULATION AND ENGINE
# ==========================================
elif st.session_state.route == 'simulation':
    st.markdown("<h2 class='title-main'>VISUAL SIMULATION</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown('<div style="background:#0a192f; height:200px; border-radius:15px; border:1px dashed #00f2ff; display:flex; align-items:center; justify-content:center; flex-direction:column; margin-bottom:20px;"><h1 style="color:#00f2ff; opacity:0.5;">👁️</h1><p style="color:#00f2ff; opacity:0.7; font-family:Montserrat;">LIVE PREVIEW FEED</p></div>', unsafe_allow_html=True)
        
        sim_c1, sim_c2 = st.columns(2)
        with sim_c1:
            if os.path.exists("desert.jpg"): st.image("desert.jpg", caption="Desert Environment Test")
            if os.path.exists("night_neon.jpg"): st.image("night_neon.jpg", caption="Night Neon Test")
        with sim_c2:
            if os.path.exists("studio_portrait.jpg"): st.image("studio_portrait.jpg", caption="Studio Lighting Test")
            if os.path.exists("humidity_tester.jpg"): st.image("humidity_tester.jpg", caption="SFX Humidity Test")
            
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.selectbox("Render Engine Test", ["Preview Mode (Fast)", "High Fidelity"])
        if st.button("⬅ BACK TO BUILDER", use_container_width=True): go_to('builder')
        if st.button("⚡ GENERATE PROMPT", use_container_width=True): go_to('prompt_engine')
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.route == 'prompt_engine':
    st.markdown("<h2 class='title-main'>PROMPT ENGINE</h2>", unsafe_allow_html=True)
    
    final_p = generate_prompt(st.session_state.draft)

    c1, c2 = st.columns([2.5, 1])
    with c1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.text_area("MASTER PROMPT (EDITABLE)", value=final_p, height=200)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        if st.button("💾 SAVE TO LIBRARY", use_container_width=True):
            projects = load_json(PROJ_FILE, [])
            projects.insert(0, {"user": st.session_state.user, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "prompt": final_p})
            save_json(PROJ_FILE, projects)
            st.success("Saved to Library!")
        if st.button("⬅ SIMULATION", use_container_width=True): go_to('simulation')
        st.markdown('</div>', unsafe_allow_html=True)
