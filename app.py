import streamlit as st

st.set_page_config(
    page_title="GreenSource",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for green sustainable theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

:root {
    --forest: #1a3d2b;
    --sage: #3d7a5a;
    --mint: #6dbf8a;
    --lime: #a8e063;
    --cream: #f4f1e8;
    --bark: #8b6f47;
    --mist: #e8f4ed;
    --charcoal: #2c2c2c;
}

* { font-family: 'DM Sans', sans-serif; }

/* Override Streamlit defaults */
.stApp {
    background: linear-gradient(135deg, #f4f1e8 0%, #e8f4ed 50%, #d4edda 100%);
    background-attachment: fixed;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a3d2b 0%, #2d6a4f 100%) !important;
}
[data-testid="stSidebar"] * { color: #e8f4ed !important; }
[data-testid="stSidebar"] .stRadio > label { color: #a8e063 !important; font-weight: 600; }
[data-testid="stSidebar"] hr { border-color: #3d7a5a !important; }

/* Navigation header */
.nav-header {
    background: linear-gradient(135deg, #1a3d2b, #2d6a4f);
    padding: 2rem 2.5rem 1.5rem;
    border-radius: 0 0 2rem 2rem;
    margin: -1rem -1rem 2rem -1rem;
    box-shadow: 0 8px 32px rgba(26,61,43,0.3);
}
.nav-header h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #a8e063;
    margin: 0;
    letter-spacing: -1px;
}
.nav-header p { color: #b7d9c3; margin: 0.3rem 0 0; font-size: 1.05rem; }

/* Cards */
.gs-card {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(12px);
    border: 1.5px solid rgba(109,191,138,0.3);
    border-radius: 1.2rem;
    padding: 1.8rem;
    margin: 1rem 0;
    box-shadow: 0 4px 24px rgba(26,61,43,0.08);
    transition: transform 0.2s, box-shadow 0.2s;
}
.gs-card:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(26,61,43,0.15); }

/* Metric cards */
.metric-card {
    background: linear-gradient(135deg, #1a3d2b, #2d6a4f);
    border-radius: 1.2rem;
    padding: 1.5rem;
    text-align: center;
    color: white;
    box-shadow: 0 4px 20px rgba(26,61,43,0.25);
}
.metric-card .metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    color: #a8e063;
    line-height: 1;
}
.metric-card .metric-label { font-size: 0.85rem; color: #b7d9c3; margin-top: 0.4rem; letter-spacing: 0.5px; text-transform: uppercase; }

/* Score ring */
.score-ring-wrapper {
    display: flex; justify-content: center; align-items: center;
    flex-direction: column; gap: 0.5rem;
}
.score-circle {
    width: 130px; height: 130px;
    border-radius: 50%;
    background: conic-gradient(#a8e063 calc(var(--pct) * 3.6deg), #e0e0e0 0deg);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #1a3d2b;
    box-shadow: 0 4px 20px rgba(168,224,99,0.4);
    position: relative;
}
.score-circle::before {
    content: '';
    position: absolute;
    width: 100px; height: 100px;
    border-radius: 50%;
    background: white;
}
.score-circle span { position: relative; z-index: 1; }

/* Badges */
.gs-badge {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.3px;
}
.badge-green { background: #d4edda; color: #1a5c33; border: 1px solid #a8e063; }
.badge-blue  { background: #d0e8f7; color: #1a4a6e; border: 1px solid #7ec8f0; }
.badge-orange{ background: #fde8d0; color: #7a3a00; border: 1px solid #f0b07e; }

/* Section titles */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #1a3d2b;
    margin-bottom: 0.2rem;
}
.section-sub { color: #5a8a6a; font-size: 0.9rem; margin-bottom: 1rem; }

/* Upload zone */
.upload-zone {
    border: 2px dashed #6dbf8a;
    border-radius: 1.2rem;
    padding: 3rem;
    text-align: center;
    background: rgba(168,224,99,0.07);
    color: #3d7a5a;
}

/* Green button */
.stButton > button {
    background: linear-gradient(135deg, #2d6a4f, #3d7a5a) !important;
    color: white !important;
    border: none !important;
    border-radius: 0.8rem !important;
    padding: 0.6rem 1.8rem !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    transition: all 0.2s !important;
    box-shadow: 0 3px 12px rgba(45,106,79,0.35) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #1a3d2b, #2d6a4f) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(45,106,79,0.45) !important;
}

/* Redeem button special */
.redeem-btn > button {
    background: linear-gradient(135deg, #a8e063, #6dbf8a) !important;
    color: #1a3d2b !important;
}

/* Impact box */
.impact-result {
    background: linear-gradient(135deg, #d4edda, #b7d9c3);
    border-left: 4px solid #2d6a4f;
    border-radius: 0.8rem;
    padding: 1.5rem;
    margin-top: 1rem;
}
.impact-result h3 { color: #1a3d2b; font-family: 'Syne', sans-serif; font-weight: 700; margin:0 0 0.5rem; }
.impact-result p  { color: #2d6a4f; margin: 0.3rem 0; font-size: 0.95rem; }

/* Success/info boxes */
.gs-success {
    background: linear-gradient(90deg, #d4edda, #e8f4ed);
    border: 1px solid #6dbf8a;
    border-radius: 0.8rem;
    padding: 1rem 1.5rem;
    color: #1a5c33;
    font-weight: 500;
}
.gs-info {
    background: linear-gradient(90deg, #e8f4ed, #d4edda);
    border: 1px solid #a8e063;
    border-radius: 0.8rem;
    padding: 1rem 1.5rem;
    color: #2d6a4f;
}

/* Discount code card */
.discount-card {
    background: linear-gradient(135deg, #1a3d2b, #2d6a4f);
    border-radius: 0.8rem;
    padding: 1rem 1.5rem;
    margin: 0.5rem 0;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.discount-code { font-family: 'Syne', monospace; color: #a8e063; font-weight: 700; font-size: 1.1rem; }

/* Sidebar logo */
.sidebar-logo {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #a8e063;
    padding: 1rem 0 0.5rem;
}
.sidebar-tagline { color: #b7d9c3; font-size: 0.8rem; margin-bottom: 1.5rem; }

/* Map caption */
.map-caption { color: #5a8a6a; font-size: 0.85rem; margin-top: 0.5rem; }

/* Divider */
.gs-divider { border: none; border-top: 1.5px solid rgba(109,191,138,0.25); margin: 1.5rem 0; }

/* Selectbox */
.stSelectbox label { color: #1a3d2b !important; font-weight: 600 !important; }

/* Slider */
.stSlider label { color: #1a3d2b !important; font-weight: 600 !important; }

/* Number input */
.stNumberInput label { color: #1a3d2b !important; font-weight: 600 !important; }

/* Radio */
.stRadio > label { color: #1a3d2b !important; font-weight: 600 !important; }

/* Expander */
.streamlit-expanderHeader { color: #1a3d2b !important; font-weight: 600 !important; }

/* Hide Streamlit branding */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🌿 GreenSource</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">Sustainable Living. Rewarded.</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    page = st.radio(
        "Navigate",
        ["🏠  AI Waste Scanner", "🗺️  Eco-Navigator", "💚  Green Wallet", "📊  Impact Calculator"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown('<div style="color:#b7d9c3; font-size:0.8rem;">🏆 Your Eco Rank</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-family:Syne,sans-serif; font-size:1.4rem; color:#a8e063; font-weight:800;">Eco Warrior 🌱</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#b7d9c3; font-size:0.8rem; margin-top:0.3rem;">Top 8% of users this month</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div style="color:#b7d9c3; font-size:0.75rem; line-height:1.5;">Every item recycled<br>is a vote for the future 🌍</div>', unsafe_allow_html=True)

# Route pages
if "🏠" in page:
    from pages_code import scanner
    scanner.show()
elif "🗺️" in page:
    from pages_code import navigator
    navigator.show()
elif "💚" in page:
    from pages_code import wallet
    wallet.show()
elif "📊" in page:
    from pages_code import calculator
    calculator.show()
