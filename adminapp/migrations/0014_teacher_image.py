# Generated by Django 5.0.6 on 2024-06-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0013_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]