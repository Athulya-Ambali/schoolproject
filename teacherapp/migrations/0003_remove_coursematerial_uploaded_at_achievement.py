# Generated by Django 5.0.4 on 2024-05-21 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_student'),
        ('teacherapp', '0002_coursematerial_batch_coursematerial_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerial',
            name='uploaded_at',
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('class_performance', models.CharField(choices=[('Good', 'Good'), ('Bad', 'Bad'), ('Average', 'Average')], max_length=7)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student')),
            ],
        ),
    ]
