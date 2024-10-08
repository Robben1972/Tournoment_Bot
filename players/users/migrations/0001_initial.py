# Generated by Django 5.0.4 on 2024-04-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('fullname', models.CharField(max_length=40)),
                ('nickname', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=5)),
            ],
        ),
    ]
