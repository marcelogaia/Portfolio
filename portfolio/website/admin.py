from models import Education, Experience, Management, Project, Project_image, Reference, Resume, User
from forms import ResumeForm
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name']
admin.site.register(User,UserAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title']
admin.site.register(Project,ProjectAdmin)

class ResumeAdmin(SummernoteModelAdmin):
    form = ResumeForm
    #list_display = ['title',]
    #search_fields = ['title']
admin.site.register(Resume,ResumeAdmin)

'''
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('get_resume','get_user')

    def get_resume(self, obj):
        return obj.resume.title
    def get_user(self, obj):
        return obj.user.name
    
    get_user.short_description = 'User'
    get_user.admin_order_field = 'user__name'
    
    get_resume.short_description = 'Resume'
    get_resume.admin_order_field = 'resume__title'
    
    search_fields = ('get_resume','get_user')
    
admin.site.register(Reference,ReferenceAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title']
admin.site.register(Education,EducationAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title']
admin.site.register(Experience,ExperienceAdmin)

class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['comment',]
    search_fields = ['comment']
admin.site.register(Project_image,ProjectImageAdmin)
class ManagementAdmin(SummernoteModelAdmin):
    list_display = ['title',]
    search_fields = ['title']
admin.site.register(Management,ManagementAdmin)
'''
