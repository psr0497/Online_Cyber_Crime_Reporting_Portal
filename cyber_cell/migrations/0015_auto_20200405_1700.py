# Generated by Django 3.0.3 on 2020-04-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_cell', '0014_auto_20200404_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='image',
            field=models.ImageField(max_length=255, upload_to='static/victim/ '),
        ),
    ]
