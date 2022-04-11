from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import get_zero_billed_data, get_total_orders_atv_data


@login_required(login_url="/login/")
def zero_billed(request):
    if request.GET:
        date=request.GET.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
        str_date = date.strftime('%d-%m-%Y')
    else:
        str_date = datetime.today().strftime('%d-%m-%Y')
    orders = get_zero_billed_data(str_date)
    context = {'orders':orders}
    return render(request, 'dashboard/zero_billed.html', context)


@login_required(login_url="/login/")
def total_orders_atv(request):
    if request.GET:
        date=request.GET.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
        str_date = date.strftime('%d-%m-%Y')
    else:
        str_date = datetime.today().strftime('%d-%m-%Y')
    orders = get_total_orders_atv_data(str_date)
    context = {'orders':orders}
    return render(request, 'dashboard/total_orders_atv.html', context)
 