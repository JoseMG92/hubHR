# Generated by Django 4.0.4 on 2022-05-20 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_contrato_job_title_contrato_job_title_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colleagues',
            new_name='Associates',
        ),
        migrations.RenameModel(
            old_name='Contrato',
            new_name='Contracts',
        ),
        migrations.RenameModel(
            old_name='StatusUser',
            new_name='UserStatus',
        ),
        migrations.RenameField(
            model_name='associates',
            old_name='contrato',
            new_name='contract',
        ),
    ]
