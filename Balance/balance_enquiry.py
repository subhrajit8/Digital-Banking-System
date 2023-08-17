from Packages.packages import *
from OTPGeneration.generate_otp import *
from Database.database_connector import *

def check_balance(accnt_no):
        
        db = connect_database()
        cursor = db.cursor()
        PIN = generate_pin()
        entered_PIN = int(input("Enter the PIN : "))
        if PIN == entered_PIN :
            query = "SELECT balance FROM details WHERE accnt_no = %s"
            values = (accnt_no,)
            cursor.execute(query, values)
            balance = cursor.fetchone()[0]  
            return json.dumps({"Balance":balance})    
        else : 
            return "Incorrect PIN"
