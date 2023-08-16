from Packages.packages import *

def account(accnt_no) :
    match = re.match("^[0-9][0-9]{18}$",str(accnt_no)) 
    if match : 
        return True
    else :
        return False