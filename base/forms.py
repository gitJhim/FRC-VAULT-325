from django import forms

from .models import GameScout

class GameScoutForm(forms.ModelForm):

    class Meta:
        model = GameScout
        fields = ('team', 'startingPosition', 'a_upperScore', 'a_lowerScore', 'a_cargoAquired', 't_upperScore', 't_lowerScore', 't_cargoAquired')

        widgets = {
            'team': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'startingPosition': forms.Select(attrs={ 'class': 'form-control' }),
            'a_upperScore': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'a_lowerScore': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'a_cargoAquired': forms.NumberInput(attrs={ 'class': 'form-control' }),
            't_upperScore': forms.NumberInput(attrs={ 'class': 'form-control' }),
            't_lowerScore': forms.NumberInput(attrs={ 'class': 'form-control' }),
            't_cargoAquired': forms.NumberInput(attrs={ 'class': 'form-control' }),
        }