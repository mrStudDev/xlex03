const questionTextURL = "{% url 'get_full_question_text' questao_x_id=questao_x_id %}";

$(document).ready(function () {
    function updateQuestionText() {
        let selectedQuestionId = $("#id_questao_x").val();
        $.get(`/questions/get_question_text/${selectedQuestionId}/`, function (data) {
            $("#question_x-text p").text(data.question_ask);
        }).fail(function () {
            $("#question_x-text p").text("Erro ao carregar texto da questão.");
        });
    }

    updateQuestionText();
    $("#id_questao_x").change(function () {
        updateQuestionText();
    });
});


