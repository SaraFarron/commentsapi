# Generated by Django 3.2.5 on 2021-08-06 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_auto_20210806_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='child_comments',
            field=models.ManyToManyField(to='comments.Comment'),
        ),
    ]