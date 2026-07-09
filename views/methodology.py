import streamlit as st


FEATURES = [
    ("1",  "jenis_perlintasan_enc", "Infrastruktur", "User — selectbox resmi/liar",          "✅ Manual"),
    ("2",  "dijaga",                "Infrastruktur", "User — radio Ya/Tidak",                 "✅ Manual"),
    ("3",  "palang",                "Infrastruktur", "User — selectbox 0/1/2",                "✅ Manual"),
    ("4",  "lampu_sinyal",          "Infrastruktur", "User — radio Ada/Tidak",                "✅ Manual"),
    ("5",  "petugas_jaga",          "Infrastruktur", "User — radio Ada/Tidak",                "✅ Manual"),
    ("6",  "rambu",                 "Infrastruktur", "User — selectbox 0/1/2",                "✅ Manual"),
    ("7",  "jarak_pandang_m",       "Infrastruktur", "User — slider 10–300m",                 "✅ Manual"),
    ("8",  "sudut_perpotongan",     "Infrastruktur", "User — slider 30–120°",                 "✅ Manual"),
    ("9",  "kondisi_jalan",         "Infrastruktur", "User — selectbox 0/1/2",                "✅ Manual"),
    ("10", "kelas_jalan_enc",       "Paparan",       "User — selectbox arteri/kolektor/lokal", "✅ Manual"),
    ("11", "volume_kendaraan",      "Paparan",       "User — slider 0–2000 kend/jam",         "✅ Manual"),
    ("12", "frekuensi_kereta",      "Paparan",       "User — slider 1–220 KA/hari",           "✅ Manual"),
    ("13", "sesi_waktu_rawan_enc",  "Paparan",       "User — selectbox pagi/siang/sore/malam", "✅ Manual"),
    ("14", "jarak_stasiun_m",       "Paparan",       "User — slider 50–15.000m",              "✅ Manual"),
    ("15", "jenis_kendaraan_enc",   "Perilaku",      "User — selectbox motor/mobil/truk/angkot", "✅ Manual"),
    ("16", "riwayat_insiden",       "Konsekuensi",   "User — selectbox 0–3+",                 "✅ Manual"),
]


