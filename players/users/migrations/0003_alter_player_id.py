# Generated by Django 5.0.4 on 2024-04-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_player_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
