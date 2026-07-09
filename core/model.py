import joblib
import numpy as np
import streamlit as st

from core.config import PICKLE_DIR

LABEL_MAP = {0: "Rendah", 1: "Sedang", 2: "Tinggi"}

cache_resource = getattr(st, "cache_resource", None) or getattr(st, "cache", None)
if cache_resource is None:
    cache_resource = lambda **_: lambda func: func

@cache_resource(show_spinner="Memuat model Random Forest...")
def load_artifacts():
    model = joblib.load(PICKLE_DIR / "rf_model.pkl")
    scaler = joblib.load(PICKLE_DIR / "scaler_rf.pkl")
    encoders = joblib.load(PICKLE_DIR / "encoders_rf.pkl")
    feature_cols = joblib.load(PICKLE_DIR / "feature_cols_rf.pkl")
    return model, scaler, encoders, feature_cols

def _safe_encode(row: dict, encoders: dict) -> dict:
    encoded = row.copy()
    for col, encoder in encoders.items():
        if col not in encoded:
            continue

        value = encoded.pop(col)
        if value not in encoder.classes_:
            allowed = ", ".join(map(str, encoder.classes_))
            raise ValueError(f"Nilai '{value}' tidak valid untuk {col}. Pilihan training: {allowed}.")

        encoded[f"{col}_enc"] = int(encoder.transform([value])[0])
    return encoded

def predict_risk(input_dict: dict) -> dict:
    model, scaler, encoders, feature_cols = load_artifacts()
    row = _safe_encode(input_dict, encoders)

    x_raw = np.array([[row.get(feature, 0) for feature in feature_cols]])
    x_scaled = scaler.transform(x_raw)
    pred = int(model.predict(x_scaled)[0])
    proba = model.predict_proba(x_scaled)[0]

    return {
        "label": LABEL_MAP[pred],
        "label_enc": pred,
        "prob": {LABEL_MAP[i]: float(prob) for i, prob in enumerate(proba)},
        "features": {feature: row.get(feature, 0) for feature in feature_cols},
    }