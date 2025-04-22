
from django.contrib import admin
from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static
from Login import views as login_views 
from Home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_views.home, name='home'), 
    path('detalhes/<int:promo_id>/', views.detalhe_view, name= 'detalhes'),
    path('', login_views.login_view, name='login'),
    path('register/', login_views.register_view, name='register'),
    path('deletar-usuario/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('cadastrar-usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('gerenciar-usuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
