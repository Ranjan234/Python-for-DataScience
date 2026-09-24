# 🏥 Healthcare Data Analysis – Case Study

A data analysis project exploring patient demographics, medical conditions, billing, and insurance trends using a real-world healthcare dataset.

## 📌 Project Overview

This project analyzes healthcare records to uncover insights about patient age distribution, common medical conditions, treatment costs over time, and insurance provider distribution. The goal is to practice data cleaning, exploratory data analysis (EDA), and data visualization using Python.

## 📂 Dataset

- **Source:** [Healthcare Dataset – Kaggle](https://www.kaggle.com/datasets/prasad22/healthcare-dataset)
- **Description:** Each row represents a patient record containing admission details and healthcare services provided.

**Key columns:**

| Column | Description |
|---|---|
| Name | Patient name |
| Age | Patient's age at admission |
| Gender | Male / Female |
| Blood Type | e.g. A+, O- |
| Medical Condition | Diagnosis (Diabetes, Hypertension, Asthma, etc.) |
| Date of Admission | Admission date |
| Doctor | Attending doctor |
| Hospital | Healthcare facility |
| Insurance Provider | Aetna, Blue Cross, Cigna, UnitedHealthcare, Medicare |
| Billing Amount | Amount billed for services |
| Room Number | Room assigned |
| Admission Type | Emergency, Elective, or Urgent |
| Discharge Date | Date of discharge |
| Medication | Prescribed medication |
| Test Results | Normal, Abnormal, or Inconclusive |

## 🧹 Data Cleaning

- Removed duplicate records
- Standardized patient name formatting
- Fixed negative values in `Billing Amount`
- Converted `Date of Admission` and `Discharge Date` to datetime format
- Engineered a new `Days_of_Stay` feature (discharge date − admission date)

## 📊 Exploratory Analysis & Visualizations

- **Age Distribution of Patients** – histogram showing patient counts across age groups
- **Patients by Medical Condition** – bar chart comparing condition frequency
- **Average Treatment Cost Over Time (Monthly)** – line chart of billing trends
- **Age vs Treatment Cost** – scatter plot examining cost variation by age
- **Patients Share by Insurance Provider** – pie chart of provider distribution

Additional analysis included:
- Average age and average billing cost for senior patients (60+)
- Monthly count of emergency admissions
- Identifying high-cost patients (top 10% by billing amount)
- Identifying priority cases (Emergency admissions with Abnormal test results)

## 🛠️ Tools & Libraries

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## 📁 Repository Structure

```
├── Healthcare_Analysis_Case_Study.ipynb   # Main analysis notebook
├── About_the_Data.docx                    # Dataset column descriptions
├── Age_distribution_of_patients.png
├── Avg_treatment_cost_over_time.png
├── Avg_vs_treatment_cost.png
├── Patients_by_medical_condition.png
├── patients_share_by_insurance_provider.png
└── README.md
```

## 🚀 How to Run

1. Clone this repository
   ```bash
   git clone https://github.com/your-username/healthcare-data-analysis.git
   cd healthcare-data-analysis
   ```
2. Install dependencies
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. Launch the notebook
   ```bash
   jupyter notebook Healthcare_Analysis_Case_Study.ipynb
   ```

## 📈 Key Insights

- Patient ages are fairly evenly distributed between 20 and 85 years
- The six tracked medical conditions (Arthritis, Diabetes, Hypertension, Obesity, Cancer, Asthma) occur in roughly equal numbers
- Average monthly treatment cost stays relatively stable, ranging between ~$25,000–$26,500
- No strong correlation exists between patient age and billing amount
- Patients are nearly evenly split across the five insurance providers (~19–20% each)

## 🙋‍♂️ Author

Feel free to connect or reach out with feedback and suggestions!

## 📄 License

This project is open source and available for learning purposes.
