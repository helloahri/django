# Generated by Django 2.2.5 on 2020-08-16 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书'},
        ),
        migrations.AlterModelOptions(
            name='peopleinfo',
            options={'verbose_name': '人物信息'},
        ),
        migrations.RenameField(
            model_name='bookinfo',
            old_name='pab_data',
            new_name='pub_date',
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]