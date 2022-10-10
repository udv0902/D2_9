from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		# fields = '__all__'
		fields = ['title', 'content', 'is_published', 'category']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
			'category': forms.Select(attrs={'class': 'form-control'}),
		}

	# Дополнительный валидатор
	def clean_title(self):
		title = self.cleaned_data['title']
		if re.match(r'\d', title):  # если в начале строки title будет найдена цифра
			raise ValidationError('Название не должно начинаться с цифры')
		return title
