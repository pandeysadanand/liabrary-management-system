from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            placeholder_list = field.split("_")
            placeholder = " ".join(placeholder_list)
            attributes = {
                "placeholder": placeholder,
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(attributes)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            attributes = {
                "placeholder": f"{str(field)}",
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(attributes)
