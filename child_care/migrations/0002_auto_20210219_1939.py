# Generated by Django 3.1.5 on 2021-02-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_care', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sender',
            field=models.EmailField(max_length=200),
        ),
    ]
