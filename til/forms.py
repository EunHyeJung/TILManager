from django import forms
from datetime import datetime
from django.forms import ModelForm
from til.models import Til, Review, Plan, Post
from django.forms import inlineformset_factory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  '__all__'


class TilForm(forms.ModelForm):
    class Meta:
        model = Til
        fields = { 'item' }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'item'}


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = {'item'}


TilInlineFormSet = inlineformset_factory(Post, Til,
                                           fields=[ 'item', ], extra=2)

ReviewInlineFormSet = inlineformset_factory(Post, Review,
                                           fields=[ 'item', ], extra=2)

PlanInlineFormSet = inlineformset_factory(Post, Plan,
                                           fields=[ 'item', ], extra=2)