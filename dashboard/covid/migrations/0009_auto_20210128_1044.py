# Generated by Django 3.1.5 on 2021-01-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0008_auto_20210128_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wcotabasenacional',
            name='date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='wcotabasenacional',
            name='last_info_date',
            field=models.TextField(),
        ),
    ]