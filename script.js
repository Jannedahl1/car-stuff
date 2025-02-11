document.addEventListener("DOMContentLoaded", function() {
    const makeSelect = document.getElementById("makeSelect");
    const modelSelect = document.getElementById("modelSelect");

    // Fetch car makes from the correct endpoint
    fetch("/api/makes")
        .then(response => response.json())
        .then(data => {
            // Populate the make dropdown with the distinct makes from the database
            data.makes.forEach(make => {
                const option = document.createElement("option");
                option.value = make;
                option.textContent = make;
                makeSelect.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching makes:", error));

    // Event listener for when a make is selected
    makeSelect.addEventListener("change", function() {
        const selectedMake = makeSelect.value;

        // Clear the model dropdown
        modelSelect.innerHTML = '<option value="" disabled selected>Select a car model</option>';
        modelSelect.disabled = true;

        // Fetch models for the selected make
        if (selectedMake) {
            fetch(`/api/models?make=${selectedMake}`)
                .then(response => response.json())
                .then(data => {
                    // Populate the model dropdown with models for the selected make
                    data.models.forEach(model => {
                        const option = document.createElement("option");
                        option.value = model;
                        option.textContent = model;
                        modelSelect.appendChild(option);
                    });
                    modelSelect.disabled = false;
                })
                .catch(error => console.error("Error fetching models:", error));
        }
    });
});
