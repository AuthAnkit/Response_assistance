"""
EMR Record Expander
===================
Real hospital records are 5,000–20,000+ words.
This module appends realistic but query-irrelevant historical content
to simulate a true EMR, making the pruning demonstration impactful.
"""

# ─── Boilerplate clinical content that pads records realistically ─────────────

ADMIN_AND_BILLING = """
ADMINISTRATIVE AND BILLING INFORMATION:
Patient Registration Date: 12 January 2019
Facility: Apollo Multispeciality Hospital, Mumbai
Ward: General Medicine (later transferred to Cardiology)
Treating Physician: Dr. Arvind Shah, MD (Internal Medicine)
Consultant Cardiologist: Dr. Priya Mehta, DM (Cardiology)
Insurance Provider: New India Assurance Co. Ltd.
Policy Number: NIA-2019-MH-449021
Pre-authorization Code: PA-2024-00471
Billing Category: Cashless — Third-Party Administrator: Medi Assist
GST Number for Hospital: 27AAACH1234F1Z5
Room Type: Twin Sharing (Bed No. 214-B)
Admission Date: 12 January 2019 | Discharge Date: 16 January 2019
Total Billed Amount (2019 admission): ₹47,320
Patient Satisfaction Survey Score: 4.2/5

PATIENT REGISTRATION HISTORY:
First Registration: Outpatient — 04 March 2018 (General Medicine, fever)
Second Visit: Outpatient — 22 August 2018 (Dermatology, skin rash — sulfonamide reaction documented)
Third Visit: Inpatient — 12 January 2019 (Dengue fever, Ward admission)
Fourth Visit: Outpatient — 15 September 2020 (Hypertension diagnosis, Cardiology OPD)
Fifth Visit: Outpatient — 02 November 2021 (Hypercholesterolemia follow-up)
Sixth Visit: Outpatient — 18 March 2022 (CKD Stage 2 detection, Nephrology consult)
Seventh Visit: Day Procedure — 04 June 2023 (Cataract surgery, right eye)
Eighth Visit: Outpatient — 12 September 2024 (Cardiology follow-up, worsening angina)
"""

NURSING_NOTES_2019 = """
NURSING PROGRESS NOTES — DENGUE ADMISSION (January 2019):
Day 1 (12 Jan): Patient admitted with high fever (104°F), severe myalgia, retroorbital headache. 
Dengue NS1 antigen positive. IV fluids started — RL 500ml over 4 hours. Paracetamol 500mg PO Q6H. 
Platelet count 140,000. Patient alert and oriented x3. Appetite poor. Input/Output charted — 
Intake 1200ml, Output 900ml. Nurse in charge: Sister Meenakshi.

Day 2 (13 Jan): Fever persisting (102°F). Platelet count dropped to 98,000/μL. Attending physician 
notified. Increased IV fluid rate. Patient complaining of generalized weakness. Blood transfusion 
not indicated at this time. Family counseled. Dengue diet (soft, easily digestible) advised. 
No rash noted. Tourniquet test weakly positive. Nurse: Sister Rani.

Day 3 (14 Jan): Fever breaking. Platelet 75,000/μL (nadir). Physician reviewed — conservative 
management continued. Patient tolerating oral fluids. IV rate reduced. Urine output adequate. 
No bleeding manifestations. Family update given by Dr. Shah. Patient restless at night — mild sedation 
with Hydroxyzine 25mg given. Nurse: Sister Kavitha.

Day 4 (15 Jan): Platelet recovering — 112,000/μL. Temperature normal for 24 hours. Appetite improving. 
IV fluids discontinued. Oral hydration maintained. Patient ambulating in ward. Discharge planning initiated.
Physiotherapy consult: advised gentle mobilization. No respiratory complications. Nurse: Sister Priya.

Day 5 (16 Jan): Platelet 178,000/μL. Patient afebrile for 48 hours. Clinically well. 
Discharge instructions given — rest for 1 week, follow-up in OPD in 7 days, return if 
fever/bleeding occurs. Discharge completed 11:30 AM. Nurse: Sister Meenakshi.
"""

