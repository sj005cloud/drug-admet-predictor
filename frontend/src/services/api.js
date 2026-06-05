import axios from "axios";

const API_BASE_URL = "https://drug-admet-predictor-production.up.railway.app";

export const predictMolecule = async (smiles) => {
  const response = await axios.post(
    `${API_BASE_URL}/predict`,
    {
      smiles: smiles,
    }
  );

  return response.data;
};