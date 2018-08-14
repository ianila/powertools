from django.forms import ModelForm, NumberInput, TextInput
from tools.models import Tool

class ToolEditForm(ModelForm):

    class Meta:
        model = Tool
        fields = ['serialno', 'make', 'rentalvalue' , 'desc']

        widgets = {
            'serialno': TextInput(attrs={'class': 'w3-input w3-border', 'autofocus': 'True', 'id': 'sn', 'required': True}),
            'make': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'mk', 'required': True}),
            'rentalvalue': NumberInput(attrs={'class': 'w3-input w3-border', 'id': 'rv', 'required': True}),
            'desc': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'dc', 'required': True}),
        }

class ToolNewForm(ModelForm):

    class Meta:
        model = Tool
        fields = ['serialno', 'make', 'rentalvalue' , 'desc']

        widgets = {
            'serialno': TextInput(attrs={'class': 'w3-input w3-border', 'autofocus': 'True', 'id': 'sno', 'required': True}),
            'make': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'mke', 'required': True}),
            'rentalvalue': NumberInput(attrs={'class': 'w3-input w3-border', 'id': 'rva', 'required': True}),
            'desc': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'dec', 'required': True}),
        }

