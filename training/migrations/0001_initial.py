# Generated by Django 2.2 on 2019-04-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='training')),
                ('title', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('date', models.DateField(null=True)),
                ('desc', models.TextField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
