# Generated by Django 2.2.5 on 2020-08-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'man'), ('F', 'female')], max_length=2),
        ),
    ]
