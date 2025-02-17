# Generated by Django 5.1 on 2024-08-15 20:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
