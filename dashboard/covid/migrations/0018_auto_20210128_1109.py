# Generated by Django 3.1.5 on 2021-01-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0017_auto_20210128_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wcotabasenacional',
            name='field_source',
            field=models.TextField(),
        ),
    ]