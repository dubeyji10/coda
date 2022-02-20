# Generated by Django 3.2.6 on 2022-02-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='category',
            field=models.IntegerField(choices=[(1, 'Client Or Customer'), (2, 'Applicant')]),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')]),
        ),
    ]