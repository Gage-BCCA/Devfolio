from django import forms
from .models import Portfolio, Project, Skill, Bio, Link


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['layout', 'color_theme']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'blurb', 'programming_language', 'project_link']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'experience_level']


class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['name', 'bio', 'location']
        def __init__(self, *args, **kwargs): #should make all fields required
            super(BioForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.required = True


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['link_type', 'url']       

