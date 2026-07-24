import streamlit as st


def apply_theme() -> None:
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ══ Reset & Light Mode Tokens ═════════════════════════════════════════════ */
:root {
    --bg-primary:   #f8fafc;
    --bg-secondary: #ffffff;
    --bg-card:      #ffffff;
    --bg-hover:     #f1f5f9;
    --border:       #e2e8f0;
    --border-glow:  rgba(37, 99, 235, 0.2);
    --text-1:       #0f172a;
    --text-2:       #334155;
    --text-3:       #64748b;
    --accent:       #2563eb;
    --green:        #059669;
    --yellow:       #d97706;
    --red:          #dc2626;
    --blue:         #2563eb;
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

/* ── Sidebar Light Styling ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f1f5f9 0%, #ffffff 100%) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-1) !important; }
[data-testid="stSidebar"] .stRadio > label { color: var(--text-2) !important; }

/* Sidebar Radio Menu Transition & styling */
[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    gap: 0.4rem !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 0.5rem 0.8rem !important;
    border-radius: 10px !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03) !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: #eff6ff !important;
    border-color: #93c5fd !important;
    transform: translateX(3px);
}

.sidebar-footer {
    margin-top: 2rem;
    padding: 1rem 0.4rem 0;
    border-top: 1px solid var(--border);
    text-align: center;
    font-size: .72rem;
    line-height: 1.55;
    color: var(--text-3);
}

/* ── Widget labels ── */
label, .stRadio > div > label, [data-testid="stWidgetLabel"] p {
    color: var(--text-2) !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
}

/* ── Select boxes ── */
div[data-baseweb="select"] > div {
    background-color: var(--bg-card) !important;
    border: 1px solid #cbd5e1 !important;
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
    border: 1px solid #cbd5e1 !important;
    color: var(--text-1) !important;
    border-radius: 10px !important;
}

/* ── Text input ── */
[data-testid="stTextInput"] input {
    background: var(--bg-card) !important;
    border: 1px solid #cbd5e1 !important;
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
    background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 50%, #3b82f6 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.85rem 2rem !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.3px !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 14px rgba(37,99,235,0.3) !important;
    width: 100% !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(37,99,235,0.45) !important;
}
.stButton > button:active { transform: translateY(0px) !important; }

/* ── Expander ── */
[data-testid="stExpander"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
}
[data-testid="stExpander"] summary {
    color: var(--text-2) !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
}

/* ── Divider ── */
hr { border-color: var(--border) !important; }

/* ═══════════════════════════════════════════════════════════════════════════
   CUSTOM COMPONENT STYLES (LIGHT THEME)
═══════════════════════════════════════════════════════════════════════════ */

