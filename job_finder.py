import requests
from bs4 import BeautifulSoup

def get_text(element):
    return element.text.strip() if element else "N/A"

def fetch_jobs():
    url = "https://internshala.com/jobs/artificial-intelligence-jobs/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    job_cards = soup.find_all("div", class_="individual_internship")

    # ✅ REPLACED LOOP STARTS HERE
    for job in job_cards[:5]:

        title = get_text(job.find("h3") or job.find("h2") or job.find("a"))

        link_tag = job.find("a")
        job_link = "https://internshala.com" + link_tag["href"] if link_tag else None

        skills = []

        if job_link:
            job_page = requests.get(job_link)
            job_soup = BeautifulSoup(job_page.text, "html.parser")

            skill_tags = job_soup.find_all("span", class_="round_tabs")

            for skill in skill_tags:
                skills.append(skill.text.strip().lower())

        jobs.append({
            "title": title,
            "skills": skills
        })
    # ✅ LOOP ENDS HERE

    return jobs
