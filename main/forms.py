from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm) :
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "brand", "numeric_size", "alphabetic_size", "quantity", "is_featured"]