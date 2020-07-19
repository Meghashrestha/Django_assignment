from django.forms import ModelForm
from .models import Blogdetails,Writername

class Form(ModelForm):
    class Meta:
        model = Blogdetails
        fields = ['blog_title','blog']
