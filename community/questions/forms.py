'''
问题表单一共需要两个字段,问题名和问题描述文本.

它们都应该是CharFiled,也就是字符型的字段.其中max_length指定了最大长度,
label指定了显示在模板中的名称,widget可以修改字段在网页中的属性,help_text是在输入框中显示帮助信息.
'''

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        label=_('Title'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=2000,
        label=_('Description'),
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        help_text=_('Write the question\'s description...')
    )

    class Meta:
        model = Question
        fields = ['title', 'description']


class AnswerForm(forms.ModelForm):
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'})
    )

    class Meta:
        model = Answer
        fields = ['description']