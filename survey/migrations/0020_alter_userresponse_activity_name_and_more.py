# Generated by Django 4.2.11 on 2024-04-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0019_alter_userresponse_activity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='activity_name',
            field=models.CharField(choices=[('Accreditation', 'S1'), ('Authentication', 'S2'), ('Certification', 'S3'), ('Data Request', 'S4'), ('Financial Assistance', 'S5'), ('Follow-up', 'S6'), ('Interview/Research', 'S7'), ('Legal Assitance', 'S8'), ('Licensing', 'S9'), ('Medical Assistance', 'S10'), ('Meetings', 'S11'), ('Policy Review', 'S12'), ('Registration', 'S13'), ('Secretariat', 'S14'), ('Submission', 'S15'), ('Technical Assistance', 'S16'), ('Others', 'Others')], default='choice1', max_length=100),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='bureau_service_region_acronym',
            field=models.CharField(choices=[('Group 1', (('choice1', 'Choice 1'), ('choice2', 'Choice 2'))), ('Group 2', (('choice3', 'Choice 3'), ('choice4', 'Choice 4')))], default='choice1', max_length=100),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='team_acronym',
            field=models.CharField(choices=[('Office of the Chief of Staff', 'OCS'), ('Administration and Finance Management Team', 'AFMT'), ('Field Implementation and Coordination Team', 'FICT'), ('Health Facilities and Infrastructure Development Team', 'HFIDT'), ('Public Health Services Team', 'PHST'), ('Health Policy and Systems Development Team', 'HPSDT'), ('Health Regulation Team', 'HRT'), ('Procurement and Supply', 'PSCMT')], default='choice1', max_length=100),
        ),
    ]
