# Generated by Django 3.2.4 on 2021-06-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_auto_20210630_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcards',
            name='check_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='creditcards',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
