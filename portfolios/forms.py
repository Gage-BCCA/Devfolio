from django import forms
from .models import Portfolio, Project, Skill, Bio, Link


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        
class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = '__all__'
        def __init__(self, *args, **kwargs): #should make all fields required
            super(BioForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.required = True


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'        

