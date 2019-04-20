from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        # modelに何を使うのかを伝える
        model = Post
        # フォームのフィールドに何を置くのかを指定
        fields = ('title', 'text',)
