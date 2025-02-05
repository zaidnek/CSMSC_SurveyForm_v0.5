# Generated by Django 4.2.11 on 2024-04-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0015_alter_userresponse_team_acronym'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamAcronym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_acronym', models.CharField(choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2')], default='choice1', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='team_acronym',
        ),
    ]
