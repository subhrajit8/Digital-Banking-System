import numpy as np
import json
import sys
sys.path.insert(1,'C://Users//jsubh//OneDrive//Documents//Wallet//AccountStatus')
import account_status
def check_balance(my_db,accnt_no,entered_Mob):
    mycursor = my_db.cursor()
    result = account_status.check_status(my_db,accnt_no,entered_Mob)
    if result == True :
        PIN = np.random.randint(1000,9999)
        print(PIN)
        entered_PIN = int(input("Enter the PIN : "))
        if PIN == entered_PIN :
            query3 = "SELECT balance FROM details WHERE accnt_no = %s"
            values = (accnt_no,)
            mycursor.execute(query3, values)
            balance = mycursor.fetchone()[0]  
            return json.dumps({"Balance":balance})    
        else : 
            return "Incorrect PIN"
    else :
        return result  