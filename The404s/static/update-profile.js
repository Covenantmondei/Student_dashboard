document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById("menuBtn");
    const closeSidebar = document.getElementById("closeSidebar");
    const sidebar = document.getElementById("sidebar");
    const darkModeToggle = document.getElementById("darkModeToggle");
    const profileForm = document.getElementById("profileForm");
    const profileImage = document.getElementById("profileImage");
    const profilePreview = document.getElementById("profilePreview");

    // Toggle Sidebar
    menuBtn.addEventListener("click", () => {
        sidebar.classList.add("active");
    });

    closeSidebar.addEventListener("click", () => {
        sidebar.classList.remove("active");
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



    // Load saved profile from localStorage
    function loadProfile() {
        const savedData = JSON.parse(localStorage.getItem("profileData"));
        if (savedData) {
            document.getElementById("dob").value = savedData.dob || "";
            document.getElementById("faculty").value = savedData.faculty || "";
            document.getElementById("course").value = savedData.course || "";
            document.getElementById("programmeType").value = savedData.programmeType || "Undergraduate";
            document.getElementById("entryMode").value = savedData.entryMode || "UTME";
            document.getElementById("session").value = savedData.session || "";
            document.getElementById("entryYear").value = savedData.entryYear || "";
            document.getElementById("semester").value = savedData.semester || "First Semester";

            if (savedData.profilePic) {
                profilePreview.src = savedData.profilePic;
            }
        }
    }
    loadProfile();

    // Handle Profile Image Upload
    profileImage.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                profilePreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle Form Submission
    profileForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const profileData = {
            dob: document.getElementById("dob").value.trim(),
            faculty: document.getElementById("faculty").value.trim(),
            course: document.getElementById("course").value.trim(),
            programmeType: document.getElementById("programmeType").value,
            entryMode: document.getElementById("entryMode").value,
            session: document.getElementById("session").value.trim(),
            entryYear: document.getElementById("entryYear").value.trim(),
            semester: document.getElementById("semester").value,
            profilePic: profilePreview.src
        };

        // Validation
        if (!profileData.dob || !profileData.faculty || !profileData.course || !profileData.session || !profileData.entryYear) {
            alert("Please fill in all fields.");
            return;
        }

        // Save profile data to localStorage
        localStorage.setItem("profileData", JSON.stringify(profileData));
        alert("Profile updated successfully!");

        
    });
});

