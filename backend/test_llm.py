from utils.llm import generate_interpretation

properties = {
    "molecular_weight": 180.16,
    "logp": 1.31,
    "h_bond_donors": 1,
    "h_bond_acceptors": 3,
    "tpsa": 63.6,
    "lipinski_pass": True
}

print(
    generate_interpretation(properties)
)