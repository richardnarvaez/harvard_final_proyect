# Generated by Django 3.2.8 on 2021-12-17 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejob_app', '0003_job_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='keywords',
            field=models.TextField(default='no_indexing', max_length=1000),
        ),
    ]