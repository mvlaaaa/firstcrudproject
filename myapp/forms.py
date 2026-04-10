from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'photo', 'email', 'password', 'mobile_number', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # This adds Bootstrap styling to your form automatically
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'