from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages  
from .models import Skill, Project, Blogpost
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.filter(is_featured=True).order_by('-created_date')[:3]
    skills = Skill.objects.all()
    return render(request, 'core/home.html', {
        'projects': featured_projects,
        'skills': skills
    })

def projects(request):
    query = request.GET.get('q')
    if query:
        project_list = Project.objects.filter(
            Q(title__icontains=query) | Q(technologies__icontains=query)
        ).order_by('-id')
    else:
        project_list = Project.objects.all().order_by('-id')

    paginator = Paginator(project_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/project_list.html', {
        'projects': page_obj, 
        'query': query
    })

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'core/project_detail.html', {'project': project})

def blog(request):
    posts = Blogpost.objects.all().order_by('-created_at')
    return render(request, 'core/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    return render(request, 'core/blog_detail.html', {'post': post})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'MESSAGE RECEIVED. I WILL GET BACK TO YOU SOON.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
