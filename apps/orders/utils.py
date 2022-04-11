from .models import Order, PlacedOrders, Packed
from apps.products.models import Products
from .constants import store_id_name_map, order_type
from django.db.models import Sum


def get_zero_billed_data(str_date):
    store_id_list = [1,6,15]
    data = {}
    for store_id in store_id_list:
        placed_orders = PlacedOrders.objects.filter(
            placed_order_delivery_date=str_date,
            placed_order_order_status_id=3,
            placed_order_store_id= store_id
            )
        zero_billed_dict = {}
        nos = 0
        no = 0
        for each_placed_order in placed_orders:
            order = Order.objects.filter(order_placed_id=each_placed_order.placed_order_id)
            for each_order in order:
                packed = Packed.objects.get(packed_order_id=each_order.order_id)
                if packed.packed_order_qty == '0':
                    nos+=1
                    if each_order.order_veg_id in zero_billed_dict:
                        zero_billed_dict[each_order.order_veg_id]['missed_out']+=float(each_order.order_veg_qty)
                        zero_billed_dict[each_order.order_veg_id]['order_id_list'].append(each_order.order_placed_id)
                        zero_billed_dict[each_order.order_veg_id]['count']+=1
                    else:
                        no += 1
                        veg_name = Products.objects.get(veg_id=each_order.order_veg_id).veg_name
                        zero_billed_dict.update({each_order.order_veg_id:{'veg_name':veg_name,'no':no,'missed_out':float(each_order.order_veg_qty), 'order_id_list':[each_order.order_placed_id],'count':1}})
                    zero_billed_dict[each_order.order_veg_id]['missed_out'] = round(zero_billed_dict[each_order.order_veg_id]['missed_out'],1)

        zero_billed_count = len(zero_billed_dict)
        data.update({store_id:
        {'store_name':store_id_name_map.get(store_id),
        'zero_billed_count':zero_billed_count,
        'nos':nos,
        'zero_billed_dict':zero_billed_dict}
        })

    return data

def total_order_store_wise(str_date,store_id_list):
    store_id_list = store_id_list
    temp = {}
    for store_id in store_id_list:
        total_orders = PlacedOrders.objects.filter(
            placed_order_delivery_date=str_date,
            placed_order_store_id= store_id,
            )
        orders = total_orders.count()
        order_amt = total_orders.values('placed_order_price').aggregate(Sum('placed_order_price')).get('placed_order_price__sum',0) or 0
        avg=0
        if orders>0 and order_amt>0:
            order_amt = float(order_amt)
            avg = round(order_amt/orders,2)

        temp.update({store_id:{'store_name':store_id_name_map.get(store_id),'orders':orders,'order_amt':order_amt,'avg':avg}})
    
    return temp


def get_total_orders_atv_data(str_date):
    store_id_list = [1,6,15]
    data = {}
    for key, val in order_type.items():
        temp = {}
        for store_id in store_id_list:
            placed_orders = PlacedOrders.objects.filter(
                placed_order_type_id=key,
                placed_order_delivery_date=str_date,
                placed_order_store_id= store_id,
                )
            orders = placed_orders.count()
            order_amt = placed_orders.values('placed_order_price').aggregate(Sum('placed_order_price')).get('placed_order_price__sum',0) or 0
            avg = 0
            if orders>0 and order_amt>0:
                order_amt = float(order_amt)
                avg = round(order_amt/orders,2)

            temp.update({store_id:{'store_name':store_id_name_map.get(store_id),'orders':orders,'order_amt':order_amt,'avg':avg}})
        data.update({val:temp})

    total = total_order_store_wise(str_date,store_id_list)
    data.update({'Total':total})

    return data

