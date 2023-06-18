from django.http import HttpResponse
from django.shortcuts import render
from .models import Cadastro_Crianca, Cadastro_Evolucao_Crianca, Cadastro_Funcionario, Unidade_Atentimento, Cadastro_Vacina_Aplicada, Cadastro_Consultas_Medicas, Cadastro_Consultas_Odontologicas, Observacoes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from datetime import date


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
            # crianca = Cadastro_Crianca.objects.all()

            # for c in crianca : 
            #     if (c.nr_nascido_vivo) == int(request.user.username):

            # biblioteca login_django importada, verifica se é valido e acessa a página se for válido
            login_django(request, user)
            return render (request, 'termo_consentimento.html')
        # se o usuário não for válido, volta para a tela de login
        else:
            # return render diz que essa função vai ser utilizada no html abaixo
            return render (request, 'login_teste.html')
        

def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')


@login_required(login_url="/login")
def calendario_vacinal(request):
    return render(request, 'calendario_vacinal.html')


@login_required(login_url="/login")
def direitos_crianca(request):
    return render(request, 'direitos_crianca.html')


@login_required(login_url="/login")
def direitos_responsaveis(request):
    return render(request, 'direitos_responsaveis.html')


@login_required(login_url="/login")
def grafico_crescimento(request):
    return render(request, 'grafico_crescimento.html')


# login_required é uma biblioteca para só acessar a tela se estiver logado
@login_required(login_url="/login")
def home(request):
    crianca = Cadastro_Crianca.objects.all()

    for c in crianca:
        if (c.nr_nascido_vivo) == int(request.user.username):
            obs_l = Observacoes.objects.last()
            con_med_l= Cadastro_Consultas_Medicas.objects.last()
            con_odon_l = Cadastro_Consultas_Odontologicas.objects.last()

            imc_grafico = Cadastro_Evolucao_Crianca.objects.all()
            teste = 10

    context = {'obs_l' : obs_l, 'con_med_l' : con_med_l, 'con_odon_l' : con_odon_l, 'teste': teste}
    return render(request, 'home.html', context,)


@login_required(login_url="/login")
def notificacoes(request):
    criancas = Cadastro_Crianca.objects.all()
    data_atual = date.today()
    mensagens = []
    vacinas = {'BCG':0, 'Adsorvida':2, 'Influenza':6}

    for c in criancas:
        if (c.nr_nascido_vivo) == int(request.user.username):
            
            data_ultima_consulta = Cadastro_Consultas_Medicas.objects.last().data_consulta_med
            tempo_consulta_meses = (data_atual - data_ultima_consulta).days//30
            vacinas_tomadas = Cadastro_Vacina_Aplicada.objects.all()
            idade_meses = (data_atual - c.data_nasc).days // 30

            if tempo_consulta_meses > 3:
                mensagens.append(f"Faz mais de {tempo_consulta_meses} meses da sua última consulta médica...Não está na hora de marcar outra?")
            
            for v in vacinas_tomadas:
                nome_vacina_aplicada = v.nome_vacina
            for nome_vacina, idade_recomendada in vacinas.items():
                if idade_meses >= idade_recomendada:
                    if nome_vacina != nome_vacina_aplicada:
                        mensagens.append(f"A vacina {nome_vacina} está atrasada. Procure um posto de saúde mais próximo!")


    context = {'mensagens' : mensagens}
    return render(request, 'notificacoes.html', context)


@login_required(login_url="/login")
def list_observacoes(request):
    crianca = Cadastro_Crianca.objects.all()

    for c in crianca:
        if (c.nr_nascido_vivo) == int(request.user.username):
            obs = Observacoes.objects.all()
            context = {'obs' : obs}

    return render(request, 'observacoes.html', context)


@login_required(login_url="/login")
def dados_pessoais(request):
    criancas = Cadastro_Crianca.objects.all()

    for c in criancas:
        if (c.nr_nascido_vivo) == int(request.user.username): #request.user.username pega o username do usuario logado (que é o numero nascido vivo)
            crianca = c
    context = {'crianca' : crianca}
    
    return render(request, 'dados_pessoais.html', context)


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
            hist_med = Cadastro_Consultas_Medicas.objects.all()
            for med in hist_med:
                medico = Cadastro_Funcionario.objects.get(id_funcionario=med.medico.id_funcionario)
                medic = medico.nome_funcionario
                
            # sempre que for passar alguma variável para o html, tem que passar por dicionário (geralmente chamado context)
    context = {'hist_med': hist_med, 'medic': medic}
    return render(request, 'historico_consultas_medic.html', context)


@login_required(login_url="/login")
def historico_consultas_odontologicas(request):
    crianca = Cadastro_Crianca.objects.all()

    for c in crianca:
        if (c.nr_nascido_vivo) == int(request.user.username): #request.user.username pega o username do usuario logado (que é o numero nascido vivo)
            consultas = Cadastro_Consultas_Odontologicas.objects.filter(crianca=c)

    context = {'consultas': consultas}
    return render(request, 'historico_consultas_odont.html', context)


# @login_required(login_url="/login")
# def cad_observacoes(request):
#     if request.method == "GET": 
#         return render (request, 'observacoes.html')
#     else:
#         # pega os valores dos campos do html e joga para a variável
#         data_obs = request.POST.get('data_obs')
#         inter_obs = request.POST.get('inter_obs')
#         obs = request.POST.get('obs')

#     #falta terminar       
#     return HttpResponse('Usuário cadastrado com sucesso!')


# @login_required(login_url="/login")
# def cadastro_consulta(request):

#     nascidoVivo = request.POST.get('nroNascidoVivo')
#     medico = request.POST.get('medico')
#     dataConsulta = request.POST.get('dataConsulta')
#     sintomas = request.POST.get('sintomas')
#     obs = request.POST.get('obs')
#     crianca = Cadastro_Crianca.objects.filter(nr_nascido_vivo=nascidoVivo)

#     consulta = Cadastro_Consultas_Medicas.objects.create(crianca = crianca, medico = medico, unidade_atendimento = 0, data_consulta_med = dataConsulta, descricao = sintomas, obs = obs)
#     consulta.save()

#     context = {'nomeCrianca': crianca}
#     return render(request, 'cadastro_consulta.html', context)
