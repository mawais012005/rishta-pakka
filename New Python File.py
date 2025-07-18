import streamlit as st
import json
import os

DATA_FILE = "profiles.json"

# Sample data if no file exists
SAMPLE_DATA = [
    {"name": "Dr. Ayesha", "age": 28, "gender": "Female", "profession": "Doctor", "city": "Lahore"},
    {"name": "Engr. Ahmed", "age": 30, "gender": "Male", "profession": "Engineer", "city": "Karachi"},
    {"name": "Mr. Bilal", "age": 35, "gender": "Male", "profession": "Businessman", "city": "Islamabad"},
]

# Load or initialize data
def load_profiles():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump(SAMPLE_DATA, f, indent=2)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_profile(profile):
    data = load_profiles()
    data.append(profile)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# App title
st.set_page_config(page_title="Rishta Pakka", layout="centered")
st.title("💍 Rishta Pakka")
st.subheader("Find the perfect match among Doctors, Engineers & Businessmen")

# Sidebar filters
st.sidebar.header("🔎 Filter Rishtas")
profession_filter = st.sidebar.selectbox("Profession", ["All", "Doctor", "Engineer", "Businessman"])
gender_filter = st.sidebar.selectbox("Gender", ["All", "Male", "Female"])
age_filter = st.sidebar.slider("Maximum Age", 18, 60, 40)

# Load data
profiles = load_profiles()

# Apply filters
filtered_profiles = [
    p for p in profiles
    if (profession_filter == "All" or p["profession"] == profession_filter)
    and (gender_filter == "All" or p["gender"] == gender_filter)
    and p["age"] <= age_filter
]

# Show profiles
st.markdown("### 📋 Available Rishtas")
if filtered_profiles:
    for p in filtered_profiles:
        st.markdown(f"""
        **Name:** {p['name']}  
        **Age:** {p['age']}  
        **Gender:** {p['gender']}  
        **Profession:** {p['profession']}  
        **City:** {p['city']}  
        ---
        """)
else:
    st.warning("No rishtas match the selected criteria.")

# Profile Submission
st.markdown("---")
st.markdown("### 📤 Submit Your Profile")
with st.form("profile_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=18, max_value=60)
    gender = st.selectbox("Gender", ["Male", "Female"])
    profession = st.selectbox("Profession", ["Doctor", "Engineer", "Businessman"])
    city = st.text_input("City")
    submit = st.form_submit_button("Submit")

    if submit:
        new_profile = {
            "name": name,
            "age": age,
            "gender": gender,
            "profession": profession,
            "city": city,
        }
        save_profile(new_profile)
        st.success("Profile submitted successfully!")
