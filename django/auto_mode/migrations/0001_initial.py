# Generated by Django 2.1.11 on 2020-01-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jpyutc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField(verbose_name='time')),
                ('open_data', models.TextField(verbose_name='open_data')),
                ('high_data', models.TextField(verbose_name='high_data')),
                ('row_data', models.TextField(verbose_name='row_data')),
                ('close_data', models.TextField(verbose_name='close_data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]