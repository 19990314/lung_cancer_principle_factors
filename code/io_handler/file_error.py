from os.path import exists


def file_exists(path):
    if not exists(path):
        print("Please update your database, something is missing:" + path)
        exit(1)
