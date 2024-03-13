from django.urls import path
from . import views
from . views import (
    XlexQuestionView,
    QuestionSingularView,
    BancaQuestionView,
    DiciplinaQuestionView,
    RamoDireitoQuestionView,
    TagQuestionView,
    CreateXlexQuestionView,
    CreateAnswerView,

)

app_name = 'app_questions'

urlpatterns = [
    path('', XlexQuestionView.as_view() ,name='questions-list'),
    path('post/<slug:slug>/', QuestionSingularView.as_view() ,name='question-single'),
    path('banca/<slug:banca_slug>/', BancaQuestionView.as_view(), name='question-banca'),
    path('disciplina/<slug:disciplina_slug>/', DiciplinaQuestionView.as_view(), name='question-disciplina'),
    path('ramo-direito/<slug:ramo_slug>/', RamoDireitoQuestionView.as_view(), name='question-ramo'),
    path('tags/<slug:tagQuestion_slug>/', TagQuestionView.as_view(), name='question-tag'),
    path('create-question/', CreateXlexQuestionView.as_view(), name='question-create'),
    path('create-answer/<int:questao_x_id>/', CreateAnswerView.as_view(), name='question-create-answer'),
    path('get_question_text/<int:questao_x_id>/', views.get_full_question_text, name='get_full_question_text'),
]