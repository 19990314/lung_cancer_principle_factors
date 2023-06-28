# ------------------------------------------------------------------------
# This module handles I/O error messages
#
# Author: Shuting Chen
# Date Created: 11/25/2022
# Date Last Modified: 11/27/2022
# ------------------------------------------------------------------------

from os.path import exists


def file_exists(path):
    """
        check if file exists
    """
    if not exists(path):
        print("Please update your tcga_db, something is missing:" + path)
        exit(1)
