# Generated by Django 3.2.6 on 2021-08-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_interviewupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewupload',
            name='comment',
        ),
        migrations.AddField(
            model_name='interviewupload',
            name='doc',
            field=models.FileField(default='None', upload_to='Uploads/doc/'),
        ),
        migrations.AddField(
            model_name='interviewupload',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]