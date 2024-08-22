import requests, pymysql

MOVIE = input("Enter the name of the film: ")

API_KEY = "5d9df2b8"

url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE}"


connection = pymysql.connect(   
    host = ...,
    user = ...,
    password= ...,
    db=...,
    port = ...,
    charset = 'utf8mb4', 
    cursorclass= pymysql.cursors.DictCursor 
)
