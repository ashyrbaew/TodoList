# Generated by Django 2.2.6 on 2019-11-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
