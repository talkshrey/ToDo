# Generated by Django 3.2.8 on 2022-01-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0002_auto_20210910_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='compulsory',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='description',
            field=models.TextField(),
        ),
    ]