# from django.shortcuts import render, redirect
# from django.views import View
# from .forms import UserRegisterForm

# class RegisterView(View):
# 	def get(self, request):
# 		form = UserRegisterForm()
# 		return render(request, 'users/register.html', {'form': form})

# 	def post(self, request):
# 		form = UserRegisterForm(request.POST)

# 		if form.is_valid():
# 		    form.save()
# 		    return redirect('questionnaire')

from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to 'questionnaire' or another success URL
            return redirect('questionnaire')
        else:
            # If the form is not valid, render the page again with form errors
            return render(request, 'users/register.html', {'form': form})




