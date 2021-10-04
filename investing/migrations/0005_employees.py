# Generated by Django 3.2.6 on 2021-09-22 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investing', '0004_auto_20210918_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]