/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault();

    // clear previous error messages
    ["name", "email", "year", "color"].forEach(field => {
        $(`#${field}-err`).text("")
    });

    // Gather from data
    const name = $("#name").val();
    const email = $("#email").val();
    const year = parseInt($("#year").val());
    const color = $("#color").val();

    const data = { name, email, year, color };

    try {
        // Make AJAX POST request
        const response = await fetch("/api/get-lucky-num", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data),
        });

        const resp = await response.json();
        
        if (response.status === 400) {
            // Handle validation errors
            for (const [field, message] of Object.entries(resp.errors)) {
                $(`#${field}-err`).text(message);
            }
        }else {
            handleResponse(resp);
        }
    } catch (error) {
        console.error("Error: ", error);
        $("#result"). text("An unexpected error occured. please try again later.");
    }
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    const resultText = `YOUR LUCKY NUMBER IS ${resp.lucky_number} (${resp.number_facts.trivia}).\n Your birth year (${resp.name}'s year) fact is ${resp.number_facts.year}.\n Your fav color: ${resp.color}.`
    $("#lucky-results").text(resultText);
}


$("#lucky-form").on("submit", processForm);
