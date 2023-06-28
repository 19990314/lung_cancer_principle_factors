from patient_info import *

expression_root_dir = tcga_path + "/gene_expression_and_mutation/"
assmbled_info = get_assembled_table()



def encode_expression(exp_dir):
    # read expression data
    expression_table = pd.read_csv(exp_dir, sep="\t")
    print(exp_dir)

def process_records(patient):

    # get expression file path
    exp_dir = expression_root_dir + patient["RNA_Seq"]



# for every patient
for index, patient in assmbled_info.iterrows():
    encoded = process_records(patient)
    print(assmbled_info)