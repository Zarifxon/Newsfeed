# Generated by Django 5.1.6 on 2025-02-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0003_alter_news_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
