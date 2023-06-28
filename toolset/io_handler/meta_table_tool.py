# ------------------------------------------------------------------------
# This module handles I/O functions for files from TCGA_LUAD dataset.
#
# Author: Shuting Chen
# Date Created: 11/25/2022
# Date Last Modified: 11/27/2022
# ------------------------------------------------------------------------

__all__ = ['load_patients_overview', 'patients_overview_to_tsv', 'uuid_connect', 'json_parser',
           'tcga_path', 'metadata_filename', 'patients_filename']

import pandas as pd
import os
import json
import toolset.io_handler.file_error as fe
from Bio import AlignIO
import os

# sync current path
current_dir = os.getcwd()
proj_root = os.path.abspath(os.path.join(current_dir, "../.."))
tcga_path = proj_root + "/tcga_db/"

# glob variables for tcga_db path
metadata_filename = "metadata.cart.2022-11-26.json"
patients_filename = "case_overview/clinical_info.tsv"


def load_patients_overview(path, prefix):
    """
        Concatenate sub-files of patients data into one
    """
    subfiles = []
    if path[-1] != "/":
        path += "/"
    # iterate through sub-files
    for path, currentDirectory, files in os.walk(path):
        for file in files:
            if file.startswith(prefix):
                # save the sub-file for concat
                subfiles.append(pd.read_table(path + file))

    return pd.concat(subfiles)


def patients_overview_to_tsv(prefix):
    """
        output the overview file of patients to tsv
    """
    # read files
    path = tcga_path + "case_overview/"
    fe.file_exists(path)
    clinical_info = load_patients_overview(path, prefix)
    # clean up columns
    #clinical_info = clinical_info.drop(
    #    columns=['Cart', 'Files', 'Seq', 'Exp', 'CNV', 'Meth', 'Clinical', 'Bio', 'Program', 'Disease Type'])
    clinical_info.to_csv(tcga_path + patients_filename, sep="\t")


def json_parser(file_path):
    """
        read json file and return file content
    """
    # check file path
    fe.file_exists(file_path)
    # open json file
    f = open(file_path)
    f_content = json.load(f)
    f.close()
    return f_content


def uuid_connect():
    """
        connect case uuids to corresponding file uuids and file names of RNA_Seq and WXS file
    """
    # read patients overview
    ov_path = tcga_path + "case_overview/" + patients_filename
    fe.file_exists(ov_path)
    ov_content = pd.read_table(ov_path)

    # read manifest data
    mf_path = tcga_path + metadata_filename
    mf_content = json_parser(mf_path)

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
    with open(tcga_path + "uuid_connections.json", "w") as outfile:
        json.dump(case_holder, outfile)



def get_maf(id, raw_db_path):
    """
        parse maf data for a certain patient by his/her id
    """
    #TODO: MAF file
    uuid_map = json_parser(tcga_path + "uuid_connections.json")
    map_path = raw_db_path + uuid_map[id]['WXS']

    print(uuid_map)


get_maf("TCGA-44-A47A", "/Users/iris/Downloads/gdc_download_20230308_190052.048907/")
