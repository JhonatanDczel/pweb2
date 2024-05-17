const canvas = document.getElementById('hangmanCanvas');
const ctx = canvas.getContext('2d');
var wordContainer = document.getElementById('word-container');
var guessesContainer = document.getElementById('guesses-container');
var resetButton = document.getElementById('reset-button');

const words = ['javascript', 'html', 'css', 'python', 'react', 'angular', 'vue'];
let selectedWord = words[Math.floor(Math.random() * words.length)];
let guessedLetters = [];
let remainingAttempts = 6;

// Draw hangman
function drawHangman() {
  ctx.beginPath();
  ctx.moveTo(100, 350);
  ctx.lineTo(300, 350);
  ctx.stroke();

  if (remainingAttempts < 6) {
    ctx.beginPath();
    ctx.moveTo(200, 350);
    ctx.lineTo(200, 100);
    ctx.lineTo(250, 100);
    ctx.lineTo(200, 150);
    ctx.stroke();
  }

  if (remainingAttempts < 5) {
    ctx.beginPath();
    ctx.arc(200, 180, 30, 0, Math.PI * 2);
    ctx.stroke();
  }

  if (remainingAttempts < 4) {
    ctx.beginPath();
    ctx.moveTo(200, 210);
    ctx.lineTo(200, 280);
    ctx.stroke();
  }

  if (remainingAttempts < 3) {
    ctx.beginPath();
    ctx.moveTo(200, 220);
    ctx.lineTo(250, 250);
    ctx.stroke();
  }

  if (remainingAttempts < 2) {
    ctx.beginPath();
    ctx.moveTo(200, 220);
    ctx.lineTo(150, 250);
    ctx.stroke();
  }

  if (remainingAttempts < 1) {
    ctx.beginPath();
    ctx.moveTo(200, 280);
    ctx.lineTo(250, 320);
    ctx.stroke();
  }
}

// Display word with guessed letters
function displayWord() {
  let displayText = '';
  for (const letter of selectedWord) {
    if (guessedLetters.includes(letter)) {
      displayText += letter + ' ';
    } else {
      displayText += '_ ';
    }
  }
  wordContainer.textContent = displayText;
}

// Display guessed letters
function displayGuesses() {
  guessesContainer.textContent = `Remaining attempts: ${remainingAttempts}`;
}

// Check if the player won
function checkWin() {
  for (const letter of selectedWord) {
    if (!guessedLetters.includes(letter)) {
      return false;
    }
  }
  return true;
}

// Check if the player lost
function checkLose() {
  return remainingAttempts === 0;
}

// Handle letter guess
function guessLetter(letter) {
  if (!guessedLetters.includes(letter)) {
    guessedLetters.push(letter);
    if (!selectedWord.includes(letter)) {
      remainingAttempts--;
    }
    drawHangman();
    displayWord();
    displayGuesses();

    if (checkWin()) {
      alert('Congratulations! You won!');
      resetGame();
    } else if (checkLose()) {
      alert('Game over! The word was: ' + selectedWord);
      resetGame();
    }
  }
}

// Reset game
function resetGame() {
  selectedWord = words[Math.floor(Math.random() * words.length)];
  guessedLetters = [];
  remainingAttempts = 6;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawHangman();
  displayWord();
  displayGuesses();
}

// Event listeners
document.addEventListener('keydown', event => {
  if (event.keyCode >= 65 && event.keyCode <= 90) {
    guessLetter(event.key.toLowerCase());
  }
});

resetButton.addEventListener('click', resetGame);

// Initial setup
drawHangman();
displayWord();
displayGuesses();
