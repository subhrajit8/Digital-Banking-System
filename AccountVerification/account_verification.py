from Regex.regex import *

def verify_accnt_no(accnt_no, cursor):

    match = account(accnt_no)

    if match : 
        # mycursor = my_db.cursor()
        query = "SELECT accnt_no FROM details WHERE accnt_no = %s"
        values = (accnt_no,)
        cursor.execute(query,values)
        a = cursor.fetchone()
        if a is None :
            return False
        else :
            return True
    else : 
        return False