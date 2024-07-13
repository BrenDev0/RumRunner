import os 
from models.database import Database

def system_scan():
    db = Database()
    exefiles = []
    for root, dirs, files in os.walk('C:/'):
        print("scan start")
        for filename in files:
                exefiles.append({
                    'file_name': filename,
                    'file_path': root + "/" + filename
                }) 
    print('scan finished')  

system_scan()             