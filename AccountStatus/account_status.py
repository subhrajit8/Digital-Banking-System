from Packages.packages import *
from Database.database_connector import *

def check_status(accnt_no):

            db = connect_database()
            cursor = db.cursor()
            query = "SELECT active FROM details WHERE accnt_no = %s"
            values = (accnt_no,)
            cursor.execute(query, values) 
            status = cursor.fetchone()[0]  
            if status == 1 :                
                return True
            else : 
                return False
