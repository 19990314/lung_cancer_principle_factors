from io_handler.meta_table_tool import *
import pandas as pd

# assemble the patient info
#patients_overview_to_tsv("repository-cases-table.2023-03-06")


# read patinet basic info
patients_info = pd.read_table(db_path + patients_filename)
uuid_map = json_parser(db_path + "uuid_connections.json")


#patients_info.drop(la)
print(patients_info)