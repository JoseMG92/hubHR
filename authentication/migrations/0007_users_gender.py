# Generated by Django 4.0.4 on 2022-05-24 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_users_sex'),
        ('dashboard', '0012_gender_remove_associates_sex_delete_sex_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.gender'),
        ),
    ]
