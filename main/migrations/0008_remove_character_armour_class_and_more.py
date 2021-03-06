# Generated by Django 4.0.3 on 2022-05-05 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_character_custom_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='armour_class',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attack',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attention',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attrib_agility',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attrib_charisma',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attrib_endurance',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attrib_intelligence',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attrib_strength',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attrib_wisdom',
        ),
        migrations.RemoveField(
            model_name='character',
            name='background',
        ),
        migrations.RemoveField(
            model_name='character',
            name='chr_class',
        ),
        migrations.RemoveField(
            model_name='character',
            name='damage',
        ),
        migrations.RemoveField(
            model_name='character',
            name='dc_class',
        ),
        migrations.RemoveField(
            model_name='character',
            name='diety',
        ),
        migrations.RemoveField(
            model_name='character',
            name='hp',
        ),
        migrations.RemoveField(
            model_name='character',
            name='is_dying',
        ),
        migrations.RemoveField(
            model_name='character',
            name='mortal_wounds',
        ),
        migrations.RemoveField(
            model_name='character',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='character',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='character',
            name='save_reflex',
        ),
        migrations.RemoveField(
            model_name='character',
            name='save_resilience',
        ),
        migrations.RemoveField(
            model_name='character',
            name='save_will',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_acrobatics',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_arcane',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_athletics',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_craft',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_decieve',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_diplomacy',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_intimidation',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_medicine',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_nature',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_occult',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_performance',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_religion',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_social',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_stealth',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_survival',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skills_theft',
        ),
        migrations.RemoveField(
            model_name='character',
            name='speed',
        ),
        migrations.RemoveField(
            model_name='character',
            name='weapon',
        ),
        migrations.RemoveField(
            model_name='character',
            name='worldview',
        ),
        migrations.RemoveField(
            model_name='character',
            name='xp',
        ),
        migrations.AddField(
            model_name='character',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='character',
            name='fate_point_number',
            field=models.IntegerField(blank=True, default=3),
        ),
        migrations.AddField(
            model_name='character',
            name='fate_point_refresh',
            field=models.IntegerField(blank=True, default=3),
        ),
        migrations.AddField(
            model_name='character',
            name='high_concept',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='character',
            name='max_skill',
            field=models.IntegerField(blank=True, default=5),
        ),
        migrations.AddField(
            model_name='character',
            name='min_skill',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='trouble',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='character',
            name='custom_avatar',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.CreateModel(
            name='stunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(blank=True, default='', max_length=10000)),
                ('chr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.character')),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('level', models.IntegerField(blank=True, default=0)),
                ('chr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.character')),
            ],
        ),
        migrations.CreateModel(
            name='extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('cost', models.CharField(blank=True, default='', max_length=100)),
                ('attached_aspects', models.CharField(blank=True, default='', max_length=10000)),
                ('attached_stunts', models.CharField(blank=True, default='', max_length=10000)),
                ('attached_skills', models.CharField(blank=True, default='', max_length=10000)),
                ('details', models.CharField(blank=True, default='', max_length=10000)),
                ('chr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.character')),
            ],
        ),
        migrations.CreateModel(
            name='consequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(blank=True, default='', max_length=10000)),
                ('chr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.character')),
            ],
        ),
        migrations.CreateModel(
            name='aspect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=1000)),
                ('chr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.character')),
            ],
        ),
    ]
