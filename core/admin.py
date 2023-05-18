from django.contrib import admin
from .models import Cadastro_Crianca, Cadastro_Evolucao_Crianca, Cadastro_Funcionario, Unidade_Atentimento, Cadastro_Vacina_Aplicada, Cadastro_Consultas_Medicas, Cadastro_Consultas_Odontologicas #new

admin.site.register(Cadastro_Crianca)
admin.site.register(Cadastro_Evolucao_Crianca)
admin.site.register(Cadastro_Funcionario) 
admin.site.register(Unidade_Atentimento) 
admin.site.register(Cadastro_Vacina_Aplicada) 
admin.site.register(Cadastro_Consultas_Medicas)
admin.site.register(Cadastro_Consultas_Odontologicas)

                     