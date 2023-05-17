from django.conf import settings
from django.db import models
from django.utils import timezone


class Unidade_Atentimento(models.Model):
    nome_unidade = models.TextField(blank=False)

    def __str__(self):
        return str(self.nome_unidade)

    class Meta:
        db_table = 'unidade_atendimento'



class Cadastro_Crianca(models.Model):
    CHOICES_ETNIA = (
        ("Branca", "Branca"),
        ("Negra", "Negra"),
        ("Amarela", "Amarela"),
        ("Parda", "Parda"),
        ("Indígena", "Indígena"),
        ("Outra", "Outra"),
    )
    CHOICES_SEXO = (
        ("Feminino", "Feminino"),
        ("Masculino", "Masculino"),
        ("Outro", "Outro"),
    )
    CHOICES_INSTITUICAO = (
        ("Mãe", "Mãe"),
        ("Pai", "Pai"),
        ("Responsável legal", "Responsável legal"),
        ("Outro", "Outro"),
        ("Instituição de Acolhimento", "Instituição de Acolhimento"),
    )
    CHOICES_MORADIA = (
        ("Urbano", "Urbano"),
        ("Rural", "Rural"),
    )
    CHOICES_FAMILIA = (
        ("Família Cigana", "Família Cigana"),
        ("Família Quilombola", "Família Quilombola"),
        ("Família Ribeirinha", "Família Ribeirinha"),
        ("Família em situação de rua", "Família em situação de rua"),
        ("Família indígena", "Família indígena"),
        ("Família indígena residente em aldeia/reserva", "Família indígena residente em aldeia/reserva"),
        ("Outros", "Outros")
    )
    CHOICES_ESF = (
        ("Não", "Não"),
        ("Sim", "Sim"),        
    )
    CHOICES_PLANO = (
        ("Não", "Não"),
        ("Sim", "Sim"),        
    )

    nome_crianca = models.TextField(blank=False)
    data_nasc = models.DateField(blank=False)
    rcn = models.IntegerField(null=True, blank=True, max_length=5)
    sexo = models.CharField(choices= CHOICES_SEXO, max_length=20)
    nome_mae = models.TextField(blank=False)
    cidade_nsc = models.TextField(blank=False)
    estado_nsc = models.TextField(blank=False)

    mora_com = models.CharField(choices= CHOICES_INSTITUICAO, max_length=20)
    nome_instituicao = models.TextField(null=True, blank=True) #para caso a pessoa selecione no combo a opção "outros" ou "inst. de acolhi." precisa digitar o nome
    rua_moradia =  models.TextField(blank=False)
    numero_moradia = models.TextField(blank=False)
    bairro_moradia = models.TextField(blank=False)
    complemento = models.TextField(blank=False)
    cep_moradia = models.TextField(blank=False)
    cidade_moradia = models.TextField(blank=False)
    estado_moradia = models.TextField(blank=False)
    tipo_moradia = models.CharField(choices= CHOICES_MORADIA, max_length=20)
    ponto_referencia = models.TextField(blank=False)
    telefone_responsavel = models.IntegerField(null=True, blank=True, max_length=13)
    email_responsavel = models.TextField(blank=False)
    
    etnia = models.CharField(choices= CHOICES_ETNIA, max_length=20)
    tipo_familia = models.CharField(choices= CHOICES_INSTITUICAO, max_length=50) 
    especificacao_tipo_familia = models.TextField(null=True, blank=True) #se a pessoa clicar no combo em "outros" precisa especificar digitando
    nr_nascido_vivo = models.IntegerField(primary_key=True, null=False, blank=False)
    nr_cartao_sus = models.IntegerField(blank=False)
    esf = models.CharField(choices= CHOICES_ESF, max_length=20) #estratégia saúde da família
    qual_esf = models.TextField(null=True, blank=True) #precisa especificar qual esf
    unidade_basica = models.ForeignKey(Unidade_Atentimento, on_delete=models.CASCADE)
    dsei = models.TextField(null=True, blank=True) #distrito sanitário especial indígena
    servico_saude = models.TextField(null=True, blank=True)
    plano_saude = models.CharField(choices= CHOICES_PLANO, max_length=20)
    qual_plano = models.TextField(null=True, blank=True)
    numero_plano = models.IntegerField(blank=True)


    unidade_educacional = models.TextField(null=True, blank=True)
    assistencia_social = models.TextField(blank=True)
    data_criacao_registro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.nr_nascido_vivo)

    class Meta:
        db_table = 'cadastro_crianca'
    


class Cadastro_Evolucao_Crianca(models.Model):
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    id_evolucao = models.AutoField(primary_key=True, null=False, blank=False)
    data_avaliacao = models.DateField(blank=False)
    idade = models.IntegerField(blank=False)
    peso = models.FloatField(blank=False)
    estatura = models.FloatField(blank=False)
    perimetro_cefalico = models.FloatField(blank=False)
    imc = models.FloatField(blank=False)
    classificacao_imc = models.TextField(blank=False)
    pressao_arterial = models.FloatField(blank=False)
    temperatura = models.FloatField(blank=False)

    def __str__(self):
        return str(self.id_evolucao)

    class Meta:
        db_table = 'cadastro_evolucao_crianca'



class Cadastro_Funcionario(models.Model):
    CHOICES_DOCUMENTO = (
        ("CRM", "CRM"),
        ("COREN", "COREN"),
    )

    id_funcionario = models.AutoField(primary_key=True, null=False, blank=False)
    nome_funcionario = models.TextField(blank=False)
    cpf_funcionario = models.IntegerField(blank=False)
    tipo_documento = models.CharField(choices= CHOICES_DOCUMENTO, max_length=20)
    numero_documento = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.id_funcionario)

    class Meta:
        db_table = 'cadastro_funcionario'



class Cadastro_Vacina_Aplicada(models.Model):
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    id_vacina = models.AutoField(primary_key=True, null=False, blank=False)
    nome_vacina = models.TextField(blank=False)
    data_aplicacao = models.DateField(blank=False)
    lote = models.IntegerField(blank=False)
    lab_produtor = models.TextField(blank=False)
    unidade = models.ForeignKey(Unidade_Atentimento, on_delete=models.CASCADE)
    dados_funcionario = models.ForeignKey(Cadastro_Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_vacina)

    class Meta:
        db_table = 'cadastro_vacina_aplicada'



class Cadastro_Consultas_Medicas(models.Model):
    id_consulta_med = models.AutoField(primary_key=True, null=False, blank=False)
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    medico = models.ForeignKey(Cadastro_Funcionario, on_delete=models.CASCADE)
    unidade_atendimento = models.ForeignKey(Unidade_Atentimento, on_delete=models.CASCADE)
    data_consulta_med = models.DateField(blank=False)
    descricao = models.TextField(blank=False)
    obs = models.TextField(blank=True)

    def __str__(self):
        return str(self.id_consulta)

    class Meta:
        db_table = 'cadastro_consultas_medicas'



class Cadastro_Consultas_Odontologicas(models.Model):
    id_consulta_odont = models.AutoField(primary_key=True, null=False, blank=False)
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Cadastro_Funcionario, on_delete=models.CASCADE)
    data_consulta_odont = models.DateField(blank=False)
    dentes = models.TextField(blank=True)
    procedimento = models.TextField(blank=True)
    data_retorno = models.DateField(blank=True)
    unidade_saude = models.ForeignKey(Unidade_Atentimento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_consulta)

    class Meta:
        db_table = 'cadastro_consultas_odontologicas'
