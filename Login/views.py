from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View # Base class for CBVs
from django.contrib import messages # For messages
from django.urls import reverse_lazy # For success_url in CBVs

# Class-Based View for Login
class UserLoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
            return render(request, self.template_name)

# Class-Based View for Registration
class UserRegisterView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password: 
            messages.error(self.request, 'Preencha todos os campos.')
            return render(self.request, self.template_name)

        if User.objects.filter(username=username).exists():
            messages.error(self.request, 'Usuário já existe. Por favor, escolha outro nome de usuário.')
            return render(self.request, self.template_name)
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, 'Registro bem-sucedido! Você está logado.')
        return redirect('home')
    

def custom_logout_view(request):
    logout(request)
    messages.info(request, "Você foi desconectado com sucesso.") 
    return redirect(reverse_lazy('login')) 