# Generated by Django 3.0.3 on 2020-04-03 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meals',
            new_name='Meal',
        ),
    ]
