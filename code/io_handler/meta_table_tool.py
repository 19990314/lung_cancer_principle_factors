# ------------------------------------------------------------------------
# This module handles I/O functions for files from TCGA_LUAD dataset.
#
# Author: Shuting Chen
# Date Created: 11/25/2022
# Date Last Modified: 11/27/2022
# ------------------------------------------------------------------------

__all__ = ['load_patients_overview', 'patients_overview_to_tsv', 'uuid_connect', 'files_overview',
           'db_path', 'metadata_filename', 'patients_filename']

import pandas as pd
import os
import json
from io_handler import file_error as fe

# glob variable for database path
db_path = "/Users/iris/Desktop/LCPF/database/"
metadata_filename = "metadata.cart.2022-11-26.json"
patients_filename = "clinical_info.tsv"


def load_patients_overview(prefix):
    """
        Concatenate sub-files of patients data into one
    """
    subfiles = []
    path = db_path + "case_overview/"
    if path[-1] != "/":
        path += "/"
    # iterate through sub-files
    for path, currentDirectory, files in os.walk(path):
        for file in files:
            if file.startswith(prefix):
                # save the sub-file for concat
                subfiles.append(pd.read_table(path + file))

    return pd.concat(subfiles)


def patients_overview_to_tsv():
    """
        output the overview file of patients to tsv
    """
    # read files
    path = db_path + "case_overview/"
    fe.file_exists(path)
    clinical_info = load_patients_overview(path, "repository-cases-table")
    # clean up columns
    clinical_info = clinical_info.drop(
        columns=['Cart', 'Files', 'Seq', 'Exp', 'CNV', 'Meth', 'Clinical', 'Bio', 'Program', 'Disease Type'])
    clinical_info.to_csv(path + patients_filename, sep="\t")


def files_overview(file_path):
    """
        read json file and return file content
    """
    # open json file
    fe.file_exists(file_path)
    f = open(file_path)
    f_content = json.load(f)
    f.close()
    return f_content


def uuid_connect():
    """
        connect case uuids to corresponding file uuids and file names of RNA_Seq and WXS file
    """
    # read patients overview
    ov_path = db_path + "case_overview/" + patients_filename
    fe.file_exists(ov_path)
    ov_content = pd.read_table(ov_path)

    # read manifest data
    mf_path = db_path + metadata_filename
    mf_content = files_overview(mf_path)

    # match patients ids to file ids
    case_holder = {}
    for i in ov_content['Case ID']:
        case_holder[i] = {}  # hold corresponding file paths for RNA-Seq and WXS
        for j in mf_content:
            if i in j["associated_entities"][0]["entity_submitter_id"]:
                # check data type: RNA-Seq or WXS
                if j['data_type'] == 'Gene Expression Quantification':
                    case_holder[i]['RNA_Seq'] = j['file_id'] + "/" + j['file_name']
                elif j['data_type'] == 'Masked Somatic Mutation':
                    case_holder[i]['WXS'] = j['file_id'] + "/" + j['file_name']

    return case_holder


def output_uuid_connections():
    """
        output uuid connections from uuid_connect() into a json file under db_path
    """
    case_holder = uuid_connect()
    with open(db_path + "uuid_connections.json", "w") as outfile:
        json.dump(case_holder, outfile)
