
from fastapi import FastAPI
import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv("api.env")

def get_db():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
   )
    return conn

app = FastAPI()

@app.get("/top_skills")
def get_top_skills():
    conn = get_db()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT skills FROM jobs") 
    rows = cursor.fetchall()
    conn.close()

    skill_count = {}
    for row in rows:
        skills = row["skills"].split(",")
        for skill in skills:
            skill = skill.strip()
            skill_count[skill] = skill_count.get(skill, 0) + 1
    sorted_skills = sorted(skill_count.items(), key=lambda x: x[1], reverse=True)
    return {"top_skills": [{"skill":s, "count":c} for s, c in sorted_skills]}

@app.get("/")
def home():
    return {"Message": "Job Tracker is running"}

@app.get("/jobs")
def get_jobs():
    conn = get_db()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return {"jobs": jobs}

@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM jobs WHERE id = %s", (job_id,))
    job = cursor.fetchone()
    conn.close()
    return {"job": job}