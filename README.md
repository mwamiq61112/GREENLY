# 🌿 GreenSource — Sustainability App

A multipage Streamlit web application for a sustainability competition.

## Features

| Page | Feature |
|---|---|
| 🔬 AI Waste Scanner | Upload images → AI classification → Recyclability Score & Green Credits |
| 🗺️ Eco-Navigator | Interactive map of recycling hubs near Pusa Road & Central Delhi |
| 💚 Green Wallet | User dashboard with metrics, activity log, and discount code redemption |
| 📊 Impact Calculator | Calculate CO₂, water, energy savings from recycling |

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py
```

The app opens at **http://localhost:8501**

## Structure

```
greensource_app/
├── app.py                  # Main entry, navigation, global CSS
├── requirements.txt
└── pages_code/
    ├── __init__.py
    ├── scanner.py          # AI Waste Scanner
    ├── navigator.py        # Eco-Navigator (Map)
    ├── wallet.py           # Green Wallet dashboard
    └── calculator.py       # Impact Calculator
```

## Design

- **Theme:** Sustainable Green — forest greens, sage, lime accents
- **Fonts:** Syne (display) + DM Sans (body) via Google Fonts
- **Layout:** Wide layout, sidebar navigation, card-based content
