# Generated by Django 4.0.5 on 2022-06-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEPets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='vacinado',
            field=models.BooleanField(choices=[(True, 'Vacinado'), (False, 'Não vacinado')], default=False),
        ),
    ]
