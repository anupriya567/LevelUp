# Generated by Django 2.2 on 2021-05-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_blogpost_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=500)),
                ('desc', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]