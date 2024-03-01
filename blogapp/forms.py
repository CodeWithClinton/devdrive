from django import forms
from .models import Blog, Category, Comment


class CreateBlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter title"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Enter body"}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder":"Add image"}))
    # category = forms.CharField(widget=forms.TextInput(attrs={"class": "form-select", "placeholder":"Enter title"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-select", "placeholder": "Select category"}))
    class Meta:
        model=Blog 
        fields = ["title", "body", "thumbnail", "category"]
        

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows":3, "placeholder": "Say something about the article"}))
    class Meta:
        model=Comment
        fields = ['body']