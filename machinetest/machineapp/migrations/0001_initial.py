# Generated by Django 4.2.7 on 2023-11-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(db_index=True, max_length=100, null=True)),
                ('Lastname', models.CharField(db_index=True, max_length=100, null=True)),
                ('email', models.CharField(db_index=True, max_length=100, null=True)),
                ('password', models.CharField(db_index=True, max_length=100, null=True)),
            ],
        ),
    ]
