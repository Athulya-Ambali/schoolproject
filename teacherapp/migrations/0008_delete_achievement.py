# Generated by Django 5.0.4 on 2024-06-04 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0007_alter_achievement_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Achievement',
        ),
    ]