from django import forms
from .models import Question, Answer, Attempts


class ChooseInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ChooseInlineFormset, self).clean()

        right_answer = 0
        for form in self.forms:
            if not form.is_valid():
                return

            if form.cleaned_data and form.cleaned_data.get('rightAnswer') is True:
                right_answer += 1

        try:
            assert right_answer == Question.ALLOWED_ANSWERS
        except AssertionError:
            raise forms.ValidationError("Only one answer is allowed")
