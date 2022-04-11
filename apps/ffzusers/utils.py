from datetime import datetime
import pytz

from .models import User
from apps.offers.models import UserReferral
from apps.orders.models import PlacedOrders

tz = pytz.timezone("Asia/Calcutta")

def get_user_referral_data(referrer_user_id, start_date, end_date, store_id):
    user_referrals = UserReferral.objects.all()
    if referrer_user_id:
        user_referrals = user_referrals.filter(user_referral_id=referrer_user_id)
    
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        start_date = start_date.replace(tzinfo=tz)
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        end_date = end_date.replace(tzinfo=tz)
        user_referrals = user_referrals.filter(referral_date__gte=start_date, referral_date__lte=end_date)

    total_referrals_count = 0
    successful_referrals_count = 0
    referrer_total_cashback = 0

    res = [[{'total_referrals_count': total_referrals_count, 'successful_referrals_count': successful_referrals_count, 'referrer_total_cashback':0}]]

    data_list = []

    for item in user_referrals:
        temp = {}
        referrer_user_id = item.user_referral_id
        refferer_user = User.objects.filter(user_id=referrer_user_id).first()
        if not refferer_user:
            continue
        refferer_user_name = refferer_user.user_name

        referee_user_id = item.user_id
        referee_user = User.objects.filter(user_id=referee_user_id).first()
        if not referee_user:
            continue
        referee_user_name = referee_user.user_name

        placed_order = PlacedOrders.objects.filter(placed_order_id=item.order_id).first()
        purchase_amount = None
        if placed_order:
            purchase_amount = placed_order.placed_order_price

        if store_id:
            if refferer_user.user_store_id == int(store_id):
                if item.active_refferal == '1':
                    successful_referrals_count += 1
                total_referrals_count += 1
            else:
                continue
        else:
            if item.active_refferal == '1':
                successful_referrals_count += 1
            total_referrals_count += 1

        if item.active_refferal == '1':
            referrer_total_cashback += round(float(item.referral_cashback_parent), 2) if item.referral_cashback_parent else 0
            temp.update({
                'referrer_user_id': referrer_user_id,
                'refferer_user_name': refferer_user_name,
                'referee_user_id': referee_user_id,
                'referee_user_name': referee_user_name,
                'purchase_amount': round(float(purchase_amount), 2) if purchase_amount else None,
                'refferer_cashback': round(float(item.referral_cashback_parent), 2) if item.referral_cashback_parent else None,
                'referee_cashback': round(float(item.referal_cashback_child), 2) if item.referal_cashback_child else None
            })

            data_list.append(temp)

    res.append(data_list)
    res[0][0]['total_referrals_count'] = total_referrals_count
    res[0][0]['successful_referrals_count'] = successful_referrals_count
    res[0][0]['referrer_total_cashback'] = referrer_total_cashback

    return res
        
