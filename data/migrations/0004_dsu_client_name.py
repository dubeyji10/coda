# Generated by Django 4.0.3 on 2022-04-06 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_dsu_uploaded_alter_dsu_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsu',
            name='client_name',
            field=models.CharField(default='admin', max_length=255),
        ),
    ]