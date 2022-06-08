import re
from django.http import JsonResponse
from django.shortcuts import render
from .models import ffz_inventory_log, ffz_main_city, ffz_orders, ffz_packed, ffz_placed_orders, ffz_razor_payment_history, ffz_store, ffz_audit_log_details, ffz_category, ffz_transaction_before, ffz_user_referral, ffz_users, ffz_veg_inventory, ffz_veg_price, ffz_vegitables, Notify, ffz_wallet_trans, ffz_wallet_trans_history
from django.db.models import Count, Max, Sum
from django.db.models import F
from django.db.models import Q
from django.utils.dateparse import parse_date
import datetime


def notify_report_view(request):
    notify_report = Notify.objects.values(
        'veg_id',
        'veg_id__veg_name',
        'delivery_date',
        'store_id__store_name',
    ).annotate(
        count=Count('veg_id')
    )
    return render(request,
                  'reports/notify-me-report.html',
                  {'notify_report': notify_report}
                  )


def getfilterNotify(request):
    if request.method == 'POST':
        min = request.POST.get('min')
        max = request.POST.get('max')
        notify_report = Notify.objects.filter(
            delivery_date__gt=min,
            delivery_date__lt=max,
        ).values(
            'veg_id', 'veg_id__veg_name',
            'delivery_date',
            'store_id__store_name'
        ).annotate(
            count=Count('veg_id')
        )
        return JsonResponse({'notify_report': list(notify_report)})


def veg_price_view(request):
    # inventory_vegs =ffz_veg_inventory.objects.filter(
    #     veg_inventory_store_id__store_name='Coimbatore'
    #     ).values(
    #         'veg_inventory_veg_id__veg_id',
    #         'veg_inventory_veg_id__veg_name',
    #         'veg_inventory_veg_id__veg_min_qty',
    #         'veg_inventory_veg_id__veg_basic_rate',
    #         )
    vegs = ffz_veg_price.objects.filter(
        veg_price_store_id__store_name='Kakkanad'
    ).values(
        'veg_price_veg_id',
        'veg_price_veg_id__veg_name',
        'veg_price_veg_id__veg_min_qty',
        'veg_price_basic_rate',
    )
    categories = ffz_category.objects.values('name')
    stores = ffz_store.objects.values('store_name')
    return render(
        request,
        'reports/vegitable-price-report.html',
        {
            'vegitables': vegs,
            'categories': categories,
            'stores': stores,
        }
    )


def getfilterVeg(request):
    if request.method == 'POST':
        store = request.POST.get('store')
        category = request.POST.get('category')
        date = request.POST.get('date')
        print(store)
        if category == 'All':
            filtered_vegData = ffz_veg_price.objects.filter(
                veg_price_store_id__store_name=store,
                veg_price_modify_date__contains=date,
            ).values(
                'veg_price_veg_id',
                'veg_price_veg_id__veg_name',
                'veg_price_veg_id__veg_min_qty',
                'veg_price_basic_rate',
            )
        else:
            filtered_vegData = ffz_veg_price.objects.filter(
                veg_price_store_id__store_name=store,
                veg_price_veg_id__veg_type__name=category,
                veg_price_modify_date__contains=date,
            ).values(
                'veg_price_veg_id',
                'veg_price_veg_id__veg_name',
                'veg_price_veg_id__veg_min_qty',
                'veg_price_basic_rate',
            )
        print(filtered_vegData)
        return JsonResponse({'filtered_vegData': list(filtered_vegData)})


def wallet_transaction_view(request):
    if request.method == 'GET':
        max = datetime.date.today()
        min=max - datetime.timedelta(30)
        walletData= ffz_wallet_trans.objects.filter(
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max
        ).values(
            'wallet_trans_id',
            'wallet_trans_user_id__user_name',
            'wallet_trans_time',
            'wallet_trans_placed_order_id',
            'wallet_trans_message',
            'wallet_trans_status',
            'wallet_trans_amount',
        )
        
        credit = ffz_wallet_trans.objects.filter(
            wallet_trans_status=1,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max,
        ).aggregate(credit=Sum('wallet_trans_amount'))
        debit = ffz_wallet_trans.objects.filter(
            wallet_trans_status=2,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max,
        ).aggregate(debit=Sum('wallet_trans_amount'))
        refund = ffz_wallet_trans.objects.filter(
            wallet_trans_status=3,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max
        ).aggregate(refund=Sum('wallet_trans_amount'))
        if refund['refund'] == None:
            refund['refund'] = 0
        total = credit['credit']+debit['debit']+refund['refund']

        return render(
            request,
            'reports/wallet-transaction-report.html',
            {
                'walletData': list(walletData),
                'credit': credit,
                'debit': debit,
                'refund': refund,
                'total': total,
            }
        )


