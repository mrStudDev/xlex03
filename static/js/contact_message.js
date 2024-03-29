
document.getElementById('sendButton').addEventListener('click', function (e) {
    e.preventDefault(); // Previne a submissão normal do formulário

    var formData = new FormData(document.querySelector('form'));

    fetch('/contato/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
    })
        .then(response => response.json()) // Converte a resposta em JSON
        .then(data => {
            if (data.success) {
                // Mostra a mensagem de confirmação
                document.getElementById('confirmationMessage').style.display = 'block';

                // Redireciona após um curto intervalo
                setTimeout(function () {
                    window.location.href = '../';
                }, 4000);
            } else {
                alert('Houve um erro ao enviar a mensagem. Por favor, tente novamente.');
            }
        })
});

