
// App_Articles
var quill = new Quill('#editor', {
    theme: 'snow'
});
var form = document.querySelector('form');
form.onsubmit = function () {
    var contentField = document.querySelector('input[name="content"]');
    contentField.value = quill.root.innerHTML;
};

// App_Casos
var quillFundamentacao = new Quill('#editor-casos', {
    theme: 'snow'
});
var form = document.querySelector('form');
form.onsubmit = function () {
    var fundamentacaoField = document.querySelector('input[name="fundamentacao"]');
    fundamentacaoField.value = quillFundamentacao.root.innerHTML;
};

// App_Modelos
var quillContent_doc = new Quill('#editor-modelos', {
    theme: 'snow'
});
var form = document.querySelector('form');
form.onsubmit = function () {
    var content_docField = document.querySelector('input[name="content_doc"]');
    content_docField.value = quillContent_doc.root.innerHTML;
};

// App_Modelos
var quillContent_principio = new Quill('#editor-principios', {
    theme: 'snow'
});
var form = document.querySelector('form');
form.onsubmit = function () {
    var content_principioField = document.querySelector('input[name="content_principio"]');
    content_principioField.value = quillContent_principio.root.innerHTML;
};