DIETARY_AND_PHYSIO = """
DIETARY ASSESSMENT AND RECOMMENDATIONS:
Dietitian: Ms. Sunita Patel, BSc Dietetics
Assessment Date: Multiple visits 2020–2024

2020 Assessment (Hypertension Diagnosis):
BMI: 26.8 (overweight). Waist circumference 96cm (above risk threshold for South Asian).
Dietary history: High sodium intake (estimated 4,800mg/day vs recommended <2,300mg). 
Frequent outside food consumption (5 days/week). Vegetarian — adequate protein from dal, paneer.
Recommendations: DASH diet counseled. Sodium restriction <2g/day. Reduce processed foods.
Increase fruits/vegetables. Portion control. Target weight loss 5kg over 6 months.
Follow-up: Patient partial compliance reported at 3-month review.

2021 Assessment (Hypercholesterolemia):
Updated dietary advice: Mediterranean-style diet adapted for Indian vegetarian.
Eliminate trans fats (vanaspati, packaged namkeen). Increase omega-3 (flaxseed, walnuts).
Add fiber (oats, psyllium husk). Patient given printed diet chart in Marathi.

2022 Assessment (CKD Stage 2):
Nephrology-dietitian coordination. Protein restriction NOT required at this stage (eGFR 58).
Potassium monitoring advised (limit high-K foods if eGFR drops below 30).
Phosphate: No restriction currently.
Patient educated on CKD-friendly diet.

PHYSIOTHERAPY NOTES:
Physiotherapist: Mr. Vikram Desai, BPT
2021 — Right knee meniscal tear follow-up:
3-session physiotherapy course. Exercises: VMO strengthening, straight leg raises, 
short arc quads. Patient compliance good. Pain reduced from 7/10 to 3/10. 
Home exercise program given. Advised swimming instead of high-impact exercise.

2024 — Reduced exercise tolerance counseling:
Patient reports reducing walking due to both knee pain and exertional chest discomfort.
Physiotherapist coordinated with cardiologist — advised cardiac rehabilitation class.
Supervised exercise test cleared before commencing program. Patient enrolled in 
Phase II cardiac rehabilitation (3 sessions/week, hospital-supervised).
"""

SOCIAL_WORK_NOTES = """
SOCIAL WORK AND PATIENT SUPPORT NOTES:
Social Worker: Ms. Rekha Nair, MSW
Date of Assessment: September 2024

Psychosocial Assessment:
Patient lives with wife (Priya Kumar, age 54, homemaker) in a 2BHK apartment (3rd floor, no elevator).
Son (Rahul Kumar, age 28) lives nearby and is primary caregiver support.
Daughter (Pooja, age 24) lives in Pune. Available for emergencies.

Financial Assessment:
Retired schoolteacher on government pension (approx ₹28,000/month).
Central Government Health Scheme (CGHS) covers most medications and hospital visits.
No significant financial stress identified. Medications affordable within current scheme.

Psychological Assessment:
Patient reports mild anxiety about cardiac condition, especially given father's history of MI.
No clinical depression. Coping strategies: religious activities, daily walks (reduced recently).
Referred for one session with psychologist for health anxiety counseling.
Psychologist note (Dr. Anjali Rao, October 2024): Sub-threshold health anxiety. 
Psychoeducation given. Relaxation techniques taught. No medication indicated.
Follow-up recommended if symptoms worsen.

Housing and Safety Assessment:
Third floor apartment without elevator poses significant challenge for patient with 
worsening exertional tolerance. Discussed options: (1) Request ground floor accommodation 
if government-allotted quarters, (2) Consider elevator building if moving. 
Patient declined to move at this time — emotional attachment to current home.
Advised to discuss with cardiologist and family.
"""

