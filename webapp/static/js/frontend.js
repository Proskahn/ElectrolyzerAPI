document.addEventListener("DOMContentLoaded", () => {
  const compileBtn = document.getElementById("btn-compile");
  const evaluateBtn = document.getElementById("btn-evaluate");
  const compilePanel = document.getElementById("panel-compile");
  const evaluatePanel = document.getElementById("panel-evaluate");

  compileBtn.addEventListener("click", () => {
    compilePanel.classList.remove("hidden");
    evaluatePanel.classList.add("hidden");
    compileBtn.classList.add("bg-blue-500", "text-white");
    evaluateBtn.classList.remove("bg-blue-500", "text-white");
  });

  evaluateBtn.addEventListener("click", () => {
    compilePanel.classList.add("hidden");
    evaluatePanel.classList.remove("hidden");
    evaluateBtn.classList.add("bg-blue-500", "text-white");
    compileBtn.classList.remove("bg-blue-500", "text-white");
  });

  document.getElementById("compile-submit").addEventListener("click", async () => {
    const membrane = document.getElementById("membrane-select").value;
    const res = await fetch("/compile/membrane", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ membrane }),
    });
    const data = await res.json();
    document.getElementById("compile-response").textContent = data.message || "Membrane selected.";
  });

  document.getElementById("evaluate-submit").addEventListener("click", async () => {
    const density = parseFloat(document.getElementById("current-density").value);
    const res = await fetch("/evaluate/temperature", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ current_density: density }),
    });
    const data = await res.json();
    document.getElementById("evaluate-response").textContent = data.temperature
      ? `Optimal temperature: ${data.temperature} °C`
      : "Temperature evaluation failed.";
  });
});
