document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (!form) return;

    form.addEventListener("submit", function (event) {

        const name = document.querySelector('input[name="name"]').value.trim();
        const description = document.querySelector('textarea[name="description"]').value.trim();
        const location = document.querySelector('input[name="location"]').value.trim();
        const contact = document.querySelector('input[name="contact"]').value.trim();

        if (name === "" || description === "" || location === "" || contact === "") {
            alert("Please fill in all the fields.");
            event.preventDefault();
            return;
        }

        if (!/^[0-9]{10}$/.test(contact)) {
            alert("Please enter a valid 10-digit contact number.");
            event.preventDefault();
            return;
        }

        alert("Form submitted successfully!");
    });

});