# Generated by Django 2.2.6 on 2020-02-18 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200218_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_type_id',
        ),
    ]
