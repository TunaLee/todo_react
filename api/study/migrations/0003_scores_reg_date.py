# Generated by Django 3.1.1 on 2020-09-15 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='reg_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
