from django.forms import ModelForm
from .models import Subject

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['title']

class TaskForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'