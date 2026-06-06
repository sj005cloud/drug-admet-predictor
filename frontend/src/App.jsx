import { useState } from "react";

import "./App.css";

import SmilesInput from "./components/SmilesInput";
import ExampleButtons from "./components/ExampleButtons";
import PropertyTable from "./components/PropertyTable";
import MoleculeCard from "./components/MoleculeCard";

import { predictMolecule } from "./services/api";

function App() {
  const [smiles, setSmiles] = useState("");
  const [selectedMolecule, setSelectedMolecule] =
    useState("Custom Molecule");
    const [predictedMolecule, setPredictedMolecule] =
  useState("Custom Molecule");

  const [loading, setLoading] = useState(false);
  const [properties, setProperties] = useState(null);
  const [imageUrl, setImageUrl] = useState("");
  const [interpretation, setInterpretation] =
    useState("");

  const handlePredict = async () => {
    if (!smiles.trim()) {
      alert("Please enter a SMILES string");
      return;
    }

    try {
      setLoading(true);

      const result =
        await predictMolecule(smiles);

      if (!result || !result.properties) {
        alert("Invalid response from server");
        return;
      }

      setProperties(
        result.properties || null
      );

      setImageUrl(
        result.image_url || ""
      );

      setInterpretation(
        result.interpretation || ""
      );
      setPredictedMolecule(
  selectedMolecule
);

    } catch (error) {

      console.error(error);

      alert(
        error?.response?.data?.detail ||
        "Prediction failed"
      );

    } finally {

      setLoading(false);
    }
  };

  return (
    <>
      <video
        autoPlay
        loop
        muted
        playsInline
        className="video-bg"
      >
        <source
          src="/molecule-bg4.mp4"
          type="video/mp4"
        />
      </video>

      <div className="container">

        <div className="header">

          <div className="tag">
            AI DRUG DISCOVERY PLATFORM
          </div>

          <div className="title-row">
            <img
              src="/logo3.PNG"
              alt="Logo"
              className="site-logo"
            />

            <h1>
              Drug ADMET Predictor
            </h1>
          </div>

          <p>
            Computational Screening for Drug Candidates
          </p>

        </div>

        <ExampleButtons
          onSelect={(smiles, name) => {
            setSmiles(smiles);
            setSelectedMolecule(name);
          }}
          selectedMolecule={
            selectedMolecule
          }
        />

        <SmilesInput
          smiles={smiles}
          setSmiles={(value) => {
            setSmiles(value);
            setSelectedMolecule(
              "Custom Molecule"
            );
          }}
          onPredict={handlePredict}
          loading={loading}
        />

        <PropertyTable
          properties={properties}
          moleculeName={
            predictedMolecule
          }
        />

        <MoleculeCard
          imageUrl={imageUrl}
          interpretation={
            interpretation
          }
        />

      </div>
    </>
  );
}

export default App;