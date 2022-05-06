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


# class Great_List_Form(ModelForm):
#     class Meta:
#         model = Character
#         fields = [
#             'attrib_strength',
#             'attrib_agility',
#             'attrib_charisma',
#             'attrib_endurance',
#             'attrib_intelligence',
#             'attrib_wisdom',
#             'name',
#             'background',
#             'diety',
#             'origin',
#             'worldview',
#             'xp',
#             'chr_class',
#             'armour_class',
#             'hp',
#             'speed',
#             'is_dying',
#             'mortal_wounds',
#         ]
#         widgets = {
#             'armour_class': NumberInput(attrs={
#                 'placeholder' : '_',
#             }),
#             'hp': NumberInput(attrs={
#                 'placeholder' : '_',
#             }),
#             'speed': NumberInput(attrs={
#                 'placeholder' : '_',
#             }),
#             'is_dying': NumberInput(attrs={
#                 'placeholder' : '_',
#             }),
#             'mortal_wounds': NumberInput(attrs={
#                 'placeholder' : '_',
#                 'style' : 'margin-left: 1rem;',
#             }),
#             'name': TextInput(attrs={
#                 'placeholder' : '________',
#             }),
#             'background': TextInput(attrs={
#                 'placeholder' : '________',
#                 'style' : 'margin-top: 5px;',
#             }),
#             'diety': TextInput(attrs={
#                 'placeholder' : '________',
#                 'style' : 'margin-top: 5px;',
#             }),
#             'origin': TextInput(attrs={
#                 'placeholder' : '________',
#                 'style' : 'margin-top: 5px;',
#             }),
#             'worldview': TextInput(attrs={
#                 'placeholder' : '________',
#                 'style' : 'margin-top: 5px;',
#             }),
#             'xp': NumberInput(attrs={
#                 'placeholder' : '___',
#             }),
#             'chr_class': TextInput(attrs={
#                 'placeholder' : '________',
#             }),
#             'attrib_strength': NumberInput(attrs={
#                 'id' : 'STR',
#                 'placeholder' : '__',
#             }),
#             'attrib_agility': NumberInput(attrs={
#                 'id' : 'DX',
#                 'placeholder' : '__',
#             }),
#             'attrib_charisma': NumberInput(attrs={
#                 'id' : 'CHR',
#                 'placeholder' : '__',
#             }),
#             'attrib_endurance': NumberInput(attrs={
#                 'id' : 'CON',
#                 'placeholder' : '__',
#             }),
#             'attrib_intelligence': NumberInput(attrs={
#                 'id' : 'IN',
#                 'placeholder' : '__',
#             }),
#             'attrib_wisdom': NumberInput(attrs={
#                 'id' : 'WIS',
#                 'placeholder' : '__',
#             }),
#         }

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