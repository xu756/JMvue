# Generated by Django 3.2.12 on 2022-03-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_auto_20220305_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isLogin',
            field=models.BooleanField(default=True),
        ),
    ]
