# Generated by Django 3.0.5 on 2022-04-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='additem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plno', models.CharField(max_length=120)),
                ('relatedplno', models.CharField(max_length=120)),
                ('unifiedplno', models.CharField(max_length=120)),
                ('desc', models.TextField(max_length=500)),
                ('aac', models.CharField(max_length=120)),
                ('specno', models.CharField(max_length=500)),
                ('gw', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
