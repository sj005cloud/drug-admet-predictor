function SmilesInput({
  smiles,
  setSmiles,
  onPredict,
  loading,
}) {
  return (
    <div className="input-section">
      <input
        type="text"
        value={smiles}
        placeholder="Enter SMILES string"
        onChange={(e) =>
          setSmiles(e.target.value)
        }
      />

      <button
        onClick={onPredict}
        disabled={loading}
      >
        {loading
          ? "Analyzing..."
          : "Predict"}
      </button>
    </div>
  );
}

export default SmilesInput;