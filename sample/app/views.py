from django.shortcuts import render


def home(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')