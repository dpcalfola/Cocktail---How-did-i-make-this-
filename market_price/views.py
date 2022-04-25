from django.shortcuts import render


def price_table(request):
    return render(request, 'market_price/price_table.html')
