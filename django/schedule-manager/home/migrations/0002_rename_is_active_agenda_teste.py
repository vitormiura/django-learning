# Generated by Django 4.0.6 on 2022-07-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='is_active',
            new_name='teste',
        ),
    ]