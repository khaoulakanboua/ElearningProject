# Generated by Django 4.1.7 on 2023-04-28 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_rename_cni_enseignant_cin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cour',
            old_name='format',
            new_name='formation',
        ),
    ]
