# Generated by Django 4.2.1 on 2023-05-29 00:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=300)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.country')),
            ],
        ),
    ]
