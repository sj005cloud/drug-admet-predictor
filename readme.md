# 🧪 Drug Candidate Property Predictor — Lightweight ADMET Screener

A full-stack AI-powered web application that predicts ADMET-like molecular properties from SMILES strings using RDKit (cheminformatics) and LLM-based interpretation. Built as a lightweight drug discovery screening tool.

---

## 🚀 Live Demo

🔬 **Frontend (Vercel):**  
https://drug-admet-predictor.vercel.app/

🧠 **Backend API (Railway):**  
drug-admet-predictor-production.up.railway.app

📌 **API Endpoint:**
POST /predict

---

## 🧬 Problem Statement

Build a web application that accepts a **SMILES string** and returns predicted ADMET-like properties using a combination of:

- Rule-based molecular property calculations (RDKit)
- LLM-generated interpretation (Gemini API)

---

## ⚙️ Features

### 🧪 Molecular Property Prediction (RDKit)
- Molecular Weight
- LogP (lipophilicity)
- Hydrogen Bond Donors
- Hydrogen Bond Acceptors
- TPSA (Topological Polar Surface Area)
- Lipinski Rule of Five (Pass/Fail)

---

### 🤖 AI Interpretation (Gemini LLM)
- Generates a **2-sentence natural language explanation**
- Describes drug-likeness and molecular behavior in simple terms

---

### 🎨 Frontend Features (React)
- SMILES input interface
- Example molecule buttons:
  - Aspirin
  - Caffeine
  - Ibuprofen
  - Paracetamol
  - Glucose
- Clean card/table UI for results
- Lipinski rule highlighted:
  - 🟢 Pass
  - 🔴 Fail
- Molecule structure visualization

---

### 🧠 Backend Features (FastAPI)
- `/predict` endpoint for SMILES input
- RDKit-based molecular computation
- Image generation for molecules
- LLM integration for interpretation
- CORS-enabled for frontend integration

---

## 🧪 Example SMILES Inputs
Aspirin: CC(=O)Oc1ccccc1C(=O)O
Caffeine: Cn1c(=O)c2c(ncn2C)n(c1=O)C
Ibuprofen: CC(C)Cc1ccc(cc1)C(C)C(=O)O
Paracetamol: CC(=O)Nc1ccc(O)cc1
Glucose: OC[C@H]1OC(O)C@HC@@H[C@@H]1O


---

## 🏗️ Tech Stack

### Frontend
- React (Vite)
- Axios
- CSS (Glassmorphism UI)

### Backend
- FastAPI
- RDKit
- Python
- Google Gemini API

### Deployment
- Frontend: Vercel
- Backend: Railway

---

## 📁 Project Structure
drug-admet-predictor/
│
├── backend/
│ ├── main.py
│ ├── utils/
│ │ ├── chemistry.py
│ │ ├── llm.py
│ ├── generated_images/
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── App.css
│ │ ├── components/
│ ├── components/
│ │ ├── ExampleButtons.jsx
│ │ ├── MoleculeCard.jsx
│ │ ├── PropertyTable.jsx
│ │ ├── SmilesInput.jsx
│ ├── package.json
│
└── README.md


---

## 📡 API Response Format

```json
{
  "success": true,
  "smiles": "CC(=O)Oc1ccccc1C(=O)O",
  "properties": {
    "molecular_weight": 180.16,
    "logp": 1.2,
    "h_bond_donors": 1,
    "h_bond_acceptors": 3,
    "tpsa": 63.6,
    "lipinski_pass": true
  },
  "image_url": "http://drug-admet-predictor-production.up.railway.app/images/515b1cc095234187b00f4f3020ce436a.png",
  "interpretation": "The molecule shows good drug-likeness with moderate lipophilicity..."
}

## 📊 Evaluation Mapping
| Dimension     | Implementation                                 |
| ------------- | ---------------------------------------------- |
| Correctness   | RDKit calculations + API working               |
| Code Quality  | Modular backend + reusable frontend components |
| UI/UX         | Clean card-based interface with visual clarity |
| Bonus         | LLM-based interpretation + molecule rendering  |
| Communication | This README + structured API response          |

💡 What I Would Improve With More Time
Add real-time 3D molecular visualization (WebGL / 3Dmol.js)
Improve LLM prompting for deeper ADMET reasoning
Add database to store predictions history
Deploy backend with GPU optimization for faster inference
Add login system for saved molecules
Add batch SMILES upload (CSV support)

⚠️ Note
This project uses free-tier LLM API (Gemini), which may have rate limits.
RDKit computations are fully local and deterministic.
👨‍💻 Author

Built as a full-stack AI/cheminformatics project combining:

Machine Learning concepts
Drug discovery fundamentals
Full-stack web development