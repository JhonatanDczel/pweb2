let nav = document.createElement("nav");
let logo = document.createElement("img");
logo.src = "./img/logo-multired.jpg";
nav.appendChild(logo);
let logo2 = document.createElement("img");
logo2.src = "./img/Logo_BN.jpg";
logo2.style.height = "40px";
logo2.style.width = "auto";
logo2.style.alignSelf = "center";
nav.appendChild(logo2);
nav.style.display = "flex";
nav.style.justifyContent = "space-between";

document.body.appendChild(nav);
