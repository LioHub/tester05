

from test_module.models import Answers, Results
from django import forms


class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answers
		fields = ('answer',)


class ResultFrom(forms.ModelForm):
	class Meta:
		model = Results
		fields = ('user', 'test_id', 'number_of_correct_answers')