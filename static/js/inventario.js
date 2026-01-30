document.addEventListener("DOMContentLoaded", async () => {
  const tbody = document.querySelector("#tablaInventario tbody");

  try {
    const response = await fetch("/inventario");
    const data = await response.json();

    data.forEach(item => {
      const fila = `
        <tr>
          <td>${item.tanque}</td>
          <td>${item.api}</td>
          <td>${item.temperatura}</td>
          <td>${item.volumen_calculado}</td>
          <td>${new Date(item.fecha).toLocaleString()}</td>
        </tr>
      `;
      tbody.innerHTML += fila;
    });
  } catch (error) {
    console.error("Error cargando inventario:", error);
  }
});
