from Packages.packages import *
# import sys
# sys.path.insert(1,'C://Users//jsubh//OneDrive//Documents//Wallet//AccountStatus')
from AccountStatus.account_status import *
def deposit(my_db,accnt_no,entered_Mob):
    mycursor = my_db.cursor()
    result = check_status(my_db,accnt_no,entered_Mob)
    if result == True :
        PIN = np.random.randint(1000,9999)
        print(PIN)
        entered_PIN = int(input("Enter the PIN : "))
        if PIN == entered_PIN :
            query3 = "SELECT balance FROM details WHERE accnt_no = %s"
            values = (accnt_no,)
            mycursor.execute(query3, values)
            balance = mycursor.fetchone()[0]  
            diposited_amount = int(input("Enter deposit amount : "))               
            new_balance = balance + diposited_amount
            query4 = "UPDATE details SET balance = %s WHERE accnt_no = %s"
            value = (new_balance, accnt_no,)
            mycursor.execute(query4, value)
            my_db.commit()
            return "Cash Deposited Successfully."       
        else : 
            return "Incorrect PIN."
    else :
        return result