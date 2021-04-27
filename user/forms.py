from django import forms
from user.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'nickname',
            'phone_number',
            'gender',
            'birthday',
            'student_id',
            'school',
            'date_joined',
            'is_active',
            'is_superuser',
        )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user