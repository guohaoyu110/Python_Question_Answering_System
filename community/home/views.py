from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render


def home(request):
    """
    homepage
    """
    return render(request, 'home/home.html')
