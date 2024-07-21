import mysql.connector
import random

#Implement  a working question bank

db = mysql.connector.connect( #connects to MySQL Server for data to be accessed
    host = "localhost",
    user = "root",
    password = "xxxxxxxxx"
)

mycursor = db.cursor()
mycursor.execute("Use discordbot") #connects to database

def question(anime):
    #pick = anime.lstrip('!') #fix this line
    num = randomNum() - 1

    sql = "SELECT * FROM cote LIMIT 1 OFFSET %s" #query statement

    mycursor.execute(sql, (num,))

    results = mycursor.fetchall()

    return num, results

#grabs the correct picture to display
def picture(anime):

    sql = "Select picture from pictures where anime = 'cote' "
    
    mycursor.execute(sql)

    results = mycursor.fetchall()

    return results


#gets random num between one and 15
def randomNum():

    num = random.randint(1,15)
    return num


