from Packages.packages import *
from Database.database_connector import *
from AccountStatus.account_status import *
from AccountVerification.account_verification import *
from Balance.balance_enquiry import *
from CashDeposit.cash_deposit import *
from CashWithdrawal.cash_withdrawal import *

def balance_check(accnt_no):

    db = connect_database()
    cursor = db.cursor()
    # cursor.execute("SELECT * FROM details")
    # res = cursor.fetchall()

    # for row in res:
    #     print(row)

    if verify_accnt_no(accnt_no, cursor):
        entered_Mobile = int(input("Enter the Mobile Number : "))
        query = "SELECT Mob FROM details WHERE accnt_no = %s"
        values = (accnt_no,)
        cursor.execute(query,values)
        Mobile = cursor.fetchone()[0]
        if Mobile == entered_Mobile:
            if check_status(accnt_no):
                return check_balance(accnt_no)
            else:
                return "Account Inactive."
        else:
            return "Incorrect Mobile Number."
    else:
        return "Invalid Account Number."
