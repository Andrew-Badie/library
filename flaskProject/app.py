from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)


def get_db_connection():
    # Use DATABASE_URL from environment variables for production
    database_url = os.getenv('DATABASE_URL')

    # Parse the DATABASE_URL to extract connection details
    if database_url:
        connection = mysql.connector.connect(
            host=database_url.split('@')[1].split('/')[0].split(':')[0],
            user=database_url.split('//')[1].split(':')[0],
            password=database_url.split(':')[2].split('@')[0],
            database=database_url.split('/')[1]
        )
    else:
        # Use local connection details for development
        connection = mysql.connector.connect(
            host="localhost",
            user="andrewbadie",
            password="Ab1063426.",
            database="library1"
        )
    return connection


@app.route('/')
def index():
    return "Library Management System"


@app.route('/books', methods=['GET'])
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)