def getfilterWallet(request):
    if request.method == 'POST':
        min = request.POST.get('min')
        max = request.POST.get('max')
        filter_date = ffz_wallet_trans.objects.filter(
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max
        ).values(
            'wallet_trans_id',
            'wallet_trans_user_id__user_name',
            'wallet_trans_time',
            'wallet_trans_placed_order_id',
            'wallet_trans_message',
            'wallet_trans_status',
            'wallet_trans_amount',
        )
        credit = ffz_wallet_trans.objects.filter(
            wallet_trans_status=1,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max,
        ).aggregate(credit=Sum('wallet_trans_amount'))
        debit = ffz_wallet_trans.objects.filter(
            wallet_trans_status=2,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max,
        ).aggregate(debit=Sum('wallet_trans_amount'))
        refund = ffz_wallet_trans.objects.filter(
            wallet_trans_status=3,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max
        ).aggregate(refund=Sum('wallet_trans_amount'))
        if refund['refund'] == None:
            refund['refund'] = 0
        total = credit['credit']+debit['debit']+refund['refund']
        return JsonResponse(
            {
                'filter_date': list(filter_date),
                'credit': credit,
                'debit': debit,
                'refund': refund,
                'total': total,
            }
        )


def stock_in_hand_view(request):
    stores = ffz_store.objects.values('store_name')
    vegs = ffz_vegitables.objects.values('veg_name')
    stock_data = ffz_veg_inventory.objects.filter(
        veg_inventory_store_id__store_name='Coimbatore',
        veg_inventory_veg_id__veg_name='Tapioca',
    ).values(
        'veg_inventory_id',
        'veg_inventory_veg_id',
        'veg_inventory_veg_id__veg_name',
        'veg_inventory_stock_in_hand',
        'veg_inventory_veg_id__veg_basic_rate',
        'veg_inventory_veg_id__veg_measurement',
    ).annotate(
        stock_total=F('veg_inventory_stock_in_hand') *
        F('veg_inventory_veg_id__veg_basic_rate')
    )

    inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
    audit_log_details = ffz_audit_log_details.objects.filter(
        audit_log_detail_veg_id__in=inventory_veg_ids).values(
            'audit_log_detail_veg_id',
            'audit_log_detail_qty')
    for data in stock_data:
        audit_log_qty = list(filter(
            lambda auditqty: auditqty['audit_log_detail_veg_id'] == data['veg_inventory_veg_id'], audit_log_details))
        if audit_log_qty:
            data.update(
                {'audit_log_detail_qty': audit_log_qty[0]['audit_log_detail_qty']})

    inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
    inventory_log_details = ffz_inventory_log.objects.filter(
        inventory_veg_id__in=inventory_veg_ids).values(
            'inventory_veg_id',
            'inventory_veg_qty')
    for data in stock_data:
        inv_veg_qty = list(filter(
            lambda veginvqty: veginvqty['inventory_veg_id'] == data['veg_inventory_veg_id'], inventory_log_details))
        if inv_veg_qty:
            data.update(
                {'inventory_veg_qty': inv_veg_qty[0]['inventory_veg_qty']})

    inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
    orders_details = ffz_orders.objects.filter(
        order_veg_id__in=inventory_veg_ids).values(
            'order_veg_id',
            'order_placed_id')
    for data in stock_data:
        orderplaced_id = list(filter(
            lambda orderid: orderid['order_veg_id'] == data['veg_inventory_veg_id'], orders_details))
        if orderplaced_id:
            data.update(
                {'order_placed_id': orderplaced_id[0]['order_placed_id']})

    inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
    inventory_log_details = ffz_inventory_log.objects.filter(
        inventory_veg_id__in=inventory_veg_ids,
        inventory_log_type=2,
        ).annotate(
            wastage_report=F('inventory_veg_qty') * F('inventory_price')
            ).values('wastage_report','inventory_veg_id')
    for data in stock_data:
        inv_veg_qty = list(filter(
            lambda wastagedata: wastagedata['inventory_veg_id'] == data['veg_inventory_veg_id'], inventory_log_details))
        if inv_veg_qty:
            data.update(
                {'wastage': inv_veg_qty[0]['wastage_report']})

    inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
    inventory_log_details = ffz_inventory_log.objects.filter(
        inventory_veg_id__in=inventory_veg_ids,
        inventory_log_type=3,
        ).annotate(stock_sent=Sum('inventory_veg_qty')).values('stock_sent','inventory_veg_id')
    for data in stock_data:
        inv_veg_qty = list(filter(
            lambda stockdata: stockdata['inventory_veg_id'] == data['veg_inventory_veg_id'], inventory_log_details))
        if inv_veg_qty:
            data.update(
                {'stock_sent': inv_veg_qty[0]['stock_sent']})

    inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
    order_details = ffz_orders.objects.filter(
        order_veg_id__in=inventory_veg_ids,
        ).values('order_id','order_veg_id')
    for data in stock_data:
        inv_veg_qty = list(filter(
            lambda stockpack: stockpack['order_veg_id'] == data['veg_inventory_veg_id'], order_details))
        if inv_veg_qty:
            data.update(
                {'order_id': inv_veg_qty[0]['order_id']})
    order_details=[data['order_id'] for data in order_details]
    packed_details=ffz_packed.objects.filter(
        packed_order_id__in=order_details
        ).values(
            'packed_order_qty',
            'packed_order_id'
            )
    for data in stock_data:
        inv_veg_qty = list(filter(
            lambda stockpack: stockpack['packed_order_id'] == data['order_id'], packed_details))
        if inv_veg_qty:
            data.update(
                {'packed_order_qty': inv_veg_qty[0]['packed_order_qty']})
            
    return render(
        request,
        'reports/stock-in-hand-report.html',
        {
            'data': stock_data,
            'stores': stores,
            'vegs': vegs,
        }
    )


