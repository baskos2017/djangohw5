from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_email', 'description', 'rating', 'is_positive', 'phone_number', 'image']
        labels = {
            'user_email': 'Email',
            'description': 'Опис',
            'rating': 'Рейтинг',
            'is_positive': 'Positive Review',
            'phone_number': 'Номер телефону',
            'image': 'Image',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.Select(),
            'is_positive': forms.RadioSelect(choices=[(True, 'Positive'), (False, 'Negative')]),
        }
