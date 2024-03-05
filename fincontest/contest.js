"use strict";

// TOGGLE DARK
const sunIcon = document.getElementById("sunIcon"),
  moonIcon = document.getElementById("moonIcon"),
  userTheme = localStorage.getItem("theme"),
  toggleBtn = document.getElementById("light__to--dark");

// TOGGLING BTN ACTIVE CLASS
const btnToggle = () => {
  moonIcon.classList.toggle("hidden");
  sunIcon.classList.toggle("hidden");
};

// CHECKING SYSTEM & LOCALSTORAGE THEME
const themeCheck = () => {
  if (userTheme === "dark") {
    document.documentElement.classList.add("dark");
    moonIcon.classList.add("hidden");
    return;
  }
  sunIcon.classList.add("hidden");
};

// SWITCHING THEME CONDITIONALLY
const themeSwitch = () => {
  if (document.documentElement.classList.contains("dark")) {
    document.documentElement.classList.remove("dark");
    localStorage.setItem("theme", "light");
    btnToggle();
    return;
  }
  document.documentElement.classList.add("dark");
  localStorage.setItem("theme", "dark");
  btnToggle();
};

// MANUALLY SWITCHING THEME
toggleBtn.addEventListener("click", themeSwitch);

// WINDOW RELOAD THEME CHECK
themeCheck();
// TOGGLE DARK
