# Generated by Django 4.2 on 2023-05-01 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0005_etudiant_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
    ]
