# Generated by Django 4.0.3 on 2022-05-07 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='is_active',
            new_name='permision',
        ),
    ]
