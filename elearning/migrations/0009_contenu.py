# Generated by Django 4.2 on 2023-05-05 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0008_alter_etudiant_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=400)),
                ('format', models.CharField(max_length=200)),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.cour')),
            ],
        ),
    ]