document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.getElementById("menuBtn");
    const closeSidebar = document.getElementById("closeSidebar");
    const sidebar = document.getElementById("sidebar");
    const darkModeToggle = document.getElementById("darkModeToggle");

    // Toggle Sidebar
    menuBtn.addEventListener("click", () => {
        sidebar.classList.toggle("open");
    });

    closeSidebar.addEventListener("click", () => {
        sidebar.classList.remove("open");
    });

    // Toggle Dark Mode
    darkModeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");

        // Save preference to localStorage
        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
        } else {
            localStorage.setItem("darkMode", "disabled");
        }
    });

    // Load Dark Mode Preference
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
    }
});