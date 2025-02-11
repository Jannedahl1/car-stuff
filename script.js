document.getElementById("find-issues").addEventListener("click", function () {
    const carModel = document.getElementById("car-model").value;
    const issuesList = document.getElementById("issues");

    // Clear previous issues
    issuesList.innerHTML = "";

    if (carModel) {
        let issues = [];

        // Add common issues for each car model
        switch (carModel) {
            case "toyota-corolla-2015":
                issues = [
                    "Engine stalling while idling",
                    "Transmission slipping",
                    "Brake pads wearing out too quickly"
                ];
                break;
            case "honda-civic-2018":
                issues = [
                    "AC not cooling properly",
                    "Uneven tire wear",
                    "Check engine light turns on frequently"
                ];
                break;
            case "ford-focus-2017":
                issues = [
                    "Steering wheel shakes when braking",
                    "Water leaking into the interior",
                    "Fuel efficiency lower than expected"
                ];
                break;
            default:
                issues = ["No issues found for this model"];
        }

        // Display the issues in a list
        issues.forEach(issue => {
            const li = document.createElement("li");
            li.textContent = issue;
            issuesList.appendChild(li);
        });
    } else {
        alert("Please select a car model.");
    }
});
