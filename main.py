import mysql.connector
import json
import AccountVerification.account_verification
import Balance.balance_enquiry
import CashWithdrawal.cash_withdrawal
import CashDeposit.cash_deposit
import AccountStatus.account_status
from flask import Flask, request

app = Flask(__name__)

my_db = mysql.connector.connect(user='root', password='nopasword', host='localhost', database='bank')
mycursor = my_db.cursor()

# mycursor.execute("SELECT * FROM details")
# res = mycursor.fetchall()

# for row in res:
#     print(row)

@app.route('/account_verification', methods=['GET'])
def check_account_route():
    data = request.get_json()
    result = AccountVerification.account_verification.verify_accnt(my_db,data['accnt_no'])
    if result :
        return "Valid Account."
    else :
        return "Invalid Account."
        
@app.route('/account_status', methods=['GET','PUT'])
def check_status_route():
    data = request.get_json()
    result = AccountStatus.account_status.check_status(my_db,data['accnt_no'],data['entered_Mob'])
    if result == True :
        return "Account Active."
    else :
        return result

@app.route('/balance_enquiry', methods=['GET'])
def check_balance_route():
    data = request.get_json()
    result = Balance.balance_enquiry.check_balance(my_db,data['accnt_no'],data['entered_Mob'])
    return result

@app.route('/cash_withdrawal', methods=['GET','PUT'])
def withdraw_cash_route():
    data = request.get_json()
    res = CashWithdrawal.cash_withdrawal.withdraw_cash(my_db,data['accnt_no'],data['entered_Mob'])
    return res
    
@app.route('/deposit', methods=['GET','POST','PUT'])
def deposit_route():
    data = request.get_json()
    res = CashDeposit.cash_deposit.deposit(my_db,data['accnt_no'],data['entered_Mob'])
    return res

if __name__ == '__main__':
    app.run(debug=True)