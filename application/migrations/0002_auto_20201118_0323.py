# Generated by Django 3.0.7 on 2020-11-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iupload',
            name='other',
            field=models.FileField(default='None', upload_to='Others/doc/'),
        ),
        migrations.CreateModel(
            name='FirstUpload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('ppt', models.FileField(upload_to='Powerpoints/doc/')),
                ('report', models.FileField(blank=True, null=True, upload_to='Reports/doc/')),
                ('workflow', models.FileField(blank=True, null=True, upload_to='Workflows/doc/')),
                ('proc', models.FileField(blank=True, null=True, upload_to='Procedures/doc/')),
                ('other', models.FileField(default='None', upload_to='Others/doc/')),
                ('Applicant', models.ManyToManyField(to='application.Application')),
            ],
        ),
    ]