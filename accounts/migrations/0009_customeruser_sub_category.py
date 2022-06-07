# Generated by Django 3.2.6 on 2022-06-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_customeruser_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='sub_category',
            field=models.IntegerField(choices=[(1, 'Client Or Customer'), (2, 'Student')], default=999),
        ),
    ]
