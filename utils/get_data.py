from models.database import Database

def get_Data(string):
    db = Database()
    
    files = db.list_files(string)

    return files
