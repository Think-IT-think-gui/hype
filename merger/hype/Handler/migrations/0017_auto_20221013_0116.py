# Generated by Django 3.2.10 on 2022-10-13 01:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0016_user_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_comments',
            name='Text',
        ),
        migrations.AddField(
            model_name='user_comments',
            name='Text_Value',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
