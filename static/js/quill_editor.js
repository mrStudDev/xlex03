
var quill = new Quill('#editor', {
    theme: 'snow'
});

var form = document.querySelector('form');
form.onsubmit = function () {
    var contentField = document.querySelector('input[name="content"]');
    contentField.value = quill.root.innerHTML;
};

