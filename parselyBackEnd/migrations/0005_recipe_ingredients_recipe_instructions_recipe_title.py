# Generated by Django 4.0.6 on 2022-08-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parselyBackEnd', '0004_remove_recipe_ingredients_remove_recipe_instructions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]