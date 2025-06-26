document.getElementById("weather-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const city = document.getElementById("city").value;
  const resultDiv = document.getElementById("result");
  resultDiv.classList.remove("hidden");

  try {
    const res = await fetch(`http://127.0.0.1:8000/weather?city_name=${city}&units=imperial`);
    if (!res.ok) throw new Error("City not found");

    const data = await res.json();

    resultDiv.innerHTML = `
      <h2>${data.city}</h2>
      <p><strong>${data.temperature}° F</strong> - ${data.description}</p>
      <p>High: ${data.temp_max}° | Low: ${data.temp_min}°</p>
    `;
  } catch (err) {
    resultDiv.innerHTML = `<p style="color:red;">${err.message}</p>`;
  }
});