import sys
sys.path.insert(1,'C://Users//jsubh//OneDrive//Documents//Wallet')
import regex
def verify_accnt(my_db,accnt_no):
    match = regex.account(accnt_no)
    if match : 
        mycursor = my_db.cursor()
        query = "SELECT accnt_no FROM details WHERE accnt_no = %s"
        values = (accnt_no,)
        mycursor.execute(query,values)
        a = mycursor.fetchone()
        if a is None :
            return False
        else :
            return True
    else : 
        return False