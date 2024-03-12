from app_juris_stj.models import STJjurisprudenciaModel
from django.db.models import Q


class JurisSTJSearchAdapter:

    @staticmethod
    def search(ementa=None):
        # Começamos com todos os registros.
        queryset = STJjurisprudenciaModel.objects.all()
        # Se o termo de busca para ementa for fornecido, filtre o queryset.
        if ementa:
            queryset = queryset.filter(Q(ementa__icontains=ementa,))

        return queryset

class AdvancedJurisSTJSearchAdapter:

    @staticmethod
    def advanced_search(params):
        ementa = params.get('ementa', None)
        data_formatada_inicial = params.get('data_formatada_inicial', None)
        data_formatada_final = params.get('data_formatada_final', None)
        descricaoClasse = params.get('descricaoClasse', None)
        numeroProcesso = params.get('numeroProcesso', None)
        ministroRelator = params.get('ministroRelator', None)
        
        queryset = STJjurisprudenciaModel.objects.all()

        if ementa:
            queryset = queryset.filter(Q(ementa__icontains=ementa))
        
        if data_formatada_inicial:
            queryset = queryset.filter(data_formatada__gte=data_formatada_inicial)
        
        if data_formatada_final:
            queryset = queryset.filter(data_formatada__lte=data_formatada_final)

        if descricaoClasse:
            queryset = queryset.filter(Q(descricaoClasse__icontains=descricaoClasse))

        if numeroProcesso:
            queryset = queryset.filter(Q(numeroProcesso__icontains=numeroProcesso))

        if ministroRelator:
            queryset = queryset.filter(Q(ministroRelator__icontains=ministroRelator))

        return queryset
