from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import get_user_referral_data


@login_required(login_url="/login/")
def user_referrals(request):
    referrer_user_id = None
    start_date = None
    end_date = None
    store_id = None
    if request.GET:
        referrer_user_id=request.GET.get('referrer_user_id')
        start_date=request.GET.get('start_date')
        end_date=request.GET.get('end_date')
        store_id=request.GET.get('store_id')
    referral_data = get_user_referral_data(referrer_user_id, start_date, end_date, store_id)
    context = {'referral_data':referral_data}
    return render(request, 'user/user_referrals.html', context)
