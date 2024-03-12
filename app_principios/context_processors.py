from django.db.models.aggregates import Count
from random import randint
from .models import PrincipiosModel

def principio_randomico(request):
    count = PrincipiosModel.objects.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    principio = PrincipiosModel.objects.all()[random_index]
    return {'principio_randomico': principio}
