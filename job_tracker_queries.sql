CREATE DATABASE job_tracker;
USE job_tracker;

CREATE TABLE companies (
id INT AUTO_INCREMENT PRIMARY KEY ,
name VARCHAR(100),
location VARCHAR(100),
industry VARCHAR(100)
);

CREATE TABLE jobs (
id INT AUTO_INCREMENT PRIMARY KEY ,
title VARCHAR(100),
company_id INT,
salary INT,
skills VARCHAR(255),
FOREIGN KEY (company_id) REFERENCES companies(id)
);

INSERT INTO companies (name, location, industry) VALUES
('Google', 'Bangalore', 'Tech'),
('Zomato', 'Delhi', 'Food-Tech'),
('Swiggy', 'Bangalore', 'Food-Tech'),
('Paytm', 'Noida', 'Fintech'),
('Infosys', 'Pune', 'IT Services');

INSERT INTO jobs (title, company_id, salary, skills) VALUES
('Python Developer', 1, 35000, 'Python, SQL, FastAPI'),
('Data Analyst', 2, 30000, 'SQL, Excel, Python'),
('Backend Engineer', 3, 40000, 'Python, Django, MySQL'),
('ML Engineer', 1, 50000, 'Python, TensorFlow, SQL'),
('Data Engineer', 4, 35000, 'SQL, Python, Spark'),
('Frontend Developer', 5, 28000, 'JavaScript, React, CSS');

SELECT * FROM companies;

SELECT * FROM jobs;


SELECT title, salary, skills
FROM jobs
WHERE salary>30000;

SELECT jobs.title, companies.name, jobs.salary, jobs.skills
FROM jobs
JOIN companies ON companies.id = jobs.company_id
WHERE jobs.salary>30000
ORDER BY jobs.salary DESC;

SELECT companies.name, COUNT(*) as total_jobs 
FROM jobs
JOIN companies ON jobs.company_id = companies.id
GROUP BY companies.name;

SELECT title, skills 
FROM jobs 
WHERE skills LIKE '%python%';

SELECT title, salary FROM jobs 
WHERE salary BETWEEN 30000 AND 45000;

SELECT COUNT(*) AS python_jobs FROM jobs
WHERE skills LIKE '%python%';

SELECT id, name, location FROM companies 
JOIN jobs ON companies.id = jobs.company_id;










