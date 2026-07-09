import streamlit as st


def render_home() -> None:
    # ── Hero ──────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="hero-wrap">
        <div style="font-size:3.2rem; margin-bottom:.3rem;">🚆</div>
        <div class="hero-title">PI1 — Prediksi Risiko Perlintasan</div>
        <div class="hero-sub">Random Forest Pipeline</div>
        <div class="hero-body">
            Sistem klasifikasi tingkat risiko perlintasan sebidang kereta api berbasis<br>
            <strong style="color:#93c5fd;">Random Forest</strong> dengan pipeline encoding, scaling,
            dan prediksi dari 4 artifact <strong style="color:#93c5fd;">pickle</strong> lokal.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stat tiles ────────────────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    tiles = [
        ("🤖", "Random Forest", "Model Utama", "#3b82f6"),
        ("📊", "16", "Fitur Input", "#10b981"),
        ("🔤", "4", "Fitur Kategorikal", "#f59e0b"),
        ("⚡", "3 Kelas", "Rendah · Sedang · Tinggi", "#ef4444"),
    ]
    for col, (ico, val, lbl, clr) in zip([c1, c2, c3, c4], tiles):
        with col:
            st.markdown(f"""
            <div class="stat-tile" style="border-top:3px solid {clr};">
                <div style="font-size:1.7rem;">{ico}</div>
                <div class="stat-val" style="color:{clr};">{val}</div>
                <div class="stat-lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Pipeline steps + Output ───────────────────────────────────────────────
    cl, cr = st.columns(2)

    with cl:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700; color:var(--text-1); margin-bottom:.9rem;">🏗️ Alur Pipeline PI1</div>
            <div style="display:flex;flex-direction:column;gap:.45rem;">
        """, unsafe_allow_html=True)

        steps = [
            ("1", "#3b82f6", "rgba(59,130,246,.1)",   "Input 16 Fitur",          "User mengisi form kondisi perlintasan"),
            ("2", "#f59e0b", "rgba(245,158,11,.1)",   "LabelEncoder",            "4 fitur kategorikal di-encode dari training"),
            ("3", "#10b981", "rgba(16,185,129,.1)",   "StandardScaler",          "Semua fitur dinormalisasi ke skala training"),
            ("4", "#8b5cf6", "rgba(139,92,246,.1)",   "Random Forest Predict",   "rf_model.pkl mengklasifikasi ke 3 kelas"),
            ("5", "#ef4444", "rgba(239,68,68,.1)",    "Output Probabilitas",     "Prediksi + P(Rendah), P(Sedang), P(Tinggi)"),
        ]
        for code, clr, bg, title, desc in steps:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:.7rem;padding:.55rem;
                        background:{bg};border-radius:9px;">
                <div style="width:28px;height:28px;border-radius:50%;background:{clr};
                            display:flex;align-items:center;justify-content:center;
                            font-size:.75rem;font-weight:800;color:#fff;flex-shrink:0;">{code}</div>
                <div>
                    <div style="font-size:.82rem;font-weight:600;color:var(--text-1);">{title}</div>
                    <div style="font-size:.7rem;color:var(--text-3);">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div></div>", unsafe_allow_html=True)

    with cr:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700; color:var(--text-1); margin-bottom:.9rem;">🎯 Klasifikasi Risiko</div>
            <div style="display:flex;flex-direction:column;gap:.6rem;">
                <div style="display:flex;align-items:center;gap:.8rem;padding:.7rem;
                            background:rgba(16,185,129,.08);border-radius:10px;border-left:3px solid #10b981;">
                    <span style="font-size:1.3rem;">🟢</span>
                    <div>
                        <div style="font-weight:700;color:#10b981;font-size:.9rem;">RENDAH</div>
                        <div style="font-size:.72rem;color:var(--text-3);">Infrastruktur memadai, risiko minimal</div>
                    </div>
                </div>
                <div style="display:flex;align-items:center;gap:.8rem;padding:.7rem;
                            background:rgba(245,158,11,.08);border-radius:10px;border-left:3px solid #f59e0b;">
                    <span style="font-size:1.3rem;">🟡</span>
                    <div>
                        <div style="font-weight:700;color:#f59e0b;font-size:.9rem;">SEDANG</div>
                        <div style="font-size:.72rem;color:var(--text-3);">Perlu monitoring & evaluasi rutin</div>
                    </div>
                </div>
                <div style="display:flex;align-items:center;gap:.8rem;padding:.7rem;
                            background:rgba(239,68,68,.08);border-radius:10px;border-left:3px solid #ef4444;">
                    <span style="font-size:1.3rem;">🔴</span>
                    <div>
                        <div style="font-weight:700;color:#ef4444;font-size:.9rem;">TINGGI</div>
                        <div style="font-size:.72rem;color:var(--text-3);">Tindakan darurat & koordinasi PT KAI</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="gc" style="margin-top:0;">
            <div style="font-weight:700; color:var(--text-1); margin-bottom:.7rem;">🗂️ Artifact Pickle</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem;font-size:.78rem;">
                <div style="background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.2);
                            border-radius:8px;padding:.6rem;color:var(--text-2);">
                    📦 <strong style="color:#93c5fd;">rf_model.pkl</strong><br>
                    <span style="color:var(--text-3);">Model Random Forest</span>
                </div>
                <div style="background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);
                            border-radius:8px;padding:.6rem;color:var(--text-2);">
                    📏 <strong style="color:#6ee7b7;">scaler_rf.pkl</strong><br>
                    <span style="color:var(--text-3);">StandardScaler</span>
                </div>
                <div style="background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);
                            border-radius:8px;padding:.6rem;color:var(--text-2);">
                    🔤 <strong style="color:#fcd34d;">encoders_rf.pkl</strong><br>
                    <span style="color:var(--text-3);">LabelEncoder x4</span>
                </div>
                <div style="background:rgba(139,92,246,.08);border:1px solid rgba(139,92,246,.2);
                            border-radius:8px;padding:.6rem;color:var(--text-2);">
                    📋 <strong style="color:#c4b5fd;">feature_cols_rf.pkl</strong><br>
                    <span style="color:var(--text-3);">Urutan 16 fitur</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;padding:1.2rem;margin-top:.5rem;">
        <span style="font-size:.88rem;color:var(--text-3);">
            Gunakan menu
            <strong style="color:#93c5fd;"> 🔍 Prediksi Risiko</strong>
            di sidebar untuk memulai analisis perlintasan
        </span>
    </div>
    """, unsafe_allow_html=True)
