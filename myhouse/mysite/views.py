from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from .models import FullProfile
# from .forms import ProfileForm
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'mysite/index.html')

# python manage.py migrate
# python manage.py collectstatic
# python manage.py makemigrations
# python manage.py migrate