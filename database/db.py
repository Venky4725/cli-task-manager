import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        database="taskdb",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    )