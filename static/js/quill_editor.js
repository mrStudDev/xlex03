document.addEventListener("DOMContentLoaded", function () {
    // Inicialização do Quill
    var quillContent = document.querySelector('#editor-content') ? new Quill('#editor-content', { theme: 'snow' }) : null;
    var quillFundamentacao = document.querySelector('#editor-fundamentacao') ? new Quill('#editor-fundamentacao', { theme: 'snow' }) : null;
    var quillContent_doc = document.querySelector('#editor-content-doc') ? new Quill('#editor-content-doc', { theme: 'snow' }) : null;
    var quillFundaments = document.querySelector('#editor-fundaments') ? new Quill('#editor-fundaments', { theme: 'snow' }) : null;
    var quillComentario = document.querySelector('#editor-comentario') ? new Quill('#editor-comentario', { theme: 'snow' }) : null;
    var quillContent_principio = document.querySelector('#editor-content-principio') ? new Quill('#editor-content-principio', { theme: 'snow' }) : null;

    // Seleciona formulários específicos se existirem na página
    var formArticles = document.querySelector('form');
    var formCasos = document.querySelector('#formCasos');
    var formModelos = document.querySelector('#formModelos');
    var formQuestions = document.querySelector('#formQuestions');
    var formSumulas = document.querySelector('#formSumulas');
    var formPrincipios = document.querySelector('#formPrincipios');

    // Função para atualizar o campo oculto e submeter o formulário
    var updateAndSubmit = function (form, quillInstance, inputName) {
        if (form && quillInstance) {
            form.onsubmit = function (event) {
                var hiddenInput = form.querySelector('input[name="' + inputName + '"]');
                if (hiddenInput) {
                    hiddenInput.value = quillInstance.root.innerHTML;
                }
            };
        }
    };

    // Aplica a lógica aos formulários correspondentes
    updateAndSubmit(formArticles, quillContent, "content");
    updateAndSubmit(formCasos, quillFundamentacao, "fundamentacao");
    updateAndSubmit(formModelos, quillContent_doc, "content_doc");
    updateAndSubmit(formQuestions, quillFundaments, "fundaments");
    updateAndSubmit(formSumulas, quillComentario, "comentario");
    updateAndSubmit(formPrincipios, quillContent_principio, "content_principio");
});