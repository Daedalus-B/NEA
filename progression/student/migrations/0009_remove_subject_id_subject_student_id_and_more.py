# Generated by Django 4.0.3 on 2022-11-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_topic_target_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='id',
        ),
        migrations.AddField(
            model_name='subject',
            name='student_id',
            field=models.BigAutoField(default=None, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.BigAutoField(default=None, primary_key=True, serialize=False, unique=True),
        ),
    ]