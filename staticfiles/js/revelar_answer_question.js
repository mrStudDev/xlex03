document.getElementById("checkAnswerBtn").addEventListener("click", function () {
    // Pega todos os inputs do tipo radio com o nome 'answer'
    const answers = document.querySelectorAll("input[type=radio][name=answer]");
    const responseMessage = document.getElementById("responseMessage");
    // Itera sobre todos os inputs
    for (let answer of answers) {
        // Se o input foi selecionado
        if (answer.checked) {
            // Verifica o valor de data-correct
            if (answer.dataset.correct === "True") {
                responseMessage.textContent = "Parabéns!!! A sua resposta está correta! \uD83C\uDF89 \uD83E\uDD47 \uD83C\uDF88";
                //responseMessage.style.color = "green"; // opcional: colorir a mensagem
            } else {
                responseMessage.textContent = "Infelismente a sua resposta está incorreta!";
                responseMessage.style.color = "red"; // opcional: colorir a mensagem
            }
            break;  // Sai do loop após verificar
        }
    }
});
