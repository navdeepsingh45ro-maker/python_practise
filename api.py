
from fastapi import FastAPI
import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")

)

app = FastAPI()

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