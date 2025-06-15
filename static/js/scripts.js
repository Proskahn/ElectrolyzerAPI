async function chooseMembrane() {
    const responseDiv = document.getElementById('response');
    const membrane = prompt('Enter membrane (e.g., Nafion115, Nafion117):', 'Nafion115');
    if (!membrane) return;
    try {
        const response = await fetch('/api/v1/compile/choose-membrane', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ membrane })
        });
        if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
        const data = await response.json();
        responseDiv.innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        responseDiv.innerText = 'Error: ' + error.message;
    }
}

async function chooseCatalyst() {
    const responseDiv = document.getElementById('response');
    const catalyst = prompt('Enter catalyst (e.g., Platinum, Iridium):', 'Combination1');
    if (!catalyst) return;
    try {
        const response = await fetch('/api/v1/compile/choose-catalyst', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ catalyst })
        });
        if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
        const data = await response.json();
        responseDiv.innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        responseDiv.innerText = 'Error: ' + error.message;
    }
}

async function computeTemperature() {
    const responseDiv = document.getElementById('response');
    try {
        const response = await fetch('/api/v1/evaluate/compute-temperature');
        if (!response.ok) throw new Error(`HTTP ${response.status}: ${await response.text()}`);
        const data = await response.json();
        responseDiv.innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        responseDiv.innerText = 'Error: ' + error.message;
    }
}
