from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView 

from Home import views as home_views
from Home.views import PromotionDetailView, GerenciarUsersView, RegisterUserView, DeleteUserView 
from Login import views as login_views
from Login.views import UserLoginView, UserRegisterView, custom_logout_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_views.home, name='home'), 
    path('detalhes/<int:pk>/', PromotionDetailView.as_view(), name='detalhes'), 
    path('', UserLoginView.as_view(), name='login'), 
    path('register/', UserRegisterView.as_view(), name='register'), 
    path('logout/', custom_logout_view, name='logout'), 
    path('gerenciar/', home_views.gerenciar, name='gerenciar'), 
    path('cadastrar-usuario/', RegisterUserView.as_view(), name='cadastrar_usuario'), 
    path('gerenciar-usuarios/', GerenciarUsersView.as_view(), name='gerenciar_usuarios'), 
    path('deletar-usuario/<int:pk>/', DeleteUserView.as_view(), name='deletar_usuario'), 

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)