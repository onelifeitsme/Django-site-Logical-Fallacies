# Generated by Django 3.2.6 on 2021-09-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallacies', '0003_auto_20210916_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='fallacy',
            name='another_names',
            field=models.TextField(default='Another name 1'),
        ),
    ]