def getfilterStock(request):
    if request.method == 'POST':
        store = request.POST.get('store')
        vegitable = request.POST.get('vegitable')
        stock_filters={}
        if vegitable == 'All':
            stock_filters={
                'veg_inventory_store_id__store_name':store,
            }
        else:
            stock_filters.update({
                'veg_inventory_store_id__store_name':store,
                'veg_inventory_veg_id__veg_name':vegitable,
            })
            
        stock_data = ffz_veg_inventory.objects.filter(Q(**stock_filters)).values(
            'veg_inventory_id',
            'veg_inventory_veg_id',
            'veg_inventory_veg_id__veg_name',
            'veg_inventory_stock_in_hand',
            'veg_inventory_veg_id__veg_basic_rate',
            'veg_inventory_veg_id__veg_measurement'
            ).annotate(
            stock_total=F('veg_inventory_stock_in_hand') *F('veg_inventory_veg_id__veg_basic_rate')
        )


        inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
        audit_log_details = ffz_audit_log_details.objects.filter(
            audit_log_detail_veg_id__in=inventory_veg_ids).values(
                'audit_log_detail_veg_id',
                'audit_log_detail_qty')
        for data in stock_data:
            audit_log_qty = list(filter(
                lambda auditqty: auditqty['audit_log_detail_veg_id'] == data['veg_inventory_veg_id'], audit_log_details))
            if audit_log_qty:
                data.update(
                    {'audit_log_detail_qty': audit_log_qty[0]['audit_log_detail_qty']})

        inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
        inventory_log_details = ffz_inventory_log.objects.filter(
            inventory_veg_id__in=inventory_veg_ids).values(
                'inventory_veg_id',
                'inventory_veg_qty')
        for data in stock_data:
            inv_veg_qty = list(filter(
                lambda veginvqty: veginvqty['inventory_veg_id'] == data['veg_inventory_veg_id'], inventory_log_details))
            if inv_veg_qty:
                data.update(
                    {'inventory_veg_qty': inv_veg_qty[0]['inventory_veg_qty']})

        inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
        orders_details = ffz_orders.objects.filter(
            order_veg_id__in=inventory_veg_ids).values(
                'order_veg_id',
                'order_placed_id')
        for data in stock_data:
            orderplaced_id = list(filter(
                lambda orderid: orderid['order_veg_id'] == data['veg_inventory_veg_id'], orders_details))
            if orderplaced_id:
                data.update(
                    {'order_placed_id': orderplaced_id[0]['order_placed_id']})

        inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
        inventory_log_details = ffz_inventory_log.objects.filter(
            inventory_veg_id__in=inventory_veg_ids,
            inventory_log_type=2,
            ).annotate(
                wastage_report=F('inventory_veg_qty') * F('inventory_price')
                ).values('wastage_report','inventory_veg_id')
        for data in stock_data:
            inv_veg_qty = list(filter(
                lambda wastagedata: wastagedata['inventory_veg_id'] == data['veg_inventory_veg_id'], inventory_log_details))
            if inv_veg_qty:
                data.update(
                    {'wastage': inv_veg_qty[0]['wastage_report']})

        inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
        inventory_log_details = ffz_inventory_log.objects.filter(
            inventory_veg_id__in=inventory_veg_ids,
            inventory_log_type=3,
            ).annotate(stock_sent=Sum('inventory_veg_qty')).values('stock_sent','inventory_veg_id')
        for data in stock_data:
            inv_veg_qty = list(filter(
                lambda stockdata: stockdata['inventory_veg_id'] == data['veg_inventory_veg_id'], inventory_log_details))
            if inv_veg_qty:
                data.update(
                    {'stock_sent': inv_veg_qty[0]['stock_sent']})

        inventory_veg_ids = [data['veg_inventory_veg_id'] for data in stock_data]
        order_details = ffz_orders.objects.filter(
            order_veg_id__in=inventory_veg_ids,
            ).values('order_id','order_veg_id')
        for data in stock_data:
            inv_veg_qty = list(filter(
                lambda stockpack: stockpack['order_veg_id'] == data['veg_inventory_veg_id'], order_details))
            if inv_veg_qty:
                data.update(
                    {'order_id': inv_veg_qty[0]['order_id']})
        order_details=[data['order_id'] for data in order_details]
        packed_details=ffz_packed.objects.filter(
            packed_order_id__in=order_details
            ).values(
                'packed_order_qty',
                'packed_order_id'
                )
        for data in stock_data:
            inv_veg_qty = list(filter(
                lambda stockpack: stockpack['packed_order_id'] == data['order_id'], packed_details))
            if inv_veg_qty:
                data.update(
                    {'packed_order_qty': inv_veg_qty[0]['packed_order_qty']})


        return JsonResponse({'data': list(stock_data)})


def user_referral_report(request):
    max=datetime.date.today()
    min= max - datetime.timedelta(30)
    referral_data = ffz_user_referral.objects.filter(
        referral_date__lt=max,
        referral_date__gt=min,
        ).values(
            'id',
            'user_id__user_name',
            'user_referral_id__user_name',
            'referral_date',
            'order_id__order_date',
            'active_refferal'
        )
    return render(request,
                  'reports/referral.html',
                  {'referral_data': referral_data}
                  )


