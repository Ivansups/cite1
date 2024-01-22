from .models import Articles
from django.forms import ModelForm, TextInput,DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['titl', 'anonse', 'full_txt', 'date_time']

        widgets = {
            'titl': TextInput(attrs={
                'class': 'form-control',
                'placeholeder': 'Название статьи'
            }),
            'anonse': TextInput(attrs={
                'class': 'form-control',
                'placeholeder': 'Анонос статьи'
            }),
            'date_time': DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'full_txt': Textarea(attrs={
                'class': 'form-control',
                'placeholeder': 'Текст статьи'
            })
        }