from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row
from django import forms

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'slug')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Например, IPhone 13'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.disable_csrf = True
            self.helper.layout = Layout(
                'title',
            )


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image', )
        widgets = {
            'image': forms.ClearableFileInput(
                attrs={'multiple': False},
            ),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.disable_csrf = True
            self.helper.layout = Layout(
                Row(
                    'image', css_class="form-group col-md-10 mb-0",
                )
            )


ProductImageFormSet = forms.models.inlineformset_factory(
    parent_model=Product,
    model=ProductImage,
    form=ProductImageForm,
    can_delete=False,
    error_messages={'image': {'Обязательное поле': 'Пожалуйста, предоставьте изображение.'}},
    extra=4,
    min_num=1,
    max_num=5,
    validate_min=True,
    validate_max=True,
)
