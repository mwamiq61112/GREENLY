import streamlit as st
import math

PAPER_FACTORS = {
    "trees_per_kg":   0.017,   # trees saved per kg paper
    "water_per_kg":   20.0,    # liters water saved per kg
    "co2_per_kg":     0.9,     # kg CO2 saved per kg paper
    "energy_per_kg":  17.0,    # kWh energy saved per kg
}

PLASTIC_FACTORS = {
    "oil_per_kg":     0.72,    # liters of oil saved per kg plastic
    "co2_per_kg":     1.5,     # kg CO2 saved per kg plastic
    "water_per_kg":   22.0,    # liters water saved per kg
    "energy_per_kg":  5.8,     # kWh energy saved per kg
}

GLASS_FACTORS = {
    "sand_per_kg":    1.2,     # kg raw sand saved per kg glass
    "co2_per_kg":     0.3,     # kg CO2 saved per kg glass
    "energy_per_kg":  0.67,    # kWh per kg
    "water_per_kg":   1.5,
}

METAL_FACTORS = {
    "co2_per_kg":     9.0,     # kg CO2 saved per kg aluminium
    "energy_per_kg":  14.0,
    "water_per_kg":   40.0,
    "ore_per_kg":     4.0,     # kg bauxite ore saved per kg aluminium
}


def human_readable_trees(n):
    if n < 1:
        return f"{n:.2f} trees (a healthy sapling)"
    elif n < 5:
        return f"{n:.1f} small trees"
    elif n < 20:
        return f"{n:.1f} medium trees"
    else:
        return f"{n:.0f} trees (a small grove!)"


