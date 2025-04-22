from django.shortcuts import render, get_object_or_404, redirect
from promotions.models.promotion import Promotion
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse


def home(request):
    promotions = Promotion.objects.all()
    context = {
        'promotions': promotions
    }
    return render(request, 'home.html', context)

def detalhe_view(request, promo_id):
    promotion = get_object_or_404(Promotion, id=promo_id)
    return render(request, 'detalhes.html', {'promotion': promotion})

def gerenciar(request):
    return render(request, 'gerenciar.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe!')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect(reverse('home'))

    return render(request, 'cadastrouser.html')

def gerenciar_usuarios(request):
    users = User.objects.all()
    return render(request, 'gerenciarusers.html', {'users': users})

def deletar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect(reverse('home'))  



