# Generated by Django 3.2 on 2021-06-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_tilte_blogpost_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='desc0',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='desc1',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='desc2',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
