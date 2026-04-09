# dbCode.py
# Author: Munkhorgil Tumurchudur
# Helper functions for database connection and queries

import pymysql
import creds

def get_conn():
    """Returns a connection to the MySQL RDS instance."""
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
    )
    return conn

def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    cur = get_conn().cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

def get_top_movies():
    query = "SELECT * FROM movie ORDER BY vote_average DESC LIMIT 10"
    return execute_query(query)

def get_genres():
    query = "select * from genre"
    return execute_query(query) 

def get_movies_by_genre(genre_id):
    query = """
        select m.title, m.vote_average, m.release_date, g.genre_name
        from movie m
        join movie_genres mg ON m.movie_id = mg.movie_id
        join genre g ON mg.genre_id = g.genre_id
        where g.genre_id = %s
        order by m.vote_average desc
        limit 10
    """
    return execute_query(query, (genre_id,))

def get_all_movies():
    query = "SELECT title FROM movie ORDER BY title"
    return execute_query(query)

# DynamoDB code


import boto3

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id=creds.aws_access_key_id,
    aws_secret_access_key=creds.aws_secret_access_key
)
table = dynamodb.Table('MovieReviews')

def create_review(movie_title, username, rating, review_text):
    review_id = username + "_" + movie_title
    table.put_item(Item={
        'review_id': review_id,
        'movie_title': movie_title,
        'username': username,
        'rating': rating,
        'review_text': review_text
    })

def print_all_reviews():
    response = table.scan()
    items = response.get('Items', [])
    if not items:
        print("No reviews found.")
    else:
        print(f"Found {len(items)} review(s)")
    return items

def get_review(review_id):
    response = table.get_item(Key={'review_id': review_id})
    return response.get('Item')

def update_review(review_id, rating, review_text):
    table.update_item(
        Key={'review_id': review_id},
        UpdateExpression="SET rating = :r, review_text = :t",
        ExpressionAttributeValues={
            ':r': rating,
            ':t': review_text
        }
    )
    print("Updated review:", review_id)

def delete_review(review_id):
    try:
        table.delete_item(Key={'review_id': review_id})
        print("Deleted review:", review_id)
    except Exception as e:
        print("Error in deleting review:", e)