# Generated by Django 4.1.1 on 2022-10-10 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0003_alter_conta_options_alter_fornecedor_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='conta',
            table='crud_app_conta',
        ),
        migrations.AlterModelTable(
            name='fornecedor',
            table='crud_app_fornecedor',
        ),
    ]
