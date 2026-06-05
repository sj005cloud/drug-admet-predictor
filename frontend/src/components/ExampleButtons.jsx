function ExampleButtons({ onSelect }) {
  const examples = [
    { name: "Aspirin", smiles: "CC(=O)Oc1ccccc1C(=O)O" },
    { name: "Caffeine", smiles: "Cn1c(=O)c2c(ncn2C)n(c1=O)C" },
    { name: "Ibuprofen", smiles: "CC(C)Cc1ccc(cc1)C(C)C(=O)O" },
    { name: "Paracetamol", smiles: "CC(=O)Nc1ccc(O)cc1" },
    { name: "Glucose", smiles: "OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O" },
  ];

  return (
    <div className="examples">
      {examples.map((m) => (
        <button
          key={m.name}
          onClick={() => onSelect(m.smiles)}
          className="example-btn"
        >
          🧪 {m.name}
        </button>
      ))}
    </div>
  );
}

export default ExampleButtons;