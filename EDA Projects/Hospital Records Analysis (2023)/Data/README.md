# Hospital Records Analysis – 2023

Exploratory data analysis of one year (Jan–Dec 2023) of hospital operations: patients, appointments, doctors, treatments and billing. Five relational tables are merged into one analysis table and explored with Python (pandas, matplotlib, seaborn, scipy).

## Dataset

| Table | Rows | Key columns |
|---|---|---|
| `patients` | 50 | patient_id, gender, date_of_birth, insurance_provider |
| `doctors` | 10 | doctor_id, specialization, hospital_branch, years_experience |
| `appointments` | 200 | appointment_id, patient_id, doctor_id, date/time, reason, status |
| `treatments` | 200 | treatment_id, appointment_id, treatment_type, cost |
| `billing` | 200 | bill_id, treatment_id, amount, payment_method, payment_status |

Each appointment has exactly one treatment and one bill, so the merged table has 200 rows (verified after every join).

## Method

1. Load the five CSVs and merge them (`appointments → patients → doctors → treatments → billing`), validating key uniqueness and row counts at each step.
2. Clean: parse dates and times, label gender, build patient and doctor names, drop direct contact details.
3. Answer 17 business questions across patients, appointments, doctors, treatments and billing.
4. Test whether the differences are bigger than chance (chi-square, n = 200 is small).

## Key findings

**Patients**
- 50 patients are registered; 48 had at least one appointment. About 62% of registered patients are male (31 of 50), and 65% of appointments are for male patients.
- Patients are aged 17–73 at the time of visit; the largest age band is 25–34 (roughly a quarter of patients).
- MedCare Plus is the most common insurer (42% of appointments), followed by WellnessCorp (29%), PulseSecure (18%) and HealthIndia (11%).

**Appointments**
- Only **23% of appointments are Completed** (46 of 200). Another 26% are no-shows and 25.5% are cancelled, so about **51.5% of booked slots were lost**. The remaining 25.5% still have the status "Scheduled" even though they are dated in 2023.
- April is the busiest month (25 appointments), September the quietest (11). Month-to-month differences are **not statistically significant** (p = 0.54), so treat this as a pattern, not proven seasonality.
- Appointment volume per doctor ranges from 29 (Sarah Taylor) to 13 (Robert Davis), also within what chance would produce (p = 0.22).

**Doctors, specialisations and branches**
- Pediatrics has the most appointments (98, 49%), then Dermatology (70, 35%) and Oncology (32, 16%). Per doctor, however, **Dermatology carries the heaviest load** (23.3 appointments per doctor vs 19.6 for Pediatrics and 16.0 for Oncology).
- Central Hospital has the most appointments (84, 42%), but it also has 4 of the 10 doctors. Per doctor, the three branches are close (21.0 Central, 20.7 Eastside, 18.0 Westside); the branch gap disappears once doctor headcount is taken into account (p = 0.65).

**Treatments and billing** *(currency not specified in the data)*
- Treatment mix is balanced: Chemotherapy 49, X-Ray 41, ECG 38, MRI 36, Physiotherapy 36. The differences are not significant (p = 0.57).
- Average treatment cost is **2,756.25** (median 2,828.17). MRI is the most expensive at 3,224.95 on average; ECG is the cheapest at 2,532.22. Only MRI stands clearly above the overall average.
- **Total billed: 551,249.85.** This is the amount *billed*, not collected, and it includes bills attached to cancelled, no-show and scheduled appointments.
- Only **32% of bills are Paid** (64 of 200); 34.5% are Pending and 33.5% Failed. Payment methods are evenly split (Credit Card 37.5%, Insurance 32%, Cash 30.5%) with no significant preference.
- Billing peaks in April (64,271.54) and January (58,701.23) and is lowest in December (27,569.71) and September (33,426.53). The second half of the year bills 23.7% less than the first half, and monthly billing tracks appointment volume closely (r = 0.91).

## Data quality notes

These are findings about the data itself and are worth knowing before drawing conclusions:

- **Bills exist for every appointment, including cancelled and no-show ones.** Billed totals are therefore not a measure of earned revenue.
- **Billing amount equals treatment cost on every row**, so the two columns carry the same information.
- **Pediatrics handles 49% of appointments, yet no patient is younger than 17.**
- **Treatment types do not match specialisations** (for example, Pediatrics and Dermatology doctors performing chemotherapy), and treatment prices are not realistic relative to each other.
- Gender and first names are unrelated in many rows, and 50 patients share only 10 first names, 10 last names and 4 addresses.
- All of the above suggest randomly generated data.

## Limitations

- Small sample: 200 appointments, 50 patients, 10 doctors, one year. Most category differences are within random variation.
- Counts are at appointment level unless stated; a few frequent patients (one patient has 10 visits) can influence the totals.
- No causal claims are made. Explanations such as facility quality, payment-system problems or machine costs cannot be tested with this data.

## Repository structure

```
├── README.md
├── data/                         # source CSVs (only if safe to publish)
├── Hospital_Record_Analysis.ipynb
├── figures/                      # charts generated by the script
└── outputs/
    └── hospital_records_anonymized.csv
```

## How to run

```bash
pip install pandas numpy matplotlib scipy
python hospital_analysis.py
```

## Charts

After running the script, the charts are saved in `figures/`:

![Monthly billing](https://github.com/Ranjan234/Python-for-DataScience/blob/main/EDA%20Projects/Hospital%20Records%20Analysis%20(2023)/Data/Files/Image/Monthly%20Billing%20Distribution.png)
![Appointment status](https://github.com/Ranjan234/Python-for-DataScience/blob/main/EDA%20Projects/Hospital%20Records%20Analysis%20(2023)/Data/Files/Image/Monthly%20Appointments%20Trend.png)
![Cost by treatment](https://github.com/Ranjan234/Python-for-DataScience/blob/main/EDA%20Projects/Hospital%20Records%20Analysis%20(2023)/Data/Files/Image/Average%20Cost%20by%20Treatment%20Type.png)

## Next steps

- Compute billed vs collected revenue using only Completed appointments.
- Model no-show risk (reason for visit, doctor, time of day, insurer).
- Repeat the analysis on a larger or real, de-identified dataset.

## Author

`Soumya Ranjan Sahoo` · [LinkedIn](https://www.linkedin.com/in/soumyaranjansahoo0/)
