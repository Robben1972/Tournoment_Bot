# Generated by Django 5.0.4 on 2024-04-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_winners_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='winner',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