OLD_LAB_RESULTS = """
HISTORICAL LABORATORY RESULTS — LONGITUDINAL TRACKING:

COMPLETE BLOOD COUNT (Annual):
2018: Hb 14.8 g/dL | Platelets 210,000 | WBC 8,200 — Normal
2019 (Post-dengue): Hb 12.9 g/dL | Platelets 178,000 | WBC 6,800 — Recovering
2019 (3-month follow-up): Hb 14.2 g/dL | Platelets 215,000 — Normal
2020: Hb 13.9 g/dL | Platelets 198,000 | WBC 7,400 — Normal
2021: Hb 13.5 g/dL | Platelets 205,000 | WBC 8,000 — Normal
2022: Hb 13.2 g/dL | Platelets 192,000 | WBC 7,600 — Normal
2023: Hb 13.0 g/dL | Platelets 185,000 | WBC 7,200 — Normal (mild anemia of chronic disease)
2024 (June): Hb 12.8 g/dL | Platelets 178,000 | WBC 7,100

RENAL FUNCTION (eGFR trend — documenting CKD progression):
2018: eGFR 84 mL/min/1.73m² — Normal
2020: eGFR 76 mL/min/1.73m² — Normal
2021: eGFR 68 mL/min/1.73m² — CKD Stage 2 threshold approached
2022: eGFR 58 mL/min/1.73m² — CKD Stage 2 confirmed
2023: eGFR 56 mL/min/1.73m² — Stable
2024 (June): eGFR 54 mL/min/1.73m² — CKD Stage 3a (new classification), progressing slowly

LIPID PROFILE (Annual):
2021 (Baseline at diagnosis): Total cholesterol 238 | LDL 185 | HDL 38 | TG 178 | HIGH RISK
2022 (6 months on Atorvastatin): Total cholesterol 178 | LDL 112 | HDL 42 | TG 145 — Improved
2023: Total cholesterol 162 | LDL 105 | HDL 44 | TG 132 — Good control
2024 (June): Total cholesterol 151 | LDL 98 | HDL 46 | TG 118 — Target achieved (<100 LDL)

THYROID FUNCTION (Checked 2020, 2022):
2020: TSH 2.4 mIU/L | Free T4 1.2 ng/dL — Normal
2022: TSH 2.8 mIU/L — Normal. No thyroid disease.

URINE ANALYSIS (Monitoring for diabetic nephropathy):
2020: Normal. No microalbuminuria.
2021: Microalbuminuria 28 mg/g creatinine (borderline).
2022: Microalbuminuria 42 mg/g creatinine — Confirmed early diabetic nephropathy. 
     Started Losartan for renoprotection.
2023: Microalbuminuria 38 mg/g creatinine — Stable/improving on Losartan.
2024: Microalbuminuria 35 mg/g creatinine — Continuing improvement.

LIVER FUNCTION (Annual):
All years 2018–2024: Within normal limits. Atorvastatin well-tolerated.
2024: ALT 28 U/L | AST 24 U/L | ALP 78 U/L — Normal. No statin hepatotoxicity.

DIABETES MONITORING (HbA1c quarterly):
2019 (Diagnosis): HbA1c 8.2% — Poorly controlled
2019 (6 months on Metformin): HbA1c 7.4% — Improving
2020: HbA1c 7.1%
2021: HbA1c 7.3%
2022: HbA1c 6.9% — At target
2023: HbA1c 7.0%
2024 Q1: HbA1c 7.4% — Slightly above target
2024 Q2 (June): HbA1c 7.6% — Worsening slightly; medication review recommended
"""

OUTPATIENT_CONSULTATION_NOTES = """
OUTPATIENT CONSULTATION NOTES — CHRONOLOGICAL:

04 March 2018 — General Medicine, Dr. Ramesh Joshi:
Chief complaint: Fever 3 days, body aches, mild cough. Examination: Throat mildly congested. 
Lungs clear. Abdomen normal. Impression: Viral URTI. Prescribed: Paracetamol 500mg TDS x5 days, 
Vitamin C 500mg daily. Advised rest and fluids. Follow-up if not improving in 5 days. 
Not improving → 08 March: dengue serology ordered → negative. Resolved spontaneously.

22 August 2018 — Dermatology, Dr. Kavita Singh:
Chief complaint: Itchy rash all over body after antibiotic course (Co-trimoxazole for UTI).
Examination: Diffuse maculopapular rash, no mucosal involvement, no systemic symptoms.
Impression: Drug reaction to sulfonamide (Co-trimoxazole). Prescribed: Cetirizine 10mg OD x7 days, 
topical calamine lotion. Advised to avoid sulfonamide antibiotics in future. Allergy documented.

Penicillin allergy event — 2018 (Dental — See allergy section above for full details)

15 September 2020 — Cardiology OPD, Dr. Priya Mehta:
Referred by GP for newly diagnosed hypertension (BP 158/96 at GP clinic, 162/98 today).
No target organ damage on examination. No retinopathy. Fundi normal (ophthalmology review). 
ECG: Normal sinus rhythm, no LVH at this time. Urine: trace protein.
Started: Amlodipine 5mg OD. Low sodium diet. Exercise counseled. 
Follow-up 6 weeks.

06 November 2020 — Cardiology Follow-up:
BP today: 138/88. Partial response to Amlodipine. Added Losartan 25mg OD (also for 
microalbuminuria protection given diabetes). Compliance: Good. No side effects.
Target BP: <130/80 in diabetic patient. Achieved at 4-month review (128/82 mmHg).

18 March 2022 — Nephrology, Dr. Ashok Verma:
Referred for declining eGFR. CKD Stage 2 classified. Discussion: CKD likely multifactorial 
(diabetes + hypertension). RAAS blockade with Losartan continued. No specialist treatment changes.
Annual monitoring plan set. Avoid nephrotoxic drugs (NSAIDs, contrast — notify before use). 
Patient counseled: CKD progression slow at current rate.

12 September 2024 — Cardiology OPD, Dr. Priya Mehta (Latest):
Presenting complaint: Increasing frequency and reduced threshold for exertional chest 
tightness over 3 months. Previously: with walking >500m. Now: climbing one flight of stairs 
or walking >100m. No rest pain yet.
Examination: BP 148/92, HR 78, regular. No signs of heart failure. 
Assessment: Worsening stable angina. Possible progression of known LAD stenosis (50% in 2023).
Plan: Increase Nicorandil 5mg BD to 10mg BD. Repeat stress test November 2024. 
If stress test significantly positive: repeat coronary angiogram, may consider PCI.
Patient counseled: Report any rest pain, pain lasting >20 minutes, or severe episode immediately.
Patient verbally acknowledged. Patient's son Rahul present, educated about ACS symptoms.
"""

