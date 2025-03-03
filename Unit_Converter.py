import streamlit as st

# 🎨 Page Config
st.set_page_config(page_title="Unit Converter", page_icon="🌍", layout="centered")

# 🌍 Title & Description
st.title("🌍 Unit Converter")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# 📌 Category Selection
category = st.selectbox("📂 Choose a Category:", ["Length", "Weight", "Time"])

# 🔄 Conversion Function
def convert_unit(category, value, unit):
    try:
        if category == "Length":
            conversions = {
                "Kilometers to Miles": value * 0.621371,
                "Miles to Kilometers": value / 0.621371,
            }
        elif category == "Weight":
            conversions = {
                "Kilograms to Pounds": value * 2.20462,
                "Pounds to Kilograms": value / 2.20462,
            }
        elif category == "Time":
            conversions = {
                "Seconds to Minutes": value / 60,
                "Minutes to Seconds": value * 60,
                "Minutes to Hours": value / 60,
                "Hours to Days": value / 24,
                "Days to Hours": value * 24,
            }
        return conversions.get(unit, "Invalid Conversion")
    except:
        return "Error: Invalid Input"

# 🔍 Unit Selection
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Days", "Days to Hours"])

# 🔢 Input Value
value = st.number_input("🔢 Enter the Value to Convert", step=0.01, format="%.2f")

# 🔘 Convert Button
if st.button("🚀 Convert"):
    if value is not None and value >= 0:
        result = convert_unit(category, value, unit)
        st.success(f"✅ The result is: **{result:.2f}**")
    else:
        st.warning("⚠ Please enter a **valid** value (greater than 0) for conversion!")

# 🎯 Footer
st.markdown("---")

