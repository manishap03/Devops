# Generated by Django 2.1.15 on 2022-11-28 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=20)),
                ('messsage', models.CharField(max_length=150)),
                ('date', models.DateField()),
            ],
        ),
    ]
