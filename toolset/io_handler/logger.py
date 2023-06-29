from os.path import exists


def check_path_with_log(path):
    """
        check if file exists
        return 2 elements: a flag, and a message
    """
    if exists(path):
        return True, "VALID FILE: " + path
    else:
        return False, "INVALID FILE: " + path
