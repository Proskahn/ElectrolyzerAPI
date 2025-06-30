async function configureElectrolyzer() {
    const form = document.getElementById("configureForm");
    const formData = new FormData(form);
    const data = {};

    formData.forEach((value, key) => {
        data[key] = parseFloat(value);
    });

    try {
        const response = await fetch("/compile/configure_electrolyzer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        displayResponse(result);
    } catch (error) {
        displayResponse({ error: "Configuration failed: " + error });
    }
}

async function computeOpenCircuitVoltage() {
    const temperature = parseFloat(document.getElementById("ocv_temperature").value);
    const data = {
        temperature: temperature,
        waterflow: 1.0,
        pressure: 1.0,
        R_membrane: 0.1,
        i0_anode: 0.0001,
        i0_cathode: 0.0001,
        alpha_anode: 0.5,
        alpha_cathode: 0.5,
        A: 0.01,
        GDL_thickness: 0.0001,
        channel_width: 0.001,
        channel_depth: 0.001
    };

    try {
        const response = await fetch("/evaluate/compute-open-circuit-voltage", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        displayResponse(result);
    } catch (error) {
        displayResponse({ error: "OCV computation failed: " + error });
    }
}

async function computeOhmPotential() {
    const R_membrane = parseFloat(document.getElementById("ohm_r_membrane").value);
    const data = {
        temperature: 298.15,
        waterflow: 1.0,
        pressure: 1.0,
        R_membrane: R_membrane,
        i0_anode: 0.0001,
        i0_cathode: 0.0001,
        alpha_anode: 0.5,
        alpha_cathode: 0.5,
        A: 0.01,
        GDL_thickness: 0.0001,
        channel_width: 0.001,
        channel_depth: 0.001
    };

    try {
        const response = await fetch("/evaluate/compute-ohm-potential", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        displayResponse(result);
    } catch (error) {
        displayResponse({ error: "Ohmic potential computation failed: " + error });
    }
}

async function predictLife() {
    try {
        const response = await fetch("/evaluate/life-prediction", {
            method: "POST"
        });

        const result = await response.json();
        displayResponse(result);
    } catch (error) {
        displayResponse({ error: "Life prediction failed: " + error });
    }
}

function displayResponse(result) {
    const output = document.getElementById("response");
    output.textContent = JSON.stringify(result, null, 2);
}
