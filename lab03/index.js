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
camp.style.overflow = "hidden";
let keyboard = document.createElement("div");

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

let numbers = Array.from({ length: 10 }, (_, i) => i); 
numbers = shuffle(numbers); 

for (let i = 0; i <= 10; i++) {
  let key = document.createElement("button");
  let name = i < 10 ? numbers[i] : "Limpiar"; 
  if (i == 10) {
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

document.documentElement.style.margin = 0;
document.documentElement.style.padding = 0;
document.body.style.margin = 0;
document.body.style.padding = 0;

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
