# Generated by Django 4.0.1 on 2022-02-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_remove_userform_gymtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='schedule',
            field=models.CharField(default=' ', max_length=25),
        ),
    ]
