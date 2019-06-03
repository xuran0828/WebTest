from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text']
        labels={'text':''}
class EntryForm(forms.ModelForm):
    class Meta:#根据Entry模型创建表单
        model=Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}
        #widgets是一个html表单元素，如单，多行文本，下拉框


