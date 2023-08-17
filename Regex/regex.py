from Packages.packages import *

def account(accnt_no) :
    if re.match(r'^\d{19}$',str(accnt_no)): 
        return True
    else :
        return False