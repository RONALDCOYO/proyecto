# Generated by Django 5.1.2 on 2024-10-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependencia',
            name='inicio_consecutivo',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='correspondencia',
            name='consecutivo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]