# Generated by Django 3.0 on 2019-12-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charField', models.CharField(max_length=1000)),
                ('fileField', models.FileField(upload_to='files')),
            ],
        ),
    ]
