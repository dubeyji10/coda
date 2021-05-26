# Generated by Django 3.0.7 on 2021-05-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customeruser_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='category',
            field=models.IntegerField(choices=[(1, 'Data Analysis Course'), (2, 'Trading Course'), (3, 'Employee'), (4, 'Applicant')], default=9999),
        ),
    ]
