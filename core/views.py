from django.shortcuts import render, get_object_or_404
from .models import Skill,Project,Blogpost

def home (request):
    featured_projects = Project.objects.filter(is_featured=True).order_by('-created_at')[:3]
    skills=Skill.objects.all()
    return render (request, 'core/home.html',{
        'projects': featured_projects,
        'skills': skills})

def projects (request):
    query= request.GET.get('q')
    if query:
        all_projects= Project.objects.filter(title__icontains=query)| Project.objects.filter(technologies__icontains=query)
    else:
        all_projects=Project.objects.all()
    return render(request, 'core/project_list.html', {'projects': all_projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'core/project_detail.html', {'project': project})

def blog(request):
    posts = Blogpost.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'core/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    return render(request, 'core/blog_detail.html', {'post': post})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
