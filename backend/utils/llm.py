import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_interpretation(properties: dict):
    """
    Generate a plain-English interpretation
    of molecular properties.
    """

    prompt = f"""
You are a pharmaceutical scientist.

Analyze the following molecular profile and provide exactly 2 concise sentences.

Properties:
- Molecular Weight: {properties['molecular_weight']}
- LogP: {properties['logp']}
- H-Bond Donors: {properties['h_bond_donors']}
- H-Bond Acceptors: {properties['h_bond_acceptors']}
- TPSA: {properties['tpsa']}
- Lipinski Pass: {properties['lipinski_pass']}

Keep the explanation simple and understandable.
"""

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash"
    )

    response = model.generate_content(prompt)

    return response.text.strip()