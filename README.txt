Lung Cancer Principle Factors

This README file introduces the pipeline of analyzing the principle factors influencing the pathology of lung cancer cases, in order to build a deep learning network which considers the global features to make clinical decisions, such as prescription and prognosis. Past studies have done great work in this area, whereas the aim of this study is to focus on upgrading the precision and accuracy by comprehensively correlated features, which could explain tumor growth based on hierachical data from multi-omic biomarkers and patients' health records.

Data we used: TCGA LUAD project (https://portal.gdc.cancer.gov/projects/TCGA-LUAD)
Located at: ./database
Number of cases included: 585


Features we expect to consider (draft):
* NC: not completed
./database/clinical/clinical.tsv
Age
Year of birth
Gender
Ethinity
Race
days_to_death (NC)
Stage data: ajcc_pathologic_m, ajcc_pathologic_n, ajcc_pathologic_stage, ajcc_pathologic_t, ajcc_staging_system_edition
Primary diagnosis
prior_malignancy + synchronous_malignancy
prior_treatment
tissue_or_organ_of_origin
treatment_or_therapy: yes/no
treatment_type: specific treatment

./database/clinical/exposure.tsv
alcohol_history	
cigarettes_per_day
pack_years_smoked															years_smoked

./database/nationwidechildrens.org_clinical_drug_luad.txt
bcr_patient_barcode
drug_name
clinical_trail_drug_classification
therapy_type
days_to_drug_therapy_start
therapy_ongoing	days_to_drug_therapy_end
measure_of_response
days_to_stem_cell_transplantation
pharm_regimen
pharm_regimen_other
number_cycles
therapy_type_notes
prescribed_dose_units
total_dose

./database/nationwidechildrens.org_clinical_follow_up_v1.0_luad.txt
bcr_patient_barcode
form_completion_date
vital_status
followup_case_report_form_submission_reason
radiation_therapy
postoperative_rx_tx
days_to_last_followup
primary_therapy_outcome_success	days_to_death
new_tumor_event_after_initial_treatment
person_neoplasm_cancer_status
new_neoplasm_event_type
days_to_new_tumor_event_after_initial_treatment
additional_radiation_therapy
progression_determined_by
additional_pharmaceutical_therapy
additional_surgery_locoregional_procedure
days_to_additional_surgery_locoregional_procedure
additional_surgery_metastatic_procedure
days_to_additional_surgery_metastatic_procedure
followup_treatment_success

./database/nationwidechildrens.org_clinical_patient_luad.txt
Assembled most of features from other previous files

./database/nationwidechildrens.org_clinical_radiation_luad.txt
bcr_patient_barcode
form_completion_date
radiation_type
anatomic_treatment_site	radiation_dosage
days_to_radiation_therapy_start
radiation_treatment_ongoing
days_to_radiation_therapy_end
measure_of_response
regimen_indication
regimen_indication_notes