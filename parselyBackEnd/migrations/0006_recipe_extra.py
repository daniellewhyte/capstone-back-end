# Generated by Django 4.0.6 on 2022-08-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parselyBackEnd', '0005_recipe_ingredients_recipe_instructions_recipe_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='extra',
            field=models.TextField(null=True),
        ),
    ]
