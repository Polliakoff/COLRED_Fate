# Generated by Django 4.0.3 on 2022-05-04 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_avatar_of_choice_custom_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar_of_choice',
            name='name',
        ),
    ]
