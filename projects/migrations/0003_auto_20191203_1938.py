# Generated by Django 3.0 on 2019-12-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191203_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
