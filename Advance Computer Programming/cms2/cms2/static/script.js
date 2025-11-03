document.addEventListener("DOMContentLoaded", () => {
    const fetchBtn = document.getElementById("fetchBtn");
    if (fetchBtn) {
        fetchBtn.addEventListener("click", async () => {
            try {
                const res = await fetch("/api/users");
                const data = await res.json();
                const ul = document.getElementById("userList");
                ul.innerHTML = "";
                Object.keys(data).forEach(username => {
                    const li = document.createElement("li");
                    const info = data[username];
                    li.textContent = `${username} → ${JSON.stringify(info)}`;
                    ul.appendChild(li);
                });
            } catch (err) {
                console.error("Error fetching users:", err);
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {
    console.log("Flask app loaded successfully!");
});

document.addEventListener("DOMContentLoaded", () => {
    console.log("Flask app loaded!");
});
