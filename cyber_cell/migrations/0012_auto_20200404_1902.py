# Generated by Django 3.0.3 on 2020-04-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_cell', '0011_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='age',
            field=models.IntegerField(max_length=30),
        ),
    ]