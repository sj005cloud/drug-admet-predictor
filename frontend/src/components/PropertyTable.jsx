function PropertyTable({ properties }) {
  if (!properties) return null;

  return (
    <div className="card">
      <h2>🔬 Molecule Analysis</h2>

      <table>
        <tbody>
          <tr>
            <td>Molecular Weight</td>
            <td>{properties.molecular_weight}</td>
          </tr>

          <tr>
            <td>LogP</td>
            <td>{properties.logp}</td>
          </tr>

          <tr>
            <td>H-Bond Donors</td>
            <td>{properties.h_bond_donors}</td>
          </tr>

          <tr>
            <td>H-Bond Acceptors</td>
            <td>{properties.h_bond_acceptors}</td>
          </tr>

          <tr>
            <td>TPSA</td>
            <td>{properties.tpsa}</td>
          </tr>

          <tr>
            <td>Lipinski Rule</td>
            <td>
              <span
                className={
                  properties.lipinski_pass
                    ? "badge-pass"
                    : "badge-fail"
                }
              >
                {properties.lipinski_pass
                  ? "PASS"
                  : "FAIL"}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default PropertyTable;