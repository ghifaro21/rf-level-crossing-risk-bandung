import streamlit as st


def render_sidebar() -> str:
    with st.sidebar:
        st.markdown("""
        <div class="nav-logo">
            <div class="nav-emoji">🚆</div>
            <div class="nav-name">PI1 — RF Crossing</div>
            <div class="nav-tag">Random Forest Pipeline<br>Perlintasan Sebidang Bandung</div>
        </div>
        <hr/>
        """, unsafe_allow_html=True)

        page = st.radio(
            "nav", ["🏠  Beranda", "🔍  Prediksi Risiko", "📊  Metodologi"],
            label_visibility="collapsed",
        )

        st.markdown("<hr/>", unsafe_allow_html=True)

        st.markdown("""
        <div style="padding:.9rem; background:var(--bg-card); border:1px solid var(--border);
                    border-radius:12px; margin-top:.5rem;">
            <div style="font-size:.7rem; color:var(--text-3); font-weight:600;
                        text-transform:uppercase; letter-spacing:.07em; margin-bottom:.7rem;">
                Status Model
            </div>
            <div style="font-size:.8rem; color:var(--text-2); line-height:2;">
                <span class="status-dot pulse"></span>Random Forest<br>
                <span class="status-dot pulse"></span>16 Fitur Input<br>
                <span class="status-dot pulse"></span>4 Fitur Kategorikal<br>
                <span class="status-dot pulse"></span>3 Kelas Risiko
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-footer">
            Proyek Integrasi 1 · ULBI · Data Science<br>© 2026 I.T Ghifari
        </div>
        """, unsafe_allow_html=True)

    return page
