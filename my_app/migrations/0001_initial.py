# Generated by Django 3.2 on 2023-02-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('place_of_birth', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Юзеры',
            },
        ),
    ]