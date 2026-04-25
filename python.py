import streamlit as st
import random

# Title
st.title("📚 AI Study Planner")
st.write("Generate a smart study schedule based on your subjects and available time.")

# User Inputs
name = st.text_input("Enter your name")

subjects = st.text_area("Enter subjects (comma separated)")
hours = st.slider("Study hours per day", 1, 12, 4)
days = st.slider("Number of days to plan", 1, 30, 7)

# Generate Plan
if st.button("Generate Study Plan"):

    if subjects == "":
        st.warning("Please enter at least one subject!")
    else:
        subject_list = [s.strip() for s in subjects.split(",")]

        st.success(f"✅ Study Plan for {name}")

        for day in range(1, days + 1):
            st.subheader(f"Day {day}")

            random.shuffle(subject_list)

            daily_hours = hours / len(subject_list)

            for sub in subject_list:
                st.write(f"📖 {sub} → {round(daily_hours,1)} hrs")