from django.contrib import admin
from .models import ContactMessage, Project, Skill, Blogpost
# Register your models here.


admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Blogpost)
admin.site.register(ContactMessage)