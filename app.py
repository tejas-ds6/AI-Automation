import streamlit as st
from resume_parser import parse_resume
from job_scraper import fetch_jobs
from matcher import rank_jobs
from generator import generate_cover_letter
from utils.display_utils import display_jobs

st.title("AI Job Automation System")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:
    result = parse_resume(uploaded_file)
    st.write("Your Skills:", result["skills"])

    if st.button("Find Jobs"):
        jobs = fetch_jobs()
        ranked_jobs = rank_jobs(result["skills"], jobs)

        display_jobs(ranked_jobs)

        if ranked_jobs:
            if st.button("Generate Cover Letter"):
                cover = generate_cover_letter(
                    ranked_jobs[0]["title"],
                    result["skills"]
                )
                st.write(cover)
