# Creating database drm

import mysql.connector as mysql

database = mysql.connect(
    host="localhost",
    user="root",
    passwd="password",
)

# prepare a cursor object
cursorObj = database.cursor()

# Create a databe
cursorObj.execute("CREATE DATABASE IF NOT EXISTS drm")

print("All Done!")
