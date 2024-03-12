function copiarEnunciado() {
    var text = document.getElementById("copiarEnunciado").innerText; // Pegue o texto que você deseja copiar
    var textarea = document.createElement("textarea"); // Crie um elemento textarea
    textarea.value = text; // Defina o valor do textarea para o texto que você deseja copiar
    document.body.appendChild(textarea); // Adicione o textarea ao DOM
    textarea.select(); // Selecione o texto no textarea
    document.execCommand("copy"); // Copie o texto selecionado
    document.body.removeChild(textarea); // Remova o textarea do DOM

    // Atualize a mensagem
    document.getElementById('message').innerText = 'Enunciado da copiado com sucesso!';
}

document.getElementById('button-copiar').addEventListener('click', copiarEnunciado);

