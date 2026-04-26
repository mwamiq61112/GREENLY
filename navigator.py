import streamlit as st
import pandas as pd

ALL_HUBS = [
    # E-Waste centers
    {"name": "TechRecycle Hub – Pusa Road",      "lat": 28.6448, "lon": 77.1753, "type": "E-Waste",  "address": "12, Pusa Road, Rajender Nagar",  "hours": "Mon–Sat 9AM–6PM",  "rating": 4.8},
    {"name": "GreenCircuit Center – Karol Bagh", "lat": 28.6519, "lon": 77.1908, "type": "E-Waste",  "address": "45, Arya Samaj Road, Karol Bagh",  "hours": "Mon–Sat 10AM–7PM", "rating": 4.5},
    # Plastic centers
    {"name": "PlasticFree Station – Connaught",  "lat": 28.6315, "lon": 77.2167, "type": "Plastic",  "address": "Block D, Connaught Place",          "hours": "Mon–Sun 8AM–8PM",  "rating": 4.7},
    {"name": "PolyRecycle Hub – Rajendra Nagar", "lat": 28.6410, "lon": 77.1695, "type": "Plastic",  "address": "22, Rajendra Nagar Market",         "hours": "Tue–Sun 9AM–5PM",  "rating": 4.3},
    # Metal centers
    {"name": "MetalLoop Center – Paharganj",     "lat": 28.6444, "lon": 77.2090, "type": "Metal",    "address": "8A, Main Bazaar, Paharganj",        "hours": "Mon–Sat 8AM–6PM",  "rating": 4.6},
    {"name": "ScrapSmart Hub – Sadar Bazar",     "lat": 28.6561, "lon": 77.2080, "type": "Metal",    "address": "56, Sadar Bazar, Central Delhi",    "hours": "Mon–Fri 9AM–5PM",  "rating": 4.4},
    {"name": "IronGreen Station – Patel Nagar",  "lat": 28.6359, "lon": 77.1729, "type": "Metal",    "address": "31, Patel Nagar West Market",       "hours": "Mon–Sat 10AM–6PM", "rating": 4.2},
]

TYPE_COLORS = {"E-Waste": "🟠", "Plastic": "🔵", "Metal": "⚫"}
TYPE_ICONS  = {"E-Waste": "💻", "Plastic": "♻️", "Metal": "🔩"}


def show():
    st.markdown("""
    <div class="nav-header">
        <h1>🗺️ Eco-Navigator</h1>
        <p>Find authorized recycling hubs near you across Central Delhi.</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar filters
    with st.sidebar:
        st.markdown("---")
        st.markdown('<div style="color:#a8e063; font-weight:700; font-size:0.9rem; text-transform:uppercase; letter-spacing:1px;">🔽 Filter Hubs</div>', unsafe_allow_html=True)
        selected_types = st.multiselect(
            "Waste Category",
            options=["E-Waste", "Plastic", "Metal"],
            default=["E-Waste", "Plastic", "Metal"],
        )
        st.markdown("---")
        st.markdown('<div style="color:#b7d9c3; font-size:0.8rem;">🕐 All hubs verified<br>as of April 2025</div>', unsafe_allow_html=True)

    # Filter hubs
    filtered = [h for h in ALL_HUBS if h["type"] in selected_types] if selected_types else ALL_HUBS

    col1, col2 = st.columns([1.5, 1], gap="large")

    with col1:
        st.markdown('<div class="section-title">Recycling Hubs Map</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="section-sub">Showing {len(filtered)} hubs · Central Delhi region</div>', unsafe_allow_html=True)

        if filtered:
            df = pd.DataFrame([{"lat": h["lat"], "lon": h["lon"]} for h in filtered])
            st.map(df, zoom=13, use_container_width=True)
        else:
            st.info("Select at least one waste category to see hubs on the map.")

        st.markdown("""
        <div style="display:flex; gap:1.5rem; margin-top:0.8rem; flex-wrap:wrap;">
            <span style="color:#5a8a6a; font-size:0.82rem;">🟠 E-Waste Centers</span>
            <span style="color:#5a8a6a; font-size:0.82rem;">🔵 Plastic Centers</span>
            <span style="color:#5a8a6a; font-size:0.82rem;">⚫ Metal Centers</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-title">Hub Directory</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Click a hub for details</div>', unsafe_allow_html=True)

        if not filtered:
            st.info("No hubs match your filter.")
        else:
            for hub in filtered:
                badge_class = {"E-Waste": "badge-orange", "Plastic": "badge-blue", "Metal": "badge-green"}[hub["type"]]
                with st.expander(f"{TYPE_ICONS[hub['type']]}  {hub['name']}"):
                    st.markdown(f"""
                    <div style="padding:0.5rem 0;">
                        <span class="gs-badge {badge_class}">{hub['type']}</span>
                        <br><br>
                        <div style="display:grid; gap:0.5rem;">
                            <div>📍 <strong>Address:</strong> {hub['address']}</div>
                            <div>🕐 <strong>Hours:</strong> {hub['hours']}</div>
                            <div>⭐ <strong>Rating:</strong> {hub['rating']} / 5.0</div>
                            <div>🪙 <strong>Credits:</strong> Earn 5–25 GC per visit</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.button("Get Directions →", key=f"dir_{hub['name']}", use_container_width=True)

        # Summary stats
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(filtered)}</div>
            <div class="metric-label">Hubs Visible</div>
        </div>
        """, unsafe_allow_html=True)
