import streamlit as st
from generator import generate_release_notes

st.title("📄 Release Notes Generator")

version = st.text_input("Version")
date = st.text_input("Release Date")

features = st.text_area("New Features (one per line)")
bug_fixes = st.text_area("Bug Fixes (one per line)")
improvements = st.text_area("Improvements (one per line)")
known_issues = st.text_area("Known Issues (one per line)")

if st.button("Generate Release Notes"):

    data = {
        "version": version,
        "date": date,
        "features": features.split("\n"),
        "bug_fixes": bug_fixes.split("\n"),
        "improvements": improvements.split("\n"),
        "known_issues": known_issues.split("\n")
    }

    result = generate_release_notes(data)

    st.subheader("Generated Output")
    st.write(result)

    st.download_button(
        label="Download as TXT",
        data=result,
        file_name="release_notes.txt"
    )
