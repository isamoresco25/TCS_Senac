from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cadastro', views.cadastro_usuario, name="cadastro"),
    path('login', views.login, name="login"),
    # path('login', views.login, name='login'),
    path('esqueci_senha', views.esqueci_senha, name='esqueci_senha'),

    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    path('calendario_vacinal', views.calendario_vacinal, name='calendario_vacinal'),
    path('dados_pessoais', views.dados_pessoais, name='dados_pessoais'),
    path('direitos_crianca', views.direitos_crianca, name='direitos_crianca'),
    path('direitos_responsaveis', views.direitos_responsaveis, name='direitos_responsaveis'),
    path('notificacoes', views.notificacoes, name='notificacoes'),
    path('observacoes', views.list_observacoes, name='observacoes'),

    path('grafico_crescimento', views.grafico_crescimento, name='grafico_crescimento'),
    path('historico_consultas_medic', views.historico_consultas_medicas, name='historico_consultas_medicas'),
    path('historico_vacinas', views.historico_vacinas, name='historico_vacinas'),
    path('medidas', views.medidas, name='medidas'),
    path('historico_consultas_odont', views.historico_consultas_odontologicas, name='historico_consultas_odontologicas'),

]
