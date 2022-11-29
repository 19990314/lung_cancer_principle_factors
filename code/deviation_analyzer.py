# ------------------------------------------------------------------------
# This module calculates and visualize population deviation for
# different factors from TCGA_LUAD dataset.
#
# Author: Shuting Chen
# Date Created: 11/25/2022
# Date Last Modified: 11/27/2022
# ------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from io_handler import meta_table_tool as io

# glob variable declare
clinical_path = io.db_path + "clinical/"


def clinical_deviations():
    clinical_tb = pd.read_table(clinical_path + "clinical.tsv")

    #dev_inputs = [clinical_tb["age_at_diagnosis"]]
    clinical_tb["age_at_diagnosis"] = pd.to_numeric(clinical_tb["age_at_diagnosis"], errors = "coerce")
    clinical_tb.boxplot(column=['age_at_diagnosis'], grid=False)
    plt.show()


def smoke_deviations():
    pd.read_table(clinical_path + "exposure.tsv")


clinical_deviations()