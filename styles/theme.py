import streamlit as st


def apply_theme() -> None:
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ══ Reset & Root ══════════════════════════════════════════════════════════ */
:root {
    --bg-primary:   var(--background-color);
    --bg-secondary: var(--secondary-background-color);
    --bg-card:      color-mix(in srgb, var(--secondary-background-color) 85%, transparent);
    --bg-hover:     color-mix(in srgb, var(--secondary-background-color) 92%, var(--text-color) 8%);
    --border:       color-mix(in srgb, var(--text-color) 14%, transparent);
    --border-glow:  color-mix(in srgb, var(--primary-color, #2563eb) 50%, transparent);
    --text-1:       var(--text-color);
    --text-2:       color-mix(in srgb, var(--text-color) 72%, transparent);
    --text-3:       color-mix(in srgb, var(--text-color) 50%, transparent);
    --accent:       var(--primary-color, #2563eb);
    --green:        #10b981;
    --yellow:       #f59e0b;
    --red:          #ef4444;
    --blue:         #3b82f6;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

.stApp {
    background: var(--bg-primary) !important;
    color: var(--text-1) !important;
}

.main .block-container {
    padding: 1.5rem 2.5rem !important;
    max-width: 1380px;
}

/* ── Hide Streamlit chrome ── */
footer { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, 
        color-mix(in srgb, var(--primary-color, #3b82f6) 12%, var(--secondary-background-color)) 0%, 
        color-mix(in srgb, var(--primary-color, #3b82f6) 3%, var(--secondary-background-color)) 100%) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-1) !important; }
[data-testid="stSidebar"] .stRadio > label { color: var(--text-2) !important; }

/* Sidebar Radio Menu Transition & styling */
[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    gap: 0.4rem !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 0.45rem 0.75rem !important;
    border-radius: 8px !important;
    transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: color-mix(in srgb, var(--primary-color, #3b82f6) 8%, var(--bg-hover)) !important;
    transform: translateX(3px);
}

.sidebar-footer {
    margin-top: 2rem;
    padding: 1rem 0.4rem 0;
    border-top: 1px solid var(--border);
    text-align: center;
    font-size: .67rem;
    line-height: 1.55;
    color: var(--text-3);
}

/* ── Widget labels ── */
label, .stRadio > div > label { color: var(--text-2) !important; font-size: 0.85rem !important; }

/* ── Select boxes ── */
div[data-baseweb="select"] > div {
    background-color: var(--bg-card) !important;
    border-color: var(--border) !important;
    color: var(--text-1) !important;
    border-radius: 10px !important;
}
div[data-baseweb="select"] svg { fill: var(--text-2) !important; }

/* ── Slider ── */
[data-testid="stSlider"] .rc-slider-track { background: var(--accent) !important; }
[data-testid="stSlider"] .rc-slider-handle { border-color: var(--accent) !important; background: var(--accent) !important; }

/* ── Number input ── */
[data-testid="stNumberInput"] input {
    background: var(--bg-card) !important;
    border-color: var(--border) !important;
    color: var(--text-1) !important;
    border-radius: 10px !important;
}

/* ── Text input ── */
[data-testid="stTextInput"] input {
    background: var(--bg-card) !important;
    border-color: var(--border) !important;
    color: var(--text-1) !important;
    border-radius: 10px !important;
}

/* ── Radio buttons ── */
[data-testid="stRadio"] > div { gap: 0.5rem; }
[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    color: var(--text-2) !important;
    font-size: 0.85rem !important;
}

/* ── Predict button ── */
.stButton > button {
    background: linear-gradient(135deg, #2563eb 0%, #3b82f6 50%, #60a5fa 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.85rem 2rem !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.3px !important;
    transition: all 0.3s cubic-bezier(.4,0,.2,1) !important;
    box-shadow: 0 4px 20px rgba(37,99,235,0.4) !important;
    width: 100% !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 35px rgba(37,99,235,0.55) !important;
}
.stButton > button:active { transform: translateY(0px) !important; }

/* ── Expander ── */
[data-testid="stExpander"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
}
[data-testid="stExpander"] summary {
    color: var(--text-2) !important;
    font-size: 0.88rem !important;
}

/* ── Divider ── */
hr { border-color: var(--border) !important; }

/* ═══════════════════════════════════════════════════════════════════════════
   CUSTOM COMPONENT STYLES
═══════════════════════════════════════════════════════════════════════════ */

/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg,
        rgba(37,99,235,0.18) 0%,
        rgba(59,130,246,0.12) 40%,
        rgba(96,165,250,0.08) 70%,
        rgba(16,185,129,0.05) 100%);
    border: 1px solid rgba(37,99,235,0.25);
    border-radius: 22px;
    padding: 2.8rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 2rem;
}
.hero-wrap::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%,
        rgba(37,99,235,0.14) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-size: 2.9rem; font-weight: 900;
    background: linear-gradient(130deg, #93c5fd, #3b82f6, #10b981);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1.15; margin: 0 0 0.4rem 0;
}
.hero-sub {
    font-size: 1.1rem; font-weight: 500;
    color: var(--text-2); margin: 0 0 0.6rem 0;
}
.hero-body { font-size: 0.9rem; color: var(--text-3); line-height: 1.7; }

/* ── Glass card ── */
.gc {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.4rem;
    margin-bottom: 1rem;
    transition: border-color .25s, background .25s;
}
.gc:hover { background: var(--bg-hover); }

/* ── Panel (legacy) ── */
.panel {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.1rem;
    margin-bottom: 1rem;
}

/* ── Stat tiles ── */
.stat-tile {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: all .25s;
}
.stat-tile:hover { background: var(--bg-hover); transform: translateY(-2px); }
.stat-val { font-size: 1.55rem; font-weight: 800; margin: 0.3rem 0 0.15rem; }
.stat-lbl { font-size: 0.72rem; color: var(--text-3); text-transform: uppercase; letter-spacing: .07em; }

/* ── Stat value / label (legacy) ── */
.stat-value { font-size: 1.55rem; font-weight: 800; color: var(--text-1); }
.stat-label { font-size: 0.72rem; color: var(--text-3); text-transform: uppercase; letter-spacing: .07em; }

/* ── Section header ── */
.sec-hdr {
    display: flex; align-items: center; gap: 0.8rem;
    padding: 1.2rem 0 0.8rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.1rem;
}
.sec-dot {
    width: 38px; height: 38px; border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; flex-shrink: 0;
}
.sec-title { font-size: 1.05rem; font-weight: 700; color: var(--text-1); margin: 0; }
.sec-desc  { font-size: 0.77rem; color: var(--text-3); margin: 0.1rem 0 0; }

/* ── Info / warning boxes ── */
.ibox {
    background: rgba(37,99,235,0.08);
    border: 1px solid rgba(37,99,235,0.2);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    font-size: 0.83rem; color: var(--text-1);
    margin-bottom: 1.1rem;
}
.wbox {
    background: rgba(245,158,11,0.07);
    border: 1px solid rgba(245,158,11,0.2);
    border-radius: 10px;
    padding: 0.7rem 1rem;
    font-size: 0.8rem; color: #fcd34d;
}
.info-box {
    background: rgba(37,99,235,0.08);
    border: 1px solid rgba(37,99,235,0.2);
    border-radius: 10px;
    padding: 0.8rem 1rem;
    font-size: .84rem;
    color: var(--text-1);
    margin-bottom: 1rem;
}

/* ── Risk result cards ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}
.risk-card {
    border-radius: 20px; padding: 2rem 1.5rem;
    text-align: center; animation: fadeUp .55s ease;
}
.risk-rendah { background: linear-gradient(135deg, rgba(16,185,129,.14), rgba(16,185,129,.04)); border: 2px solid rgba(16,185,129,.4); }
.risk-sedang { background: linear-gradient(135deg, rgba(245,158,11,.14), rgba(245,158,11,.04)); border: 2px solid rgba(245,158,11,.4); }
.risk-tinggi { background: linear-gradient(135deg, rgba(239,68,68,.14), rgba(239,68,68,.04)); border: 2px solid rgba(239,68,68,.4); }

.risk-badge { font-size: 3.2rem; font-weight: 900; letter-spacing: -1px; margin: 0.4rem 0; }
.risk-desc { font-size: 0.85rem; color: var(--text-3); margin: 0.6rem 0 0; line-height: 1.6; }
.action-pill {
    margin-top: 1rem; padding: 0.65rem 1rem;
    background: rgba(0,0,0,.12); border-radius: 10px;
    font-size: 0.8rem; font-weight: 600; line-height: 1.4;
}

/* ── Prob bars ── */
.prob-row { display: flex; align-items: center; gap: .75rem; margin-bottom: .65rem; }
.prob-label { width: 64px; font-size: .82rem; font-weight: 600; }
.prob-track { flex: 1; height: 10px; background: var(--border); border-radius: 99px; overflow: hidden; }
.prob-fill  { height: 100%; border-radius: 99px; transition: width .6s cubic-bezier(.4,0,.2,1); }
.prob-pct   { width: 46px; text-align: right; font-size: .82rem; font-weight: 700; }

/* ── Sidebar nav ── */
.nav-logo  { text-align: center; padding: 1.2rem 0 1.5rem; }
.nav-emoji { font-size: 2.6rem; }
.nav-name  { font-weight: 800; font-size: 1.1rem; color: var(--text-1); margin-top: .4rem; }
.nav-tag   { font-size: .72rem; color: var(--text-3); margin-top: .15rem; line-height: 1.4; }

.status-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--green); box-shadow: 0 0 7px var(--green);
    display: inline-block; margin-right: .5rem;
}

/* ── Methodology table ── */
.feat-table { width: 100%; border-collapse: collapse; font-size: .8rem; }
.feat-table th { color: var(--text-3); padding: .5rem .6rem; text-align: left; border-bottom: 1px solid var(--border); }
.feat-table td { padding: .38rem .6rem; border-bottom: 1px solid var(--border); color: var(--text-1); }
.badge-manual { background: rgba(16,185,129,.15); color: #6ee7b7; padding: .12rem .5rem; border-radius: 5px; font-size: .7rem; font-weight: 600; }
.badge-auto   { background: rgba(37,99,235,.15); color: #93c5fd; padding: .12rem .5rem; border-radius: 5px; font-size: .7rem; font-weight: 600; }

/* ── Pulse animation ── */
@keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:.45; } }
.pulse { animation: pulse 2.2s ease-in-out infinite; }
</style>
""", unsafe_allow_html=True)
