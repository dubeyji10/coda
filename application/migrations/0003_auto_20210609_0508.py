# Generated by Django 3.0.7 on 2021-06-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='policy_doc',
            field=models.FileField(blank=True, default=None, null=True, upload_to='policy/doc/'),
        ),
    ]