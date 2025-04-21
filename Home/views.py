from django.shortcuts import render, get_object_or_404
from promotions.models.promotion import Promotion




def home(request):
    promotions = Promotion.objects.all()
    context = {
        'promotions': promotions
    }
    return render(request, 'home.html', context)

def detalhe_view(request, promo_id):
    promotion = get_object_or_404(Promotion, id=promo_id)
    return render(request, 'detalhes.html', {'promotion': promotion})

