function MoleculeCard({ imageUrl, interpretation }) {
  if (!imageUrl) return null;

  return (
    <>
      <div className="card">
        <h2>Molecule Structure</h2>

        <img
          src={imageUrl}
          alt="Molecule"
          className="molecule-image"
        />
      </div>

      {interpretation && (
        <div className="card">
          <h2>AI Interpretation</h2>

          <p className="interpretation">
            {interpretation}
          </p>
        </div>
      )}
    </>
  );
}

export default MoleculeCard;