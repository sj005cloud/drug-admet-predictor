from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Crippen
from rdkit.Chem import Lipinski
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import Draw
import uuid

import os


def calculate_properties(smiles: str):
    """
    Calculate ADMET-like molecular properties from a SMILES string.
    """

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid SMILES string")

    molecular_weight = round(Descriptors.MolWt(mol), 2)

    logp = round(Crippen.MolLogP(mol), 2)

    h_bond_donors = Lipinski.NumHDonors(mol)

    h_bond_acceptors = Lipinski.NumHAcceptors(mol)

    tpsa = round(rdMolDescriptors.CalcTPSA(mol), 2)

    lipinski_pass = (
        molecular_weight <= 500
        and logp <= 5
        and h_bond_donors <= 5
        and h_bond_acceptors <= 10
    )

    return {
        "molecular_weight": molecular_weight,
        "logp": logp,
        "h_bond_donors": h_bond_donors,
        "h_bond_acceptors": h_bond_acceptors,
        "tpsa": tpsa,
        "lipinski_pass": lipinski_pass,
    }


def generate_molecule_image(smiles: str):
    """
    Generate molecule image and return filename.
    """

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid SMILES string")

    filename = f"{uuid.uuid4().hex}.png"

    output_path = os.path.join(
        "generated_images",
        filename
    )

    Draw.MolToFile(
        mol,
        output_path,
        size=(500, 500)
    )

    return filename