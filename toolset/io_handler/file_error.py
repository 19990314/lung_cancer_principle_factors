# ------------------------------------------------------------------------
# This module handles I/O error messages
#
# Author: Shuting Chen
# Date Created: 11/25/2022
# Date Last Modified: 11/27/2022
# ------------------------------------------------------------------------

from os.path import exists

__all__ = ['file_exists', 'check_path_with_log']


def file_exists(path):
    """
        check if file exists
    """
    if not exists(path):
        print("Please update your tcga_db, something is missing:" + path)
        exit(1)


def check_path_with_log(path):
    """
        check if file exists
        return 2 elements: a flag, and a message
    """
    if exists(path):
        return True, "VALID FILE: " + path
    else:
        return False, "INVALID FILE: " + path
