# Generated by Django 4.0.4 on 2022-05-23 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_users_job_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='job_title',
            new_name='job_title_id',
        ),
    ]
