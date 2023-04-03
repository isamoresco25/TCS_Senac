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

    nr_nascido_vivo = models.ForeignKey(blank=False, on_delete=models.CASCADE)
    nome_criana = models.TextField(blank=False)
    cpf_crianca = models.IntegerField(null=True, blank=True, max_length=11)
    data_nasc = models.DateField(blank=False)
    cidade = models.TextField(blank=False)
    estado = models.TextField(blank=False)
    nr_cartao_sus = models.IntegerField(blank=False)
    sexo = models.CharField(choices= CHOICES_SEXO, max_length=20)
    etnia = models.CharField(choices= CHOICES_ETNIA, max_length=20)
    tipo_sanguineo = models.TextField(blank=False)
    #endereco = models.CharField()
    nome_mae = models.TextField(blank=True)
    nome_pai = models.TextField(blank=True)
    data_criacao_registro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.nr_nascido_vivo)

    class Meta:
        db_table = 'cadastro_crianca'
    


class Cadastro_Vacina_Aplicada(models.Model):
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    id_vacina = models.AutoField(primary_key=True, null=False, blank=False)
    nome_vacina = models.TextField(blank=False)
    data_aplicacao = models.DateField(blank=False)
    lote = models.IntegerField(blank=False)
    lab_produtor = models.TextField(blank=False)
    unidade = models.IntegerField(blank=False)
    assinatura = models.TextField(blank=False)

    def __str__(self):
        return str(self.id_vacina)

    class Meta:
        db_table = 'cadastro_vacina_aplicada'



class Cadastro_Evolucao_Crianca(models.Model):
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    id_evolucao = models.AutoField(primary_key=True, null=False, blank=False)
    data_avaliacao = models.DateField(blank=False)
    idade = models.IntegerField(blank=False)
    peso = models.IntegerField(blank=False)
    estatura = models.IntegerField(blank=False)
    perimetro_cefalico = models.IntegerField(blank=False)
    imc = models.IntegerField(blank=False)
    pressao_arterial = models.IntegerField(blank=False)
    classificacao = models.TextField(blank=False)

    def __str__(self):
        return str(self.id_evolucao)

    class Meta:
        db_table = 'cadastro_evolucao_crianca'



class Cadastro_Medico(models.Model):
    nome_medico = models.TextField(blank=False)
    cpf_medico = models.IntegerField(blank=False)
    crm_medico = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.crm_medico)

    class Meta:
        db_table = 'cadastro_medico'



class Unidade_Atentimento(models.Model):
    nome_unidade = models.TextField(blank=False)
    endereco = models.TextField(blank=False)

    def __str__(self):
        return str(self.nome_unidade)

    class Meta:
        db_table = 'unidade_atendimento'



class Cadastro_Consultas(models.Model):
    crianca = models.ForeignKey(Cadastro_Crianca, on_delete=models.CASCADE)
    medico = models.ForeignKey(Cadastro_Medico, on_delete=models.CASCADE)
    unidade_atendimento = models.ForeignKey(Unidade_Atentimento, on_delete=models.CASCADE)
    id_consulta = models.AutoField(primary_key=True, null=False, blank=False)
    data_consulta = models.DateField(blank=False)
    descricao = models.TextField(blank=False)
    obs = models.TextField(blank=True)
    responsavel_crianca = models.TextField(blank=False)

    def __str__(self):
        return str(self.id_consulta)

    class Meta:
        db_table = 'cadastro_consulta'

