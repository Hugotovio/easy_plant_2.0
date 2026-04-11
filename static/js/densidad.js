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
        `<div class="text-danger">${data.error}</div>`;
    } else {
      const d = data.densidad;

      document.getElementById("resultadoDensidad").innerHTML = `
        <div style="
          background: #f8f9fa;
          border-radius: 10px;
          padding: 15px;
          box-shadow: 0 2px 6px rgba(0,0,0,0.1);
          max-width: 300px;
        ">
          <div style="font-weight: bold; margin-bottom: 10px; color: #333;">
            Densidad
          </div>

          <div style="display: flex; justify-content: space-between;">
            <span>kg/gal:</span>
            <span>${d.kg_gal.toFixed(3)}</span>
          </div>

          <div style="display: flex; justify-content: space-between;">
            <span>kg/m³:</span>
            <span>${d.kg_m3.toFixed(2)}</span>
          </div>

          <div style="display: flex; justify-content: space-between;">
            <span>g/cm³:</span>
            <span>${d.g_cm3.toFixed(4)}</span>
          </div>
          
          <div style="display: flex; justify-content: space-between;">
            <span>lb/gal:</span>
            <span>${d.lb_gal.toFixed(3)}</span>
          </div>
        </div>
      `;
    }
  })
  .catch(() => {
    document.getElementById("resultadoDensidad").innerHTML =
      `<div class="text-danger">Error de conexión</div>`;
  });
}