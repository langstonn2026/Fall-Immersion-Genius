document.addEventListener("DOMContentLoaded",() => {
    const form = document.getElementById("survey-form");

    form.addEventListener("submit",function(event) {
        event.preventDefault();

        // grabbing the values of the input fields from the form 
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const comments = document.getElementById("comments").value;

        if (name && email && comments) {
            alert(`form submitted succesfully!\nName: ${name}\nEmail:${email}\nComments:${comments}`);
        } else {
            alert("Please fill out all the fields");
        }
    });
});
