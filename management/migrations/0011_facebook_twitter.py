# Generated by Django 3.2.6 on 2022-06-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_requirement_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_access_token', models.CharField(blank=True, max_length=500, null=True)),
                ('facebook_page_id', models.CharField(blank=True, max_length=100, null=True)),
                ('page_name', models.CharField(blank=True, max_length=100, null=True)),
                ('post_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Uploads/Facebook/')),
                ('file', models.FileField(blank=True, null=True, upload_to='Uploads/Facebook/')),
                ('link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_api_key', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter_api_key_secret', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter_bearer_token', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter_access_token', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter_access_token_secret', models.CharField(blank=True, max_length=500, null=True)),
                ('post_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Uploads/Twitter/')),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]