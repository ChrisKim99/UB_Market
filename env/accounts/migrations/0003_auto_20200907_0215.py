# Generated by Django 3.1 on 2020-09-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200907_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
