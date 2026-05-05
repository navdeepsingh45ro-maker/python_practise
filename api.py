
from fastapi import FastAPI , HTTPException, Query
import mysql.connector
import os
from dotenv import load_dotenv
from pydantic import BaseModel


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
    sorted_skills = sorted(skill_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return {"top_skills": [{"skill":s, "count":c} for s, c in sorted_skills]}

@app.get("/")
def home():
    return {"Message": "Job Tracker is running"}

@app.get("/jobs")
def get_jobs(skill: str = Query(None)):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    if skill:
        cursor.execute("SELECT * FROM jobs WHERE skills LIKE %s", (f"%{skill}%",))
    else:
        cursor.execute("SELECT * FROM jobs")

    jobs = cursor.fetchall()
    conn.close()

    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found")

    return {"jobs": jobs}

@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM jobs WHERE id = %s", (job_id,))
    job = cursor.fetchone()
    conn.close()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job": job}

class JobCreate(BaseModel):
    title: str
    company_id: int
    salary: int
    skills: str

@app.post("/jobs")
def create_job(job: JobCreate):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jobs (title, company_id, salary, skills) VALUES (%s, %s, %s,%s)",(job.title, job.company_id, job.salary, job.skills))
        conn.commit()
        conn.close()
        return {"message": "Job created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

import uvicorn 
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000)
    