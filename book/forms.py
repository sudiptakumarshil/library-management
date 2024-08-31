from django import forms
from .constants import RATING
from .models import BookReview


class BookReviewForm(forms.ModelForm):
    comment = forms.Textarea()
    rating = forms.ChoiceField(choices=RATING)

    class Meta:
        model = BookReview
        fields = [
            "comment",
            "rating",
        ]

    def __init__(self, *args, **kwargs):
        super(BookReviewForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
