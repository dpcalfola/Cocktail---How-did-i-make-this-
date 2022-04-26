from django.shortcuts import render
from .models import LiqueurPriceInformation


def price_table(request):
    # price_list = DrinkPriceInformation.objects.order_by('-confirmation_date')
    price_list = LiqueurPriceInformation.objects.exclude(note='더미데이터').order_by('-confirmation_date')
    price_list_dummy = LiqueurPriceInformation.objects.filter(note='더미데이터').order_by('-confirmation_date')

    context = {
        'price_list': price_list,
        'price_list_dummy': price_list_dummy,

    }

    return render(request, 'market_price/price_table.html', context)
