# 🧪 Drug Candidate Property Predictor — Lightweight ADMET Screener

A full-stack AI-powered web application that predicts ADMET-like molecular properties from SMILES strings using RDKit (cheminformatics) and LLM-based interpretation. Built as a lightweight drug discovery screening tool.

---

## 🚀 Live Demo

### 🔬 Frontend (Vercel)

https://drug-admet-predictor.vercel.app/

### 🧠 Backend API (Railway)

https://drug-admet-predictor-production.up.railway.app/

### 📌 API Endpoint

```http
POST /predict
```

---

## 🧬 Problem Statement

Build a web application that accepts a SMILES string and returns predicted ADMET-like properties using:

* Rule-based molecular property calculations (RDKit)
* LLM-generated interpretation (Gemini API)

---

## ⚙️ Features

### 🧪 Molecular Property Prediction (RDKit)

* Molecular Weight
* LogP (Lipophilicity)
* Hydrogen Bond Donors
* Hydrogen Bond Acceptors
* TPSA (Topological Polar Surface Area)
* Lipinski Rule of Five (Pass/Fail)

### 🤖 AI Interpretation (Gemini LLM)

* Generates a concise 2-sentence natural language explanation
* Explains drug-likeness and molecular behavior in simple terms
* Makes cheminformatics outputs easier to interpret

### 🎨 Frontend Features (React)

* SMILES input interface
* Example molecule buttons:

  * Aspirin
  * Caffeine
  * Ibuprofen
  * Paracetamol
  * Glucose
* Responsive card/table UI
* Lipinski Rule highlighting:

  * 🟢 Pass
  * 🔴 Fail
* Molecule structure visualization (RDKit-generated images)

### 🧠 Backend Features (FastAPI)

* `/predict` endpoint for SMILES input
* RDKit-based molecular descriptor computation
* Molecule image generation (PNG output)
* Gemini LLM integration for interpretation
* Static file serving for generated images
* CORS-enabled API for frontend communication

---

## 🧪 Example SMILES Inputs

| Molecule    | SMILES                                   |
| ----------- | ---------------------------------------- |
| Aspirin     | `CC(=O)Oc1ccccc1C(=O)O`                  |
| Caffeine    | `Cn1c(=O)c2c(ncn2C)n(c1=O)C`             |
| Ibuprofen   | `CC(C)Cc1ccc(cc1)C(C)C(=O)O`             |
| Paracetamol | `CC(=O)Nc1ccc(O)cc1`                     |
| Glucose     | `OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O` |

---

## 🏗️ Tech Stack

### 🖥️ Frontend

* React (Vite)
* React DOM
* Axios
* JavaScript (ES6+)
* CSS (Glassmorphism UI)

### ⚙️ Backend

* FastAPI
* RDKit
* Python 3.11+
* Google Gemini API
* Pillow

### 🌐 Deployment

* Frontend: Vercel
* Backend: Railway

---

## 📁 Project Structure

```text
drug-admet-predictor/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── utils/
│   │   ├── chemistry.py
│   │   └── llm.py
│   ├── generated_images/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── components/
│   │   │   ├── ExampleButtons.jsx
│   │   │   ├── MoleculeCard.jsx
│   │   │   ├── PropertyTable.jsx
│   │   │   └── SmilesInput.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 📡 API Response Format

```json
{
  "success": true,
  "smiles": "CC(=O)Oc1ccccc1C(=O)O",
  "properties": {
    "molecular_weight": 180.16,
    "logp": 1.31,
    "h_bond_donors": 1,
    "h_bond_acceptors": 3,
    "tpsa": 63.60,
    "lipinski_pass": true
  },
  "image_url": "http://drug-admet-predictor-production.up.railway.app/images/515b1cc095234187b00f4f3020ce436a.png",
  "interpretation": "The molecule shows good drug-likeness with moderate lipophilicity and favorable ADMET properties."
}
```

---

## 📊 Evaluation Mapping

| Dimension     | Implementation                                      |
| ------------- | --------------------------------------------------- |
| Correctness   | RDKit calculations + working API                    |
| Code Quality  | Modular FastAPI backend + reusable React components |
| UI/UX         | Responsive card-based interface                     |
| Bonus         | Gemini interpretation + molecule visualization      |
| Communication | Structured documentation and API design             |

---

## 🚀 Local Setup

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## 💡 What I Would Improve With More Time

* Add interactive 3D molecular visualization (3Dmol.js/WebGL)
* Improve LLM prompting for deeper ADMET reasoning
* Add prediction history database
* Support batch SMILES upload (CSV)
* Add PDF report export
* Add authentication and saved molecule profiles
* Add additional descriptors and drug-likeness metrics

---

## ⚠️ Notes

* This project uses the free-tier Gemini API, so rate limits may apply.
* RDKit computations are performed locally and are deterministic.
* Descriptor values are calculated using RDKit's built-in implementations (Crippen LogP, Lipinski descriptors, TPSA).
* Generated molecule images are stored in the backend `generated_images/` directory.

---

## 👨‍💻 Author

Built as a full-stack AI + cheminformatics project combining:

* Artificial Intelligence
* Drug Discovery Fundamentals
* RDKit Cheminformatics
* FastAPI Backend Development
* React Frontend Development

---

## ⭐ Acknowledgements

* RDKit Open-Source Cheminformatics Library
* Google Gemini API
* FastAPI
* React
* Vite
