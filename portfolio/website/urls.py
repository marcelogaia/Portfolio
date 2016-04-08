from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views
from . import staticserve

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from portfolio import settings
from dal import autocomplete

if settings.DEBUG == True:
    urlpatterns = staticfiles_urlpatterns()

urlpatterns = [
    url( r'^$', views.index),
    url( r'^summernote/', include('django_summernote.urls')),
    url( r'^skills-autocomplete/$', views.SkillAutocomplete.as_view(create_field='name'), name='skills-autocomplete',),
    url( r'^languages-autocomplete/$', views.LanguageAutocomplete.as_view(), name='languages-autocomplete',),
    url( r'(.*.png)', staticserve.serve),
    url( r'(.*.css)', staticserve.serve),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)