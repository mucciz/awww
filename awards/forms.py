from django import forms
from django.contrib.auth.models import User
from .models import Profile, Project, Rating


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('user', )

class ProjectRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['project', 'pub_date', 'user']