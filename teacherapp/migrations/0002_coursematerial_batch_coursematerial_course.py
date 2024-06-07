# Generated by Django 5.0.4 on 2024-05-17 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_student'),
        ('teacherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerial',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.batch'),
        ),
        migrations.AddField(
            model_name='coursematerial',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.course'),
        ),
    ]