def get_extended_record(base_record: str, patient_type: str = "cardiac") -> str:
    """
    Expand a base patient record with realistic bulk historical content.
    This simulates a real EMR (5,000–7,000 tokens) vs a summary record.
    """
    extension = f"""
{ADMIN_AND_BILLING}
{NURSING_NOTES_2019}
{OLD_LAB_RESULTS}
{DIETARY_AND_PHYSIO}
{SOCIAL_WORK_NOTES}
{OUTPATIENT_CONSULTATION_NOTES}

MISCELLANEOUS HISTORICAL NOTES:
Previous GP records transferred from Dr. Suresh Clinic, Dadar (2015–2018):
2015 — Annual health check: All normal. BMI 24.2. BP 124/78. Advised to maintain lifestyle.
2016 — Mild GERD symptoms. Started antacid PRN. No scope done.
2017 — Aspirin 325mg given post minor TIA scare — GI bleed (melena) within 48 hours. 
        Hospitalized briefly at local clinic. Aspirin stopped. GI scoped — 
        superficial antral erosions. Healed with PPI. Aspirin dose reduced to 75mg later 
        when cardiac indication established.
2018 — Penicillin anaphylaxis (dental procedure) — full details in allergy section above.

OPTICAL RECORDS:
2023 — Cataract surgery (right eye). Pre-operative assessment: Fit for surgery.
        General anesthesia used (Propofol induction, Sevoflurane maintenance). 
        Tolerated well. Post-op: Prednisolone eye drops, Moxifloxacin eye drops, 4 weeks.
        Vision in right eye: 6/9 post-op (up from 6/24 pre-op).
        Left eye: 6/6, no cataract yet. Annual review recommended.

DENTAL RECORDS (transferred from Dr. Kapoor's Dental Clinic):
Regular dental checkups 2016–2024. Last visit: April 2024. 
No active dental disease. Teeth: 28 present (upper wisdom teeth extracted 2015).
NOTE: Penicillin-based antibiotics CONTRAINDICATED. Alternatives for dental procedures:
Clindamycin 600mg single dose or Azithromycin 500mg single dose for prophylaxis.

OPHTHALMOLOGY ANNUAL REVIEW (for Diabetic Retinopathy screening):
2020: No diabetic retinopathy. Background changes: None.
2021: No diabetic retinopathy.
2022: Mild non-proliferative diabetic retinopathy (dot haemorrhages, 1-2 microaneurysms).
2023: Same grade. No macular edema. Annual follow-up.
2024 (March): Mild NPDR stable. No change. Continue annual review.

VACCINATION HISTORY (COMPLETE):
BCG — Birth
DPT, OPV — Childhood (1966–1969, government schedule)
Hepatitis B — 2004 (3 doses, completed)
Typhoid — 2016 (Vi antigen)
Hepatitis A — 2017 (2 doses)
Pneumococcal (PCV13) — 2022 (given given CKD + Diabetes risk factors)
Pneumococcal (PPSV23) — to be given 1 year after PCV13 (due 2023, not yet confirmed)
COVID-19 (Covishield AZ): Dose 1 — March 2021, Dose 2 — May 2021, Booster — January 2022
Influenza: Annual from 2020. Last dose October 2023.
Herpes Zoster: Not yet given. Recommended by physician (age >50, immunocompromised risk with DM).
"""
    return base_record + extension
