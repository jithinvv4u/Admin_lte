from unittest import result
from django.http import JsonResponse
from django.shortcuts import render
from .models import ffz_inventory_log, ffz_orders, ffz_packed, ffz_store,ffz_audit_log_details, ffz_category, ffz_veg_inventory, ffz_veg_price, ffz_vegitables,Notify,ffz_wallet_trans
from django.db.models import Count,Max,Sum
from django.db.models import F
from itertools import chain
from operator import attrgetter

def notify_report_view(request):
    notify_report=Notify.objects.values(
        'veg_id',
        'veg_id__veg_name',
        'delivery_date',
        'store_id__store_name',
        ).annotate(
            count=Count('veg_id')
            )
    return render(request, 'reports/notify-me-report.html',{'notify_report':notify_report})

def getfilterNotify(request):
    if request.method=='POST':
        min=request.POST.get('min') 
        max=request.POST.get('max')
        notify_report=Notify.objects.filter(
            delivery_date__gt=min,
            delivery_date__lt=max,
            ).values(
                'veg_id','veg_id__veg_name',
                'delivery_date',
                'store_id__store_name'
                ).annotate(
                    count=Count('veg_id')
                    )
        return JsonResponse({'notify_report':list(notify_report)})

def veg_price_view(request):
    # inventory_vegs =ffz_veg_inventory.objects.filter(
    #     veg_inventory_store_id__store_name='Coimbatore'
    #     ).values(
    #         'veg_inventory_veg_id__veg_id',
    #         'veg_inventory_veg_id__veg_name',
    #         'veg_inventory_veg_id__veg_min_qty',
    #         'veg_inventory_veg_id__veg_basic_rate',
    #         )
    vegs =ffz_veg_price.objects.filter(
        veg_price_store_id__store_name='Coimbatore'
        ).values(
            'veg_price_veg_id',
            'veg_price_veg_id__veg_name',
            'veg_price_veg_id__veg_min_qty',
            'veg_price_basic_rate',
            )
    categories=ffz_category.objects.values('name')
    stores=ffz_store.objects.values('store_name')
    return render(request, 'reports/vegitable-price-report.html', {'vegitables': vegs,'categories':categories,'stores':stores})

def getfilterVeg(request):
    if request.method=='POST':
        store=request.POST.get('store')
        category=request.POST.get('category')
        date=request.POST.get('date')
        if category=='All':
            filtered_vegData=ffz_veg_price.objects.filter(
                veg_price_store_id__store_name=store,
                veg_price_modify_date__contains=date,
                ).values(
                    'veg_price_veg_id',
                    'veg_price_veg_id__veg_name',
                    'veg_price_veg_id__veg_min_qty',
                    'veg_price_basic_rate',
                    )
        else:
            filtered_vegData=ffz_veg_price.objects.filter(
                veg_price_store_id__store_name=store,
                veg_price_veg_id__veg_type__name=category,
                ).values(
                    'veg_price_veg_id',
                    'veg_price_veg_id__veg_name',
                    'veg_price_veg_id__veg_min_qty',
                    'veg_price_basic_rate',
                    )
        return JsonResponse({'filtered_vegData':list(filtered_vegData)})

def wallet_transaction_view(request):
    credit=ffz_wallet_trans.objects.filter(
        wallet_trans_status=1
        ).aggregate(
            credit=Max('wallet_trans_amount')
            )
    debit=ffz_wallet_trans.objects.filter(
        wallet_trans_status=2
        ).aggregate(
            debit=Max('wallet_trans_amount')
            )
    return render(request, 'reports/wallet-transaction-report.html')

def getfilterWallet(request):
    if request.method=='POST':
        min=request.POST.get('min')
        max=request.POST.get('max')
        filter_date=ffz_wallet_trans.objects.filter(
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
        credit=ffz_wallet_trans.objects.filter(
            wallet_trans_status=1,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max,
            ).aggregate(credit=Sum('wallet_trans_amount'))
        debit=ffz_wallet_trans.objects.filter(
            wallet_trans_status=2,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max,
            ).aggregate(debit=Sum('wallet_trans_amount'))
        refund=ffz_wallet_trans.objects.filter(
            wallet_trans_status=3,
            wallet_trans_time__gt=min,
            wallet_trans_time__lt=max
            ).aggregate(refund=Sum('wallet_trans_amount'))
        if refund['refund']==None:
            refund['refund']=0
        total=credit['credit']+debit['debit']+refund['refund']
        return JsonResponse({'filter_date':list(filter_date),'credit':credit,'debit':debit,'refund':refund,'total':total})

def stock_in_hand_view(request):
    stores=ffz_store.objects.values('store_name')
    vegs=ffz_vegitables.objects.values('veg_name')
    data=ffz_veg_inventory.objects.filter(
        veg_inventory_store_id__store_name='Coimbatore',
        ).values(
            'veg_inventory_id',
            'veg_inventory_veg_id',
            'veg_inventory_veg_id__veg_name',
            'veg_inventory_stock_in_hand',
            'veg_inventory_veg_id__veg_basic_rate',
            'veg_inventory_veg_id__veg_measurement',
            ).annotate(
                stock_total=F('veg_inventory_stock_in_hand') * F('veg_inventory_veg_id__veg_basic_rate')
                )
    audit=ffz_audit_log_details.objects.values('audit_log_detail_veg_id','audit_log_detail_qty')
    inventory_added=ffz_inventory_log.objects.values('inventory_veg_id','inventory_veg_qty')
    order_not_yet_packed=ffz_orders.objects.filter(
        order_order_status_id=2,
        ).values(
            'order_veg_id',
            'order_placed_id'
            )
    stock_packed=ffz_packed.objects.values('packed_order_id','packed_order_qty')
    
    # result=audit | inventory_added
    # result = list(chain(audit, inventory_added))
    
    # result = audit.union(inventory_added.select_related("foreignModel"))
    # result = sorted(chain(audit, data),key=attrgetter('audit_log_detail_veg_id'))
    
    print(data)

    return render(request,'reports/stock-in-hand-report.html',{'data':data,'stores':stores,'vegs':vegs})

def getfilterStock(request):
    if request.method=='POST':
        store=request.POST.get('store')
        vegitable=request.POST.get('vegitable')
        if vegitable=='All':
            data=ffz_veg_inventory.objects.filter(
                veg_inventory_store_id__store_name=store
                ).values(
                    'veg_inventory_id',
                    'veg_inventory_veg_id',
                    'veg_inventory_veg_id__veg_name',
                    'veg_inventory_stock_in_hand',
                    'veg_inventory_veg_id__veg_basic_rate',
                    'veg_inventory_veg_id__veg_measurement'
                    ).annotate(
                        stock_total=F('veg_inventory_stock_in_hand') * F('veg_inventory_veg_id__veg_basic_rate')
                        )
        else:
            data=ffz_veg_inventory.objects.filter(
                veg_inventory_store_id__store_name=store,
                veg_inventory_veg_id__veg_name=vegitable
                ).values(
                    'veg_inventory_id',
                    'veg_inventory_veg_id',
                    'veg_inventory_veg_id__veg_name',
                    'veg_inventory_stock_in_hand',
                    'veg_inventory_veg_id__veg_basic_rate',
                    'veg_inventory_veg_id__veg_measurement'
                    ).annotate(
                        stock_total=F('veg_inventory_stock_in_hand') * F('veg_inventory_veg_id__veg_basic_rate')
                        )
        return JsonResponse({'data':list(data)})