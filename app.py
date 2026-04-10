with c_form:
        f1, f2 = st.columns(2)
        with f1:
            st.markdown('<p class="label-text">Actor Reference <span class="star">*</span></p>', unsafe_allow_html=True)
            actor = st.selectbox("Select Reference Status", ["None", "No", "Yes"], key="act", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">Gender & Age <span class="star">*</span></p>', unsafe_allow_html=True)
            gen = st.selectbox("Select Gender", list(gender_d.keys()), key="gen", label_visibility="collapsed")
            age = st.selectbox("Select Age Range", list(age_d.keys()), key="age", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">SFX Category <span class="star">*</span></p>', unsafe_allow_html=True)
            s_cat = st.selectbox("Select SFX Category", ["None"] + list(sfx_cats.keys()), key="scat", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">Specific Trauma / Wound</p>', unsafe_allow_html=True)
            s_type = st.selectbox("Select Specific Wound", sfx_cats[s_cat] if s_cat != "None" else ["None"], key="stype", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">Lighting Environment</p>', unsafe_allow_html=True)
            light = st.selectbox("Select Lighting", list(light_d.keys()), key="light", label_visibility="collapsed")
            
        with f2:
            st.markdown('<p class="label-text">Nationality & Era <span class="star">*</span></p>', unsafe_allow_html=True)
            nat = st.selectbox("Select Nationality", list(nat_d.keys()), key="nat", label_visibility="collapsed")
            era = st.selectbox("Select Historical Era", list(era_d.keys()), key="era", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">Character Concept & Grooming</p>', unsafe_allow_html=True)
            char = st.selectbox("Select Character Type", list(char_d.keys()), key="char", label_visibility="collapsed")
            groom = st.selectbox("Select Grooming/Beard Style", list(groom_d.keys()), key="groom", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">Camera & Lens Perspective <span class="star">*</span></p>', unsafe_allow_html=True)
            cam = st.selectbox("Select Camera Angle", list(cam_d.keys()), key="cam", label_visibility="collapsed")
            
            st.markdown('<p class="label-text">Frame Size / Aspect Ratio</p>', unsafe_allow_html=True)
            size_sel = st.selectbox("Select Aspect Ratio", size_l, key="psize", label_visibility="collapsed")
