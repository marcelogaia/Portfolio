from django.shortcuts import render_to_response
from django.template import RequestContext
from dal import autocomplete
from models import Skill,Language

def index(request):
    return render_to_response('underconstruction.html',RequestContext(request))

class LanguageAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Language.objects.none()

        qs = Language.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
    
class SkillAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Skill.objects.none()

        qs = Skill.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs