# Generated by Django 4.0.3 on 2022-03-23 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='client',
            new_name='user',
        ),
    ]