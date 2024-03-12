const phrases = ["Bem-vindo(a) ao nosso site!", "Juntos,", "somos mais fortes!", "Estude, ", "pesquise... ", "Vai Brasil!"];
let currentPhrase = 0;
let currentLetter = 0;
const typingSpeed = 150; // Velocidade de digitação em milissegundos
const erasingSpeed = 100; // Velocidade de apagamento em milissegundos
const typingEffectElement = document.getElementById("typing-effect");

function typePhrase() {
  if (currentLetter < phrases[currentPhrase].length) {
    typingEffectElement.textContent = ": " + phrases[currentPhrase].substring(0, currentLetter + 1);
    currentLetter++;
    setTimeout(typePhrase, typingSpeed);
  } else {
    setTimeout(erasePhrase, 2000); // Espera 2 segundos antes de começar a apagar
  }
}

function erasePhrase() {
  if (currentLetter > 0) {
    typingEffectElement.textContent = ": " + phrases[currentPhrase].substring(0, currentLetter - 1);
    currentLetter--;
    setTimeout(erasePhrase, erasingSpeed);
  } else {
    currentPhrase = (currentPhrase + 1) % phrases.length;
    currentLetter = 0; // Reinicie currentLetter para começar a digitar a próxima frase
    setTimeout(typePhrase, typingSpeed);
  }
}

typePhrase(); // Inicia o efeito

