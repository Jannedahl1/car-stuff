// Fetch car makes and models from the Flask API
fetch('http://127.0.0.1:5000/api/cars')
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log the response to check the data structure

        const carSelect = document.getElementById('carSelect');

        // Check if data is an array and contains elements
        if (Array.isArray(data) && data.length > 0) {
            // Populate dropdown with car makes and models
            data.forEach(car => {
                const option = document.createElement('option');
                option.value = car.make + ' ' + car.model;
                option.text = car.make + ' ' + car.model;
                carSelect.appendChild(option);
            });
        } else {
            console.log('No data found or incorrect format');
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
