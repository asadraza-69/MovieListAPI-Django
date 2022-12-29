# Generated by Django 3.2a1 on 2022-12-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('active', models.BooleanField(blank=True, default=True, null=True, verbose_name='active')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
