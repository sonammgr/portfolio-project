from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Fixed: added max_length here
    technologies = models.CharField(max_length=200) 
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOCIES = [ 
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('design', 'Design'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOCIES)

    def __str__(self):
        return self.name 
    
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)    
    content = models.TextField() 
    excerpt = models.TextField(max_length=300)
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True) 
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"