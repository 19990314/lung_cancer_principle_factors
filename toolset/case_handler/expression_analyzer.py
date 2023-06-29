from patient_info import *
from toolset.io_handler.file_error import *


def encode_expression(exp_dir):
    # read expression data
    expression_table = pd.read_csv(exp_dir, sep="\t")
    print(exp_dir)


def process_row(patient):
    # get basic info
    print(patient)

    # get expression file path
    exp_dir = expression_root_dir + patient["RNA_Seq"]
    exist_flag, message = check_path_with_log(path = exp_dir)
    print(message) # log later

    # get content
    if exist_flag:
        expression_df = pd.read_csv(exp_dir, skiprows=1)
        expression_df.head()
        print(expression_df)

    return expression_df


# main
expression_root_dir = tcga_path + "/gene_expression_and_mutation/"
assmbled_info = get_assembled_table()

# for every patient
for index, patient in assmbled_info[0:1].iterrows():
    encoded = process_row(patient)