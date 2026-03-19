# Response_assistance

# 🚨 TriageAI — Real-Time Emergency Triage Assistant

> ⚡ Intelligent Context Pruning + LLM-powered Emergency Decision Support
> 🏆 HPE GenAI for GenZ Challenge 2025 | Intel Unnati Programme

---

## 🧠 Overview

**TriageAI** is an AI-powered emergency triage system that processes large-scale patient medical records (EMRs) and delivers **instant, clinically relevant insights** for life-critical situations.

In real hospitals, patient records can exceed **5,000–20,000+ words**, making it difficult for doctors to extract key information quickly.

👉 TriageAI solves this by:

* **Compressing medical context by 75–90%**
* Retaining **critical clinical information (allergies, medications, risks)**
* Delivering **real-time emergency recommendations using LLMs**

---

## 🔥 Key Features

### ⚡ Intelligent Context Pruning Engine

* Custom-built pruning algorithm (TF-IDF + medical urgency scoring)
* Preserves **critical sections**:

  * Allergies
  * Medications
  * Code status
  * Emergency alerts
* Reduces token usage by **75–90%**

### 🏥 Realistic EMR Simulation

* Synthetic patient records (~5,000–7,000 tokens)
* Includes:

  * Medical history
  * Lab reports
  * Billing + admin data
  * Nursing notes
* Demonstrates real-world hospital complexity

### 🤖 AI-Powered Emergency Response

* Integrated with **Gemini API**
* Provides:

  * ⚠️ Critical alerts
  * 📋 Clinical assessment
  * 💊 Treatment recommendations
  * 🚫 Contraindications
  * ⏱️ First 5-minute action plan

### 🎨 Interactive UI (Streamlit)

* Clean emergency dashboard
* Real-time token comparison
* Before vs after compression visualization

---

## 🏗️ Architecture

```
Patient EMR (~5000 tokens)
        ↓
⚡ Context Pruner / ScaleDown API
        ↓
Compressed Context (~900 tokens)
        ↓
🤖 Gemini AI
        ↓
🚨 Emergency Triage Response
```

---

## 📂 Project Structure

```
├── app.py                # Streamlit UI + API integration
├── context_pruner.py    # Core pruning algorithm
├── record_expander.py   # Expands EMR with realistic data
├── sample_patients.py   # Synthetic patient scenarios
```

---

## 🧪 Core Innovation

### 🧩 Context Pruning Algorithm

The system combines:

* **TF-IDF Relevance Scoring**
* **Medical Urgency Boosting**
* **Critical Section Preservation**
* **Token Budget Optimization**

Result:

```
Original: 5000+ tokens
After pruning: ~900 tokens
Reduction: ~80%
```

---

## 🚑 Demo Scenarios

* ❤️ Chest Pain (Cardiac Emergency)
* ⚠️ Anaphylaxis (Pregnancy + allergies)
* 🚗 Polytrauma (Accident + anticoagulants)

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI Model:** Gemini API
* **Compression:** ScaleDown API
* **Algorithms:** TF-IDF, heuristic scoring

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/triage-ai
cd triage-ai

pip install -r requirements.txt

streamlit run app.py
```

---

## 🔑 API Setup

Add keys in the sidebar:

* ScaleDown API Key → https://scaledown.xyz
* Gemini API Key → https://aistudio.google.com

---

## 📊 Impact

* ⏱️ Reduces decision time in emergencies
* 💰 Cuts LLM cost significantly
* 🧠 Improves clinical accuracy by removing noise
* 🚨 Helps doctors focus on **what matters most**

---

## 🚀 Future Improvements

* Integration with real hospital EMRs (FHIR)
* Multi-language support (Hindi, Marathi)
* Voice-based emergency assistant
* Edge deployment for ambulances

---

## 👨‍💻 Author

**Ankit Singh**

---

## ⭐ If you like this project

Give it a ⭐ and share it!
