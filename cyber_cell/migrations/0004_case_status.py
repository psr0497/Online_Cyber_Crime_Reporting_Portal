# Generated by Django 3.0.3 on 2020-04-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_cell', '0003_auto_20200403_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.CharField(default='In_Progress', max_length=30),
        ),
    ]
