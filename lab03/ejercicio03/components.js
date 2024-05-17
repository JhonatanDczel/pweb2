// Crear el contenedor del juego
var gameContainer = document.createElement("div");
gameContainer.id = "game-container";

// Crear el lienzo del ahorcado
const hangmanCanvas = document.createElement("canvas");
hangmanCanvas.id = "hangmanCanvas";
hangmanCanvas.width = "400";
hangmanCanvas.height = "400";
gameContainer.appendChild(hangmanCanvas);

// Crear el contenedor de la palabra
var wordContainer = document.createElement("div");
wordContainer.id = "word-container";
gameContainer.appendChild(wordContainer);

// Crear el contenedor de las letras adivinadas
var guessesContainer = document.createElement("div");
guessesContainer.id = "guesses-container";
gameContainer.appendChild(guessesContainer);

// Crear el botón de reset
resetButton = document.createElement("button");
resetButton.id = "reset-button";
resetButton.textContent = "Reset";
gameContainer.appendChild(resetButton);

// Agregar el contenedor del juego al body
document.body.appendChild(gameContainer);
