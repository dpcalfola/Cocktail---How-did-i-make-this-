from django.shortcuts import render, redirect
from django.utils import timezone
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


def insert_price_info(request):
    """

    :param request:
    :return:
    """

    if request.method == 'POST':
        form = LiqueurPriceInformation()

        # Input data from form
        form.category_1 = request.POST.get('input_category_1')
        form.category_2 = request.POST.get('input_category_2')
        form.name = request.POST.get('input_liqueur_name')
        form.lineup = request.POST.get('input_lineup')
        form.price = request.POST.get('input_price')
        form.size = request.POST.get('input_size')
        form.purchasing_route = request.POST.get('input_purchasing_route')
        form.confirmation_date = request.POST.get('input_confirmation_date')
        form.note = request.POST.get('input_note')
        form.recoded_date = timezone.now()

        # This code is the way to avoid Value Error:
        # Django tries to insert ''(null string) to Integer field in DB
        # But I don't know why Django doesn't translate null string to None
        form.aged = request.POST.get('input_aged') if request.POST.get('input_aged') else None

        form.save()

        return redirect('market_price:price_table')
