# Generated by Django 3.1.6 on 2021-08-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20210710_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roomno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
