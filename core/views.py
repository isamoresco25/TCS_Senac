from django.shortcuts import render
from .models import Cadastro_Crianca, Cadastro_Evolucao_Crianca, Cadastro_Funcionario, Unidade_Atentimento, Cadastro_Vacina_Aplicada, Cadastro_Consultas



def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')


def calendario_vacinal(request):
    return render(request, 'calendario_vacinal.html')


def dados_pessoais(request):
    return render(request, 'dados_pessoais.html')


def direitos_crianca(request):
    return render(request, 'direitos_crianca.html')


def direitos_responsaveis(request):
    return render(request, 'direitos_responsaveis.html')


def grafico_crescimento(request):
    return render(request, 'grafico_crescimento.html')


def historico_consultas(request):
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
    return render(request, 'historico_consultas.html', context)


def historico_vacinas(request):
    return render(request, 'historico_vacinas.html')


def medidas(request):
    return render(request, 'medidas.html')


# def calculo_IMC(request):
#     crianca = Cadastro_Evolucao_Crianca.objects.all()
#     for c in crianca:
#         imc = c.peso * c.estatura
        
#     context = {'imc': imc}

#     return render(request, 'dados_pessoais.html', context)

