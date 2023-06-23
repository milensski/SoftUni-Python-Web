# Generated by Django 4.2.2 on 2023-06-23 08:31

import django.core.validators
from django.db import migrations, models
import my_plant_app.plant_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Username')),
                ('first_name', models.CharField(max_length=20, validators=[my_plant_app.plant_app.validators.validate_name_capital_letter], verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, validators=[my_plant_app.plant_app.validators.validate_name_capital_letter], verbose_name='Last name')),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]