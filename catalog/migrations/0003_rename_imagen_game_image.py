# Generated by Django 5.1.1 on 2024-10-10 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_descripcion_game_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='imagen',
            new_name='image',
        ),
    ]