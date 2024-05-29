from django import forms
from .models import Item, Outlet, Sale, Prediction

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_id', 'weight', 'fat_content', 'visibility', 'item_type', 'mrp']
        widgets = {
            'item_id': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'fat_content': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'visibility': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_type': forms.TextInput(attrs={'class': 'form-control'}),
            'mrp': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields = ['outlet_id', 'establishment_year', 'size', 'location_type', 'outlet_type']
        widgets = {
            'outlet_size': forms.RadioSelect,
            'outlet_type': forms.RadioSelect,
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['item', 'outlet', 'sale_amount']

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['item_mrp', 'outlet_ID', 'outlet_size', 'outlet_type', 'outlet_establishment_year']