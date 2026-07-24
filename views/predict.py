import json
import urllib.parse
import urllib.request
import streamlit as st
import streamlit.components.v1 as components

from components.charts import RISK_COLORS, make_bar, make_gauge
from core.model import predict_risk


BANDUNG_JPL_PRESETS = {
    "📌 Pilih Perlintasan Sebidang Terdaftar...": None,
    "JPL 165 Cikudapateuh (Jl. A. Yani)": (-6.920800, 107.625800, "JPL 165 Cikudapateuh — Jl. Ahmad Yani"),
    "JPL 161 Cimindi (Jl. Raya Cimindi)": (-6.897450, 107.562700, "JPL 161 Cimindi — Jl. Raya Cimindi"),
    "JPL 169 Sunda (Jl. Sunda)": (-6.918150, 107.616600, "JPL 169 Sunda — Jl. Sunda"),
    "JPL 167 Laswi (Jl. Laswi)": (-6.923400, 107.632100, "JPL 167 Laswi — Jl. Laswi"),
    "JPL Garuda (Jl. Garuda)": (-6.907700, 107.579400, "JPL Garuda — Jl. Garuda"),
    "JPL Andir (Jl. Jend. Sudirman)": (-6.914100, 107.574600, "JPL Andir — Jl. Jend. Sudirman"),
    "JPL Kiaracondong (Jl. St. Kiaracondong)": (-6.925100, 107.646800, "JPL Kiaracondong — Jl. St. Kiaracondong"),
    "JPL Pasirkaliki (Jl. Pasir Kaliki)": (-6.910300, 107.599100, "JPL Pasirkaliki — Jl. Pasir Kaliki"),
    "Stasiun Bandung (Jl. Kebon Kawung)": (-6.914744, 107.609810, "Stasiun Bandung — Jl. Kebon Kawung"),
}


def geocode_location(query_str: str):
    if not query_str or len(query_str.strip()) < 3:
        return None
    try:
        search_q = query_str.strip()
        if "bandung" not in search_q.lower() and "jawa barat" not in search_q.lower():
            search_q += ", Bandung"
        url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(search_q)}&format=json&limit=1"
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'StreamlitPI1_App/1.0 (contact: info@ulbi.ac.id)'}
        )
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode())
            if data and len(data) > 0:
                lat = float(data[0]['lat'])
                lon = float(data[0]['lon'])
                name = data[0].get('display_name', query_str)
                return lat, lon, name
    except Exception:
        pass
    return None


def on_preset_select():
    preset_name = st.session_state.get("preset_select")
    if preset_name and BANDUNG_JPL_PRESETS.get(preset_name) is not None:
        plat, plon, pname = BANDUNG_JPL_PRESETS[preset_name]
        st.session_state["map_lat"] = float(plat)
        st.session_state["map_lon"] = float(plon)
        st.session_state["map_label"] = pname