def getfilterReferrals(request):
    if request.method == 'POST':
        min = request.POST.get('min')
        max = request.POST.get('max')
        print(min)
        print(max)
        referral_data = ffz_user_referral.objects.filter(
            referral_date__lt=max,
            referral_date__gt=min,
            ).values(
                'id',
                'user_id__user_name',
                'user_referral_id__user_name',
                'referral_date',
                'order_id__order_date',
                'active_refferal'
            )
        print(referral_data)
        return JsonResponse({'referral_data': list(referral_data)})


def order_wallet_trans(request):
    max=datetime.date.today()
    min=max - datetime.timedelta(30)
    order_wallet_data = ffz_wallet_trans.objects.filter(
        wallet_trans_placed_order_id__placed_order_date__gt=min,
        wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).values(
            'wallet_trans_id',
            'wallet_trans_user_id',
            'wallet_trans_user_id__user_email',
            'wallet_trans_placed_order_id',
            'wallet_trans_placed_order_id__placed_order_date',
            'wallet_trans_time',
            'wallet_trans_id__reson',
            'wallet_trans_message',
            'wallet_trans_status',
            'wallet_trans_amount'
        )
    person_data = ffz_wallet_trans.objects.filter(
        wallet_trans_user_id=126120,
        wallet_trans_placed_order_id__placed_order_date__gt=min,
        wallet_trans_placed_order_id__placed_order_date__lt=max,
    ).values(
        'wallet_trans_user_id__user_email'
    ).annotate(
        transactions=Count('wallet_trans_user_id'),
        amount=Sum('wallet_trans_amount')
    )

    others = ffz_wallet_trans.objects.filter(
        wallet_trans_placed_order_id__placed_order_date__gt=min,
        wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).exclude(
        wallet_trans_user_id=126120
    ).aggregate(
        other_transactions=Count('wallet_trans_user_id'),
        other_amount=Sum('wallet_trans_amount')
    )
    other_transactions = others['other_transactions']
    other_amount = others['other_amount']

    credit = ffz_wallet_trans.objects.filter(
        wallet_trans_placed_order_id__placed_order_date__gt=min,
        wallet_trans_placed_order_id__placed_order_date__lt=max,
        wallet_trans_status=1,
    ).aggregate(
        credit=Sum('wallet_trans_amount')
    )
    debit = ffz_wallet_trans.objects.filter(
        wallet_trans_status=2,
        wallet_trans_placed_order_id__placed_order_date__gt=min,
        wallet_trans_placed_order_id__placed_order_date__lt=max,
    ).aggregate(
        debit=Sum('wallet_trans_amount')
    )
    refund = ffz_wallet_trans.objects.filter(
        wallet_trans_placed_order_id__placed_order_date__gt=min,
        wallet_trans_placed_order_id__placed_order_date__lt=max,
        wallet_trans_status=3,
    ).aggregate(
        refund=Sum('wallet_trans_amount')
    )
    if refund['refund'] == None:
        refund['refund'] = 0
    total = credit['credit']+debit['debit']+refund['refund']

    all_data = {}
    all_data['person_email'] = person_data[0]['wallet_trans_user_id__user_email']
    all_data['person_transactions'] = person_data[0]['transactions']
    all_data['person_amount'] = person_data[0]['amount']
    all_data['other_transactions'] = other_transactions
    all_data['other_amount'] = other_amount
    all_data['credit'] = credit['credit']
    all_data['debit'] = debit['debit']
    all_data['refund'] = refund['refund']
    all_data['total'] = total

    return render(request,
                  'reports/order_wallet_trans.html',
                  {
                      'order_wallet_data': order_wallet_data,
                      'all_data': all_data,
                  }
                  )


def getPiechartWallet(request):
    if request.method == 'GET':
        billing_error = ffz_wallet_trans_history.objects.filter(
            reson='billing_error').aggregate(billing_error_count=Count('wallet_trans_id'))
        god_will = ffz_wallet_trans_history.objects.filter(
            reson='God_Will').aggregate(god_will_count=Count('wallet_trans_id'))
        system = ffz_wallet_trans_history.objects.filter().exclude(
            reson='billing_error').aggregate(system_count=Count('wallet_trans_id'))
        
        return JsonResponse(
            {
                'billing_error': billing_error,
                'god_will': god_will,
                'system': system,
            }
        )


