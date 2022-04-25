from django.shortcuts import render
from .models import DrinkPriceInformation


def price_table(request):
    price_list = DrinkPriceInformation.objects.order_by('-confirmation_date')

    context = {
        'price_list': price_list,
    }

    return render(request, 'market_price/price_table.html', context)
