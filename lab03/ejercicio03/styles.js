// Establecer estilos para el body
document.body.style.fontFamily = 'Arial, sans-serif';
document.body.style.display = 'flex';
document.body.style.justifyContent = 'center';
document.body.style.alignItems = 'center';
document.body.style.height = '100vh';
document.body.style.margin = '0';

// Establecer estilos para el contenedor del juego
var gameContainer = document.getElementById('game-container');
gameContainer.style.textAlign = 'center';

// Establecer estilos para el contenedor de la palabra
var wordContainer = document.getElementById('word-container');
wordContainer.style.margin = '20px 0';
wordContainer.style.fontSize = '24px';

// Establecer estilos para el contenedor de las letras adivinadas
var guessesContainer = document.getElementById('guesses-container');
guessesContainer.style.margin = '10px 0';
guessesContainer.style.fontSize = '18px';

// Establecer estilos para el botón de reset
var resetButton = document.getElementById('reset-button');
resetButton.style.marginTop = '20px';
resetButton.style.padding = '10px 20px';
resetButton.style.fontSize = '16px';
resetButton.style.backgroundColor = '#007bff';
resetButton.style.color = 'white';
resetButton.style.border = 'none';
resetButton.style.borderRadius = '5px';
resetButton.style.cursor = 'pointer';

// Establecer estilos para el hover del botón de reset
resetButton.addEventListener('mouseover', () => {
  resetButton.style.backgroundColor = '#0056b3';
});

resetButton.addEventListener('mouseout', () => {
  resetButton.style.backgroundColor = '#007bff';
});
