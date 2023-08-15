import sys
sys.path.insert(1,'C://Users//jsubh//OneDrive//Documents//Wallet//AccountVerification')
import account_verification

def check_status(my_db,accnt_no,entered_Mob):
    result = account_verification.verify_accnt(my_db,accnt_no)
    if result :
        mycursor = my_db.cursor()
        query1 = "SELECT Mob FROM details WHERE accnt_no = %s"
        values = (accnt_no,)
        mycursor.execute(query1,values)
        user_Mob = mycursor.fetchone()[0]
        if user_Mob == entered_Mob : 
            query2 = "SELECT active FROM details WHERE accnt_no = %s"
            mycursor.execute(query2, values) 
            status = mycursor.fetchone()[0]  
            if status == 1 :                
                return True
            else : 
                return "Account Inactive."
        else : 
            return "Incorrect Mobile Number."
    else :
        return "Invalid Account."
