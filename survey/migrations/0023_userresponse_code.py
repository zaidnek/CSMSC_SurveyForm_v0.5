# Generated by Django 4.2.11 on 2024-04-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0022_alter_userresponse_activity_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
