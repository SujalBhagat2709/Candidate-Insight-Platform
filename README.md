# Candidate Insight Platform

## Overview

Candidate Insight Platform is a terminal-based Python application that helps recruiters evaluate, compare, and rank job candidates based on multiple hiring factors.

The platform calculates an Insight Score, generates hiring recommendations, stores candidate records, and provides useful recruitment statistics.

---

## Features

- Add Candidate
- Candidate Insight Score
- Hiring Recommendation
- Candidate Ranking
- Search Candidate
- Remove Candidate
- Platform Statistics
- JSON Storage

---

## Project Structure

candidate-insight-platform/

├── candidate_analysis.py

├── insight_platform.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python insight_platform.py
```

---

## Menu

```
1. Add Candidate
2. View Candidate Insights
3. Search Candidate
4. Remove Candidate
5. Platform Statistics
6. Exit
```

---

## Candidate Evaluation Parameters

- Experience
- Technical Skills
- Projects
- Communication
- Certifications

Each candidate receives an **Insight Score (0–100)** and a hiring recommendation.

---

## Recommendation Logic

| Score | Recommendation |
|-------:|----------------|
| 90 - 100 | Strong Hire |
| 75 - 89 | Hire |
| 60 - 74 | Consider |
| Below 60 | Reject |

---

## Example

Candidate

```
Name

Rahul Patel

Role

Backend Developer

Experience

4 Years

Skills

8

Projects

6

Communication

9

Certifications

3
```

Output

```
Insight Score

91

Recommendation

Strong Hire
```

---

## Generated File

candidates.json

Example

```json
[
    {
        "name": "Rahul Patel",
        "role": "Backend Developer",
        "experience": 4,
        "skills": 8,
        "projects": 6,
        "communication": 9,
        "certifications": 3,
        "score": 91,
        "recommendation": "Strong Hire"
    }
]
```

---

## Platform Statistics

Example

```
Total Candidates : 15

Average Score : 81.6

Highest Score : 98

Lowest Score : 52
```

---

## Future Improvements

- Resume PDF Upload
- Resume Skill Extraction
- Job Description Matching
- ATS Score
- Skill Gap Analysis
- Recruiter Notes
- Candidate Status Tracking
- Interview Scheduling
- Candidate Comparison Dashboard
- CSV Import / Export
- AI-Based Resume Summary
- Email Report Generation

---

## License

MIT License