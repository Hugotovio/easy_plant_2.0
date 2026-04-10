function calcularDensidad() {
  const temperatura = document.getElementById("temp_densidad").value;
  const api = document.getElementById("api_densidad").value;

  fetch("https://backenddensidad-production.up.railway.app/calcular-densidad", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      temperatura: Number(temperatura),
      api: Number(api)   // 🔥 CORREGIDO
    })
  })
  .then(res => res.json())
  .then(data => {
    console.log(data);

    if (data.error) {
      document.getElementById("resultadoDensidad").innerHTML =
        `<span class="text-danger">${data.error}</span>`;
    } else {
      // 🔥 CORREGIDO (AQUÍ ESTÁ LA CLAVE)
      document.getElementById("resultadoDensidad").innerHTML =
        `Densidad: ${data.densidad_base.toFixed(3)} kg/gal`;
    }
  })
  .catch(() => {
    document.getElementById("resultadoDensidad").innerHTML =
      `<span class="text-danger">Error de conexión</span>`;
  });
}