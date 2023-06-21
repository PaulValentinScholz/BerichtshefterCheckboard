// script.js

// Check the current mode stored in localStorage
const currentMode = localStorage.getItem('mode');

// Set the initial mode based on the value in localStorage
if (currentMode === 'dark') {
    enableDarkMode();
} else {
    enableLightMode();
}

// Toggle between light and dark mode when the switch is clicked
document.getElementById('modeSwitch').addEventListener('change', function () {
    if (this.checked) {
        enableDarkMode();
    } else {
        enableLightMode();
    }
});

// Enable dark mode
function enableDarkMode() {
    document.body.classList.add('dark-mode');
    localStorage.setItem('mode', 'dark');
}

// Enable light mode
function enableLightMode() {
    document.body.classList.remove('dark-mode');
    localStorage.setItem('mode', 'light');
}
