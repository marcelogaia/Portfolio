from models import Education, Experience, Management, Project, Project_image, Reference, Resume, User
from forms import ResumeForm
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name']

class ProjectImageAdmin(admin.TabularInline):
    model = Project_image
    extra = 1
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title']
    inlines = [ProjectImageAdmin]

class ExperienceAdmin(admin.StackedInline):
    model = Experience
    extra = 0

class EducationAdmin(admin.StackedInline):
    model = Education
    extra = 0

class ReferenceAdmin(admin.TabularInline):
    model = Reference
    extra = 0

class ResumeAdmin(SummernoteModelAdmin):
    form = ResumeForm
    inlines = [ExperienceAdmin,EducationAdmin,ReferenceAdmin]
    
admin.site.register(Project,ProjectAdmin)
admin.site.register(Resume,ResumeAdmin)
admin.site.register(User,UserAdmin)