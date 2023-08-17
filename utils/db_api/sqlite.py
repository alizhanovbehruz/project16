import sqlite3


def sendex(command):
    mydb = sqlite3.connect("db_all.db")
    mycursor = mydb.cursor()

    mycursor.execute(command)
    res = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return res

