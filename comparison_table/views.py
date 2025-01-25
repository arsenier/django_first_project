from django.shortcuts import render

from .models import Feedback
from .forms import FeedbackForm

# Create your views here.

# def greet_and_compare(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def advanced_page(request):
    # Handle POST requests
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()

    # Context data to render
    context = {
        'form': form,
        'feedbacks': Feedback.objects.all(),
        'page_title': 'Advanced Page',
        'example_data': {
            'list': ['a', 'b', 'c'],
            'table_data': [
                {'Feature': 'Target', 'Django': 'Web Applications', 'PyQT5': 'Desktop Applications'},
                {'Feature': 'Ease of Use', 'Django': 'High', 'PyQT5': 'Moderate'},
                {'Feature': 'Target Audience', 'Django': 'Networked Users', 'PyQT5': 'Local Users'},
                {'Feature': 'Real-Time Capabilities', 'Django': 'Networked Users', 'PyQT5': 'High'},
                {'Feature': 'UI Complexity', 'Django': 'Moderate', 'PyQT5': 'High'},
            ]
        }
    }
    return render(request, 'advanced_page.html', context)

def greet_and_compare(request):
    comparison_data = [
        {'Feature': 'Target', 'Django': 'Web Applications', 'PyQT5': 'Desktop Applications'},
        {'Feature': 'Ease of Use', 'Django': 'High', 'PyQT5': 'Moderate'},
        {'Feature': 'Target Audience', 'Django': 'Networked Users', 'PyQT5': 'Local Users'},
        {'Feature': 'Real-Time Capabilities', 'Django': 'Networked Users', 'PyQT5': 'High'},
        {'Feature': 'UI Complexity', 'Django': 'Moderate', 'PyQT5': 'High'},
    ]
    return render(request, 'page.html', {'comparison_data': comparison_data})