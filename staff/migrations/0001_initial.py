# Generated by Django 3.1.6 on 2021-03-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=14)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('permanentaddress', models.CharField(max_length=60)),
                ('dob', models.DateField()),
                ('idcard', models.ImageField(upload_to='idcard/')),
                ('joindate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]