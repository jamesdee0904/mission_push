document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("learnMoreBtn");
    if (button) {
        button.addEventListener("click", () => {
            alert("You are learning Flask step by step!");
        });
    }
});
