# Generated by Django 5.0.6 on 2024-06-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_alter_teacher_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]