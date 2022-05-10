from pyexpat import model
from tkinter.ttk import Widget
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ModelForm, Textarea, Select, Form
from .models import Character
from .models import Avatar_of_choice
from django.forms import NumberInput, TextInput

class psw_ch(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(psw_ch, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None

class name_desc_form(ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'desc',
        ]

        widgets = {
            'name': Textarea(attrs={
                'id' : 'name_field',
                'class' : 'line_area',
            }),

            'desc': Textarea(attrs={
                'id' : 'desc_field',
                'class' : 'big_area',
            }),
        }


class main_aspects_form(ModelForm):
    class Meta:
        model = Character
        fields = [
            'high_concept',
            'trouble',
        ]

        widgets = {
            'high_concept': Textarea(attrs={
                'id' : 'high_concept_field',
                'class' : 'line_area',
            }),

            'trouble': Textarea(attrs={
                'id' : 'trouble_field',
                'class' : 'line_area',
            }),
        }

class fate_points_form(ModelForm):
    class Meta:
        model = Character
        fields = [
            'fate_point_number',
            'fate_point_refresh',
        ]

        widgets = {
            'fate_point_number': NumberInput(attrs={
                'id' : 'fate_point_number_field',
                'class' : 'number_input',
            }),

            'fate_point_refresh': NumberInput(attrs={
                'id' : 'fate_point_refresh_field',
                'class' : 'number_input',
            }),
        }

class Image_Upload_Form(ModelForm):
    class Meta:
        model = Character
        fields = [
            'portrait',
        ]

class Image_Upload_Form_ava_edition(ModelForm):
    class Meta:
        model = Avatar_of_choice
        fields = [
            'portrait',
        ]