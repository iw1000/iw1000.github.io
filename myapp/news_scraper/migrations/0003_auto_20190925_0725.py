# Generated by Django 2.2.5 on 2019-09-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_scraper', '0002_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(default='Empty content', max_length=1000),
        ),
    ]
