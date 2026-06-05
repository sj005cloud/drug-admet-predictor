from fastapi import FastAPI, HTTPException, Request
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

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "generated_images"

# ensure folder exists in production
os.makedirs(IMAGE_DIR, exist_ok=True)

app.mount(
    "/images",
    StaticFiles(directory=str(IMAGE_DIR)),
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
def predict(request_data: SmilesRequest, request: Request):
    try:

        # Calculate molecular properties
        properties = calculate_properties(
            request_data.smiles
        )

        # Generate molecule image
        image_filename = generate_molecule_image(
            request_data.smiles
        )

        # Generate Gemini interpretation
        interpretation = generate_interpretation(
            properties
        )

        image_url = (
            str(request.base_url)
            + f"images/{image_filename}"
        )

        return {
            "success": True,
            "smiles": request_data.smiles,
            "properties": properties,
            "image_url": image_url,
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