# Generated by Django 4.1.3 on 2022-12-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerHome', '0005_auto_20210129_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=256)),
                ('facebook', models.CharField(max_length=256)),
                ('linkedin', models.CharField(max_length=256)),
            ],
        ),
    ]
