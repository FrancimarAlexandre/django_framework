# Generated by Django 5.0.3 on 2024-03-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='atualizacao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data_concluido',
            field=models.DateField(),
        ),
    ]
