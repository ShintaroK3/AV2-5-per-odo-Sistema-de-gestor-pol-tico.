from django.shortcuts import render
from promotions.models.promotion import Promotion

def home(request):
    promotions = Promotion.objects.all()
    context = {
        'promotions': promotions
    }
    return render(request, 'home.html', context)
