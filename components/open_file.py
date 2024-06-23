import os


def find_files(file):
    for root, dirs, files in os.walk('C:/Program Files/', topdown=True):
        for fname in files:
            if fname == file + ".exe":
                os.startfile(root + "/" + fname)
               

  