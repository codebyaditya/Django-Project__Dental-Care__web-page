# Generated by Django 4.1.7 on 2023-04-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_news_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_desc',
            field=models.TextField(),
        ),
    ]
