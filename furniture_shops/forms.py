from django import forms 
from.models import Furniture

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ["name",  "description",  "price",  "discount",  "category",  "material",  "color",  "dimensions",  "weight",  "stock_count",  "image",  "is_available"]

