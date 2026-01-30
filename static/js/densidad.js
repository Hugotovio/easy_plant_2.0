function calcularDensidad() {
  const temperatura = document.getElementById("temp_densidad").value;
  const api = document.getElementById("api_densidad").value;

  fetch("https://web-production-e08df.up.railway.app/calcular-densidad", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      temperatura: Number(temperatura),
      api60: Number(api)
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      document.getElementById("resultadoDensidad").innerHTML =
        `<span class="text-danger">${data.error}</span>`;
    } else {
      document.getElementById("resultadoDensidad").innerHTML =
        `Densidad: ${data.densidad_kg_gal} kg/gal`;
    }
  })
  .catch(() => {
    document.getElementById("resultadoDensidad").innerHTML =
      `<span class="text-danger">Error de conexión</span>`;
  });
}
