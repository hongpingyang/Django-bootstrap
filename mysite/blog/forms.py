from django import forms
from .models import Comment
from django.forms import widgets as Fwidgets

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        labels = {
            'name': '姓名',
            'body': '评论',
        }
        help_texts = {
            'name': '用户名',
            'body': '文明社会,理性评论',
        }
        widgets = {
            'name': Fwidgets.TextInput(attrs={'class': 'form-control','placeholder':'请输入名称'}),
            'body': Fwidgets.Textarea(attrs={'class': 'form-control','rows':'3','placeholder':'文明社会,理性评论'}),
        }
        error_messages = {
            'name':{
                'required': '姓名不能为空'
            },
            'body':{
                'required': '评论不能为空'
            }
        }

    #def __init__(self,*args,**kwargs):
    #	super(CommentForm,self).__init__(*args,**kwargs)
    #	for field_name in self.base_fields:
    #		field=self.base_fields[field_name]
    #		field.widget.attrs.update({'class':"form-control"})