def getfilterOrderWallet(request):
    if request.method == 'POST':
        min = request.POST.get('min')
        max = request.POST.get('max')
        order_wallet_data = ffz_wallet_trans.objects.filter(
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).values(
            'wallet_trans_id',
            'wallet_trans_user_id',
            'wallet_trans_user_id__user_email',
            'wallet_trans_placed_order_id',
            'wallet_trans_placed_order_id__placed_order_date',
            'wallet_trans_time',
            'wallet_trans_id__reson',
            'wallet_trans_message',
            'wallet_trans_status',
            'wallet_trans_amount'
        )

        credit = ffz_wallet_trans.objects.filter(
            wallet_trans_status=1,
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).aggregate(
            credit=Sum('wallet_trans_amount'),
        )
        debit = ffz_wallet_trans.objects.filter(
            wallet_trans_status=2,
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).aggregate(
            debit=Sum('wallet_trans_amount')
        )
        refund = ffz_wallet_trans.objects.filter(
            wallet_trans_status=3,
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).aggregate(
            refund=Sum('wallet_trans_amount')
        )
        if credit['credit'] == None:
            credit['credit'] = 0
        if debit['debit'] == None:
            debit['debit'] = 0
        if refund['refund'] == None:
            refund['refund'] = 0
        total = credit['credit']+debit['debit']+refund['refund']

        person_data = ffz_wallet_trans.objects.filter(
            wallet_trans_user_id=126120,
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).values(
            'wallet_trans_user_id__user_email',
        ).annotate(
            transactions=Count('wallet_trans_user_id'),
            amount=Sum('wallet_trans_amount')
        )

        others = ffz_wallet_trans.objects.filter(
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
        ).exclude(
            wallet_trans_user_id=126120,
        ).aggregate(
            other_transactions=Count('wallet_trans_user_id'),
            other_amount=Sum('wallet_trans_amount')
        )
        billing_error=ffz_wallet_trans.objects.filter(
            wallet_trans_id__reson='billing_error',
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
            ).aggregate(
                billing_error_count=Count('wallet_trans_id')
                )
        god_will=ffz_wallet_trans.objects.filter(
            wallet_trans_id__reson='God_Will',
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
            ).aggregate(
                god_will_count=Count('wallet_trans_id')
                )
        
        system=ffz_wallet_trans.objects.filter(
            wallet_trans_placed_order_id__placed_order_date__gt=min,
            wallet_trans_placed_order_id__placed_order_date__lt=max,
            ).exclude(
                wallet_trans_id__reson='billing_error',
                ).aggregate(
                    system_count=Count('wallet_trans_id')
                    )
                
        all_data = {}
        all_data['person_email'] = [data['wallet_trans_user_id__user_email']
                                    for data in person_data]
        all_data['person_transactions'] = [data['transactions']
                                           for data in person_data]
        all_data['person_amount'] = [data['amount'] for data in person_data]
        all_data['other_transactions'] = others['other_transactions']
        all_data['other_amount'] = others['other_amount']
        all_data['credit'] = credit['credit']
        all_data['debit'] = debit['debit']
        all_data['refund'] = refund['refund']
        all_data['total'] = total
        return JsonResponse({
            'order_wallet_data': list(order_wallet_data),
            'all_data': all_data,
            'billing_error':billing_error,
            'god_will':god_will,
            'system':system,
        }
        )




