from toolset.io_handler.meta_table_tool import *
import pandas as pd

# assemble the patient info
# patients_overview_to_tsv("repository-cases-table.2023-03-06")

# read patient basic info
patients_info = pd.read_table(tcga_path + patients_filename)
uuid_map = pd.read_json(tcga_path + "uuid_connections.json", orient="index")
uuid_map.reset_index(inplace=True)
uuid_map = uuid_map.rename(columns = {'index':'Case ID'})

# assemble all the infos
asembled = pd.merge(patients_info, uuid_map, left_on='Case ID', right_on='Case ID', how="outer")

# patients_info.drop(la)
asembled.to_csv(tcga_path + "final_assemble.csv")
print(patients_info)
