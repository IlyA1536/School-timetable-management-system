# Generated by Django 5.0.2 on 2024-02-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='title',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]