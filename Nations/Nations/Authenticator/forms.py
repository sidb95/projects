from django import forms


class AccessForm(forms.ModelForm):
  act = forms.CharField(label='ACT', required=True, 
                        widget=forms.TextInput(attrs={'class': 'form-control'}))
