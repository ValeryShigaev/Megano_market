from django import forms
from goods_app.models import ProductComment
from django.utils.translation import gettext_lazy as _


class RatingField(forms.IntegerField):
    default_error_messages = {'required': _('You must to choose rating star for adding the review'), }


class ReviewForm(forms.ModelForm):
    rating = RatingField(required=True)

    class Meta:
        model = ProductComment
        fields = ['product', 'user', 'author', 'content', 'rating']
        exclude = ['added', ]
