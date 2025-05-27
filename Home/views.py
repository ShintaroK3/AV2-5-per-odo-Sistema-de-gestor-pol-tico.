from django.shortcuts import render, redirect
from promotions.models.promotion import Promotion
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required 
from django.views.generic import DetailView, ListView, CreateView, DeleteView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse_lazy 



@login_required 
def home(request):
    promotions = Promotion.objects.all()
    context = {
        'promotions': promotions
    }
    return render(request, 'home.html', context)


class PromotionDetailView(LoginRequiredMixin, DetailView): 
    model = Promotion
    template_name = 'detalhes.html'
    context_object_name = 'promotion'
    


@login_required 
@permission_required('auth.view_user', raise_exception=True) 
def gerenciar(request):
    return render(request, 'gerenciar.html')


class RegisterUserView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'cadastrouser.html'
    success_url = reverse_lazy('home')
    success_message = 'Usuário cadastrado com sucesso!'
    permission_required = 'auth.add_user'

    def form_valid(self, form):
        
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST' and not self.request.POST.get('username'):
            messages.error(self.request, 'O campo de usuário não pode ser vazio.')
        return context



class GerenciarUsersView(LoginRequiredMixin, PermissionRequiredMixin, ListView): 
    model = User
    template_name = 'gerenciarusers.html'
    context_object_name = 'users'
    permission_required = 'auth.view_user' 


class DeleteUserView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'confirm_delete.html' 
    success_url = reverse_lazy('gerenciar_usuarios')
    success_message = "Usuário deletado com sucesso!"
    permission_required = 'auth.delete_user' 

    def form_valid(self, form):
        if self.request.user.id == self.get_object().id:
            messages.error(self.request, "Você não pode deletar sua própria conta!")
            return redirect(self.success_url)
        return super().form_valid(form)