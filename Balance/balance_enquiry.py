from Packages.packages import *
# import sys
# sys.path.insert(1,'C://Users//jsubh//OneDrive//Documents//Wallet//AccountStatus')
from OTPGeneration.generate_otp import *

def check_balance(cursor, accnt_no):
        PIN = generate_pin(accnt_no, cursor)
        entered_PIN = int(input("Enter the PIN : "))
        if PIN == entered_PIN :
            query = "SELECT balance FROM details WHERE accnt_no = %s"
            values = (accnt_no,)
            cursor.execute(query, values)
            balance = cursor.fetchone()[0]  
            return json.dumps({"Balance":balance})    
        else : 
            return "Incorrect PIN"
