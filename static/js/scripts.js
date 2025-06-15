async function chooseMembrane() {
    const responseDiv = document.getElementById('response');
    try {
        const response = await fetch('/api/v1/compile/choose-membrane', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ membrane: 'Nafion115' }) // Placeholder membrane
        });
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
        const data = await response.json();
        responseDiv.innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        responseDiv.innerText = 'Error: ' + error.message;
    }
}