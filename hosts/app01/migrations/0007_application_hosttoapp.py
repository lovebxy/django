# Generated by Django 2.2.6 on 2019-12-30 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_business_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostToApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aobj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Application')),
                ('hobj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Host')),
            ],
        ),
    ]