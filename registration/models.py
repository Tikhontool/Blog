from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class MyPasswordChangeModel(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''
