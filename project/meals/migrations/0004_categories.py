# Generated by Django 3.0.3 on 2020-04-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_meal_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]