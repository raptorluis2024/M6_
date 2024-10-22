from django import forms
from articleManagement.models import Article

class FormularioArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'address', 'price', 'category')