def settlement_report(request):
    if request.method == 'GET':
        settlement_data = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name='Kakkanad',
            placed_order_date__gt='2022-03-08',
            placed_order_date__lt='2022-04-08',
        ).values(
            'placed_order_user_id',
            'placed_order_user_id__user_name',
            'placed_order_id',
            'placed_order_date',
            'placed_order_delivery_date',
            'placed_order_packed_time',
            'placed_order_price',
            'placed_order_shipping_charge',
            'placed_order_gst',
            'placed_order_packed_sum',
            'placed_order_wallet_amount',
            'placed_order_packed_wallet_adjustment',
            'placed_order_payment_status_id__payment_status_name',
            'placed_order_order_status_id',
            'placed_order_type_id',
            'placed_order_txtn_id',
            'placed_order_store_id',
            'placed_order_discount',
            'placed_order_pq_total')
        
        sum_used_credit=0
        sum_used_debit=0
        for data in settlement_data:
            data['wallet_used_credit'], data['wallet_used_debit'] = 0, 0
            if data['placed_order_wallet_amount']==None:
                pass
            elif data['placed_order_wallet_amount']<0:
                data['wallet_used_debit'] = data['placed_order_wallet_amount']
            else:
                data['wallet_used_credit'] = data['placed_order_wallet_amount']
            sum_used_credit+=data['wallet_used_credit']
            sum_used_debit+=data['wallet_used_debit']
            
        sum_adjst_credit=0
        sum_adjst_debit=0
        for data in settlement_data:
            data['wallet_adjst_credit'], data['wallet_adjst_debit'] = 0, 0
            if data['placed_order_packed_wallet_adjustment']==None:
                pass
            elif data['placed_order_packed_wallet_adjustment']<0:
                data['wallet_adjst_debit'] = data['placed_order_packed_wallet_adjustment']
            else:
                data['wallet_adjst_credit'] = data['placed_order_packed_wallet_adjustment']
            sum_adjst_credit+=data['wallet_adjst_credit']
            sum_adjst_debit+=data['wallet_adjst_debit']
            
        sum_by_cash=0
        for data in settlement_data:
            if data['placed_order_payment_status_id__payment_status_name']=='COD':
                if data['placed_order_packed_sum'] and data['placed_order_shipping_charge']:
                    data['by_cash']=data['placed_order_shipping_charge']+data['placed_order_packed_sum'] 
                elif data['placed_order_packed_sum']:
                    data['by_cash']=data['placed_order_packed_sum']
                elif data['placed_order_shipping_charge']:
                    data['by_cash']=data['placed_order_shipping_charge'] 
                else:             
                    data['by_cash']=0
                sum_by_cash+=data['by_cash']
        
        online_credited = 0
        user_ids = [data['placed_order_user_id'] for data in settlement_data]
        transaction_bf_details = ffz_transaction_before.objects.filter(
            bf_user_id__in=user_ids).values(
                'bf_user_id',
                'bf_amount')
        for data in settlement_data:
            amount = list(filter(
                lambda bf_transaction: bf_transaction['bf_user_id'] == data['placed_order_user_id'], transaction_bf_details))
            if amount:
                data.update({'bf_amount': amount[0]['bf_amount']})
                online_credited += int(data['bf_amount'])
                

        placed_ids = [data['placed_order_id'] for data in settlement_data]
        razorpay_details = ffz_razor_payment_history.objects.filter(
            razor_order_placed_id__in=placed_ids).values(
                'razor_order_placed_id',
                'razor_payment_id')
        for data in settlement_data:
            razor_pay_id = list(filter(
                lambda razorpay: razorpay['razor_order_placed_id'] == data['placed_order_id'], razorpay_details))
            if razor_pay_id:
                data.update(
                    {'razor_payment_id': razor_pay_id[0]['razor_payment_id']})

  
        
        
        # user_ids=[data['placed_order_user_id'] for data in settlement_data]
        # walllet_debited_details=ffz_wallet_trans.objects.filter(
        #     wallet_trans_user_id__in=user_ids,wallet_trans_status=1).values(
        #         'wallet_trans_user_id',
        #         'wallet_trans_amount')
        # for data in settlement_data:
        #     debited=list(filter(lambda wallet: wallet['wallet_trans_user_id'] == data['placed_order_user_id'], walllet_debited_details))
        #     if debited:
        #         data.update({'walllet_trans_debited':debited[0]['wallet_trans_amount']})

        # user_ids=[data['placed_order_user_id'] for data in settlement_data]
        # walllet_credited_details=ffz_wallet_trans.objects.filter(
        #     wallet_trans_user_id__in=user_ids,wallet_trans_status=2).values(
        #         'wallet_trans_user_id',
        #         'wallet_trans_amount')
        # for data in settlement_data:
        #     credited=list(filter(lambda wallet: wallet['wallet_trans_user_id'] == data['placed_order_user_id'], walllet_credited_details))
        #     if credited:
        #         data.update({'walllet_trans_credited':credited[0]['wallet_trans_amount']})


        # by_cash=ffz_placed_orders.objects.filter(placed_order_payment_status_id=1).annotate(bycash=F('placed_order_shipping_charge') + F('placed_order_packed_sum')).values_list('bycash')
        # print(by_cash)

        sum_sub_total = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name='Kakkanad',
            placed_order_date__gt='2022-03-08',
            placed_order_date__lt='2022-04-08',).aggregate(sub_total=Sum('placed_order_price'))
        sum_shipping = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name='Kakkanad',
            placed_order_date__gt='2022-03-08',
            placed_order_date__lt='2022-04-08',).aggregate(shipping=Sum('placed_order_shipping_charge'))
        sum_gst = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name='Kakkanad',
            placed_order_date__gt='2022-03-08',
            placed_order_date__lt='2022-04-08',).aggregate(gst_sum=Sum('placed_order_gst'))
        sum_packed = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name='Kakkanad',
            placed_order_date__gt='2022-03-08',
            placed_order_date__lt='2022-04-08',).aggregate(packed_sum=Sum('placed_order_packed_sum'))
        # wallet_used=ffz_placed_orders.objects.filter(
        #     placed_order_store_id__store_name='Kakkanad',
        #     placed_order_date__gt='2022-03-08',
        #     placed_order_date__lt='2022-04-08',).aggregate(wallet_used=Sum('placed_order_wallet_amount'))
        # wallet_adjustment=ffz_placed_orders.objects.filter(
        #     placed_order_store_id__store_name='Kakkanad',
        #     placed_order_date__gt='2022-03-08',
        #     placed_order_date__lt='2022-04-08',).aggregate(wallet_adjustment=Sum('placed_order_packed_wallet_adjustment'))
        sum_discount = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name='Kakkanad',
            placed_order_date__gt='2022-03-08',
            placed_order_date__lt='2022-04-08',).aggregate(discount=Sum('placed_order_discount'))
        sum_pq = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name='Kakkanad',
            placed_order_date__gt='2022-03-08',
            placed_order_date__lt='2022-04-08',).aggregate(placed_order_pq_total=Sum('placed_order_pq_total'))

        sum_data = {}
        sum_data['sub_total'] = sum_sub_total['sub_total']
        sum_data['shipping'] = sum_shipping['shipping']
        sum_data['packed_sum'] = sum_packed['packed_sum']
        sum_data['discount'] = sum_discount['discount']
        sum_data['placed_order_pq_total'] = sum_pq['placed_order_pq_total']
        sum_data['online_credited'] = online_credited
        sum_data['gst'] = sum_gst['gst_sum']
        sum_data['sum_by_Cash']=sum_by_cash
        sum_data['sum_used_credit']=sum_used_credit
        sum_data['sum_used_debit']=sum_used_debit
        sum_data['sum_adjst_credit']=sum_adjst_credit
        sum_data['sum_adjst_debit']=sum_adjst_debit
        
        # delivery_date=ffz_placed_orders.objects.values('placed_order_delivery_date')
        # print(delivery_date)
        
        stores = ffz_store.objects.filter(store_is_mdc=1).values('store_name')

        cities = ffz_main_city.objects.filter(
            main_store_id__store_name='Kakkanad',status=1).values('name')
        
        
        return render(
            request,
            'reports/settlement_report.html',
            {
                'settlement_data': settlement_data,
                'stores': stores,
                'sum_data': sum_data,
                'cities': cities,
            }
        )


