from django.conf import settings
from django.db import models
from django.utils import timezone


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

    nr_nascido_vivo = models.IntegerField(primary_key=True, null=False, blank=False)
    nome_crianca = models.TextField(blank=False)
    cpf_crianca = models.IntegerField(null=True, blank=True, max_length=11)
    data_nasc = models.DateField(blank=False)
    cidade = models.TextField(blank=False)
    estado = models.TextField(blank=False)
    cep = models.TextField(blank=False)
    bairro = models.TextField(blank=False)
    rua =  models.TextField(blank=False)
    numero = models.TextField(blank=False)
    nr_cartao_sus = models.IntegerField(blank=False)
    sexo = models.CharField(choices= CHOICES_SEXO, max_length=20)
    etnia = models.CharField(choices= CHOICES_ETNIA, max_length=20)
    tipo_sanguineo = models.TextField(blank=False)
    nome_mae = models.TextField(blank=False)
    nome_pai = models.TextField(blank=True)
    data_criacao_registro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.nr_nascido_vivo)

    class Meta:
        db_table = 'cadastro_crianca'
    
# teste

class Cadastro_Evolucao_Crianca(models.Model):
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    id_evolucao = models.AutoField(primary_key=True, null=False, blank=False)
    data_avaliacao = models.DateField(blank=False)
    idade_anos = models.IntegerField(blank=False)
    idade_meses = models.IntegerField(blank=False)
    peso = models.FloatField(blank=False)
    estatura = models.FloatField(blank=False)
    perimetro_cefalico = models.FloatField(blank=False)
    imc = models.FloatField(blank=False)
    pressao_arterial = models.FloatField(blank=False)
    classificacao_imc = models.TextField(blank=False)
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



class Unidade_Atentimento(models.Model):
    nome_unidade = models.TextField(blank=False)

    def __str__(self):
        return str(self.nome_unidade)

    class Meta:
        db_table = 'unidade_atendimento'




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



class Cadastro_Consultas(models.Model):
    id_consulta = models.AutoField(primary_key=True, null=False, blank=False)
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    medico = models.ForeignKey(Cadastro_Funcionario, on_delete=models.CASCADE)
    unidade_atendimento = models.ForeignKey(Unidade_Atentimento, on_delete=models.CASCADE)
    data_consulta = models.DateField(blank=False)
    descricao = models.TextField(blank=False)
    obs = models.TextField(blank=True)

    def __str__(self):
        return str(self.id_consulta)

    class Meta:
        db_table = 'cadastro_consulta'
