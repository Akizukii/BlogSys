from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=40)
    text = forms.Textarea()
