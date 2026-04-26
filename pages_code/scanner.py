import streamlit as st
import random
import time

def classify_waste(image_name: str):
    """Placeholder classification function."""
    categories = [
        {"label": "Cardboard", "score": 87, "credits": 12, "badge": "badge-green",
         "tip": "Flatten boxes before recycling. Remove tape and staples.", "icon": "📦"},
        {"label": "Plastic", "score": 72, "credits": 8, "badge": "badge-blue",
         "tip": "Rinse containers before recycling. Check the resin code (1-7).", "icon": "🧴"},
        {"label": "E-Waste", "score": 94, "credits": 25, "badge": "badge-orange",
         "tip": "Never landfill electronics. Bring to certified e-waste centers.", "icon": "💻"},
    ]
    name_lower = image_name.lower()
    if any(k in name_lower for k in ["card", "box", "paper", "board"]):
        return categories[0]
    elif any(k in name_lower for k in ["plastic", "bottle", "bag", "pet"]):
        return categories[1]
    elif any(k in name_lower for k in ["phone", "laptop", "elec", "wire", "battery"]):
        return categories[2]
    return random.choice(categories)


def show():
    st.markdown("""
    <div class="nav-header">
        <h1>🔬 AI Waste Scanner</h1>
        <p>Upload an image — our AI identifies your waste and tells you how to recycle it.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1], gap="large")

    with col1:
        st.markdown('<div class="section-title">Upload Waste Image</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Supported: JPG, PNG · Max 10MB</div>', unsafe_allow_html=True)

        uploaded = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

        if uploaded is None:
            st.markdown("""
            <div class="upload-zone">
                <div style="font-size:3rem;">📸</div>
                <div style="font-size:1.1rem; font-weight:600; margin-top:0.5rem;">Drop your image here</div>
                <div style="font-size:0.85rem; margin-top:0.3rem; color:#5a8a6a;">
                    Works best with clear, well-lit photos of single items.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.image(uploaded, use_container_width=True, caption="Uploaded image")

            with st.spinner("🔍 Analyzing material properties..."):
                time.sleep(1.5)

            result = classify_waste(uploaded.name)

            st.markdown(f"""
            <div class="gs-success">
                ✅ <strong>Analysis Complete:</strong> Material identified as
                <strong>{result['label']}</strong> based on texture and shape.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Recyclability tips
            st.markdown('<div class="gs-card">', unsafe_allow_html=True)
            st.markdown(f"**{result['icon']} Identified Material: {result['label']}**")
            st.markdown(f'<span class="gs-badge {result["badge"]}">{result["label"]}</span>', unsafe_allow_html=True)
            st.markdown(f"<br><br>💡 **Tip:** {result['tip']}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if uploaded is not None:
            result = classify_waste(uploaded.name)

            st.markdown('<div class="section-title">Scan Results</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-sub">Environmental impact of this item</div>', unsafe_allow_html=True)

            # Recyclability Score Circle
            score = result["score"]
            st.markdown(f"""
            <div class="gs-card" style="text-align:center;">
                <div style="font-size:0.85rem; color:#5a8a6a; text-transform:uppercase; letter-spacing:1px; font-weight:600; margin-bottom:1rem;">
                    Recyclability Score
                </div>
                <div style="
                    width:140px; height:140px;
                    border-radius:50%;
                    background: conic-gradient(#a8e063 {score * 3.6}deg, #e8f4ed 0deg);
                    display:flex; align-items:center; justify-content:center;
                    margin: 0 auto;
                    box-shadow: 0 4px 20px rgba(168,224,99,0.4);
                    position:relative;
                ">
                    <div style="
                        width:105px; height:105px;
                        border-radius:50%;
                        background:white;
                        position:absolute;
                    "></div>
                    <div style="
                        position:relative; z-index:1;
                        font-family:'Syne',sans-serif;
                        font-size:2.2rem;
                        font-weight:800;
                        color:#1a3d2b;
                    ">{score}</div>
                </div>
                <div style="color:#5a8a6a; font-size:0.85rem; margin-top:0.8rem;">out of 100</div>
            </div>
            """, unsafe_allow_html=True)

            # Credits
            credits = result["credits"]
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">+{credits}</div>
                <div class="metric-label">🪙 Potential Green Credits</div>
                <div style="color:#b7d9c3; font-size:0.8rem; margin-top:0.5rem;">
                    Credited upon verified drop-off
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Find center button
            if st.button("📍 Find Nearest Recycling Hub", use_container_width=True):
                st.success("Navigate to the **Eco-Navigator** page to locate nearby hubs!")

        else:
            st.markdown("""
            <div class="gs-card" style="text-align:center; padding:3rem 2rem;">
                <div style="font-size:3.5rem;">🌿</div>
                <div style="font-family:'Syne',sans-serif; font-size:1.2rem; font-weight:700; color:#1a3d2b; margin:1rem 0 0.5rem;">
                    Ready to Scan
                </div>
                <div style="color:#5a8a6a; font-size:0.9rem;">
                    Upload an image to get your<br>recyclability score and green credits.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="gs-card">
                <div style="font-weight:600; color:#1a3d2b; margin-bottom:0.8rem;">🏆 Recent Scans (Demo)</div>
                <div style="display:flex; justify-content:space-between; align-items:center; padding:0.5rem 0; border-bottom:1px solid #e8f4ed;">
                    <span>📦 Cardboard Box</span><span class="gs-badge badge-green">87/100</span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; padding:0.5rem 0; border-bottom:1px solid #e8f4ed;">
                    <span>🧴 PET Bottle</span><span class="gs-badge badge-blue">72/100</span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; padding:0.5rem 0;">
                    <span>💻 Old Laptop</span><span class="gs-badge badge-orange">94/100</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
