from flask import Blueprint
from Packages.packages import *
import AccountVerification.account_verification
import Balance.balance_enquiry
import CashWithdrawal.cash_withdrawal
import CashDeposit.cash_deposit
import AccountStatus.account_status
from workflow import *

rout = Blueprint("route",__name__)

# @rout.route('/account_verification', methods=['GET'])
# def check_account_route():
#     data = request.get_json()
#     result = AccountVerification.account_verification.verify_accnt(cursor,data['accnt_no'])
#     if result :
#         return "Valid Account."
#     else :
#         return "Invalid Account."
        
# @rout.route('/account_status', methods=['GET','PUT'])
# def check_status_route():
#     data = request.get_json()
#     result = AccountStatus.account_status.check_status(cursor,data['accnt_no'],data['entered_Mob'])
#     if result == True :
#         return "Account Active."
#     else :
#         return result

@rout.route('/balance_enquiry', methods=['GET'])
def balance_enquiry():
    data = request.get_json()
    return (balance_check(data['accnt_no']))

# def check_balance_route():
#     data = request.get_json()
#     result = Balance.balance_enquiry.check_balance(cursor,data['accnt_no'],data['entered_Mob'])
#     return result

@rout.route('/cash_withdrawal', methods=['GET','PUT'])
def withdraw_cash_route():
    data = request.get_json()
    res = CashWithdrawal.cash_withdrawal.withdraw_cash(cursor,data['accnt_no'],data['entered_Mob'])
    return res
    
@rout.route('/deposit', methods=['GET','POST','PUT'])
def deposit_route():
    data = request.get_json()
    res = CashDeposit.cash_deposit.deposit(cursor,data['accnt_no'],data['entered_Mob'])
    return res