def getfilterSettlement(request):
    if request.method == 'POST':
        store = request.POST.get('store')
        city = request.POST.get('city')
        date_filter = request.POST.get('date_filter')
        order_type=request.POST.get('order_type')
        min = request.POST.get('min')
        max = request.POST.get('max')
        
        # date_data=ffz_placed_orders.objects.delivery_date_filter(min,max)
        # print(date_data)
        
        settlement_filters = {
            'placed_order_store_id__store_name': store
        }
        if date_filter == 'Delivery Date':
            # date_list=[]
            # all_delivery_dates=ffz_placed_orders.objects.values('placed_order_delivery_date')
            # print(all_delivery_dates['placed_order_delivery_date'])
            # for date in all_delivery_dates:
            #     to_date=parse_date(date)
            #     date_list.append(to_date)
            # print(date_list)
      
            # date=ffz_placed_orders.objects.filter(placed_order_delivery_date__gt=min,placed_order_delivery_date__lt=max)
            # print(date)
            # settlement_filters.update({
            #     'placed_order_delivery_date__gt': min,
            #     'placed_order_delivery_date__lt': max,
            # })
            
            pass
            
        else:
            print('placed order date')
            settlement_filters.update({
                'placed_order_date__gt': min,
                'placed_order_date__lt': max 
            })
        if order_type=='Cancelled':
            settlement_filters.update({
                'placed_order_order_status_id':4,
            })
        elif order_type=='Active':
            settlement_filters.update({
                'placed_order_order_status_id__lt':4,
            })
        else:
            pass
        if city != 'All':
            print(city)
            settlement_filters.update({'placed_order_city_id__name': city})
            
        settlement_data = ffz_placed_orders.objects.filter(
                    Q(**settlement_filters)
                ).values(
            'placed_order_user_id',
            'placed_order_user_id__user_name',
            'placed_order_id',
            'placed_order_date',
            'placed_order_delivery_date',
            'placed_order_packed_time',
            'placed_order_price',
            'placed_order_shipping_charge',
            'placed_order_gst',
            'placed_order_packed_sum',
            'placed_order_wallet_amount',
            'placed_order_packed_wallet_adjustment',
            'placed_order_payment_status_id__payment_status_name',
            'placed_order_order_status_id',
            'placed_order_type_id',
            'placed_order_txtn_id',
            'placed_order_store_id',
            'placed_order_discount',
            'placed_order_pq_total')
        
        sum_used_credit=0
        sum_used_debit=0
        for data in settlement_data:
            data['wallet_used_credit'], data['wallet_used_debit'] = 0, 0
            if data['placed_order_wallet_amount']==None:
                pass
            elif data['placed_order_wallet_amount']<0:
                data['wallet_used_debit'] = data['placed_order_wallet_amount']
            else:
                data['wallet_used_credit'] = data['placed_order_wallet_amount']
            sum_used_credit+=data['wallet_used_credit']
            sum_used_debit+=data['wallet_used_debit']
            
        sum_adjst_credit=0
        sum_adjst_debit=0
        for data in settlement_data:
            data['wallet_adjst_credit'], data['wallet_adjst_debit'] = 0, 0
            if data['placed_order_packed_wallet_adjustment']==None:
                pass
            elif data['placed_order_packed_wallet_adjustment']<0:
                data['wallet_adjst_debit'] = data['placed_order_packed_wallet_adjustment']
            else:
                data['wallet_adjst_credit'] = data['placed_order_packed_wallet_adjustment']
            sum_adjst_credit+=data['wallet_adjst_credit']
            sum_adjst_debit+=data['wallet_adjst_debit']
            
        sum_by_cash=0
        for data in settlement_data:
            if data['placed_order_payment_status_id__payment_status_name']=='COD':
                if data['placed_order_packed_sum'] and data['placed_order_shipping_charge']:
                    data['by_cash']=data['placed_order_shipping_charge']+data['placed_order_packed_sum'] 
                elif data['placed_order_packed_sum']:
                    data['by_cash']=data['placed_order_packed_sum']
                elif data['placed_order_shipping_charge']:
                    data['by_cash']=data['placed_order_shipping_charge'] 
                else:             
                    data['by_cash']=0
                sum_by_cash+=data['by_cash']
        
        
        placed_ids = [data['placed_order_id'] for data in settlement_data]
        razorpay_details = ffz_razor_payment_history.objects.filter(
            razor_order_placed_id__in=placed_ids).values(
                'razor_order_placed_id',
                'razor_payment_id')
        for data in settlement_data:
            razor_pay_id = list(filter(
                lambda razorpay: razorpay['razor_order_placed_id'] == data['placed_order_id'], razorpay_details))
            if razor_pay_id:
                data.update(
                    {'razor_payment_id': razor_pay_id[0]['razor_payment_id']})

        online_credited = 0
        user_ids = [data['placed_order_user_id'] for data in settlement_data]
        transaction_bf_details = ffz_transaction_before.objects.filter(
            bf_user_id__in=user_ids).values(
                'bf_user_id',
                'bf_amount')
        for data in settlement_data:
            amount = list(filter(
                lambda bf_transaction: bf_transaction['bf_user_id'] == data['placed_order_user_id'], transaction_bf_details))
            if amount:
                data.update({'bf_amount': amount[0]['bf_amount']})
                online_credited += int(data['bf_amount'])


        sum_sub_total = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name=store,
            placed_order_date__gt=min,
            placed_order_date__lt=max,).aggregate(sub_total=Sum('placed_order_price'))
        sum_discount = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name=store,
            placed_order_date__gt=min,
            placed_order_date__lt=max,).aggregate(discount=Sum('placed_order_discount'))
        sum_shipping = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name=store,
            placed_order_date__gt=min,
            placed_order_date__lt=max,).aggregate(shipping=Sum('placed_order_shipping_charge'))
        sum_gst = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name=store,
            placed_order_date__gt=min,
            placed_order_date__lt=max,).aggregate(gst_sum=Sum('placed_order_gst'))
        sum_packed = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name=store,
            placed_order_date__gt=min,
            placed_order_date__lt=max,).aggregate(packed_sum=Sum('placed_order_packed_sum'))
        sum_pq = ffz_placed_orders.objects.filter(
            placed_order_store_id__store_name=store,
            placed_order_date__gt=min,
            placed_order_date__lt=max,).aggregate(placed_order_pq_total=Sum('placed_order_pq_total'))

        sum_data = {}
        sum_data['sub_total'] = sum_sub_total['sub_total']
        sum_data['shipping'] = sum_shipping['shipping']
        sum_data['packed_sum'] = sum_packed['packed_sum']
        sum_data['discount'] = sum_discount['discount']
        sum_data['placed_order_pq_total'] = sum_pq['placed_order_pq_total']
        sum_data['online_credited'] = online_credited
        sum_data['gst'] = sum_gst['gst_sum']
        sum_data['sum_by_Cash']=sum_by_cash
        sum_data['sum_used_credit']=sum_used_credit
        sum_data['sum_used_debit']=sum_used_debit
        sum_data['sum_adjst_credit']=sum_adjst_credit
        sum_data['sum_adjst_debit']=sum_adjst_debit
        
        
        return JsonResponse(
            {
                'settlement_data': list(settlement_data),
                'sum_data': sum_data,
            }
        )

