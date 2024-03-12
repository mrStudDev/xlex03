function copiarEmenta() {
    var text = document.getElementById("copiarEmenta").innerText; // Pegue o texto que você deseja copiar
    var textarea = document.createElement("textarea"); // Crie um elemento textarea
    textarea.value = text; // Defina o valor do textarea para o texto que você deseja copiar
    document.body.appendChild(textarea); // Adicione o textarea ao DOM
    textarea.select(); // Selecione o texto no textarea
    document.execCommand("copy"); // Copie o texto selecionado
    document.body.removeChild(textarea); // Remova o textarea do DOM

    // Atualize a mensagem
    document.getElementById('message').innerText = 'Ementa copiada com sucesso! \nCopiado: Ementa + Tipo da Decisão, Ministro Relator, Orgão Julgador, Data Publicação e o Número do Processo.';
}

document.getElementById('button-copiar').addEventListener('click', copiarEmenta);

