# Generated by Django 4.1.7 on 2023-06-19 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_cadastro_crianca_tipo_moradia'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro_consultas_medicas',
            name='imc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
