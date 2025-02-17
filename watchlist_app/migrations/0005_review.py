# Generated by Django 3.2a1 on 2022-12-31 14:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_alter_movie_plateform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='rating')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='description')),
                ('active', models.BooleanField(blank=True, default=True, null=True, verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_movie', to='watchlist_app.movie', verbose_name='movie')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
