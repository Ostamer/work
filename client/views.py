from django.shortcuts import render
from client.models import Client
from service.models import Service
from project.models import Project
from media.models import Image, VideoReview
from settings.models import Settings
from employee.models import Employee

def homepage(request):
    clients = Client.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    images = Image.objects.all()
    video_reviews = VideoReview.objects.all()
    settings = Settings.objects.all()
    employees = Employee.objects.all()

    return render(request, 'home.html', {
        'clients': clients,
        'services': services,
        'projects': projects,
        'images': images,
        'video_reviews': video_reviews,
        'settings': settings,
        'employees': employees
    })

def assessment(request):
    clients = Client.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    images = Image.objects.all()
    video_reviews = VideoReview.objects.all()
    settings = Settings.objects.all()
    employees = Employee.objects.all()

    return render(request, 'assessment.html', {
        'clients': clients,
        'services': services,
        'projects': projects,
        'images': images,
        'video_reviews': video_reviews,
        'settings': settings,
        'employees': employees
    })

def design(request):
    clients = Client.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    images = Image.objects.all()
    video_reviews = VideoReview.objects.all()
    settings = Settings.objects.all()
    employees = Employee.objects.all()

    return render(request, 'design.html', {
        'clients': clients,
        'services': services,
        'projects': projects,
        'images': images,
        'video_reviews': video_reviews,
        'settings': settings,
        'employees': employees
    })

def build(request):
    clients = Client.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    images = Image.objects.all()
    video_reviews = VideoReview.objects.all()
    settings = Settings.objects.all()
    employees = Employee.objects.all()

    return render(request, 'build.html', {
        'clients': clients,
        'services': services,
        'projects': projects,
        'images': images,
        'video_reviews': video_reviews,
        'settings': settings,
        'employees': employees
    })

def projects(request):
    clients = Client.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    images = Image.objects.all()
    video_reviews = VideoReview.objects.all()
    settings = Settings.objects.all()
    employees = Employee.objects.all()

    return render(request, 'projects.html', {
        'clients': clients,
        'services': services,
        'projects': projects,
        'images': images,
        'video_reviews': video_reviews,
        'settings': settings,
        'employees': employees
    })

from django.http import JsonResponse
from .forms import ClientForm

def ajax_submit_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базе
            return JsonResponse({'success': True, 'message': 'Заявка успешно отправлена!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'message': 'Недопустимый запрос'}, status=400)
