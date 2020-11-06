import psycopg2
import os

connection = psycopg2.connect(
    database="library_api",
    user="postgres",
    password="testing1",
    host="3.87.111.196"
    
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()