/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg,
        rgba(37,99,235,0.08) 0%,
        rgba(59,130,246,0.05) 50%,
        rgba(16,185,129,0.04) 100%);
    border: 1px solid rgba(37,99,235,0.2);
    border-radius: 22px;
    padding: 2.8rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(37,99,235,0.06);
}
.hero-title {
    font-size: 2.9rem; font-weight: 900;
    background: linear-gradient(130deg, #1e40af, #2563eb, #047857);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1.15; margin: 0 0 0.4rem 0;
}
.hero-sub {
    font-size: 1.15rem; font-weight: 700;
    color: #2563eb; margin: 0 0 0.6rem 0;
}
.hero-body { font-size: 0.92rem; color: #475569; line-height: 1.7; font-weight: 500; }

/* ── Glass card / Panel ── */
.gc, .panel {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.4rem;
    margin-bottom: 1rem;
    transition: all .2s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.gc:hover {
    background: var(--bg-hover);
    border-color: #cbd5e1;
}

/* ── Stat tiles ── */
.stat-tile {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: all .2s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
}
.stat-tile:hover {
    background: var(--bg-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.06);
}
.stat-val { font-size: 1.6rem; font-weight: 800; margin: 0.3rem 0 0.15rem; }
.stat-lbl { font-size: 0.74rem; color: var(--text-3); text-transform: uppercase; letter-spacing: .07em; font-weight: 700; }

/* ── Stat value / label (legacy) ── */
.stat-value { font-size: 1.55rem; font-weight: 800; color: var(--text-1); }
.stat-label { font-size: 0.72rem; color: var(--text-3); text-transform: uppercase; letter-spacing: .07em; font-weight: 700; }

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
.sec-title { font-size: 1.1rem; font-weight: 800; color: var(--text-1); margin: 0; }
.sec-desc  { font-size: 0.8rem; color: var(--text-3); margin: 0.1rem 0 0; }

/* ── Info / warning boxes ── */
.ibox, .info-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 12px;
    padding: 0.85rem 1.1rem;
    font-size: 0.88rem;
    color: #1e40af;
    margin-bottom: 1.1rem;
    line-height: 1.6;
}
.wbox {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-radius: 12px;
    padding: 0.8rem 1.1rem;
    font-size: 0.85rem;
    color: #92400e;
    line-height: 1.6;
}

/* ── Risk result cards ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}
.risk-card {
    border-radius: 20px; padding: 2rem 1.5rem;
    text-align: center; animation: fadeUp .45s ease;
    box-shadow: 0 4px 16px rgba(0,0,0,0.04);
}
.risk-rendah { background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); border: 2px solid #059669; }
.risk-sedang { background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border: 2px solid #d97706; }
.risk-tinggi { background: linear-gradient(135deg, #fef2f2 0%, #ffe4e6 100%); border: 2px solid #dc2626; }

.risk-badge { font-size: 3.2rem; font-weight: 900; letter-spacing: -1px; margin: 0.4rem 0; }
.risk-desc { font-size: 0.88rem; color: #334155; margin: 0.6rem 0 0; line-height: 1.65; }
.action-pill {
    margin-top: 1rem; padding: 0.65rem 1rem;
    background: rgba(255,255,255,0.8); border-radius: 10px;
    font-size: 0.82rem; font-weight: 700; line-height: 1.4; color: #0f172a;
}

/* ── Prob bars ── */
.prob-row { display: flex; align-items: center; gap: .75rem; margin-bottom: .65rem; }
.prob-label { width: 64px; font-size: .85rem; font-weight: 700; color: #1e293b; }
.prob-track { flex: 1; height: 10px; background: #e2e8f0; border-radius: 99px; overflow: hidden; }
.prob-fill  { height: 100%; border-radius: 99px; transition: width .6s ease; }
.prob-pct   { width: 46px; text-align: right; font-size: .85rem; font-weight: 800; color: #0f172a; }

/* ── Sidebar nav ── */
.nav-logo  { text-align: center; padding: 1.2rem 0 1.2rem; }
.nav-emoji { font-size: 2.8rem; }
.nav-name  { font-weight: 900; font-size: 1.15rem; color: #0f172a; margin-top: .4rem; }
.nav-tag   { font-size: .75rem; color: #64748b; margin-top: .2rem; line-height: 1.4; font-weight: 500; }

.status-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: #059669; box-shadow: 0 0 6px #059669;
    display: inline-block; margin-right: .5rem;
}

/* ── Methodology table ── */
.feat-table { width: 100%; border-collapse: collapse; font-size: .84rem; }
.feat-table th { color: #475569; padding: .6rem .75rem; text-align: left; border-bottom: 2px solid #e2e8f0; background: #f8fafc; font-weight: 700; }
.feat-table td { padding: .5rem .75rem; border-bottom: 1px solid #f1f5f9; color: #0f172a; font-weight: 500; }
.badge-manual { background: #d1fae5; color: #065f46; padding: .15rem .6rem; border-radius: 6px; font-size: .72rem; font-weight: 700; }
.badge-auto   { background: #dbeafe; color: #1e40af; padding: .15rem .6rem; border-radius: 6px; font-size: .72rem; font-weight: 700; }

/* ── Pulse animation ── */
@keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:.45; } }
.pulse { animation: pulse 2.2s ease-in-out infinite; }
</style>
""", unsafe_allow_html=True)
