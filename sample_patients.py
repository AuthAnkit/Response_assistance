"""
Sample patient records for TriageAI demo scenarios.
Each is a realistic, detailed medical record (~1500-2000 words)
to showcase dramatic token reduction.
"""

PATIENTS = {

"Raj Kumar — Chest Pain (58M)": {
    "summary": "58-year-old male, severe chest pain, diabetic, multiple medications",
    "chief_complaint": "Severe crushing chest pain, radiating to left arm, 8/10 pain score. Onset 45 minutes ago.",
    "record": """
PATIENT RECORD — RAJ KUMAR
Patient ID: EMR-2024-00471
Date of Birth: 14 March 1966 | Age: 58 | Sex: Male | Blood Group: B+

ALLERGIES:
Penicillin — Severe anaphylaxis (throat swelling, BP drop). Documented 2018.
Sulfonamides — Rash and urticaria. Documented 2021.
Aspirin — GI bleeding reported at 325mg dose. Low-dose 75mg tolerated.
Latex — Contact dermatitis.

CODE STATUS: Full resuscitation. No DNR order on file.

EMERGENCY CONTACT:
Priya Kumar (Wife) — +91-98765-43210

CHIEF COMPLAINT (TODAY):
Severe crushing chest pain, 8/10 severity. Radiating to left arm and jaw. Diaphoresis.
Onset 45 minutes ago during physical exertion (climbing stairs). Not relieved by rest.

CURRENT MEDICATIONS:
Metformin 500mg — twice daily (for Type 2 Diabetes)
Atorvastatin 40mg — once daily at bedtime (Hypercholesterolemia)
Amlodipine 5mg — once daily (Hypertension)
Losartan 50mg — once daily (Hypertension, Diabetic Nephropathy)
Pantoprazole 40mg — once daily (GERD)
Aspirin 75mg — once daily (Cardiovascular prophylaxis — NOTE: higher doses cause GI bleed)
Nicorandil 10mg — twice daily (Stable angina — started 6 months ago)

PAST MEDICAL HISTORY:
2019 — Diagnosed with Type 2 Diabetes Mellitus (HbA1c 8.2% at diagnosis)
2020 — Hypertension diagnosed, started on Amlodipine
2021 — Hypercholesterolemia (LDL 185 mg/dL), started Atorvastatin
2022 — Mild renal impairment noted (eGFR 58 mL/min/1.73m²), classified as CKD Stage 2
2023 — Stress test mildly abnormal; coronary angiogram showed 50% LAD stenosis. Conservative management chosen. Nicorandil added.
2023 — Underwent cataract surgery (right eye). No complications. General anesthesia used. Tolerates propofol.

SURGICAL HISTORY:
2023 — Cataract surgery (right eye), uneventful
2009 — Appendectomy (open surgery), no complications
2001 — Right knee arthroscopy for meniscal tear

FAMILY HISTORY:
Father — Myocardial infarction at age 62, deceased
Mother — Hypertension, Type 2 Diabetes, alive (82 years)
Brother — CABG at age 55

SOCIAL HISTORY:
Former smoker — quit 2018 (20 pack-year history)
Alcohol — occasional (1-2 units/week)
Occupation — Retired schoolteacher
Residence — 3rd floor apartment, no elevator

VITALS (ON ARRIVAL):
Blood Pressure: 178/112 mmHg
Heart Rate: 102 bpm (regular)
Respiratory Rate: 22/min
SpO2: 94% on room air
Temperature: 37.1°C
Pain Score: 8/10

RECENT INVESTIGATIONS (Last 6 months):
HbA1c — 7.6% (June 2024)
eGFR — 54 mL/min/1.73m² (June 2024) [CKD Stage 3a — progressing]
LDL Cholesterol — 98 mg/dL (June 2024)
ECG (June 2024) — Sinus rhythm, LVH, no ischemic changes at that time
Echocardiogram (March 2024) — EF 52%, mild diastolic dysfunction, no wall motion abnormalities

REVIEW OF SYSTEMS (Last visit, 3 months ago):
CNS — No headaches, dizziness, or visual changes
CVS — Stable exertional chest tightness (anginal equivalent), no palpitations
Respiratory — Mild exertional dyspnea (New York Heart Association Class II)
GI — Occasional heartburn, managed with Pantoprazole. No melena or hematemesis.
Renal — Nocturia x2, no hematuria. Monitoring CKD progression.
Musculoskeletal — Mild right knee pain, managed with physiotherapy
Endocrine — Diabetes well-controlled on current regimen

IMMUNIZATION HISTORY:
COVID-19 (Covishield) — 2 doses 2021, booster 2022
Influenza — Annual (last October 2023)
Pneumococcal — 2022

LIFESTYLE AND DIET:
Vegetarian diet. Low salt diet counseled. Exercises 20 minutes walking 3 times/week (reduced recently due to knee pain and exertional chest discomfort).

PREVIOUS HOSPITALIZATIONS:
2019 — Dengue fever, 4-day admission, conservative management
2009 — Appendectomy (as noted above)

FOLLOW-UP NOTES (Cardiologist, Dr. Mehta, September 2024):
Patient reports increasing frequency of exertional chest discomfort over the past 3 months. Previously occurring with walking >500m, now occurring with walking 100m or climbing one flight of stairs. Nicorandil dose increased from 5mg to 10mg twice daily. Repeat stress test scheduled for November 2024. Patient counseled on symptoms of ACS and instructed to present to ER immediately if symptoms at rest. Patient verbally acknowledged understanding.

RADIOLOGY:
Chest X-Ray (June 2024) — Mild cardiomegaly. No pulmonary edema or consolidation.

ADVERSE DRUG REACTIONS (DETAILED):
1. Penicillin: Patient reports receiving Amoxicillin in 2018 for dental procedure. Within 30 minutes developed throat tightness, generalized urticaria, and hypotension. Treated with epinephrine and IV antihistamines in ER. Formal allergy confirmed. All beta-lactam antibiotics should be avoided. Use cephalosporins with caution (cross-reactivity risk ~2%).
2. Sulfonamide: Rash with Co-trimoxazole in 2021. Non-anaphylactic. Avoid sulfonamide class.
3. Aspirin at 325mg: GI bleed (melena) documented in 2017 before cardiac prophylaxis indication. Currently tolerating 75mg with Pantoprazole cover. Do NOT increase aspirin dose beyond 75mg without GI consultation.

NURSING NOTES (Previous admission 2019):
Patient is cooperative and compliant with medications. Good health literacy. Speaks Hindi and English. Requires translator for complex medical discussions in English.

INSURANCE / ADMINISTRATIVE:
CGHS beneficiary (Central Government Health Scheme). Policy active. Pre-authorization required for PCI or CABG procedures. Contact insurance team before invasive procedures.
""",
    "demo_questions": [
        "Patient has crushing chest pain and BP 178/112. What thrombolytics or anticoagulants can I give? Any contraindications?",
        "Can I give morphine for pain? Are there any drug interactions with his current medications?",
        "Patient needs emergency PCI. Are there any allergy concerns with contrast dye or medications used in cath lab?",
    ]
},

"Fatima Shaikh — Anaphylaxis (34F)": {
    "summary": "34-year-old female, anaphylactic reaction, multiple severe allergies, pregnant",
    "chief_complaint": "Acute anaphylaxis — throat swelling, hives, BP dropping. Brought in by ambulance after eating at restaurant.",
    "record": """
PATIENT RECORD — FATIMA SHAIKH
Patient ID: EMR-2024-00892
Date of Birth: 22 July 1990 | Age: 34 | Sex: Female | Blood Group: A-
Obstetric Status: PREGNANT — 24 weeks gestation (G2P1)

CRITICAL ALERTS ⚠️:
1. MULTIPLE SEVERE ALLERGIES — See allergy section. High anaphylaxis risk.
2. PREGNANT 24 WEEKS — All medications must be pregnancy-safe (Category B or C only unless life-threatening emergency).
3. Rh NEGATIVE BLOOD GROUP — Requires Anti-D immunoglobulin if any bleeding or invasive procedure.
4. Previous anaphylaxis requiring ICU admission (2022).

ALLERGIES:
1. Peanuts — SEVERE ANAPHYLAXIS. Airway involvement. ICU admission 2022. Carries EpiPen.
2. Tree nuts (cashew, walnut, almond) — Severe allergic reaction with urticaria and angioedema.
3. Shellfish (shrimp, crab) — Severe allergic reaction.
4. Penicillin — Anaphylaxis. Confirmed by allergist.
5. NSAIDs (Ibuprofen, Naproxen) — Aspirin-exacerbated respiratory disease. Bronchospasm.
6. Iodine-based contrast dye — Severe reaction documented 2021 (pre-medication protocol required if use is unavoidable).
7. Latex — Moderate reaction. Operating theatres must be latex-free.
8. Hair dye (PPD — paraphenylenediamine) — Contact dermatitis.

CODE STATUS: Full resuscitation. Active pregnancy — neonatology to be alerted if maternal emergency.

EMERGENCY CONTACT:
Ahmed Shaikh (Husband) — +91-99887-76655
Dr. Aisha Rajan (OB-GYN, Sunshine Hospital) — +91-22-55441122

CHIEF COMPLAINT (TODAY):
Acute onset urticaria, angioedema, throat tightness, wheezing. BP on arrival 82/50 mmHg. SpO2 89%. Brought by ambulance from restaurant (possible peanut exposure in food).

CURRENT MEDICATIONS (Pregnancy-adjusted):
Folic Acid 5mg — once daily
Iron Sucrose (oral) — for mild iron deficiency anemia
Calcium + Vitamin D supplement
Cetirizine 10mg — daily (for chronic urticaria, continued in pregnancy with OB approval)
Pantoprazole 20mg — for pregnancy-related GERD
EpiPen (Epinephrine 0.3mg auto-injector) — prescribed PRN anaphylaxis. Carries at all times. 

OBSTETRIC HISTORY:
G2P1 — Currently 24 weeks gestation.
Previous pregnancy (2021) — Normal vaginal delivery, healthy male infant (now 3 years). No obstetric complications.
Current pregnancy — Low risk except for anaphylaxis history. Anomaly scan normal. GDM screen negative. BP normal throughout.

PAST MEDICAL HISTORY:
2021 — Iodine contrast reaction (for appendix CT) — urticaria, required IV antihistamines. Pre-medication protocol: Prednisolone 50mg oral 13h, 7h, 1h before procedure + Diphenhydramine 50mg 1h before.
2022 — Severe peanut anaphylaxis. Accidental ingestion at wedding. Airway swelling requiring intubation. ICU 3 days. Epinephrine infusion required. Full recovery.
2023 — Diagnosed with mild asthma (triggered by NSAIDs, cold air, exercise). Managed with Salbutamol inhaler PRN.

CURRENT ASTHMA MEDICATIONS:
Salbutamol (Ventolin) inhaler — PRN for asthma symptoms (NOT contraindicated in pregnancy)
Budesonide inhaler — not currently prescribed (mild intermittent asthma)

IMMUNIZATION (PREGNANCY):
Tdap — Given at 20 weeks (this pregnancy)
Influenza — Given October 2024
COVID-19 — Fully vaccinated 2021, booster 2022

ANAPHYLAXIS ACTION PLAN (Documented by Allergist, Dr. Priya Nair):
Step 1: Epinephrine 0.3mg IM (EpiPen) — FIRST LINE, even in pregnancy (benefit outweighs risk)
Step 2: Call emergency services
Step 3: Diphenhydramine 50mg IV/IM
Step 4: Ranitidine 50mg IV (H2 blocker)
Step 5: Hydrocortisone 200mg IV (steroids — acceptable short course in pregnancy emergency)
Step 6: For bronchospasm — Salbutamol nebulization
Step 7: If refractory — Epinephrine infusion
NOTE: Avoid glucagon if beta-blockers used (patient is NOT on beta-blockers). 
NOTE: Avoid vasopressin — not studied in pregnancy.
NOTE: Fetal monitoring required after maternal anaphylaxis episode.

SOCIAL HISTORY:
Non-smoker. No alcohol (pregnancy). Housewife. Lives in Mumbai with husband and son.

LABORATORY (Last visit, 2 weeks ago — 22 weeks gestation):
Hemoglobin — 10.8 g/dL (mild anemia, on iron)
Blood Glucose — 92 mg/dL fasting (normal)
Platelet count — 198,000/μL
Coagulation screen — Normal
Urine routine — Trace protein (monitoring)

NOTES FOR EMERGENCY STAFF:
- Epinephrine is SAFE and recommended even in pregnancy for life-threatening anaphylaxis
- Do NOT delay epinephrine for fear of fetal effects — maternal death is the greater risk
- After stabilization, contact OB-GYN Dr. Aisha Rajan immediately for fetal assessment
- Anti-D immunoglobulin required if any procedures involve risk of fetomaternal hemorrhage
- Latex-free environment mandatory
- If intubation required: RSI preferred, use ketamine (avoid succinylcholine if possible — check potassium first)
""",
    "demo_questions": [
        "Patient in anaphylaxis, BP 82/50, pregnant 24 weeks. What do I give first? Is epinephrine safe?",
        "Can I use corticosteroids and antihistamines? Any specific ones to avoid in pregnancy?",
        "Patient needs IV access — any contrast or dye concerns? She's Rh negative, does that matter here?",
    ]
},

"Arjun Mehta — Polytrauma (22M)": {
    "summary": "22-year-old male, road traffic accident, head trauma, on anticoagulants",
    "chief_complaint": "Road traffic accident. Multiple injuries: head trauma, suspected internal bleeding, open femur fracture. Unconscious on arrival.",
    "record": """
PATIENT RECORD — ARJUN MEHTA
Patient ID: EMR-2024-01103
Date of Birth: 5 January 2002 | Age: 22 | Sex: Male | Blood Group: O+

CRITICAL ALERTS ⚠️:
1. ON ANTICOAGULATION — Rivaroxaban (for DVT). Risk of uncontrolled hemorrhage. Reversal agent may be required.
2. HISTORY OF EPILEPSY — On anti-epileptic medication. Seizure precautions required, especially with head trauma.
3. SICKLE CELL TRAIT (not disease) — Heterozygous. Relevant for oxygenation targets and transfusion.
4. SEVERE NEEDLE PHOBIA — Noted for elective procedures; not relevant in emergency context.

ALLERGIES:
Codeine — Severe nausea and vomiting. Possible opioid hypersensitivity. Alternative opioids (fentanyl, morphine) used without prior reaction.
Tetracycline antibiotics — Rash. Non-anaphylactic.
No known allergy to contrast dye, penicillin, or NSAIDs.

CODE STATUS: Full resuscitation (age 22, no advance directive).

EMERGENCY CONTACT:
Sunita Mehta (Mother) — +91-98765-11223
Dr. Rajan Mehta (Father, also a physician, Cardiologist) — +91-98765-11224

CHIEF COMPLAINT (TODAY):
Brought by ambulance. Road traffic accident (motorcycle vs truck). GCS 9 on scene, now 7 in ER.
Suspected traumatic brain injury. Open right femur fracture with active bleeding. Abdominal distension (possible splenic injury). BP 88/60 mmHg. HR 134 bpm.

CURRENT MEDICATIONS:
Rivaroxaban 20mg — once daily with dinner (for DVT diagnosed 3 months ago; 6-month course)
Levetiracetam 500mg — twice daily (Epilepsy, diagnosed age 18)
Vitamin D 60,000 IU — weekly (deficiency)
Zinc supplement — daily

ANTICOAGULATION STATUS:
Rivaroxaban (Factor Xa inhibitor). Last dose: approximately 9 hours ago per family.
Reversal agent: Andexanet alfa (preferred) or Prothrombin Complex Concentrate (PCC) 4-factor if andexanet not available.
DAPT or heparin should be AVOIDED given active hemorrhage.

PAST MEDICAL HISTORY:
2020 — Diagnosed with generalized epilepsy after first tonic-clonic seizure. MRI brain normal. EEG showed generalized spike-wave discharges. Started on Levetiracetam.
2021 — Second seizure episode (missed medication dose). No change in treatment. Seizure-free for 3 years now.
2024 (July) — Right leg DVT diagnosed after prolonged immobility (3-week hospital admission for typhoid fever). Started Rivaroxaban for 6-month course (ends January 2025).
2022 — Sickle cell trait identified incidentally on CBC during sports physical. Hematology reviewed — heterozygous HbAS, not sickle cell disease. Advised to maintain good oxygenation and hydration.

SURGICAL HISTORY:
No prior surgeries.

FAMILY HISTORY:
Mother — Hypothyroidism
Father — Hypertension, Cardiologist (contact above)
No family history of bleeding disorders or clotting disorders.

SOCIAL HISTORY:
Engineering student. Non-smoker. Occasional alcohol (weekends). Motorcycle rider (helmet worn per family — helmet found at scene, unclear if properly secured). No recreational drugs. Lives in college hostel.

IMMUNIZATION:
Tetanus — Up to date (booster 2022 during sports injury)
COVID-19 — Fully vaccinated

EPILEPSY MANAGEMENT NOTES (Neurologist, Dr. Kapoor):
Patient seizure-free on Levetiracetam 500mg BD for 3 years. Consider IV Levetiracetam in hospital if oral administration not possible. Do NOT use phenytoin as first-line AED (patient not previously on it; Levetiracetam preferred). If breakthrough seizure: IV Lorazepam 0.1mg/kg as first-line benzodiazepine. Avoid hypoxia, hypoglycemia, and hyponatremia — all seizure precipitants.

BLOOD TRANSFUSION HISTORY:
No prior transfusions. Blood type O+. Blood bank to be contacted for emergency crossmatch.
Note: Sickle cell trait — transfuse with standard blood (no special requirements for trait, unlike disease). Monitor oxygen saturation (target SpO2 >95%).

RECENT INVESTIGATIONS (3 months ago, before Rivaroxaban initiation):
CBC — Hb 14.2 g/dL, Platelets 245,000, WBC normal
Sickle cell screen — HbAS (trait confirmed)
Renal function — Normal (eGFR >90)
LFT — Normal
Anti-Xa level — Not checked (Rivaroxaban monitoring not routinely required)

KNOWN DRUG INTERACTIONS (Rivaroxaban):
Avoid concurrent NSAIDs — increased bleeding risk (Ketorolac should be used with extreme caution)
Avoid dual antiplatelet therapy
Avoid other anticoagulants without reversal

PAIN MANAGEMENT NOTE:
Codeine — AVOID (severe nausea/vomiting reaction). 
Morphine and Fentanyl — previously given without reaction.
Tramadol — lowers seizure threshold. USE WITH CAUTION in epileptic patient.
Ketamine — can lower seizure threshold theoretically but generally acceptable in trauma; use lowest effective dose.
NSAIDs — caution given anticoagulation and potential renal injury in hemorrhagic shock.

EMERGENCY SURGERY CONSIDERATIONS:
If surgery required — inform anesthesia team of:
1. Rivaroxaban: request andexanet alfa or PCC 4-factor for reversal
2. Epilepsy: continue IV Levetiracetam perioperatively; prophylactic IV benzodiazepine if high seizure risk
3. Sickle cell trait: maintain SpO2 >95%, good hydration, avoid hypothermia
4. Blood type O+ — contact blood bank immediately for emergency crossmatch; O- negative blood if crossmatch delayed
5. Codeine allergy — use fentanyl or morphine for pain
"""
,
    "demo_questions": [
        "Patient has active hemorrhage and is on Rivaroxaban. How do I reverse anticoagulation emergently?",
        "Patient needs urgent surgery. What anesthesia precautions are needed given epilepsy and sickle cell trait?",
        "What pain management can I use? He has a codeine allergy and epilepsy.",
    ]
},

}


def get_patient_names() -> list:
    return list(PATIENTS.keys())


def get_patient(name: str) -> dict:
    return PATIENTS.get(name, {})
