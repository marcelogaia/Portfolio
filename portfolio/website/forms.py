from dal import autocomplete
from django import forms
from models import Resume, Skill, Language, Experience, Education


class ResumeForm(forms.ModelForm):
    skill = forms.ModelMultipleChoiceField(
		required = False,
        queryset = Skill.objects.all(),
        widget	 = autocomplete.ModelSelect2Multiple(url='skills-autocomplete'),
    )
	
    language = forms.ModelMultipleChoiceField(
		required = False,
        queryset = Language.objects.all(),
        widget	 = autocomplete.ModelSelect2Multiple(url='languages-autocomplete'),
    )
	
    class Meta:
        model = Resume
        fields = ('__all__')