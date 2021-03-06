# Generated by Django 4.0.3 on 2022-05-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_avatar_of_choice_portrait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspect',
            name='chr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_aspects', to='main.character'),
        ),
        migrations.AlterField(
            model_name='aspect',
            name='desc',
            field=models.CharField(default='Пустой аспект', max_length=1000),
        ),
        migrations.AlterField(
            model_name='consequence',
            name='chr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_consequences', to='main.character'),
        ),
        migrations.AlterField(
            model_name='extra',
            name='chr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_extras', to='main.character'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='chr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_skills', to='main.character'),
        ),
        migrations.AlterField(
            model_name='stunt',
            name='chr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_stunts', to='main.character'),
        ),
    ]
