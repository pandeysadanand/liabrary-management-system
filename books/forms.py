from django import forms

from .models import Book


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            attributes = {
                "placeholder": f"Books {str(field)}",
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(attributes)
