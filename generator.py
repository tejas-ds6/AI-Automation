from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_cover_letter(job_title, skills):
    prompt = f"""
    Write a professional cover letter for the role {job_title}.
    Candidate skills: {skills}.
    Keep it short and impactful.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
