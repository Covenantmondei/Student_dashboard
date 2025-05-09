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
});




document.addEventListener("DOMContentLoaded", () => {
    const facultySelect = document.getElementById("faculty");
    const deptSelect = document.getElementById("course_of_study");

    facultySelect.addEventListener("change", function () {
        const selectedFaculty = this.value;

        fetch(`${getDepartmentsUrl}?faculty=${encodeURIComponent(selectedFaculty)}`)
            .then(response => response.json())
            .then(data => {
                deptSelect.innerHTML = '<option value="select">--Select Department--</option>';
                data.departments.forEach(dept => {
                    const option = document.createElement("option");
                    option.value = dept;
                    option.textContent = dept;
                    deptSelect.appendChild(option);
                });
            });
    });
});
