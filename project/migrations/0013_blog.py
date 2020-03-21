# Generated by Django 3.0.4 on 2020-03-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('blog', models.TextField()),
                ('username', models.TextField(default='')),
            ],
        ),
    ]
