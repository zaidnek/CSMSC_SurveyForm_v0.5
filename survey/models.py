from django.db import models
from django.contrib.auth.models import User
from django import forms

class UserResponse(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    staff_name = models.CharField(max_length=100, null=True)
       
    SEX_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, null=True)
    
    DOH_EMPLOYEE_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ]
    doh_employee = models.CharField(max_length=3, choices=DOH_EMPLOYEE_CHOICES, null=True)

    #################TEAM ACRONYM################
    MY_CHOICES = [
    ('Office of the Chief of Staff', 'OCS - Office of the Chief of Staff'),
    ('Administration and Finance Management Team', 'AFMT - Administration and Finance Management Team'),
    ('Field Implementation and Coordination Team', 'FICT - Field Implementation and Coordination Team'),
    ('Health Facilities and Infrastructure Development Team', 'HFIDT - Health Facilities and Infrastructure Development Team'),
    ('Public Health Services Team', 'PHST - Public Health Services Team'),
    ('Health Policy and Systems Development Team', 'HPSDT - Health Policy and Systems Development Team'),
    ('Health Regulation Team', 'HRT - Health Regulation Team'),
    ('Procurement and Supply', 'PSCMT - Procurement and Supply'),
    ]
    team_acronym = models.CharField(
        max_length=100,
        choices=MY_CHOICES,
    )
    
    #################Bureau/Region ACRONYM################
    MY_CHOICES2 = [
    ('Administration and Financial Management Team', (
        ('Administrative Service', 'AS - Administrative Service'),
        ('Personnel Administrative Division', 'PAD - Personnel Administrative Division'),
        ('Malasakit Program Office', 'MPO - Malasakit Program Office'),
        ('Financial Management Service', 'FMS - Financial Management Service'),
    )),
    ('Field Implementation and Coordination Team', (
        ('Center for Health Development I', 'CHD I - Center for Health Development I'),
        ('Center for Health Development II', 'CHD II - Center for Health Development II'),
        ('Center for Health Development III', 'CHD III - Center for Health Development III'),
        ('Center for Health Development IV-A', 'CHD IV-A - Center for Health Development IV-A'),
        ('Center for Health Development IV-B', 'CHD IV-B - Center for Health Development IV-B'),
        ('Center for Health Development V', 'CHD V - Center for Health Development V'),
        ('Center for Health Development VI', 'CHD VI - Center for Health Development VI'),
        ('Center for Health Development VII', 'CHD VII - Center for Health Development VII'),
        ('Center for Health Development VIII', 'CHD VIII - Center for Health Development VIII'),
        ('Center for Health Development IX', 'CHD IX - Center for Health Development IX'),
        ('Center for Health Development X', 'CHD X - Center for Health Development X'),
        ('Center for Health Development XI', 'CHD XI - Center for Health Development XI'),
        ('Center for Health Development XII', 'CHD XII - Center for Health Development XII'),
        ('Center for Health Development NCR', 'CHD NCR - Center for Health Development NCR'),
        ('Center for Health Development CAR', 'CHD CAR - Center for Health Development CAR'),
        ('Center for Health Development CARAGA', 'CHD CARAGA - Center for Health Development CARAGA'),
        ('Center for Health Development ARMM', 'CHD ARMM - Center for Health Development ARMM'),
    )),
    ('Health Facilities and Infrastructure Development Team', (
        ('Health Facilities Development Bureau', 'HFDB - Health Facilities Development Bureau'),
        ('Knowledge Management and Information Technology', 'KMITS - Knowledge Management and Information Technology'),
    )),
    ('Procurement and Supply Chain Management Team', (
        ('Procurement Service', 'PS - Procurement Service'),
        ('Supply Chain Management Office', 'SCMO - Supply Chain Management Office'),
    )),
    ('Health Policy and Systems Development Team', (
        ('Bureau of International Health Cooperation', 'BIHC - Bureau of International Health Cooperation'),
        ('Bureau of Local Health Systems and Development', 'BLHSD - Bureau of Local Health Systems and Development'),
        ('Health Human Resource Development Bureau', 'HHRDB - Health Human Resource Development Bureau'),
        ('Health Policy Development and Planning Bureau', 'HPDPB - Health Policy Development and Planning Bureau'),       
    )),    
    ('Health Regulation Team', (
        ('Bureau of Quarantine', 'BOQ - Bureau of Quarantine'),
        ('Food and Drug Administration', 'FDA - Food and Drug Administration'),
        ('Health Facilities Services and Regulatory Bureau', 'HFSRB - Health Facilities Services and Regulatory Bureau'),
    )),
    ('Public Health Service Team', (
        ('Disease Prevention and Control Bureau', 'DPCB - Disease Prevention and Control Bureau'),
        ('Epidemiology Bureau', 'EB - Epidemiology Bureau'),
        ('Health Emergency Management Bureau', 'HEMB - Health Emergency Management Bureau'),
        ('Health Promotion and Communication Services', 'HPCS - Health Promotion and Communication Services'),
    )),      
    ]
    bureau_service_region_acronym = models.CharField(
        max_length=100,
        choices=MY_CHOICES2,
    )

    #################Activity ACRONYM################
    MY_CHOICES3 = [
    ('Accreditation', 'S1 - Accreditation'),
    ('Authentication', 'S2 - Authentication'),
    ('Certification', 'S3 - Certification'),
    ('Data Request', 'S4 - Data Request'),
    ('Financial Assistance', 'S5 - Financial Assistance'),
    ('Follow-up', 'S6 - Follow-up'),
    ('Interview/Research', 'S7 - Interview/Research'),
    ('Legal Assitance', 'S8 - Legal Assitance'),
    ('Licensing', 'S9 - Licensing'),
    ('Medical Assistance', 'S10 - Medical Assistance'),
    ('Meetings', 'S11 - Meetings'),
    ('Policy Review', 'S12 - Policy Review'),
    ('Registration', 'S13 - Registration'),
    ('Secretariat', 'S14 - Secretariat'),
    ('Submission', 'S15 - Submission'),
    ('Technical Assistance', 'S16 - Technical Assistance'),
    ('Others', 'Others'),
    ] 
    activity_name = models.CharField(
        max_length=100,
        choices=MY_CHOICES3,
    )


    expectation = models.CharField(max_length=20, null=True)
    statement1_rating = models.IntegerField(null=True)
    statement2_rating = models.IntegerField(null=True)
    statement3_rating = models.IntegerField(null=True)
    statement4_rating = models.IntegerField(null=True)
    statement5_rating = models.IntegerField(null=True)
    statement6_rating = models.IntegerField(null=True)
    quality = models.CharField(max_length=20, null=True)
    comments = models.TextField(null=True)

    def __str__(self):
        return f"UserResponse object (id: {self.id})"

