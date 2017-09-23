from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title','second_title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'second_title':forms.TextInput(attrs={'class':'second_title_class'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
