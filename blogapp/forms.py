from django import forms
from .models import PostModel,comment
class post_form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'style': 'width: 300px;'}))
    class Meta:
        model=PostModel
        fields=('title','content',)

class comment_form(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Add comment here', 'style': 'width: 600px;'}))
    class Meta:
        model=comment
        fields=('content',)
