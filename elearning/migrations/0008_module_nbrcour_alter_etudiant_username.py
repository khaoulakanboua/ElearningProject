# Generated by Django 4.2 on 2023-05-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0007_alter_etudiant_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='nbrCour',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]