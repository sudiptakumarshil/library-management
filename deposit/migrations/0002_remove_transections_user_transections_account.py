# Generated by Django 5.0.6 on 2024-08-31 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transections',
            name='user',
        ),
        migrations.AddField(
            model_name='transections',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='user.useraccount'),
            preserve_default=False,
        ),
    ]
