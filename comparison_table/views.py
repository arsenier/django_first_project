from django.shortcuts import render

# Create your views here.

# def greet_and_compare(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def greet_and_compare(request):
    comparison_data = [
        {'Feature': 'Target', 'Django': 'Web Applications', 'PyQT5': 'Desktop Applications'},
        {'Feature': 'Ease of Use', 'Django': 'High', 'PyQT5': 'Moderate'},
        {'Feature': 'Target Audience', 'Django': 'Networked Users', 'PyQT5': 'Local Users'},
        {'Feature': 'Real-Time Capabilities', 'Django': 'Networked Users', 'PyQT5': 'High'},
        {'Feature': 'UI Complexity', 'Django': 'Moderate', 'PyQT5': 'High'},
    ]
    return render(request, 'page.html', {'comparison_data': comparison_data})