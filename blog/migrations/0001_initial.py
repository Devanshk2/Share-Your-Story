# Generated by Django 3.1 on 2020-10-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('author', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
