from django import forms
from .models import LiqueurPriceInformation


class CreateLiqueurPriceForm(forms.ModelForm):
    class Meta:
        model = LiqueurPriceInformation

        fields = [
            'category_1',
            'category_2',
            'liqueur_name',
            'lineup',
            'aged',
            'price',
            'size',
            'purchasing_route',
            'confirmation_date',
            'note'
        ]

        # labels = {
        #              'category_1': '대분류',
        #              'category_2': '소분류',
        #              'name' : ,
        #          'lineup',
        #          'aged',
        #          'price',
        #          'size',
        #          'purchasing_route',
        #          'confirmation_date',
        #          'note',
        # }
