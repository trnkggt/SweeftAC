# Generated by Django 4.1.7 on 2023-03-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0002_url_date_created_url_is_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
