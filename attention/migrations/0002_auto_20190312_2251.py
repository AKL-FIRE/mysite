# Generated by Django 2.1.5 on 2019-03-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attention', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attention',
            old_name='text',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='attention',
            name='attention_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
