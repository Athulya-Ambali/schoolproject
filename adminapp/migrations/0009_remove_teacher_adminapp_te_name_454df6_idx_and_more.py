# Generated by Django 5.0.6 on 2024-06-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_alter_teacher_email_alter_teacher_mobile_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_name_454df6_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_usernam_fdfc68_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_mobile_bb0338_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_email_efe1ac_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_course__021813_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_batch_i_1e0f1b_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_country_3ba787_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_state_i_880fe4_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='adminapp_te_city_id_651fbd_idx',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
