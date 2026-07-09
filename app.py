import streamlit as st

from components.sidebar import render_sidebar
from styles.theme import apply_theme
from views.home import render_home
from views.methodology import render_methodology
from views.predict import render_predict

st.set_page_config(
    page_title="PI1 - Prediksi Tingkat Risiko Perlintasan Sebidang",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_theme()

def main() -> None:
    page = render_sidebar()

    if "Beranda" in page:
        render_home()
    elif "Prediksi" in page:
        render_predict()
    elif "Metodologi" in page:
        render_methodology()

if __name__ == "__main__":
    main()