"""caderneta_crianca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', views.login, name='login'),
    path('esqueci_senha', views.esqueci_senha, name='esqueci_senha'),

    path('', views.home, name='home'),

    path('calendario_vacinal', views.calendario_vacinal, name='calendario_vacinal'),
    path('dados_pessoais', views.dados_pessoais, name='dados_pessoais'),
    path('direitos_crianca', views.direitos_crianca, name='direitos_crianca'),
    path('direitos_responsaveis', views.direitos_responsaveis, name='direitos_responsaveis'),

    path('grafico_crescimento', views.grafico_crescimento, name='grafico_crescimento'),
    path('historico_consultas', views.historico_consultas, name='historico_consultas'),
    path('historico_vacinas', views.historico_vacinas, name='historico_vacinas'),
    path('medidas', views.medidas, name='medidas'),

]
