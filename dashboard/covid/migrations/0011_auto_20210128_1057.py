# Generated by Django 3.1.5 on 2021-01-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0010_auto_20210128_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wcotabasenacional',
            name='cod_regiaodesaude',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='wcotabasenacional',
            name='ibgeid',
            field=models.TextField(),
        ),
    ]