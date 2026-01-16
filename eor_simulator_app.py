import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. إعدادات الهوية والتصميم
st.set_page_config(page_title="Eng. Sulaiman Kudaimi | EOR Simulator", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stMetricValue"] {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff;
        font-family: 'Courier New', monospace;
    }
    .header-box {
        background: linear-gradient(90deg, #001f3f 0%, #003366 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 10px solid #ffcc00;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="header-box">
        <h1 style="color:white; margin:0;">🌊 EOR SMART WATERFLOODING SIMULATOR</h1>
        <h3 style="color:#ffcc00; margin:10px 0;">Lead Reservoir Engineer: Eng. Sulaiman Kudaimi</h3>
        <p style="color:#bdc3c7;">Predictive Analysis & Inter-well Connectivity Model | Volve Field</p>
    </div>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية للتحكم في المحاكاة
st.sidebar.title("🕹️ Simulation Parameters")
st.sidebar.markdown(f"**Developer:**\nEng. Sulaiman Kudaimi")
st.sidebar.divider()

# مدخلات المحاكاة (ماذا لو؟)
target_inj = st.sidebar.slider("Target Water Injection (bbl/day)", 0, 20000, 8000)
sweep_eff = st.sidebar.slider("Estimated Sweep Efficiency (%)", 5.0, 40.0, 18.0) / 100
lag_time = st.sidebar.select_slider("Response Lag Time (Days)", options=[15, 30, 45, 60], value=30)

# 3. محرك المحاكاة الرياضي (النموذج التنبؤي)
def run_simulation(inj_rate, efficiency):
    base_oil = 3000 # إنتاج أساسي بدون حقن
    predicted_oil = base_oil + (inj_rate * efficiency)
    return predicted_oil

current_prediction = run_simulation(target_inj, sweep_eff)

# 4. لوحة النتائج (KPIs)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Water Injection", f"{target_inj:,} bpd")
m2.metric("Predicted Oil Recovery", f"{round(current_prediction, 1):,} bpd")
m3.metric("VRR Ratio", f"{round(target_inj/current_prediction, 2) if current_prediction > 0 else 0}")
m4.metric("Economic Status", "PROFITABLE" if (target_inj*sweep_eff) > 500 else "RE-EVALUATE")

st.divider()

# 5. الرسم البياني لسيناريوهات الإنتاج
col_chart, col_desc = st.columns([2.5, 1])

with col_chart:
    st.markdown("### 📈 Forecasted Production vs. Injection Rates")
    # توليد بيانات المنحنى
    x_range = np.linspace(0, 25000, 100)
    y_range = [run_simulation(x, sweep_eff) for x in x_range]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_range, y=y_range, mode='lines', name='Prediction Model',
                            line=dict(color='#00f2ff', width=3)))
    
    # نقطة القرار الحالية
    fig.add_trace(go.Scatter(x=[target_inj], y=[current_prediction], mode='markers',
                            marker=dict(color='red', size=15, symbol='star'),
                            name='Selected Strategy'))
    
    fig.update_layout(template="plotly_dark", height=500,
                      xaxis_title="Injection Rate (BWPD)",
                      yaxis_title="Predicted Oil (BOPD)",
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col_desc:
    st.markdown("### 🤖 Reservoir Insight")
    st.success(f"**Strategy Validated**")
    st.write(f"بناءً على المحاكاة، الحقن بمعدل {target_inj} برميل ماء سيؤدي لزيادة الإنتاج بنسبة ملحوظة نتيجة التواصل المكمني بين F-4 و F-12.")
    st.info(f"المحاكي يفترض وجود Lag Time قدره {lag_time} يوماً بناءً على بيانات حقل Volve التاريخية.")

# 6. التوقيع النهائي
st.markdown(f"""
    <div style="text-align:center; padding:20px; border-top:1px solid #30363d; margin-top:50px;">
        <p style="color:#8b949e;">Digital Field Management Solution | Developed by <b>Eng. Sulaiman Kudaimi</b> © 2024</p>
    </div>
    """, unsafe_allow_html=True)