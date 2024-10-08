// open the menu
function toggleMenu() {
    const menu = document.getElementById('category-menu');
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

// to hide the menu when not in use
window.onclick = function(event) {
    if (!event.target.matches('.menu-icon')) {
        const menu = document.getElementById('category-menu');
        if (menu.style.display === "block") {
            menu.style.display = "none";
        }
    }
};


function toggleMenu() {
    const menu = document.getElementById('category-menu');
    menu.classList.toggle('show'); // Toggle the 'show' class to slide in/out
}

// Close the menu when clicking outside of it
window.onclick = function(event) {
    const menu = document.getElementById('category-menu');
    if (!event.target.matches('.menu-icon') && menu.classList.contains('show')) {
        menu.classList.remove('show');
    }
};


// Get the current URL path (e.g., '/sports.html')
    const currentPage = window.location.pathname.split("/").pop();

    // Get all menu links
    const menuLinks = document.querySelectorAll("#category-menu li a");

    // Loop through each link and compare its href attribute with the current page
    menuLinks.forEach(link => {
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active"); // Add the "active" class to the matching link
        }
    });