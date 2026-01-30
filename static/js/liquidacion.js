document.getElementById('calculation-form')
  .addEventListener('submit', function(event) {

  event.preventDefault();

  const formData = new FormData(this);
  const data = Object.fromEntries(formData.entries());

  fetch('/calculate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(result => {
    // AQUÍ pegas tu código actual de resultados
  })
  .catch(error => {
    document.getElementById('results').innerHTML =
      `<p class="bold">Error: ${error.message}</p>`;
  });
});
