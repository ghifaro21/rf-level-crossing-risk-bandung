import plotly.graph_objects as go


RISK_COLORS = {
    "Rendah": "#059669",
    "Sedang": "#d97706",
    "Tinggi": "#dc2626",
}


def make_gauge(p_tinggi: float) -> go.Figure:
    val = p_tinggi * 100
    color = "#059669" if val < 33 else ("#d97706" if val < 66 else "#dc2626")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=val,
        number={"suffix": "%", "font": {"color": color, "size": 26, "family": "Inter"}},
        gauge={
            "axis"      : {"range": [0, 100], "tickcolor": "#64748b",
                           "tickfont": {"color": "#475569", "size": 9, "family": "Inter"}},
            "bar"       : {"color": color, "thickness": 0.26},
            "bgcolor"   : "rgba(241,245,249,0.5)",
            "bordercolor": "rgba(203,213,225,0.6)",
            "steps"     : [
                {"range": [0,  33], "color": "rgba(16,185,129,0.12)"},
                {"range": [33, 66], "color": "rgba(245,158,11,0.12)"},
                {"range": [66,100], "color": "rgba(239,68,68,0.12)"},
            ],
            "threshold" : {"line": {"color": color, "width": 3},
                           "thickness": 0.82, "value": val},
        },
        title={"text": "P(Risiko Tinggi)", "font": {"color": "#475569", "size": 11, "family": "Inter"}},
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=210, margin=dict(l=18, r=18, t=42, b=8),
    )
    return fig


def make_bar(probs: dict) -> go.Figure:
    names  = ["Rendah", "Sedang", "Tinggi"]
    vals   = [probs[n] * 100 for n in names]
    colors = ["#059669", "#d97706", "#dc2626"]
    fig = go.Figure(go.Bar(
        x=names, y=vals, marker_color=colors, marker_line_width=0,
        text=[f"{v:.1f}%" for v in vals], textposition="outside",
        textfont={"color": "#334155", "size": 12, "family": "Inter", "weight": "bold"},
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=230, margin=dict(l=8, r=8, t=16, b=8), showlegend=False,
        yaxis=dict(range=[0, 118], showgrid=True, gridcolor="rgba(226, 232, 240, 0.9)",
                   ticksuffix="%", tickfont={"color": "#64748b", "size": 9, "family": "Inter"}),
        xaxis=dict(tickfont={"color": "#1e293b", "size": 11, "family": "Inter"}),
        bargap=0.35,
    )
    return fig
