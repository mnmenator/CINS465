# Generated by Django 2.1.7 on 2019-03-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190227_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChirpItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chirp_field', models.CharField(max_length=240)),
            ],
        ),
    ]
