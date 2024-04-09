from django import forms
from django.forms import ModelForm
# from .models import TeamAcronym

class QuestionnaireForm(forms.Form):
    # Basic Information
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    staff_name = forms.CharField(label='Name of staff who rendered the service?', max_length=100)
    sex = forms.ChoiceField(label='Sex', choices=(('Male', 'Male'), ('Female', 'Female')), widget=forms.RadioSelect)
    doh_employee = forms.ChoiceField(label='DOH Employee', choices=(('Yes', 'Yes'), ('No', 'No')), widget=forms.RadioSelect)
   

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
    team_acronym = forms.ChoiceField(choices=MY_CHOICES)

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
    bureau_service_region_acronym = forms.ChoiceField(choices=MY_CHOICES2)

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
    activity_name = forms.ChoiceField(choices=MY_CHOICES3)

    # Section A: Overall Expectation
    EXPECTATION_CHOICES = [
        ('1', 'Very Poor'), ('2', 'Poor'), ('3', 'Fair'), ('4', 'Good'), ('5', 'Very Good'), ('6', 'Excellent'), ('7', 'Outstanding')
    ]
    expectation = forms.ChoiceField(label='Section A: How would you rate your overall expectation of the service provider’s service?', choices=EXPECTATION_CHOICES, widget=forms.RadioSelect)

    # Section B: Statement Ratings fields...
    STATEMENTS = {
        "1. The service provider/s provides its service at the time it promises to do so.": 'statement1',
        "2. You receive prompt service from service providers.": 'statement2',
        "3. The service provider/s is/are polite.": 'statement3',
        "4. The service provider/s is/are sensitive to the client’s needs.": 'statement4',
        "5. The service provider/s is/are well dressed and appear neat.": 'statement5',
        "6. The appearance of the physical/virtual facility of the service provider is in keeping with the type of service/s provided.": 'statement6'
    }
    for statement, field_name in STATEMENTS.items():
        locals()[field_name] = forms.ChoiceField(
            label=statement,  # Set label for each statement
            choices=[(i, i) for i in range(1, 8)],
            widget=forms.RadioSelect
        )

    # Section C: Service Quality
    QUALITY_CHOICES = [
        ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Excellent')
    ]
    quality = forms.ChoiceField(label='Section C: Overall, how would you rate the quality of service provided by the service provider/s?', choices=QUALITY_CHOICES, widget=forms.RadioSelect)

    # Section D: Comments and Feedback
    # comments = forms.CharField(label='Section D: For comments, recommendations, concerns, or aspects of our service(s) that need improvement, please put it down below. If you wish for us to respond to your feedback, please include your contact details.', widget=forms.Textarea)
    comments = forms.CharField(required=False,
        label='Section D: For comments, recommendations, concerns, or aspects of our service(s) that need improvement, please put it down below. If you wish for us to respond to your feedback, please include your contact details.',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 100})  # Adjust the rows and cols as needed
    )

    def clean(self):
        cleaned_data = super().clean()

        # Perform custom validation here
        # Example: Ensure that either 'Male' or 'Female' is selected for the 'sex' field
        sex = cleaned_data.get('sex')
        if sex not in ['Male', 'Female']:
            self.add_error('sex', 'Please select a valid option for sex.')

        # Add more custom validation rules as needed...

        return cleaned_data

# class TeamAcronymForm(ModelForm):
#         models = TeamAcronym
#         fields = ['team_acronym']

