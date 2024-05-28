from django import forms
from .models import Item, Outlet, Prediction

class ItemForm(forms.ModelForm):
    """
    Capturar un item
    """
    class Meta:
        model = Item
        fields = ['item_id', 'weight', 'fat_content', 'visibility', 'item_type', 'mrp']

class OutletForm(forms.ModelForm):
    """
    Capturar un outlet
    """
    class Meta:
        model = Outlet
        fields = ['outlet_id', 'establishment_year', 'size', 'location_type', 'outlet_type']

class SaleForm(forms.ModelForm):
    """
    Capturar una venta
    """
    class Meta:
        model = Sale
        fields = ['item', 'outlet', 'sale_amount']

class PredictionForm(forms.ModelForm):
    """
    Capturar una prediccion
    """
    class Meta:
        model = Prediction
        fields = ['item_mrp', 'outlet_id', 'outlet_size', 'outlet_type', 'outlet_establishment_year']