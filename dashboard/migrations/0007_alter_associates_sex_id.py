# Generated by Django 4.0.4 on 2022-05-23 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rename_genre_id_associates_sex_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associates',
            name='sex_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.sex'),
        ),
    ]
