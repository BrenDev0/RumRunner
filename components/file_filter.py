import os 

def exe_files(string):
    exefiles = []
    for root, dirs, files in os.walk('C:/'):
        for filename in files:
            if string in filename and filename.endswith('.exe'):
                exefiles.append({
                    'file_name': filename,
                    'file_path': root + "/" + filename
                }) 
    return exe_files            