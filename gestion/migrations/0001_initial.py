# Generated by Django 5.1.2 on 2024-10-25 21:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_empresas/')),
            ],
        ),
        migrations.CreateModel(
            name='gestion_empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada_salida', models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=10)),
                ('tipo_correspondencia', models.CharField(choices=[('Carta', 'Carta'), ('Memorando', 'Memorando'), ('Email', 'Email'), ('DP', 'DP')], max_length=20)),
                ('consecutivo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('documento', models.FileField(blank=True, null=True, upload_to='correspondencias/')),
                ('asunto', models.CharField(max_length=255)),
                ('remitente', models.CharField(max_length=255)),
                ('destinatario', models.CharField(max_length=255)),
                ('necesita_respuesta', models.BooleanField(default=False)),
                ('fecha_respuesta', models.DateTimeField(blank=True, null=True)),
                ('fecha_limite_respuesta', models.DateTimeField(blank=True, null=True)),
                ('respondida', models.BooleanField(default=False)),
                ('respuesta', models.TextField(blank=True, null=True)),
                ('documento_respuesta', models.FileField(blank=True, null=True, upload_to='respuestas/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.dependencia')),
            ],
        ),
        migrations.AddField(
            model_name='dependencia',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.empresa'),
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencias', models.ManyToManyField(blank=True, to='gestion.dependencia')),
                ('empresas', models.ManyToManyField(blank=True, to='gestion.empresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaCorrespondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField()),
                ('fecha_respuesta', models.DateField()),
                ('documento_respuesta', models.FileField(blank=True, null=True, upload_to='respuestas/')),
                ('correspondencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.correspondencia')),
            ],
        ),
    ]
