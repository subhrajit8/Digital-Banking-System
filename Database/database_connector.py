from Packages.packages import *

def connect_database():
    my_db = mysql.connector.connect(user='root', password='nopasword', host='localhost', database='bank')
    # mycursor = my_db.cursor()

    # mycursor.execute("SELECT * FROM details")
    # res = mycursor.fetchall()

    # for row in res:
    #     print(row)

    return my_db