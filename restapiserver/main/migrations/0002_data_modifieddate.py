# Generated by Django 3.0.3 on 2020-03-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='modifiedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]