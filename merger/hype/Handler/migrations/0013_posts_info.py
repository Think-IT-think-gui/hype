# Generated by Django 3.2.10 on 2022-10-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0012_delete_posts_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.CharField(max_length=100)),
                ('Link', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Text', models.CharField(max_length=500)),
                ('Rate', models.CharField(max_length=100)),
                ('User_Idd', models.CharField(max_length=100)),
            ],
        ),
    ]
