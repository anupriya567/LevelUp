# Generated by Django 2.2 on 2021-05-14 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_blogcomment_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
