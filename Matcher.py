def match_skills(user_skills, job_skills):
    if not job_skills:
        return 0

    user_skills = set(user_skills)
    job_skills = set(job_skills)

    match = user_skills.intersection(job_skills)

    score = len(match) / len(job_skills)

    return round(score * 100, 2)

def rank_jobs(user_skills, jobs):
    ranked = []

    for job in jobs:
        score = match_skills(user_skills, job["skills"])
        job["match_score"] = score
        ranked.append(job)

    ranked.sort(key=lambda x: x["match_score"], reverse=True)

    return ranked
