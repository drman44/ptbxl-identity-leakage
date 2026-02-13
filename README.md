This repository contains the analysis code accompanying our study on patient identity signals in the PTB-XL electrocardiography dataset.

The work investigates whether ECG recordings contain reproducible patient-specific structure that may influence artificial intelligence benchmarking strategies.

Due to licensing restrictions, the PTB-XL dataset is not redistributed. Researchers can obtain access via PhysioNet and reproduce all experiments using the scripts provided here.
# PTB-XL Methodological Audit: Leakage, Splits & Lead-Sensitivity

This repository contains a comprehensive audit and sensitivity analysis of the [PTB-XL ECG Dataset](https://physionet.org/content/ptb-xl/). The project focuses on identifying methodological pitfalls in standard benchmarks, specifically patient identity leakage across splits and the impact of reduced lead sets on model performance.

## 🎯 Project Scope

1.  **Patient Identity Leakage Audit:**
    * Investigation of "overlap" between training, validation, and test splits based on `patient_id`.
    * Quantification of samples that violate strict subject-wise splitting.
    * Correction proposal for strict disjoint splitting.

2.  **Split Integrity & Reproducibility:**
    * Verification of the standard `stratified_fold` provided in the original dataset.
    * Audit of distribution consistency (label balance) across re-generated splits.

3.  **Lead-Set Sensitivity Analysis:**
    * Performance benchmarking of classifiers using varying lead configurations:
        * Standard 12-Lead
        * Limb Leads (I, II, III, aVR, aVL, aVF)
        * Single Lead (Lead I or II)
    * Analysis of performance degradation/robustness when reducing lead dimensionality.

## 📂 Data

* **Source:** [PTB-XL: A Large Publicly Available Electrocardiography Dataset](https://physionet.org/content/ptb-xl/) (PhysioNet)
* **Version:** 1.0.3 (or relevant version used)
* **Access:** Ensure you have the necessary credentials/license approval from PhysioNet to download and use the dataset.
* **Structure:**
    * Raw waveforms: `records100/` or `records500/`
    * Metadata: `ptbxl_database.csv`

## 🚀 How to Run

### Requirements
Ensure you have Python 3.8+ and the necessary libraries installed. 

```bash
pip install -r requirements.txt
