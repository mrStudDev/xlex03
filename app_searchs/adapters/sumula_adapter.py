from app_sumulas.models import SumulaModel
from django.db.models import Q


class SumulasSearchAdapter:

    @staticmethod
    def sumula_advanced_search(params):
        enunciado = params.get('enunciado', None)
        sigla_tribunal = params.get('sigla_tribunal', None)
        numero_sumula = params.get('numero_sumula', None)
        nome_tribunal = params.get('nome_tribunal', None)
        tema_juridico = params.get('tema_juridico', None)
        
        queryset = SumulaModel.objects.all()

        if enunciado:
            queryset = queryset.filter(Q(enunciado__icontains=enunciado))
        
        if sigla_tribunal:
            queryset = queryset.filter(Q(sigla_tribunal__icontains=sigla_tribunal))

        if numero_sumula:
            queryset = queryset.filter(Q(numero_sumula__icontains=numero_sumula))

        if nome_tribunal:
            queryset = queryset.filter(Q(nome_tribunal__icontains=nome_tribunal))

        if tema_juridico:
            queryset = queryset.filter(Q(tema_juridico__icontains=tema_juridico))

        return queryset