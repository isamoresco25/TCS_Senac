# Generated by Django 4.1.7 on 2023-05-27 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cadastro_consultas_medicas_medico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastro_consultas_odontologicas',
            old_name='procedimento',
            new_name='procedimento_orientacoes',
        ),
    ]