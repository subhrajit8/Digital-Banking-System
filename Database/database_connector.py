from Packages.packages import *

def connect_database():
    my_db = mysql.connector.connect(user='root', password='nopasword', host='localhost', database='bank')
    mycursor = my_db.cursor()
    return mycursor