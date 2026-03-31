import streamlit as st

def display_jobs(jobs):
    for job in jobs:
        st.subheader(job["title"])
        st.write("Skills:", job["skills"])
        st.write("Match Score:", job.get("match_score", 0), "%")
        st.markdown("---")
