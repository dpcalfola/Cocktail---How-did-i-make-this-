from django.shortcuts import render, redirect
from django.utils import timezone
from .models import LiqueurPriceInformation
from .forms import CreateLiqueurPriceForm


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
    if request.method == "POST":
        price_form = CreateLiqueurPriceForm(request.POST)
        if price_form.is_valid():
            new_price = price_form.save(commit=False)
            # 여기에서 생성할 객체의 작성자 계정 정보를 입력할 예정
            new_price.save()
            return redirect('market_price:price_table')

    # 여기서 else 구문이 필요한 이유가 이해되지 않음
    # POST method form 의 summit 이 아니면 본 함수가 실행되는 경우의 수가 없는 것 같은데 왜 예제코드에서는 모두 GET 방식의 호출이 있을 것이라 생각하는지?
    # 답: else 구문이 없으면 context에 price_form 을 담을 수 없다.
    else:
        price_form = CreateLiqueurPriceForm()

    # Get Price info
    price_list = LiqueurPriceInformation.objects.exclude(note='더미데이터').order_by('-confirmation_date')
    price_list_dummy = LiqueurPriceInformation.objects.filter(note='더미데이터').order_by('-confirmation_date')

    context = {
        'price_list': price_list,
        'price_list_dummy': price_list_dummy,
        'form': price_form,

        # Collapse 를 기본으로 열려있게 하기 위한 context
        'collapse_show': 'show',
        'aria_expanded_true': 'true',
    }

    return render(request, 'market_price/price_table.html', context)