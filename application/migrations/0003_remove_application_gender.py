# Generated by Django 3.0.7 on 2020-11-16 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20201115_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='gender',
        ),
    ]