from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        exclude = ('room_status',)


class UserDetailsForms(forms.ModelForm):
    class Meta:
        model = UserDetails
        exclude = ('cheak_in_time','room_number','status',)



class EmapyForm(forms.ModelForm):
    class Meta:
        model = Emplyee
        exclude = ('join_date','status',)


class EmaplyeCategoryForm(forms.ModelForm):
    class Meta:
        model = EmplyeeCategory
        fields = '__all__'