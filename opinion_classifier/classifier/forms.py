from django.forms import Form, CharField

class ArticleForm(Form):
    class Meta:
        article_url = CharField(max_length=100, required=True)