def load_cities(request):
    if request.method == 'POST':
        store_name = request.POST.get('store')
        city_data = ffz_main_city.objects.filter(
            main_store_id__store_name=store_name,status=1).values('name')
    return JsonResponse({'city_data': list(city_data)})



def newUser(request):
    if request.method == 'GET':
        user_data = ffz_users.objects.values(
            'user_id',
            'user_name',
            'user_email',
            'user_phone',
            'user_signup_date',
            'user_registration_type',
            'user_email_verified'
        )
        # stores=ffz_store.objects.filter()
        return render(request, 'reports/new_user.html', {
            'user_data': user_data,
            # 'stores':stores,
        })


def getfilterUser(requset):
    if requset.method == 'POST':
        # store=requset.POST.get('store')
        min = requset.POST.get('min')
        max = requset.POST.get('max')
        user_data = ffz_users.objects.filter(user_signup_date__gt=min, user_signup_date__lt=max).values(
            'user_id',
            'user_name',
            'user_email',
            'user_phone',
            'user_signup_date',
            'user_registration_type',
            'user_email_verified'
        )
        print(min)
        print(max)
        print(user_data)
        return JsonResponse({
            'user_data': list(user_data),
        })
        

def delivery_sales_report(request):
    delivery_sales_data=ffz_placed_orders.objects.filter().values(
        'placed_order_delivery_date',
        'placed_order_delivery_status'
        ).order_by(
            'placed_order_delivery_date'
            ).annotate(
                total_order=Sum('placed_order_delivery_date'),
                order_sum=Sum('placed_order_price'),
                exp_sum=Sum('placed_delivery_express_pref'),
                discount_sum=Sum('placed_order_discount'),
                packed_sum=Sum('placed_order_packed_sum'),
                wallet=Sum('placed_order_wallet_amount'),
                pq_total=Sum('placed_order_pq_total'),
                exp_orders=Sum('placed_delivery_express_pref',filter=~Q(placed_delivery_express_pref=0),),
                shipping_charge=Sum('placed_order_shipping_charge'),
                online=Sum('placed_order_price',filter=Q(placed_order_payment_method=0)),
                offline=Sum('placed_order_price',filter=~Q(placed_order_payment_method=0)),
                )
    # exp_orders=ffz_placed_orders.objects.filter(~Q(placed_delivery_express_pref=0)).values(
    #     'placed_delivery_express_pref',
    #     'placed_order_delivery_date').order_by('placed_order_delivery_date')
    # print(exp_orders)
    return render(
        request,
        'reports/delivery_sale_report.html',
        {'delivery_sales_data':delivery_sales_data}
        )
