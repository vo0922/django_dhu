# Generated by Django 3.2.7 on 2021-10-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20211028_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
