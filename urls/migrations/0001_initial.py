# Generated by Django 4.1.7 on 2023-03-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.URLField(max_length=250)),
                ('shorturl', models.URLField()),
            ],
        ),
    ]