def show():
    st.markdown("""
    <div class="nav-header">
        <h1>📊 Impact Calculator</h1>
        <p>Discover the real-world difference your recycling makes.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.1], gap="large")

    with col1:
        st.markdown('<div class="section-title">Configure Your Recycling</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Enter details about materials you plan to recycle</div>', unsafe_allow_html=True)

        st.markdown('<div class="gs-card">', unsafe_allow_html=True)

        material = st.selectbox(
            "🗂️ Material Type",
            ["Paper / Cardboard", "Plastic", "Glass", "Aluminium / Metal"],
        )

        weight = st.number_input(
            "⚖️ Weight (kg)",
            min_value=0.1,
            max_value=500.0,
            value=5.0,
            step=0.5,
            format="%.1f",
        )

        freq = st.selectbox(
            "📅 Recycling Frequency",
            ["One-time", "Weekly", "Monthly", "Yearly"],
        )

        multiplier = {"One-time": 1, "Weekly": 52, "Monthly": 12, "Yearly": 1}[freq]
        annual_weight = weight * multiplier

        st.markdown(f"""
        <div class="gs-info" style="margin-top:1rem;">
            📦 Annual equivalent: <strong>{annual_weight:.1f} kg</strong> of {material.split('/')[0].strip().lower()}
        </div>
        """, unsafe_allow_html=True)

        calculate = st.button("⚡ Calculate My Impact", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # How it works
        with st.expander("ℹ️ How are these values calculated?"):
            st.markdown("""
            Our calculations are based on life-cycle analysis data from:
            - **Paper:** EPA Waste Reduction Model (WARM)
            - **Plastic:** PlasticsEurope Environmental Profiles
            - **Glass:** British Glass sustainability data
            - **Metal:** International Aluminium Institute

            Values represent average savings compared to virgin material production.
            Actual results vary by local processing methods.
            """)

    with col2:
        st.markdown('<div class="section-title">Environmental Impact</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">What your recycling achieves</div>', unsafe_allow_html=True)

        if calculate or True:  # always show default
            w = weight

            if "Paper" in material:
                f = PAPER_FACTORS
                trees = w * f["trees_per_kg"]
                water = w * f["water_per_kg"]
                co2   = w * f["co2_per_kg"]
                energy= w * f["energy_per_kg"]

                headline = f"By recycling **{w:.1f} kg** of paper, you save **{human_readable_trees(trees)}** and **{water:.0f} litres of water**."
                extras = [
                    f"🌍 **{co2:.2f} kg CO₂** kept out of the atmosphere",
                    f"⚡ **{energy:.1f} kWh** of energy conserved",
                    f"🌊 **{water:.0f} litres** of water saved",
                    f"🌳 Equivalent to protecting **{human_readable_trees(trees)}**",
                ]
                credits = int(w * 5)
                fun_fact = "It takes about 24 trees to make 1 tonne of newsprint. Your recycling helps preserve forests!"

            elif "Plastic" in material:
                f = PLASTIC_FACTORS
                oil   = w * f["oil_per_kg"]
                water = w * f["water_per_kg"]
                co2   = w * f["co2_per_kg"]
                energy= w * f["energy_per_kg"]

                headline = f"By recycling **{w:.1f} kg** of plastic, you save **{oil:.2f} litres of crude oil** and keep **{co2:.2f} kg of CO₂** out of the air."
                extras = [
                    f"🛢️ **{oil:.2f} litres** of crude oil conserved",
                    f"🌍 **{co2:.2f} kg CO₂** emissions avoided",
                    f"⚡ **{energy:.1f} kWh** of energy saved",
                    f"🌊 **{water:.0f} litres** of water conserved",
                ]
                credits = int(w * 4)
                fun_fact = "Plastic takes up to 500 years to decompose. Recycling it can save the same oil that fuelled its creation!"

            elif "Glass" in material:
                f = GLASS_FACTORS
                sand  = w * f["sand_per_kg"]
                co2   = w * f["co2_per_kg"]
                energy= w * f["energy_per_kg"]
                water = w * f["water_per_kg"]

                headline = f"By recycling **{w:.1f} kg** of glass, you conserve **{sand:.2f} kg of raw sand** and save **{co2:.2f} kg CO₂**."
                extras = [
                    f"🏖️ **{sand:.2f} kg** of raw silica sand preserved",
                    f"🌍 **{co2:.2f} kg CO₂** avoided",
                    f"⚡ **{energy:.2f} kWh** energy saved",
                    f"🌊 **{water:.2f} litres** of water conserved",
                ]
                credits = int(w * 3)
                fun_fact = "Glass is 100% recyclable and can be recycled endlessly without loss of quality or purity!"

            else:  # Metal / Aluminium
                f = METAL_FACTORS
                ore   = w * f["ore_per_kg"]
                co2   = w * f["co2_per_kg"]
                energy= w * f["energy_per_kg"]
                water = w * f["water_per_kg"]

                headline = f"By recycling **{w:.1f} kg** of aluminium, you save **{ore:.2f} kg of bauxite ore** and **{co2:.2f} kg of CO₂**."
                extras = [
                    f"⛏️ **{ore:.2f} kg** of bauxite ore spared",
                    f"🌍 **{co2:.2f} kg CO₂** prevented",
                    f"⚡ **{energy:.1f} kWh** energy conserved (95% savings!)",
                    f"🌊 **{water:.0f} litres** of water saved",
                ]
                credits = int(w * 8)
                fun_fact = "Recycling aluminium uses 95% less energy than producing it from raw ore. One can recycled = enough energy to power a TV for 3 hours!"

            # Headline result
            st.markdown(f"""
            <div class="impact-result">
                <h3>🎯 Your Impact Summary</h3>
                <p>{headline.replace("**", "<strong>").replace("**", "</strong>")}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Detail grid
            for e in extras:
                icon, rest = e.split(" ", 1)
                st.markdown(f"""
                <div style="
                    display:flex; align-items:center; gap:0.8rem;
                    background:rgba(255,255,255,0.7);
                    border:1px solid rgba(109,191,138,0.25);
                    border-radius:0.7rem; padding:0.8rem 1rem; margin-bottom:0.5rem;
                ">
                    <span style="font-size:1.4rem;">{icon}</span>
                    <span style="color:#1a3d2b;">{rest}</span>
                </div>
                """, unsafe_allow_html=True)

            # Credits + Fun fact
            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">+{credits}</div>
                    <div class="metric-label">Green Credits to Earn</div>
                </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                <div class="gs-card" style="height:100%; box-sizing:border-box;">
                    <div style="font-size:0.8rem; text-transform:uppercase; color:#5a8a6a; font-weight:600; letter-spacing:0.5px; margin-bottom:0.5rem;">💡 Did You Know?</div>
                    <div style="color:#1a3d2b; font-size:0.87rem; line-height:1.5;">{fun_fact}</div>
                </div>
                """, unsafe_allow_html=True)

            if freq != "One-time":
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"""
                <div class="gs-info">
                    📅 <strong>Annual projection ({freq}):</strong> Recycling {annual_weight:.1f} kg per year multiplies your impact {multiplier}×.
                    That's equivalent to <strong>{(annual_weight * (PAPER_FACTORS["co2_per_kg"] if 'Paper' in material else PLASTIC_FACTORS["co2_per_kg"] if 'Plastic' in material else GLASS_FACTORS["co2_per_kg"] if 'Glass' in material else METAL_FACTORS["co2_per_kg"])):.1f} kg CO₂</strong> saved annually.
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="gs-card" style="text-align:center; padding:3rem;">
                <div style="font-size:3rem;">📊</div>
                <div style="font-family:'Syne',sans-serif; font-size:1.1rem; color:#1a3d2b; font-weight:700; margin-top:1rem;">
                    Set your inputs and click Calculate
                </div>
                <div style="color:#5a8a6a; font-size:0.88rem; margin-top:0.4rem;">
                    See the real impact of your recycling actions.
                </div>
            </div>
            """, unsafe_allow_html=True)
