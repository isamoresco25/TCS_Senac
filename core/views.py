from django.http import HttpResponse
from django.shortcuts import render
from .models import Cadastro_Crianca, Cadastro_Evolucao_Crianca, Cadastro_Funcionario, Unidade_Atentimento, Cadastro_Vacina_Aplicada, Cadastro_Consultas_Medicas, Cadastro_Consultas_Odontologicas
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required



def cadastro_usuario(request):
    if request.method == "GET": 
        return render (request, 'cadastro_usuario.html')
    else:
        # pega os valores dos campos do html e joga para a variável
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # validação da própria biblioteca User do django verificando se o usuario digitado já é cadastrado
        user = User.objects.filter(username=usuario).first()
        if user:
            # mensagem de erro se já existe (precisa melhorar pois é apenas uma tela branca)
            return HttpResponse('Já existe um usuário com esse nome!')
        
        # cria um usuário no banco na tela de cadastro com as credenciais preenchidas
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        # salva usuario
        user.save()
        # mensagem de sucesso (precisa melhorar pois é apenas uma tela branca)
        return HttpResponse('Usuário cadastrado com sucesso!')


def login(request):
    if request.method == "GET":
        return render (request, 'login_teste.html')
    else:
        # pega o usuário e a senha digitados no html
        nr_nascido_vivo = request.POST.get('nr_nascido_vivo')
        senha = request.POST.get('senha')
        
        # utiliza a biblioteca User para autenticar as credenciais
        user = authenticate(username=nr_nascido_vivo, password=senha)

        if user is not None:
            # biblioteca login_django importada, verifica se é valido e acessa a página se for válido
            login_django(request, user)
            return render (request, 'home.html')
        # se o usuário não for válido, volta para a tela de login
        else:
            # return render diz que essa função vai ser utilizada no html abaixo
            return render (request, 'login_teste.html')
        

def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')

# login_required é uma biblioteca para só acessar a tela se estiver logado
@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')


@login_required(login_url="/login")
def calendario_vacinal(request):
    return render(request, 'calendario_vacinal.html')


@login_required(login_url="/login")
def notificacoes(request):
    return render(request, 'notificacoes.html')


@login_required(login_url="/login")
def dados_pessoais(request):
    criancas = Cadastro_Crianca.objects.all()

    for c in criancas:
        if (c.nr_nascido_vivo) == int(request.user.username): #request.user.username pega o username do usuario logado (que é o numero nascido vivo)
            crianca = c
    context = {'crianca' : crianca}
    
    return render(request, 'dados_pessoais.html', context)


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
    # para pegar do banco tem que utilizar o nome da model.objects.all() -> para pegar todos os objetos cadastrados
    crianca = Cadastro_Crianca.objects.all()

    for c in crianca:
        if (c.nr_nascido_vivo) == int(request.user.username): #request.user.username pega o username do usuario logado (que é o numero nascido vivo)

            evolucao = Cadastro_Evolucao_Crianca.objects.filter(crianca=c)
            imc = 0

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

            # sempre que for passar alguma variável para o html, tem que passar por dicionário (geralmente chamado context)
    context = {'evolucao': evolucao, 'imc' : imc}
    return render(request, 'medidas.html', context)


@login_required(login_url="/login")
def historico_vacinas(request):
    crianca = Cadastro_Crianca.objects.all()

    for c in crianca:
        if (c.nr_nascido_vivo) == int(request.user.username): #request.user.username pega o username do usuario logado (que é o numero nascido vivo)
            vacinas = Cadastro_Vacina_Aplicada.objects.filter(crianca=c)

            
    context = {'vacinas': vacinas}
    return render(request, 'historico_vacinas.html', context)


@login_required(login_url="/login")
def historico_consultas_medicas(request):
    # para pegar do banco tem que utilizar o nome da model.objects.all() -> para pegar todos os objetos cadastrados
    crianca = Cadastro_Crianca.objects.all()

    for c in crianca:
        if (c.nr_nascido_vivo) == int(request.user.username): #request.user.username pega o username do usuario logado (que é o numero nascido vivo)

            evolucao = Cadastro_Evolucao_Crianca.objects.filter(crianca=c)
            imc = 0

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

            # sempre que for passar alguma variável para o html, tem que passar por dicionário (geralmente chamado context)
    context = {'evolucao': evolucao, 'imc' : imc}
    return render(request, 'historico_consultas_medic.html', context)


@login_required(login_url="/login")
def historico_consultas_odontologicas(request):
    crianca = Cadastro_Crianca.objects.all()

    for c in crianca:
        if (c.nr_nascido_vivo) == int(request.user.username): #request.user.username pega o username do usuario logado (que é o numero nascido vivo)
            consultas = Cadastro_Consultas_Odontologicas.objects.filter(crianca=c)

            
    context = {'consultas': consultas}
    return render(request, 'historico_consultas_odont.html', context)



