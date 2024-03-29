
document.getElementById('sendButton').addEventListener('click', function (e) {
    e.preventDefault(); // Ainda útil se você estiver enviando um formulário via AJAX, por exemplo.

    // Mostra a mensagem de confirmação.
    document.getElementById('confirmationMessage').style.display = 'block';

    // Redireciona após um curto intervalo.
    setTimeout(function () {
        window.location.href = '../';
    }, 4000); // Ajuste conforme necessário.
});

