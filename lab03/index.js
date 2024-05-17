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

let main = document.createElement("main");
document.body.appendChild(main);

let mainDiv = document.createElement("div");
main.appendChild(mainDiv);

let label = document.createElement("p");
label.textContent = "Digite su clave secreta:";
label.style.fontSize = "1.5rem";
label.style.fontWeight = "bold";
mainDiv.appendChild(label);

let camp = document.createElement("p");
camp.style.fontSize = "1.5rem";
mainDiv.appendChild(camp);
camp.style.minHeight = "1.5rem";
camp.style.padding = "10px 10px";
camp.style.border = "1px solid black";
camp.style.backgroundColor = "#eee";
camp.style.display = "flex";
camp.style.alignContent = "center";

let keyboard = document.createElement("div");

for (let i = 0; i < 11; i++) {
  let key = document.createElement("button");
  let name = i;
  if (i == 10) {
    name = "Limpiar";
    key.style.gridColumn = "span 2";
  }
  key.textContent = name;
  key.style.height = "80px";
  keyboard.appendChild(key);
  key.addEventListener("click", () => {
    if (name == "Limpiar") {
      camp.textContent = "";
      return;
    }
    camp.textContent += name;
  });
  key.style.fontSize = "1.5rem";
}

mainDiv.appendChild(keyboard);

// Aquí van los estilos
document.documentElement.style.margin = 0;
document.documentElement.style.padding = 0;
document.body.style.margin = 0;
document.body.style.padding = 0;

// Aplicar estilos a main
document.body.style.height = "calc(100vh - 70px)";
main.style.width = "100vw";
main.style.height = "calc(100vh - 70px)";
main.style.display = "flex";
main.style.backgroundColor = "#ccc";
main.style.justifyContent = "center";
main.style.alignContent = "center";

mainDiv.style.width = "240px";
mainDiv.style.height = "100px";

keyboard.style.display = "grid";
keyboard.style.gridTemplateColumns = "1fr 1fr 1fr";
