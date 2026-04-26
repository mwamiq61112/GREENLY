import streamlit as st

DISCOUNT_CODES = [
    {"brand": "EcoWear 🧥",      "code": "GREEN20",   "desc": "20% off sustainable clothing",  "expiry": "31 May 2025"},
    {"brand": "SolarBox 🌞",     "code": "SOLAR15",   "desc": "₹150 off solar accessories",    "expiry": "30 Jun 2025"},
    {"brand": "BambooHome 🏠",   "code": "BAMB10",    "desc": "10% off bamboo furniture",      "expiry": "15 Jul 2025"},
    {"brand": "PureEats 🥗",     "code": "ORGANIC25", "desc": "25% off organic food basket",   "expiry": "31 May 2025"},
    {"brand": "CycloGear 🚲",    "code": "CYCLE30",   "desc": "₹300 off cycling accessories",  "expiry": "30 Jun 2025"},
]

ACTIVITIES = [
    {"icon": "📦", "action": "Cardboard recycled",   "date": "Today, 10:42 AM", "credits": "+12"},
    {"icon": "💻", "action": "E-Waste drop-off",     "date": "Yesterday",        "credits": "+25"},
    {"icon": "🧴", "action": "Plastic collected",    "date": "Apr 22",           "credits": "+8"},
    {"icon": "🏭", "action": "Hub visit bonus",      "date": "Apr 20",           "credits": "+5"},
    {"icon": "📦", "action": "Cardboard recycled",   "date": "Apr 18",           "credits": "+12"},
]


def show():
    st.markdown("""
    <div class="nav-header">
        <h1>💚 Green Wallet</h1>
        <p>Track your environmental impact and redeem rewards.</p>
    </div>
    """, unsafe_allow_html=True)

    # Profile header
    st.markdown("""
    <div class="gs-card" style="display:flex; align-items:center; gap:1.5rem; flex-wrap:wrap;">
        <div style="
            width:70px; height:70px; border-radius:50%;
            background: linear-gradient(135deg, #a8e063, #6dbf8a);
            display:flex; align-items:center; justify-content:center;
            font-size:2rem; flex-shrink:0;
        ">🌱</div>
        <div>
            <div style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800; color:#1a3d2b;">
                Eco-Warrior
            </div>
            <div style="color:#5a8a6a; font-size:0.9rem; margin-top:0.1rem;">
                Member since January 2025 · Delhi, India
            </div>
            <div style="margin-top:0.5rem; display:flex; gap:0.5rem; flex-wrap:wrap;">
                <span class="gs-badge badge-green">🏆 Top Recycler</span>
                <span class="gs-badge badge-blue">🌍 Carbon Hero</span>
                <span class="gs-badge badge-orange">⚡ E-Waste Champion</span>
            </div>
        </div>
        <div style="margin-left:auto; text-align:center;">
            <div style="font-family:'Syne',sans-serif; font-size:2rem; font-weight:800; color:#1a3d2b;">347</div>
            <div style="color:#5a8a6a; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.5px;">Green Credits</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Metrics
    st.markdown('<div class="section-title">📊 Impact Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Your cumulative environmental contribution</div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3, gap="medium")
    with m1:
        st.metric(
            label="♻️ Total Waste Recycled",
            value="48.5 kg",
            delta="3.2 kg this week",
        )
    with m2:
        st.metric(
            label="🌿 CO₂ Saved",
            value="62.3 kg",
            delta="4.1 kg this week",
        )
    with m3:
        st.metric(
            label="🪙 Green Credits Earned",
            value="347 GC",
            delta="45 GC this week",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 1], gap="large")

    with col1:
        st.markdown('<div class="section-title">📋 Activity Log</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Recent recycling actions</div>', unsafe_allow_html=True)

        st.markdown('<div class="gs-card">', unsafe_allow_html=True)
        for act in ACTIVITIES:
            st.markdown(f"""
            <div style="display:flex; align-items:center; gap:1rem; padding:0.7rem 0; border-bottom:1px solid #e8f4ed;">
                <div style="font-size:1.5rem;">{act['icon']}</div>
                <div style="flex:1;">
                    <div style="font-weight:600; color:#1a3d2b; font-size:0.92rem;">{act['action']}</div>
                    <div style="color:#5a8a6a; font-size:0.78rem;">{act['date']}</div>
                </div>
                <div style="font-family:'Syne',sans-serif; font-weight:700; color:#2d6a4f; font-size:1rem;">
                    {act['credits']} GC
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-title">🎁 Redeem Rewards</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Use your Green Credits for eco-friendly discounts</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #a8e063, #6dbf8a);
            border-radius:1rem; padding:1.2rem 1.5rem; margin-bottom:1rem;
            display:flex; align-items:center; justify-content:space-between;
        ">
            <div>
                <div style="font-family:'Syne',sans-serif; font-size:1.6rem; font-weight:800; color:#1a3d2b;">347 GC</div>
                <div style="color:#2d6a4f; font-size:0.85rem;">Available to redeem</div>
            </div>
            <div style="font-size:2.5rem;">🪙</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🎟️ Reveal Discount Codes", use_container_width=True):
            st.session_state["show_codes"] = True

        if st.session_state.get("show_codes"):
            st.markdown("<br>", unsafe_allow_html=True)
            for d in DISCOUNT_CODES:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #1a3d2b, #2d6a4f);
                    border-radius:0.8rem; padding:1rem 1.2rem; margin-bottom:0.5rem;
                    display:flex; justify-content:space-between; align-items:center;
                ">
                    <div>
                        <div style="color:#e8f4ed; font-weight:600; font-size:0.9rem;">{d['brand']}</div>
                        <div style="color:#b7d9c3; font-size:0.78rem;">{d['desc']}</div>
                        <div style="color:#6dbf8a; font-size:0.75rem;">Expires {d['expiry']}</div>
                    </div>
                    <div style="
                        font-family:'Syne',monospace; font-weight:800;
                        color:#a8e063; font-size:1rem;
                        background:rgba(168,224,99,0.1);
                        padding:0.3rem 0.7rem; border-radius:0.4rem;
                        border:1px solid rgba(168,224,99,0.3);
                    ">{d['code']}</div>
                </div>
                """, unsafe_allow_html=True)

            st.success("🎉 Codes revealed! Valid for 30 days. Share with friends for bonus credits.")
