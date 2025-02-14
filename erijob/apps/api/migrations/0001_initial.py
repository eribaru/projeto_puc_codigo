# Generated by Django 4.1.1 on 2022-09-25 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('recrutador', 'Recrutador'), ('candidato', 'Candidato')], max_length=30, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('telefone', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'tb_usuario',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('cod_cidade', models.IntegerField(db_column='cod_cidade', primary_key=True, serialize=False)),
                ('nom_cidade', models.CharField(db_column='nom_cidade', max_length=255)),
            ],
            options={
                'db_table': 'tb_cidade',
                'ordering': ('nom_cidade',),
            },
        ),
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('objetivo', models.TextField(max_length=4000)),
                ('contato', models.TextField(max_length=200)),
                ('dados_pessoais', models.TextField(max_length=4000)),
                ('sobre', models.TextField(max_length=4000)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_curriculo',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('ramo', models.CharField(max_length=14)),
                ('sede', models.ForeignKey(db_column='cod_cidade', on_delete=django.db.models.deletion.CASCADE, to='api.cidade')),
            ],
            options={
                'db_table': 'tb_empresa',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('cod_pais', models.IntegerField(db_column='cod_pais', primary_key=True, serialize=False)),
                ('sgl_pais', models.CharField(db_column='sgl_pais', max_length=2)),
                ('nom_pais', models.CharField(db_column='nom_pais', max_length=255)),
            ],
            options={
                'db_table': 'tb_pais',
                'ordering': ('nom_pais',),
            },
        ),
        migrations.CreateModel(
            name='StatusEntrevista',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tb_status_entrevista',
                'ordering': ('valor',),
            },
        ),
        migrations.CreateModel(
            name='StatusInscricao',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tb_status_inscricao',
                'ordering': ('valor',),
            },
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('resposabilidades', models.TextField(blank=True, max_length=4000, null=True)),
                ('requisitos', models.TextField(blank=True, max_length=4000, null=True)),
                ('pcsc', models.TextField(blank=True, max_length=4000, null=True)),
                ('remoto', models.BooleanField()),
                ('departamento', models.CharField(max_length=255)),
                ('faixa_salarial', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('cargo_horaria', models.CharField(max_length=255)),
                ('data_cadastro', models.DateField(auto_now=True)),
                ('data_fechamento', models.DateField(blank=True, null=True)),
                ('tipo_contrato', models.CharField(choices=[('indeterminado', 'Indeterminado'), ('indeterminado', 'Determinado'), ('obra_certa', 'Obra certa'), ('intermitente', 'Intermitente')], max_length=30)),
                ('contratacao', models.CharField(choices=[('clt', 'CLT'), ('pj', 'PJ')], max_length=30)),
                ('fim', models.DateField()),
                ('atual', models.BooleanField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
            options={
                'db_table': 'tb_vaga',
                'ordering': ('data_cadastro',),
            },
        ),
        migrations.CreateModel(
            name='InstituicaoEnsino',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('sede', models.ForeignKey(db_column='cod_cidade', on_delete=django.db.models.deletion.CASCADE, to='api.cidade')),
            ],
            options={
                'db_table': 'tb_instituicao',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('data_inscricao', models.DateField(auto_created=True)),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('feedback', models.CharField(blank=True, max_length=4000, null=True)),
                ('apto_entrevista', models.BooleanField(blank=True, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.statusinscricao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vaga')),
            ],
            options={
                'db_table': 'tb_inscricao',
                'ordering': ('data_inscricao',),
            },
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=4000)),
                ('nivel', models.CharField(choices=[('médio', 'Médio'), ('superior', 'Superior'), ('especialização', 'Especialização'), ('mestrado', 'Mestrado'), ('doutorado', 'doutorado')], max_length=30)),
                ('inicio', models.DateField()),
                ('previsao_termino', models.DateField(blank=True, null=True)),
                ('em_andamento', models.BooleanField(blank=True, null=True)),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curriculo')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instituicaoensino')),
            ],
            options={
                'db_table': 'tb_formacao',
                'ordering': ('inicio',),
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=4000)),
                ('cargo', models.CharField(max_length=4000)),
                ('local', models.CharField(choices=[('médio', 'Médio'), ('superior', 'Superior'), ('especialização', 'Especialização'), ('mestrado', 'Mestrado'), ('doutorado', 'doutorado')], max_length=30)),
                ('inicio', models.DateField()),
                ('fim', models.DateField(blank=True, null=True)),
                ('atual', models.BooleanField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curriculo')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
            options={
                'db_table': 'tb_experiencia',
                'ordering': ('inicio',),
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('cod_estado', models.IntegerField(db_column='cod_estado', primary_key=True, serialize=False)),
                ('nom_estado', models.CharField(db_column='nom_estado', max_length=255)),
                ('sgl_estado', models.CharField(db_column='sgl_estado', max_length=2)),
                ('cod_pais', models.OneToOneField(db_column='cod_pais', on_delete=django.db.models.deletion.CASCADE, to='api.pais')),
            ],
            options={
                'db_table': 'tb_estado',
                'ordering': ('nom_estado',),
            },
        ),
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('data', models.DateField(auto_created=True)),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('feedback', models.CharField(blank=True, max_length=4000, null=True)),
                ('inscricao', models.ForeignKey(db_column='id_inscricao', on_delete=django.db.models.deletion.CASCADE, to='api.inscricao')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.statusentrevista')),
            ],
            options={
                'db_table': 'tb_entrevista',
                'ordering': ('data',),
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='cod_estado',
            field=models.OneToOneField(db_column='cod_estado', on_delete=django.db.models.deletion.CASCADE, to='api.estado'),
        ),
    ]