def render_osm_location_input() -> None:
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(16,185,129,.15);">📍</div>
        <div>
            <div class="sec-title">Bagian 5 — Titik Lokasi Peta Perlintasan</div>
            <div class="sec-desc">Cari nama jalan/perlintasan sebidang, pilih preset, atau tentukan koordinat lokasi pada peta</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Initialize map state
    if "map_lat" not in st.session_state:
        st.session_state["map_lat"] = -6.914744
    if "map_lon" not in st.session_state:
        st.session_state["map_lon"] = 107.609810
    if "map_label" not in st.session_state:
        st.session_state["map_label"] = "Stasiun Bandung — Jl. Kebon Kawung"

    loc_col, map_col = st.columns([1.0, 1.3])

    with loc_col:
        st.markdown("**1. Pilih Perlintasan Sebidang Terdaftar**")
        st.selectbox(
            "Preset Perlintasan",
            options=list(BANDUNG_JPL_PRESETS.keys()),
            key="preset_select",
            on_change=on_preset_select,
            label_visibility="collapsed",
        )

        st.markdown("**2. Atau Cari Nama Jalan / Perlintasan Sebidang**")
        search_query = st.text_input(
            "Cari Nama Jalan",
            placeholder="Contoh: Jalan Sunda Bandung, JPL 167 Laswi, dll",
            key="search_query_input",
            label_visibility="collapsed",
            help="Ketik nama jalan atau lokasi perlintasan lalu klik tombol cari.",
        )

        if st.button("🔍  Cari & Titikkan di Peta", use_container_width=True):
            if search_query:
                with st.spinner("🔍 Mencari lokasi di OpenStreetMap..."):
                    geo_res = geocode_location(search_query)
                    if geo_res:
                        glat, glon, gname = geo_res
                        short_name = gname.split(",")[0]
                        st.session_state["map_lat"] = float(glat)
                        st.session_state["map_lon"] = float(glon)
                        st.session_state["map_label"] = short_name
                        st.success(f"📍 Ditemukan: {short_name}")
                    else:
                        st.warning("⚠️ Lokasi tidak ditemukan. Silakan periksa ejaan atau gunakan koordinat manual.")

        st.markdown("<hr style='margin:0.8rem 0;'/>", unsafe_allow_html=True)
        st.markdown("**3. Koordinat Manual & Catatan**")

        st.number_input(
            "Latitude",
            min_value=-90.0,
            max_value=90.0,
            step=0.000100,
            format="%.6f",
            key="map_lat",
        )
        st.number_input(
            "Longitude",
            min_value=-180.0,
            max_value=180.0,
            step=0.000100,
            format="%.6f",
            key="map_lon",
        )

        st.text_input(
            "Label / Catatan Lokasi",
            key="map_label",
            help="Catatan visual lokasi perlintasan sebidang.",
        )

        lat = float(st.session_state["map_lat"])
        lon = float(st.session_state["map_lon"])
        label_osm = str(st.session_state["map_label"])
        st.caption(f"📍 **{label_osm}** · `{lat:.6f}, {lon:.6f}`")

    with map_col:
        curr_lat = float(st.session_state["map_lat"])
        curr_lon = float(st.session_state["map_lon"])
        curr_label = str(st.session_state["map_label"]).replace('"', '\\"')

        leaflet_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
            <style>
                html, body {{ margin: 0; padding: 0; height: 100%; width: 100%; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
                #map {{ width: 100%; height: 410px; border-radius: 14px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }}
                .leaflet-popup-content-wrapper {{ border-radius: 10px; padding: 4px; }}
                .popup-title {{ font-weight: 800; color: #1e293b; font-size: 13px; margin-bottom: 2px; }}
                .popup-coords {{ font-size: 11px; color: #2563eb; font-weight: 600; }}
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script>
                var lat = {curr_lat};
                var lon = {curr_lon};
                var map = L.map('map').setView([lat, lon], 16);

                L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                    maxZoom: 19,
                    attribution: '© OpenStreetMap contributors'
                }}).addTo(map);

                var marker = L.marker([lat, lon]).addTo(map);
                marker.bindPopup("<div class='popup-title'>📍 {curr_label}</div><div class='popup-coords'>" + lat.toFixed(6) + ", " + lon.toFixed(6) + "</div>").openPopup();
            </script>
        </body>
        </html>
        """
        components.html(leaflet_html, height=430)


def render_predict() -> None:
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-size:1.75rem;font-weight:800;color:var(--text-1);">🔍 Prediksi Tingkat Risiko</div>
        <div style="font-size:.88rem;color:var(--text-3);margin-top:.25rem;">
            Isi 16 fitur perlintasan di bawah ini — semua nilai di-encode dan di-scale
            sebelum masuk ke model Random Forest
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="ibox">
        📦 <strong>Pipeline RF Aktif</strong> — Form ini mengirim 16 fitur sesuai
        <code>feature_cols_rf.pkl</code>. Nilai kategori di-encode via
        <code>encoders_rf.pkl</code>, lalu di-scale via <code>scaler_rf.pkl</code>,
        kemudian diprediksi oleh <code>rf_model.pkl</code>.
    </div>
    """, unsafe_allow_html=True)

    # Auto-fill Toggle
    autofill = st.checkbox(
        "💡 **Estimasi Otomatis (Advanced Observation)**: Isi otomatis Sudut Perpotongan, Jarak Pandang, & Volume Kendaraan berdasarkan Kelas Jalan & Jenis Perlintasan.",
        value=True,
        help="Jika diaktifkan, volume kendaraan, jarak pandang, dan sudut perpotongan akan diisi otomatis dengan nilai standar berdasarkan jenis perlintasan dan kelas jalan yang Anda pilih. Anda tetap dapat menyesuaikan secara manual."
    )

    # ── BAGIAN 1 — Kondisi Fisik ──────────────────────────────────────────────
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(59,130,246,.15);">🛤️</div>
        <div>
            <div class="sec-title">Bagian 1 — Kondisi Fisik Perlintasan</div>
            <div class="sec-desc">Informasi yang dapat dilihat langsung di lapangan</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    b1c1, b1c2, b1c3 = st.columns(3)

    with b1c1:
        jenis_perlintasan = st.selectbox(
            "Jenis Perlintasan",
            options=["resmi", "liar"],
            format_func=lambda x: "✅ Resmi (terdaftar PT KAI)" if x == "resmi" else "⚠️ Liar (tidak resmi)",
            help="Perlintasan resmi = terdaftar & dipantau PT KAI",
        )
        palang = st.selectbox(
            "Kondisi Palang Pintu",
            options=[0, 1, 2],
            format_func=lambda x: {0: "❌ Tidak Ada Palang", 1: "🔧 Palang Manual", 2: "⚡ Palang Otomatis"}[x],
        )
        rambu = st.selectbox(
            "Kelengkapan Rambu",
            options=[0, 1, 2],
            format_func=lambda x: {0: "❌ Tidak Ada Rambu", 1: "⚠️ Rambu Sebagian", 2: "✅ Rambu Lengkap"}[x],
        )

    with b1c2:
        dijaga_raw = st.radio(
            "Status Penjagaan Perlintasan",
            ["Ya — Dijaga", "Tidak — Tanpa Penjagaan"],
            help="Ada penjagaan oleh petugas atau sistem otomatis?",
        )
        dijaga = 1 if dijaga_raw.startswith("Ya") else 0

        lampu_raw = st.radio(
            "Lampu Sinyal / Warning Light",
            ["Ada", "Tidak Ada"],
            horizontal=True,
        )
        lampu_sinyal = 1 if lampu_raw == "Ada" else 0

        petugas_raw = st.radio(
            "Petugas Jaga Tetap",
            ["Ada", "Tidak Ada"],
            horizontal=True,
        )
        petugas_jaga = 1 if petugas_raw == "Ada" else 0

    with b1c3:
        kondisi_jalan = st.selectbox(
            "Kondisi Jalan",
            options=[0, 1, 2],
            format_func=lambda x: {0: "🔴 Buruk (berlubang/retak)", 1: "🟡 Sedang", 2: "🟢 Baik (mulus)"}[x],
        )

    # ── BAGIAN 2 — Lalu Lintas & Kereta ──────────────────────────────────────
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(245,158,11,.15);">🚗</div>
        <div>
            <div class="sec-title">Bagian 2 — Kondisi Lalu Lintas</div>
            <div class="sec-desc">Karakteristik volume dan jenis kendaraan yang melintasi</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    b2c1, b2c2, b2c3 = st.columns(3)

    with b2c1:
        kelas_jalan = st.selectbox(
            "Kelas Jalan",
            options=["arteri", "kolektor", "lokal"],
            format_func=lambda x: {
                "arteri"  : "🔴 Arteri — Volume tinggi",
                "kolektor": "🟡 Kolektor — Volume sedang",
                "lokal"   : "🟢 Lokal — Volume rendah",
            }[x],
        )
        if autofill:
            default_volume = {"arteri": 1200, "kolektor": 600, "lokal": 150}[kelas_jalan]
            st.caption(f"✨ Estimasi kelas {kelas_jalan}: **{default_volume}** kend/jam")
        else:
            default_volume = 450

        volume_kendaraan = st.slider(
            "Volume Kendaraan (kend/jam)",
            min_value=0, max_value=2000, value=default_volume, step=10,
        )

    with b2c2:
        jenis_kendaraan = st.selectbox(
            "Jenis Kendaraan Dominan",
            options=["motor", "mobil", "truk", "angkot"],
            format_func=lambda x: {
                "motor" : "🏍️ Motor — Risiko tertinggi",
                "mobil" : "🚗 Mobil / Sedan",
                "truk"  : "🚛 Truk / Kendaraan Berat",
                "angkot": "🚌 Angkot / Minibus",
            }[x],
        )
        sesi_waktu_rawan = st.selectbox(
            "Sesi Waktu Rawan",
            options=["pagi", "siang", "sore", "malam"],
            format_func=lambda x: {
                "pagi"  : "🌅 Pagi (06.00–10.00)",
                "siang" : "☀️  Siang (10.00–15.00)",
                "sore"  : "🌇 Sore (15.00–20.00)",
                "malam" : "🌙 Malam (20.00–06.00)",
            }[x],
        )

    with b2c3:
        frekuensi_kereta = st.slider(
            "Frekuensi Kereta (KA/hari)",
            min_value=1, max_value=220, value=70, step=1,
            help="Bisa dicek via jadwal resmi KAI / Stasiun terdekat",
        )
        jarak_stasiun_m = st.slider(
            "Jarak ke Stasiun Terdekat (m)",
            min_value=50, max_value=15000, value=1200, step=50,
        )

    # ── BAGIAN 3 — Parameter Teknis ───────────────────────────────────────────
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(139,92,246,.15);">📐</div>
        <div>
            <div class="sec-title">Bagian 3 — Parameter Teknis</div>
            <div class="sec-desc">Dimensi fisik perlintasan yang dapat diukur atau diestimasi</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    b3c1, b3c2 = st.columns(2)

    with b3c1:
        if autofill:
            default_jarak = 150 if jenis_perlintasan == "resmi" else 50
            st.caption(f"✨ Estimasi perlintasan {jenis_perlintasan}: **{default_jarak} m**")
        else:
            default_jarak = 80

        jarak_pandang_m = st.slider(
            "Jarak Pandang (m)",
            min_value=10, max_value=300, value=default_jarak, step=5,
            help="Jarak pandang pengemudi saat mendekati perlintasan",
        )

    with b3c2:
        if autofill:
            default_sudut = 90 if jenis_perlintasan == "resmi" else 60
            st.caption(f"✨ Estimasi perlintasan {jenis_perlintasan}: **{default_sudut}°**")
        else:
            default_sudut = 70

        sudut_perpotongan = st.slider(
            "Sudut Perpotongan (derajat)",
            min_value=30, max_value=120, value=default_sudut, step=1,
            help="Sudut antara jalan raya dan jalur kereta api",
        )

    # ── BAGIAN 4 — Riwayat Insiden ────────────────────────────────────────────
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(239,68,68,.15);">🚨</div>
        <div>
            <div class="sec-title">Bagian 4 — Riwayat Insiden</div>
            <div class="sec-desc">Catatan kejadian kecelakaan historis di lokasi ini</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    b4c1, _, _ = st.columns(3)
    with b4c1:
        riwayat_insiden = st.selectbox(
            "Riwayat Insiden (3 tahun terakhir)",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "✅ 0 kejadian — Aman",
                1: "⚠️  1 kejadian",
                2: "🟠 2 kejadian",
                3: "🔴 3+ kejadian — Sering terjadi",
            }[x],
        )

    # ── BAGIAN 5 — Lokasi OSM ─────────────────────────────────────────────────
    render_osm_location_input()

    # ── Tombol Prediksi ───────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 1.8, 1])
    with btn_col:
        run_predict = st.button("🔍  Analisis Tingkat Risiko Sekarang", use_container_width=True)

    if not run_predict:
        return

    # ── Inference ─────────────────────────────────────────────────────────────
    input_data = {
        "jenis_perlintasan" : jenis_perlintasan,
        "dijaga"            : dijaga,
        "palang"            : palang,
        "lampu_sinyal"      : lampu_sinyal,
        "petugas_jaga"      : petugas_jaga,
        "rambu"             : rambu,
        "kondisi_jalan"     : kondisi_jalan,
        "kelas_jalan"       : kelas_jalan,
        "volume_kendaraan"  : volume_kendaraan,
        "frekuensi_kereta"  : frekuensi_kereta,
        "sesi_waktu_rawan"  : sesi_waktu_rawan,
        "jarak_stasiun_m"   : jarak_stasiun_m,
        "jenis_kendaraan"   : jenis_kendaraan,
        "jarak_pandang_m"   : jarak_pandang_m,
        "sudut_perpotongan" : sudut_perpotongan,
        "riwayat_insiden"   : riwayat_insiden,
    }

    try:
        with st.spinner("⚙️  Menjalankan pipeline Random Forest…"):
            result = predict_risk(input_data)
    except Exception as exc:
        st.error(f"❌ Prediksi gagal: {exc}")
        return

    label = result["label"]
    probs = result["prob"]
    color = RISK_COLORS[label]

    # Risk configuration
    cfg = {
        "Rendah": {
            "card" : "risk-rendah",
            "icon" : "🟢",
            "desc" : "Perlintasan ini memiliki tingkat risiko rendah. Infrastruktur cukup memadai dan kepatuhan pengendara relatif baik.",
            "act"  : "✅ Pertahankan kondisi & lakukan inspeksi rutin setiap 3 bulan",
        },
        "Sedang": {
            "card" : "risk-sedang",
            "icon" : "🟡",
            "desc" : "Perlintasan ini memerlukan perhatian lebih. Beberapa faktor risiko perlu segera ditangani.",
            "act"  : "⚠️ Segera evaluasi infrastruktur & tingkatkan frekuensi pengawasan",
        },
        "Tinggi": {
            "card" : "risk-tinggi",
            "icon" : "🔴",
            "desc" : "PERHATIAN! Perlintasan ini berisiko TINGGI. Potensi kecelakaan signifikan berdasarkan kombinasi fitur yang dianalisis.",
            "act"  : "🚨 Tindakan darurat! Segera koordinasi dengan PT KAI & Dinas Perhubungan",
        },
    }[label]

    # ─────────────────────────────────────────────────────────────────────────
    # HASIL ANALISIS
    # ─────────────────────────────────────────────────────────────────────────
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.2rem;">
        <div style="font-size:1.4rem;font-weight:900;color:var(--text-1);">📊 Hasil Analisis Tingkat Risiko</div>
        <div style="padding:0.25rem 0.9rem;border-radius:99px;font-size:0.75rem;font-weight:700;
                    letter-spacing:0.08em;text-transform:uppercase;
                    background:color-mix(in srgb,{color} 15%,transparent);
                    color:{color};border:1px solid color-mix(in srgb,{color} 35%,transparent);">
            {label}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── ROW 1: Gauge  |  Risk Card  |  Probability Details ───────────────────
    gauge_col, card_col, prob_col = st.columns([0.85, 1.1, 0.85])

    with gauge_col:
        st.markdown("""
        <div style="background:var(--bg-card);border:1px solid var(--border);
                    border-radius:18px;padding:1rem 0.8rem 0.5rem;text-align:center;">
            <div style="font-size:0.72rem;font-weight:700;color:var(--text-3);
                        text-transform:uppercase;letter-spacing:.07em;margin-bottom:0.2rem;">
                🎯 Gauge — P(Risiko Tinggi)
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(
            make_gauge(probs["Tinggi"]),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with card_col:
        st.markdown(f"""
        <div class="risk-card {cfg['card']}" style="height:100%;box-sizing:border-box;">
            <div style="font-size:3.8rem;line-height:1;margin-bottom:0.3rem;">{cfg['icon']}</div>
            <div style="font-size:.72rem;color:var(--text-3);text-transform:uppercase;
                        letter-spacing:.12em;margin-bottom:0.15rem;">Prediksi Tingkat Risiko</div>
            <div class="risk-badge" style="color:{color};font-size:2.6rem;margin:0.1rem 0 0.5rem;">
                {label.upper()}
            </div>
            <div style="display:inline-block;padding:0.3rem 1rem;border-radius:99px;
                        background:color-mix(in srgb,{color} 12%,transparent);
                        border:1px solid color-mix(in srgb,{color} 30%,transparent);
                        font-size:0.82rem;font-weight:700;color:{color};margin-bottom:0.8rem;">
                Keyakinan Model: {probs[label]:.1%}
            </div>
            <p class="risk-desc" style="margin:0;font-size:0.84rem;line-height:1.65;color:var(--text-2);">
                {cfg['desc']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    with prob_col:
        html_prob = """<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:18px;padding:1.2rem;height:100%;box-sizing:border-box;">
<div style="font-size:0.72rem;font-weight:700;color:var(--text-3);text-transform:uppercase;letter-spacing:.07em;margin-bottom:1rem;">
    🔍 Rincian Probabilitas
</div>"""

        for rname, rclr in [("Rendah", "#059669"), ("Sedang", "#d97706"), ("Tinggi", "#dc2626")]:
            pv = probs[rname]
            ico = "🟢" if rname == "Rendah" else "🟡" if rname == "Sedang" else "🔴"
            is_predicted = (rname == label)
            bdr = f"border:2px solid {rclr};" if is_predicted else "border:1px solid var(--border);"
            badge_html = (
                f'<span style="font-size:0.6rem;font-weight:700;color:{rclr};'
                f'background:color-mix(in srgb,{rclr} 15%,transparent);'
                f'padding:0.1rem 0.4rem;border-radius:4px;margin-left:0.3rem;">PREDIKSI</span>'
                if is_predicted else ""
            )
            html_prob += f"""<div style="background:color-mix(in srgb,{rclr} {'8' if is_predicted else '4'}%,transparent);{bdr}border-radius:12px;padding:0.75rem 0.9rem;margin-bottom:0.55rem;">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.3rem;">
<div style="display:flex;align-items:center;gap:0.4rem;">
<span style="font-size:1rem;">{ico}</span>
<span style="font-size:0.85rem;font-weight:600;color:var(--text-1);">{rname}</span>
{badge_html}
</div>
<span style="font-size:1rem;font-weight:800;color:{rclr};">{pv:.1%}</span>
</div>
<div style="height:6px;background:color-mix(in srgb,var(--text-color) 8%,transparent);border-radius:99px;overflow:hidden;">
<div style="width:{pv*100:.1f}%;height:100%;background:{rclr};border-radius:99px;transition:width .6s ease;"></div>
</div>
</div>"""

        html_prob += "</div>"
        st.markdown(html_prob, unsafe_allow_html=True)

    # ── ROW 2: Bar Chart  |  Recommendation ──────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    bar_col, rec_col = st.columns([1.1, 0.9])

    with bar_col:
        st.markdown("""
        <div style="background:var(--bg-card);border:1px solid var(--border);
                    border-radius:18px;padding:1.2rem 1.4rem 0.5rem;">
            <div style="font-size:0.75rem;font-weight:700;color:var(--text-3);
                        text-transform:uppercase;letter-spacing:.06em;margin-bottom:0.2rem;">
                📈 Distribusi Probabilitas Model
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(make_bar(probs), use_container_width=True, config={"displayModeBar": False})
        st.markdown("</div>", unsafe_allow_html=True)

    with rec_col:
        st.markdown(f"""
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:18px;
                    padding:1.4rem;height:100%;box-sizing:border-box;
                    display:flex;flex-direction:column;gap:0.8rem;">
            <div style="font-size:0.75rem;font-weight:700;color:var(--text-3);
                        text-transform:uppercase;letter-spacing:.06em;">💡 Rekomendasi Tindakan</div>
            <div style="background:color-mix(in srgb,{color} 10%,transparent);
                        border-left:4px solid {color};border-radius:0 12px 12px 0;padding:1rem;">
                <div style="font-size:0.78rem;font-weight:700;color:{color};margin-bottom:0.4rem;">
                    Tindakan yang Disarankan:
                </div>
                <div style="font-size:0.88rem;color:var(--text-1);line-height:1.6;font-weight:500;">
                    {cfg['act']}
                </div>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5rem;">
                <div style="background:color-mix(in srgb,var(--text-color) 4%,transparent);
                            border:1px solid var(--border);border-radius:10px;
                            padding:0.65rem;text-align:center;">
                    <div style="font-size:0.68rem;color:var(--text-3);text-transform:uppercase;
                                letter-spacing:.05em;">Prediksi</div>
                    <div style="font-size:1rem;font-weight:800;color:{color};">{label}</div>
                </div>
                <div style="background:color-mix(in srgb,var(--text-color) 4%,transparent);
                            border:1px solid var(--border);border-radius:10px;
                            padding:0.65rem;text-align:center;">
                    <div style="font-size:0.68rem;color:var(--text-3);text-transform:uppercase;
                                letter-spacing:.05em;">Keyakinan</div>
                    <div style="font-size:1rem;font-weight:800;color:{color};">{probs[label]:.1%}</div>
                </div>
            </div>
            <div style="font-size:0.73rem;color:var(--text-3);line-height:1.5;
                        padding-top:0.4rem;border-top:1px solid var(--border);">
                Rekomendasi dihasilkan otomatis oleh model Random Forest berdasarkan 16 fitur input.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Fitur akhir yang dikirim ke model ─────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📋  Lihat fitur akhir yang dikirim ke model"):
        st.markdown("""
        <div style="font-size:.8rem;color:var(--text-3);margin-bottom:1rem;line-height:1.7;">
            16 fitur berikut (setelah encoding &amp; scaling) yang dikirim ke
            <strong>rf_model.pkl</strong>. Nilai sudah di-encode via
            <code>encoders_rf.pkl</code> dan urutan sesuai <code>feature_cols_rf.pkl</code>.
        </div>
        """, unsafe_allow_html=True)
        st.json(result["features"])
