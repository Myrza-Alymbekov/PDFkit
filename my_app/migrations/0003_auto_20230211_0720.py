# Generated by Django 3.2 on 2023-02-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_user_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Юзер', 'verbose_name_plural': 'Юзеры'},
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='Photo'),
        ),
    ]
