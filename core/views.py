from django.http import HttpResponse
from django.shortcuts import render
from .models import Cadastro_Crianca, Cadastro_Evolucao_Crianca, Cadastro_Funcionario, Unidade_Atentimento, Cadastro_Vacina_Aplicada, Cadastro_Consultas
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required



def cadastro_usuario(request):
    if request.method == "GET":
        return render (request, 'cadastro_usuario.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=usuario).first()
        if user:
            return HttpResponse('Já existe um usuário com esse nome!')
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso!')


def login(request):
    if request.method == "GET":
        return render (request, 'login_teste.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        user = authenticate(username=usuario, password=senha)

        if user is not None:
            login_django(request, user)
            return render (request, 'home.html')
        else:
            return render (request, 'login_teste.html')
        

def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')


@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')


@login_required(login_url="/login")
def calendario_vacinal(request):
    return render(request, 'calendario_vacinal.html')


@login_required(login_url="/login")
def dados_pessoais(request):
    return render(request, 'dados_pessoais.html')


@login_required(login_url="/login")
def direitos_crianca(request):
    return render(request, 'direitos_crianca.html')


@login_required(login_url="/login")
def direitos_responsaveis(request):
    return render(request, 'direitos_responsaveis.html')


@login_required(login_url="/login")
def grafico_crescimento(request):
    return render(request, 'grafico_crescimento.html')


@login_required(login_url="/login")
def medidas(request):
    evolucao = Cadastro_Evolucao_Crianca.objects.all()

    for i in evolucao:
        altura_metros = i.estatura *0.01
        imc = round(i.peso/altura_metros ** 2, 1)

        if imc < 18.5:
            i.classificacao_imc = 'Abaixo do peso normal'
        elif 18.5 < imc < 24.9:
            i.classificacao_imc = 'Peso normal'
        elif 25.0 < imc < 29.9:
            i.classificacao_imc = 'Excesso de peso'
        elif 30.0 < imc < 34.9:
            i.classificacao_imc = 'Obesidade classe |'
        elif 35.0 < imc < 39.9:
            i.classificacao_imc = 'Obesidade classe ||'
        else:
            i.classificacao_imc = 'Obesidade classe |||'

    context = {'evolucao': evolucao,
               'imc': imc}
    return render(request, 'medidas.html', context)


@login_required(login_url="/login")
def historico_vacinas(request):
    return render(request, 'historico_vacinas.html')


@login_required(login_url="/login")
def historico_consultas(request):
    return render(request, 'historico_consultas.html')


# def calculo_IMC(request):
#     crianca = Cadastro_Evolucao_Crianca.objects.all()
#     for c in crianca:
#         imc = c.peso * c.estatura
        
#     context = {'imc': imc}

#     return render(request, 'dados_pessoais.html', context)

