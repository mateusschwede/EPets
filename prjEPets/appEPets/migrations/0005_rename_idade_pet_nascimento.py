# Generated by Django 4.0.5 on 2022-06-09 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appEPets', '0004_alter_pet_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='idade',
            new_name='nascimento',
        ),
    ]
