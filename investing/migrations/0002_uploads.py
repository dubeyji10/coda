# Generated by Django 3.0.7 on 2021-02-27 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('investing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doc_type', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_name', models.CharField(blank=True, max_length=100, null=True)),
                ('doc', models.FileField(upload_to='Uploads/doc/')),
                ('link', models.FileField(upload_to='Uploads/doc/')),
            ],
        ),
    ]