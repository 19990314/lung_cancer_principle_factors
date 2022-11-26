import pandas as pd
import os
import json
from file_error import *

__all__ = ['load_patients_overview']

db_path = "/Users/iris/Desktop/LCPF/database/"  # glob variable for database path
metadata_filename = "metadata.cart.2022-11-26.json"
patients_filename = "clinical_info.tsv"

def load_patients_overview(path, prefix):
    subfiles = []
    if path[-1] != "/":
        path += "/"
    for path, currentDirectory, files in os.walk(path):
        for file in files:
            if file.startswith(prefix):
                subfiles.append(pd.read_table(path + file))

    return pd.concat(subfiles)


def patients_overview_to_tsv():
    # read files
    path = db_path + "case_overview/"
    clinical_info = load_patients_overview(path, "repository-cases-table")
    # clean up columns
    clinical_info = clinical_info.drop(
        columns=['Cart', 'Files', 'Seq', 'Exp', 'CNV', 'Meth', 'Clinical', 'Bio', 'Program', 'Disease Type'])
    clinical_info.to_csv(path + patients_filename, sep="\t")


def files_overview(path):
    # open json file
    f = open(path)
    f_content = json.load(f)
    f.close()
    return f_content


def uuid_connect():
    # read patients overview
    ov_path = db_path + "case_overview/" + patients_filename
    file_exists(ov_path)
    ov_content = pd.read_table(ov_path)

    # read manifest data
    mf_path = db_path + metadata_filename
    mf_content = files_overview(mf_path)

    # match patients ids to file ids
    case_holder = {}
    for i in ov_content['Case ID']:
        case_holder[i] = {} # hold corresponding file paths for RNA-Seq and WXS
        for j in mf_content:
            if i in j["associated_entities"][0]["entity_submitter_id"]:
                if j['data_type'] == 'Gene Expression Quantification':
                    case_holder[i]['RNA_Seq'] = j['file_id'] + "/" + j['file_name']
                elif j['data_type'] == 'Masked Somatic Mutation':
                    case_holder[i]['WXS'] = j['file_id'] + "/" + j['file_name']

    return case_holder


def output_uuid_connections():
    case_holder = uuid_connect()
    with open(db_path + "uuid_connections.json", "w") as outfile:
        json.dump(case_holder, outfile)