def render_methodology() -> None:
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-size:1.75rem;font-weight:800;color:var(--text-1);">📊 Metodologi Pipeline PI1</div>
        <div style="font-size:.88rem;color:var(--text-3);margin-top:.25rem;">
            Penjelasan teknis pipeline machine learning mengikuti notebook
            <strong>new_pipeline.ipynb</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    cl, cr = st.columns(2)

    # ── Pipeline Steps ─────────────────────────────────────────────────────────
    with cl:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700;color:var(--text-1);margin-bottom:.9rem;">🏗️ Pipeline S1–S6</div>
            <div style="display:flex;flex-direction:column;gap:.45rem;">
        """, unsafe_allow_html=True)

        steps = [
            ("S1", "#3b82f6", "rgba(59,130,246,.1)",  "Load & Validasi Dataset",  "Data perlintasan KA kota Bandung"),
            ("S2", "#10b981", "rgba(16,185,129,.1)",  "Preprocessing",            "LabelEncoder · StandardScaler · SMOTE"),
            ("S3", "#f59e0b", "rgba(245,158,11,.1)",  "EDA",                      "Distribusi · Korelasi · Profil kelas"),
            ("S4", "#8b5cf6", "rgba(139,92,246,.1)",  "Training Random Forest",   "300 estimators · depth=8 · n_jobs=-1"),
            ("S5", "#06b6d4", "rgba(6,182,212,.1)",   "Evaluasi Performa",        "CM · Classification Report · Feature Importance"),
            ("S6", "#ec4899", "rgba(236,72,153,.1)",  "Export + Predict",         "4 pickle artifacts · predict_risk()"),
        ]
        for code, clr, bg, title, desc in steps:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:.7rem;padding:.55rem;
                        background:{bg};border-radius:9px;">
                <div style="width:28px;height:28px;border-radius:50%;background:{clr};
                            display:flex;align-items:center;justify-content:center;
                            font-size:.65rem;font-weight:800;color:#fff;flex-shrink:0;">{code}</div>
                <div>
                    <div style="font-size:.82rem;font-weight:600;color:var(--text-1);">{title}</div>
                    <div style="font-size:.7rem;color:var(--text-3);">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    # ── Artifacts & Categorical ────────────────────────────────────────────────
    with cr:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700;color:var(--text-1);margin-bottom:.9rem;">📦 Artifact Pickle</div>
            <table class="feat-table">
                <tbody>
                    <tr>
                        <td>rf_model.pkl</td>
                        <td>Model Random Forest Classifier</td>
                    </tr>
                    <tr>
                        <td>scaler_rf.pkl</td>
                        <td>StandardScaler (fit pada training)</td>
                    </tr>
                    <tr>
                        <td>encoders_rf.pkl</td>
                        <td>LabelEncoder untuk 4 fitur kategorikal</td>
                    </tr>
                    <tr>
                        <td>feature_cols_rf.pkl</td>
                        <td>Urutan 16 fitur yang dikirim ke model</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="gc" style="margin-top:0;">
            <div style="font-weight:700;color:var(--text-1);margin-bottom:.9rem;">🔤 Fitur Kategorikal (LabelEncoder)</div>
            <table class="feat-table">
                <tbody>
                    <tr><td>jenis_perlintasan</td><td>resmi / liar</td></tr>
                    <tr><td>kelas_jalan</td><td>arteri / kolektor / lokal</td></tr>
                    <tr><td>sesi_waktu_rawan</td><td>pagi / siang / sore / malam</td></tr>
                    <tr><td>jenis_kendaraan</td><td>motor / mobil / truk / angkot</td></tr>
                </tbody>
            </table>
            <div style="margin-top:.6rem;font-size:.72rem;color:var(--text-3);line-height:1.55;">
                Setelah encoding, kolom diganti menjadi <code>*_enc</code>
                sesuai urutan <code>feature_cols_rf.pkl</code>.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Feature Table ──────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)

    rows = "\n".join(
        f"""<tr>
            <td>{num}</td>
            <td><code>{feat}</code></td>
            <td>{comp}</td>
            <td style="color:var(--text-3);font-size:.72rem;">{src}</td>
            <td><span class="badge-manual">{badge}</span></td>
        </tr>"""
        for num, feat, comp, src, badge in FEATURES
    )

    st.markdown(f"""
    <div class="gc">
        <div style="font-weight:700;color:var(--text-1);margin-bottom:1rem;">
            📋 Pemetaan 16 Fitur Model — Semua Input Manual
        </div>
        <div style="overflow-x:auto;">
        <table class="feat-table">
            <thead>
                <tr>
                    <th>#</th><th>Fitur Backend</th><th>Komponen</th>
                    <th>Sumber Input</th><th>Metode</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
        </div>
        <div style="margin-top:.85rem;font-size:.75rem;color:var(--text-3);">
            <span class="badge-manual">✅ Manual</span> = semua 16 fitur diisi langsung oleh pengguna melalui form prediksi
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Model Info ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="gc" style="margin-top:0;">
        <div style="font-weight:700;color:var(--text-1);margin-bottom:.9rem;">🌲 Konfigurasi Random Forest</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem;">
            <div style="background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.2);
                        border-radius:11px;padding:.9rem;text-align:center;">
                <div style="font-size:.72rem;color:var(--text-3);text-transform:uppercase;letter-spacing:.06em;">Estimators</div>
                <div style="font-size:1.5rem;font-weight:800;color:#3b82f6;margin:.3rem 0;">300</div>
                <div style="font-size:.72rem;color:var(--text-3);">n_estimators</div>
            </div>
            <div style="background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);
                        border-radius:11px;padding:.9rem;text-align:center;">
                <div style="font-size:.72rem;color:var(--text-3);text-transform:uppercase;letter-spacing:.06em;">Max Depth</div>
                <div style="font-size:1.5rem;font-weight:800;color:#10b981;margin:.3rem 0;">8</div>
                <div style="font-size:.72rem;color:var(--text-3);">max_depth</div>
            </div>
            <div style="background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);
                        border-radius:11px;padding:.9rem;text-align:center;">
                <div style="font-size:.72rem;color:var(--text-3);text-transform:uppercase;letter-spacing:.06em;">Preprocessing</div>
                <div style="font-size:1rem;font-weight:800;color:#f59e0b;margin:.3rem 0;">SMOTE</div>
                <div style="font-size:.72rem;color:var(--text-3);">k=4 · balancing kelas</div>
            </div>
        </div>
        <div style="margin-top:.85rem;">
            <div style="font-size:.75rem;color:var(--text-3);margin-bottom:.4rem;">Preprocessing chain:</div>
            <div style="font-size:.78rem;color:var(--text-2);font-family:monospace;
                        background:var(--bg-card);border-radius:8px;padding:.65rem;">
                Raw Data → LabelEncoder (4 cat.) → StandardScaler → SMOTE (k=4) → Random Forest
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
