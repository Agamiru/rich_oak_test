# Generated by Django 3.2.4 on 2021-06-30 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_auto_20210630_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountdetails',
            name='bvn',
        ),
    ]
