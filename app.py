import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Crop Health Monitoring",
    page_icon="🌱",
    layout="wide"
)

# Main title
st.title("🌱 AI-Driven Crop Health Monitoring and Precision Irrigation Advisory System")

st.markdown("""
### Welcome 👋

This application provides AI-based agricultural decision support through four modules:
""")

# Modules
st.markdown("""
- 🌾 **Crop Recommendation** – Recommends the most suitable crop based on soil and environmental parameters.
- 📊 **Crop Yield Prediction** – Predicts expected crop yield using agricultural parameters.
- 🌱 **Crop Health Monitoring** – Calculates a Crop Health Index and identifies crop health status.
- 💧 **Precision Irrigation Advisory** – Provides irrigation requirement and suggested water quantity.
""")

st.divider()

st.subheader("🎯 Project Objective")

st.write("""
The main objective of this project is to use Machine Learning to support
farmers in making better crop selection, yield prediction, crop health,
and irrigation decisions.
""")

st.success("✅ System Loaded Successfully")

st.info("👈 Use the navigation panel on the left to open each module.")