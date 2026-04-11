function calcularDensidad() {
  const temperatura = document.getElementById("temp_densidad").value;
  const api = document.getElementById("api_densidad").value;

  fetch("https://backenddensidad-production.up.railway.app/calcular-densidad", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      temperatura: Number(temperatura),
      api: Number(api)
    })
  })
  .then(res => res.json())
  .then(data => {
    console.log(data);

    if (data.error) {
      document.getElementById("resultadoDensidad").innerHTML =
        `<div style="color:red;">${data.error}</div>`;
    } else {
      const d = data.densidad;

      document.getElementById("resultadoDensidad").innerHTML = `
        <div style="
          background: #f8f9fa;
          border-radius: 10px;
          padding: 15px;
          box-shadow: 0 2px 6px rgba(0,0,0,0.1);
          max-width: 350px;
        ">
          <div style="font-weight: bold; margin-bottom: 10px; color: #333;">
            Densidad
          </div>

          <table style="
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
          ">
            <thead>
              <tr style="border-bottom: 1px solid #ddd;">
                <th style="text-align: left; padding: 6px;">Unidad</th>
                <th style="text-align: right; padding: 6px;">Valor</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding: 6px;">kg/gal</td>
                <td style="padding: 6px; text-align: right;">${d.kg_gal.toFixed(3)}</td>
              </tr>
              <tr style="background: #f1f1f1;">
                <td style="padding: 6px;">kg/m³</td>
                <td style="padding: 6px; text-align: right;">${d.kg_m3.toFixed(2)}</td>
              </tr>
              <tr>
                <td style="padding: 6px;">g/cm³</td>
                <td style="padding: 6px; text-align: right;">${d.g_cm3.toFixed(4)}</td>
              </tr>
              <tr style="background: #f1f1f1;">
                <td style="padding: 6px;">lb/gal</td>
                <td style="padding: 6px; text-align: right;">${d.lb_gal.toFixed(3)}</td>
              </tr>
            </tbody>
          </table>
        </div>
      `;
    }
  })
  .catch(() => {
    document.getElementById("resultadoDensidad").innerHTML =
      `<div style="color:red;">Error de conexión</div>`;
  });
}