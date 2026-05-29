// Intelligence Deployment Logic
document.querySelector('#deploy-btn').addEventListener('click', async () => {
  const signal = document.querySelector('#input-signal').value;
  if (!signal) return;

  const loading = document.querySelector('#loading-indicator');
  const results = document.querySelector('#results-section');
  const deployBtn = document.querySelector('#deploy-btn');

  loading.style.display = 'block';
  deployBtn.disabled = true;
  results.classList.remove('visible');

  setTimeout(() => {
    loading.style.display = 'none';
    deployBtn.disabled = false;
    results.classList.add('visible');
  }, 2000);
});

// Impact Calculator Logic
document.querySelector('#calc-btn').addEventListener('click', () => {
  const capex = parseFloat(document.querySelector('#calc-capex').value);
  const social = parseFloat(document.querySelector('#calc-social').value);
  const resultDiv = document.querySelector('#calc-result');

  if (isNaN(capex) || isNaN(social)) {
    resultDiv.style.display = 'block';
    resultDiv.textContent = "Error: Ingrese valores válidos.";
    return;
  }

  const impactScore = (capex * (social / 100) * 1.25).toFixed(2);
  resultDiv.style.display = 'block';
  resultDiv.innerHTML = `
    <strong>Proyección PND 2026:</strong><br>
    Valor Agregado Social: $${impactScore}M
  `;
});

// Lente Verde IA Logic (Unsupervised Learning Simulator)
document.querySelector('#ai-run-btn').addEventListener('click', () => {
  const runBtn = document.querySelector('#ai-run-btn');
  const resultsDiv = document.querySelector('#ai-results');
  
  runBtn.textContent = "Procesando Algoritmo...";
  runBtn.disabled = true;

  // Simulate clustering calculations
  setTimeout(() => {
    runBtn.textContent = "Clusterización Completada";
    resultsDiv.style.display = 'flex';
    
    // Detailed analysis in console for the strategist
    console.log("--- RESULTADOS MODELO NO SUPERVISADO (LENTE VERDE) ---");
    console.log("Variables: Intensidad Carbono, Riesgo Hídrico, Estabilidad Social.");
    console.log("Cluster Alfa (Líderes): Antioquia, Atlántico, Santander.");
    console.log("Cluster Beta (Críticos): Chocó, Putumayo, Cauca.");
    console.log("Cluster Gamma (Fósiles): Cesar, Casanare, La Guajira.");
  }, 2500);
});

export function updateResults(data) {
  const { radar, linkedin, networking, consulting } = data;
  document.querySelector('#content-radar').textContent = radar;
  document.querySelector('#content-linkedin').textContent = linkedin;
  document.querySelector('#content-networking').textContent = networking;
  document.querySelector('#content-consulting').textContent = consulting;
  document.querySelector('#results-section').classList.add('visible');
}
