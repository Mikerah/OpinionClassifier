from django import forms

class ArticleForm(forms.Form):
    article_url = forms.CharField(max_length=250, required=True)