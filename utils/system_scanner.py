import os 
from models.database import Database

def system_scan():
    db = Database()
    exefiles = []
    print('scanning...')
    for root, dirs, files in os.walk('C:/'):
        for filename in files:
            if filename.endswith('.exe') or filename.endswith('.txt'):
                file = [
                     filename,
                     root + '/' + filename
                ]
                db.insert(file)
                
    print('scan finished')  

             