# Generated by Django 4.0.2 on 2022-02-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkersApp', '0002_alter_worker_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='picture',
            field=models.ImageField(upload_to='./images/'),
        ),
    ]
