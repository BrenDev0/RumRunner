import os 

def list_files(string):
    files = [ f for f in os.listdir("C:/Program Files") if string in f]
    print(files)


