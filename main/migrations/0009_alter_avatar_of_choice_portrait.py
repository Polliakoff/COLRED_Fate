# Generated by Django 4.0.3 on 2022-05-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_character_armour_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar_of_choice',
            name='portrait',
            field=models.ImageField(null=True, upload_to='user_images/'),
        ),
    ]
