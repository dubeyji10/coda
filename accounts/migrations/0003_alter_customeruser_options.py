# Generated by Django 3.2.6 on 2022-07-06 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customeruser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customeruser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]