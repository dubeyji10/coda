# Generated by Django 3.2.6 on 2021-08-19 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20210609_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('interview_type', models.CharField(choices=[('First Interview', 'First Interview'), ('Second Interview', 'Second Interview'), ('Third Interview', 'Third Interview'), ('No Outside Interview', 'No Outside Interview')], max_length=25)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10, null=True)),
                ('method', models.CharField(blank=True, choices=[('INSIDE', 'INSIDE'), ('OUTSIDE', 'OUTSIDE')], max_length=10, null=True)),
                ('reporting_date', models.DateTimeField(blank=True, null=True, verbose_name='Reporting Date(mm/dd/yyyy)')),
                ('update_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('comment', models.TextField()),
            ],
        ),
    ]