# Generated by Django 2.2 on 2019-04-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='tutor',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='duration',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='training',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
