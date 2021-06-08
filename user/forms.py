from django import forms
from user.models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
