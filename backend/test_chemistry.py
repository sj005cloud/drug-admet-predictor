from utils.chemistry import calculate_properties

smiles = "CC(=O)Oc1ccccc1C(=O)O"

result = calculate_properties(smiles)

print(result)