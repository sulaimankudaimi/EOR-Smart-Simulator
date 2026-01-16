# 🌊 EOR Smart Waterflooding Simulator
**Advanced Predictive Analytics for Reservoir Management & Enhanced Oil Recovery**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-00f2ff.svg)
![Status](https://img.shields.io/badge/Project-Live-success.svg)

## 👤 Developed by
**Eng. Sulaiman Kudaimi** *Lead Petroleum Production & Digital Transformation Engineer*

---

## 🎯 Project Overview
This project is an **AI-Driven Proxy Simulator** designed to optimize Waterflooding operations in oil reservoirs. By analyzing historical Inter-well Connectivity, the simulator predicts the oil production response in producing wells based on the water injection rates in adjacent injectors.

Inspired by real-world data from the **Equinor Volve Field**, this tool bridges the gap between complex reservoir simulation software and real-time operational decision-making.

## 🚀 Key Features
- **Inter-well Connectivity Modeling:** Analyzes the relationship between Injector (e.g., F-4) and Producer (e.g., F-12) pairs.
- **Predictive Analytics:** Uses a mathematical proxy model to forecast oil production based on injection strategy.
- **What-if Scenario Analysis:** Interactive sliders allow users to adjust injection rates and see immediate production forecasts.
- **Custom Data Support:** Users can upload their own CSV well-log or production data to run global simulations.
- **Neon-Pro UI:** A high-end, dark-themed dashboard designed for professional engineering environments.

## 🔬 Technical Methodology
The simulator utilizes a **Physics-Informed Data Science** approach:
1. **Data Processing:** Cleaning and synchronizing injection and production time-series.
2. **Lag-Time Analysis:** Accounting for the time delay between water injection at the sandface and oil response at the producer.
3. **VRR Calculation:** Real-time monitoring of the **Voidage Replacement Ratio** to ensure reservoir pressure maintenance.

## 🛠️ Tech Stack
- **Backend:** Python 3.x
- **Frontend:** Streamlit (Web UI Framework)
- **Data Handling:** Pandas, NumPy
- **Visualization:** Plotly (Interactive Graphs)
- **Data Source:** Equinor Volve Field Open Data
- <img width="1915" height="886" alt="Screenshot_2026_01_16-11" src="https://github.com/user-attachments/assets/985f8bf9-4ded-4520-9c60-51c3d14a030a" />
<img width="1920" height="893" alt="Screenshot_2026_01_16-10" src="https://github.com/user-attachments/assets/bea594d9-6dad-4478-b8f1-6cbb485f3af5" />


## 📂 Project Structure
```text
├── eor_simulator_app.py   # Main Application Script
├── requirements.txt       # Necessary Python Libraries
├── README.md              # Project Documentation
└── assets/                # Images and Technical Diagrams
