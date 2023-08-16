# import sys
# sys.path.insert(1,'C://Users//jsubh//OneDrive//Documents//Wallet//AccountVerification')

def check_status(cursor,accnt_no):

            query = "SELECT active FROM details WHERE accnt_no = %s"
            values = accnt_no
            cursor.execute(query, values) 
            status = cursor.fetchone()[0]  
            if status == 1 :                
                return True
            else : 
                return False
