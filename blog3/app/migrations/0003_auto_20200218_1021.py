# Generated by Django 2.2.6 on 2020-02-18 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200218_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_type',
            new_name='article_type_id',
        ),
    ]
