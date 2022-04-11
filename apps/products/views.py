from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import get_product_data


@login_required(login_url="/login/")
def active_products(request):
    if request.GET:
        date=request.GET.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
        day = date.strftime('%a')
    else:
        day = datetime.today().strftime('%a')
    products = get_product_data(day)
    context = {'products':products}
    return render(request, 'dashboard/active_products.html', context)
