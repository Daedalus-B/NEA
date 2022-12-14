# Generated by Django 4.0.3 on 2022-11-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=100)),
                ('Year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mark_for_Astar', models.PositiveSmallIntegerField()),
                ('mark_for_A', models.PositiveSmallIntegerField()),
                ('mark_for_B', models.PositiveSmallIntegerField()),
                ('mark_for_C', models.PositiveSmallIntegerField()),
                ('mark_for_D', models.PositiveSmallIntegerField()),
                ('mark_for_E', models.PositiveSmallIntegerField()),
                ('mark_for_F', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
