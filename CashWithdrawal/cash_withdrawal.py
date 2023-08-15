import numpy as np
import sys
sys.path.insert(1,'C://Users//jsubh//OneDrive//Documents//Wallet//AccountStatus')
import account_status
def withdraw_cash(my_db,accnt_no,entered_Mob):
    mycursor = my_db.cursor()
    result = account_status.check_status(my_db,accnt_no,entered_Mob)
    if result == True :
        PIN = np.random.randint(1000,9999)
        print(PIN)
        entered_PIN = int(input("Enter the PIN : "))
        if PIN == entered_PIN :
            query1 = "SELECT balance FROM details WHERE accnt_no = %s"
            values = (accnt_no,)
            mycursor.execute(query1, values)
            balance = mycursor.fetchone()[0]  
            entered_amount = int(input("Enter the amount : "))              
            if balance >= entered_amount : 
                amount_left = balance - entered_amount
                query2 = "UPDATE details SET balance = %s WHERE accnt_no = %s"
                value = (amount_left, accnt_no,)
                mycursor.execute(query2, value)
                my_db.commit()
                return "Transaction Successfull."
            else :
                return "Transaction Failed."
        else : 
            return "Incorrect PIN."
    else :
        return result
    



    #  query1 = "SELECT +balance +"FROM "details" WHERE" accnt_no "="" %s"