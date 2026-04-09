# [Movie Favorites & Reviews]

**CS178: Cloud and Database Systems — Project #1**
**Author:** [Munkh-Orgil Tumurchudur]
**GitHub:** [orgilemu]

---

## Overview

A movie browsing and review website. Users can explore top rated movies by genre, and write personal reviews.

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for [describe what you stored]
- **AWS DynamoDB** — non-relational database for [describe what you stored]
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds_sample.py      # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html        # Landing page with all time top 10 movies
│   ├── add_review.html  # form to add new review
│   ├── edit_review.html # form to edit old review
│   ├── genres.html      # browse movies by genre
│   ├── reviews.html     # view all reviews with edit and delete options
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/orgilemu/cs178-flask-app.git
   cd cs178-flask-app
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://ec2-3-227-243-227.compute-1.amazonaws.com:8080
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)

<!-- this project uses "movies" database from https://analytics.drake.edu/~urness/CS178/movies.sql. i mainly used tables from "movie", "genre" and "movie_genres" and used JOIN query to connect all three tables to find the top movies-->

**Example:**

- `[movie]` — stores all movie data informations; primary key is `[movie_id]`
- `[genre]` — stores all genre names; primary key links to `[genre_id]`
- `[movie_genre]` — stores movie_id and genre_id; foreign key links to `[movie_id, genre_id]`

The JOIN query used in this project: <!-- describe it in plain English -->

### DynamoDB

<!-- Describe your DynamoDB table. What is the partition key? What attributes does each item have? How does it connect to the rest of the app? -->

- **Table name:** `[MovieReviews]`
- **Partition key:** `[review_id]`
- **Used for:** [stores users movie reviews. each review is identified by combination of the username and movie title.]

---

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Create    | `/[create_review]` | [sumbits a new movie review] |
| Read      | `/[print_all_reviews]` | [displays all reviews from dynamoDB] |
| Update    | `/[update_review]` | [edits the rating ad text of their review] |
| Delete    | `/[delete_review]` | [removes a review from dynamoDB] |

---

## Challenges and Insights

The hardest part was writing the html file, because I have no background of html, but with the help of chatgpt I learned a lot about html, another challenging part was setting up new VPC and RDS, needed to go back multiple times through old lab lessons.

---

## AI Assistance

I used Chatgpt to help with writing html and debugging my flaskapp.
