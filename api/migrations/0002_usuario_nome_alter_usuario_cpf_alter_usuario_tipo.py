# Generated by Django 4.0.5 on 2022-09-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(blank=True, choices=[('recrutador', 'Recrutador'), ('candidato', 'Candidato')], max_length=30, null=True),
        ),
    ]
