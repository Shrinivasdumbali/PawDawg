from django.shortcuts import render, redirect
from .forms import RescueReportForm
from django.contrib import messages

# Home page view
def home(request):
    return render(request, 'PawApp/home.html')  # Renders the home page

# About page view
def about(request):
    return render(request, 'PawApp/about.html')  # Renders the About Us page

# Report rescue view
def report_rescue(request):
    if request.method == 'POST':
        form = RescueReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your rescue report has been submitted successfully.")
            #return redirect('home')  
            return render(request, 'PawApp/submission_received.html')
        '''
        back to home page, instead create a "sent success note for user confirmation" add button saying go back to the home page
        '''
    else:
        form = RescueReportForm()
    return render(request, 'PawApp/report_rescue.html', {'form': form})


# Submission received view
def submission_received(request):
    return render(request, 'PawApp/submission_received.html')  # Renders the confirmation page