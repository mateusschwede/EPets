# Generated by Django 4.0.5 on 2022-06-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEPets', '0003_alter_pet_adotado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
