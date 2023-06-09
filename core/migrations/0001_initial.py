# Generated by Django 4.1.7 on 2023-05-18 01:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Crianca',
            fields=[
                ('nome_crianca', models.TextField()),
                ('data_nasc', models.DateField()),
                ('rcn', models.IntegerField(blank=True, max_length=5, null=True)),
                ('sexo', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], max_length=40)),
                ('nome_mae', models.TextField()),
                ('cidade_nsc', models.TextField()),
                ('estado_nsc', models.TextField()),
                ('mora_com', models.CharField(choices=[('Mãe', 'Mãe'), ('Pai', 'Pai'), ('Responsável legal', 'Responsável legal'), ('Outro', 'Outro'), ('Instituição de Acolhimento', 'Instituição de Acolhimento')], max_length=40)),
                ('nome_instituicao', models.TextField(blank=True, null=True)),
                ('rua_moradia', models.TextField()),
                ('numero_moradia', models.TextField()),
                ('bairro_moradia', models.TextField()),
                ('complemento', models.TextField(blank=True, null=True)),
                ('cep_moradia', models.TextField()),
                ('cidade_moradia', models.TextField()),
                ('estado_moradia', models.TextField()),
                ('tipo_moradia', models.CharField(choices=[('Urbano', 'Urbano'), ('Rural', 'Rural')], max_length=40)),
                ('ponto_referencia', models.TextField(blank=True, null=True)),
                ('telefone_responsavel', models.IntegerField(max_length=13)),
                ('email_responsavel', models.TextField()),
                ('etnia', models.CharField(choices=[('Branca', 'Branca'), ('Negra', 'Negra'), ('Amarela', 'Amarela'), ('Parda', 'Parda'), ('Indígena', 'Indígena'), ('Outra', 'Outra')], max_length=40)),
                ('tipo_familia', models.CharField(choices=[('Família Cigana', 'Família Cigana'), ('Família Quilombola', 'Família Quilombola'), ('Família Ribeirinha', 'Família Ribeirinha'), ('Família em situação de rua', 'Família em situação de rua'), ('Família indígena', 'Família indígena'), ('Família indígena residente em aldeia/reserva', 'Família indígena residente em aldeia/reserva'), ('Outros', 'Outros')], max_length=50)),
                ('especificacao_tipo_familia', models.TextField(blank=True, null=True)),
                ('nr_nascido_vivo', models.IntegerField(primary_key=True, serialize=False)),
                ('nr_cartao_sus', models.IntegerField()),
                ('esf', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=40)),
                ('qual_esf', models.TextField(blank=True, null=True)),
                ('dsei', models.TextField(blank=True, null=True)),
                ('servico_saude', models.TextField(blank=True, null=True)),
                ('plano_saude', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=40)),
                ('qual_plano', models.TextField(blank=True, null=True)),
                ('numero_plano', models.IntegerField(blank=True, null=True)),
                ('unidade_educacional', models.TextField(blank=True, null=True)),
                ('assistencia_social', models.TextField(blank=True, null=True)),
                ('data_criacao_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'cadastro_crianca',
            },
        ),
        migrations.CreateModel(
            name='Cadastro_Funcionario',
            fields=[
                ('id_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_funcionario', models.TextField()),
                ('cpf_funcionario', models.IntegerField()),
                ('tipo_documento', models.CharField(choices=[('CRM', 'CRM'), ('COREN', 'COREN')], max_length=40)),
                ('numero_documento', models.IntegerField()),
            ],
            options={
                'db_table': 'cadastro_funcionario',
            },
        ),
        migrations.CreateModel(
            name='Unidade_Atentimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_unidade', models.TextField()),
            ],
            options={
                'db_table': 'unidade_atendimento',
            },
        ),
        migrations.CreateModel(
            name='Cadastro_Vacina_Aplicada',
            fields=[
                ('id_vacina', models.AutoField(primary_key=True, serialize=False)),
                ('nome_vacina', models.TextField()),
                ('data_aplicacao', models.DateField()),
                ('lote', models.IntegerField()),
                ('lab_produtor', models.TextField()),
                ('crianca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastro_crianca')),
                ('dados_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastro_funcionario')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidade_atentimento')),
            ],
            options={
                'db_table': 'cadastro_vacina_aplicada',
            },
        ),
        migrations.CreateModel(
            name='Cadastro_Evolucao_Crianca',
            fields=[
                ('id_evolucao', models.AutoField(primary_key=True, serialize=False)),
                ('data_avaliacao', models.DateField()),
                ('idade', models.IntegerField()),
                ('peso', models.FloatField()),
                ('estatura', models.FloatField()),
                ('perimetro_cefalico', models.FloatField()),
                ('imc', models.FloatField()),
                ('classificacao_imc', models.TextField()),
                ('pressao_arterial', models.FloatField()),
                ('temperatura', models.FloatField()),
                ('crianca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastro_crianca')),
            ],
            options={
                'db_table': 'cadastro_evolucao_crianca',
            },
        ),
        migrations.AddField(
            model_name='cadastro_crianca',
            name='unidade_basica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidade_atentimento'),
        ),
        migrations.CreateModel(
            name='Cadastro_Consultas_Odontologicas',
            fields=[
                ('id_consulta_odont', models.AutoField(primary_key=True, serialize=False)),
                ('data_consulta_odont', models.DateField()),
                ('dentes', models.TextField(blank=True, null=True)),
                ('procedimento', models.TextField(blank=True, null=True)),
                ('data_retorno', models.DateField(blank=True, null=True)),
                ('crianca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastro_crianca')),
                ('dentista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastro_funcionario')),
                ('unidade_saude', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidade_atentimento')),
            ],
            options={
                'db_table': 'cadastro_consultas_odontologicas',
            },
        ),
        migrations.CreateModel(
            name='Cadastro_Consultas_Medicas',
            fields=[
                ('id_consulta_med', models.AutoField(primary_key=True, serialize=False)),
                ('data_consulta_med', models.DateField()),
                ('descricao', models.TextField()),
                ('obs', models.TextField(blank=True, null=True)),
                ('crianca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastro_crianca')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cadastro_funcionario')),
                ('unidade_atendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidade_atentimento')),
            ],
            options={
                'db_table': 'cadastro_consultas_medicas',
            },
        ),
    ]
