document.addEventListener("DOMContentLoaded", function () {
    var toolbarOptions = [
        ['bold', 'italic', 'underline', 'strike'],
        ['blockquote', 'code-block'], // Bloco de citação e bloco de código

        [{ 'header': 1 }, { 'header': 2 }], // Títulos
        [{ 'list': 'ordered' }, { 'list': 'bullet' }],
        [{ 'script': 'sub' }, { 'script': 'super' }], // Subscript/superscript
        [{ 'indent': '-1' }, { 'indent': '+1' }], // Indentação
        [{ 'direction': 'rtl' }], // Direção do texto

        [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

        [{ 'color': [] },], // Cor do texto Fonte
        [{ 'align': [] }], // Alinhamento

        ['clean'] // Remove formatações
    ];
    // Inicialização do Quill

    var quillContent = document.querySelector('#editor-content') ? new Quill('#editor-content', {
        theme: 'snow',
        modules: { toolbar: toolbarOptions },
        placeholder: 'Digite o conteúdo...'
    }) : null;

    var quillFundamentacao = document.querySelector('#editor-fundamentacao') ? new Quill('#editor-fundamentacao', {
        theme: 'snow',
        modules: { toolbar: toolbarOptions },
        placeholder: 'Digite o conteúdo...'
    }) : null;

    var quillContent_doc = document.querySelector('#editor-content-doc') ? new Quill('#editor-content-doc', {
        theme: 'snow',
        modules: { toolbar: toolbarOptions },
        placeholder: 'Digite o conteúdo...'
    }) : null;

    var quillFundaments = document.querySelector('#editor-fundaments') ? new Quill('#editor-fundaments', {
        theme: 'snow',
        modules: { toolbar: toolbarOptions },
        placeholder: 'Digite o conteúdo...'
    }) : null;

    var quillComentario = document.querySelector('#editor-comentario') ? new Quill('#editor-comentario', {
        theme: 'snow',
        modules: { toolbar: toolbarOptions },
        placeholder: 'Digite o conteúdo...'
    }) : null;

    var quillContent_principio = document.querySelector('#editor-content-principio') ? new Quill('#editor-content-principio', {
        theme: 'snow',
        modules: { toolbar: toolbarOptions },
        placeholder: 'Digite o conteúdo...'
    }) : null;

    var quilContent_social = document.querySelector('#editor-content-social') ? new Quill('#editor-content-social', {
        theme: 'snow',
        modules: { toolbar: toolbarOptions },
        placeholder: 'Digite o conteúdo...'
    }) : null;

    // Seleciona formulários específicos se existirem na página
    var formArticles = document.querySelector('form');
    var formCasos = document.querySelector('#formCasos');
    var formModelos = document.querySelector('#formModelos');
    var formQuestions = document.querySelector('#formQuestions');
    var formSumulas = document.querySelector('#formSumulas');
    var formPrincipios = document.querySelector('#formPrincipios');
    var formEduSocial = document.querySelector('#formEduSocial');

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
    updateAndSubmit(formEduSocial, quilContent_social, "content_social");
});