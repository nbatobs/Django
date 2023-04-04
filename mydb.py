import mysql.connector

database = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd ='Oluwatobi09'

)

#prepare cursor object

cursorObject = database.cursor()

#create database
cursorObject.execute('CREATE DATABASE Elders')
print('all done!')