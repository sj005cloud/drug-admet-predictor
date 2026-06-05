from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from utils.chemistry import (
    calculate_properties,
    generate_molecule_image
)

from utils.llm import generate_interpretation


app = FastAPI(
    title="Drug Candidate Property Predictor",
    description="Lightweight ADMET Screener",
    version="1.0.0"
)

app.mount(
    "/images",
    StaticFiles(directory="generated_images"),
    name="images"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SmilesRequest(BaseModel):
    smiles: str


@app.get("/")
def home():
    return {
        "message": "Drug Candidate Property Predictor API Running"
    }


@app.post("/predict")
def predict(request: SmilesRequest):
    try:
        # Calculate molecular properties
        properties = calculate_properties(
            request.smiles
        )

        # Generate molecule image
        image_filename = generate_molecule_image(
            request.smiles
        )

        # Generate Gemini interpretation
        interpretation = generate_interpretation(
            properties
        )

        return {
            "success": True,
            "smiles": request.smiles,
            "properties": properties,
            "image_url": f"http://127.0.0.1:8000/images/{image_filename}",
            "interpretation": interpretation
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )