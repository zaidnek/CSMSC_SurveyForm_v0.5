import re
from django.shortcuts import render, redirect
from .forms import QuestionnaireForm
from .models import UserResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def questionnaire(request):
    if request.method == 'POST':
        # Validation pattern to only accept letters
        pattern = re.compile("^[A-Za-z ]+$")
        
        # Retrieve data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        staff_name = request.POST.get('staff_name')
        
        # Validate first name, last name, and staff name
        if not (pattern.match(first_name) and pattern.match(last_name) and pattern.match(staff_name)):
            # Return to the form with an error message if validation fails
            form = QuestionnaireForm(request.POST)
            error_message = 'Names must only contain letters and spaces.'
            return render(request, 'survey/questionnaire_form.html', {'form': form, 'error_message': error_message})
        
        # If validation passes, proceed with creating UserResponse
        user_response = UserResponse(
            first_name=first_name,
            last_name=last_name,
            date=request.POST.get('date'),
            staff_name=staff_name,
            sex=request.POST.get('sex'),
            doh_employee=request.POST.get('doh_employee'),
            team_acronym=request.POST.get('team_acronym'),
            bureau_service_region_acronym=request.POST.get('bureau_service_region_acronym'),
            activity_name=request.POST.get('activity_name'),
            expectation=request.POST.get('expectation'),
            statement1_rating=request.POST.get('statement1'),
            statement2_rating=request.POST.get('statement2'),
            statement3_rating=request.POST.get('statement3'),
            statement4_rating=request.POST.get('statement4'),
            statement5_rating=request.POST.get('statement5'),
            statement6_rating=request.POST.get('statement6'),
            quality=request.POST.get('quality'),
            comments=request.POST.get('comments'),
            # Add more fields as needed
        )
        # Save the UserResponse instance to the database
        user_response.save()
        
        # Optionally, perform additional tasks such as sending email notifications
        
        return redirect('confirmation')  # Redirect to a confirmation page upon successful form submission
    else:
        form = QuestionnaireForm()
    
    statement_fields = [field for field in form if field.name.startswith('statement')]
    
    return render(request, 'survey/questionnaire_form.html', {'form': form, 'statement_fields': statement_fields})

def confirmation(request):
    return render(request, 'survey/confirmation.html')

def landingpage(request):
    return render(request, 'survey/landing_page.html')

@login_required(login_url='/admin/login/')
def dashboard(request):
    # return render(request, 'survey/dashboard.html')
    if request.user.is_staff:
        return render(request, 'survey/dashboard.html')
    else:
        # Return a '403 Forbidden' response if the user is not an admin
        return HttpResponseForbidden("You are not authorized to view this page.")

