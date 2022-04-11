from .models import Products
from apps.inventory.models import Inventory
from .constants import store_id_name_map, category_id_map, day_map


# def get_product_datav2(day):
#     store_id_list = [1,6,15]
#     category_id_list = [0,2,3,4,5]
#     data = {}
#     for cat_id in category_id_list:
#         veg_dict = {}
#         for store_id in store_id_list:
#             temp = {}
#             veg_id_list = list(Products.objects.filter(veg_type=cat_id).values_list('veg_id',flat=True))
#             inv = Inventory.objects.filter(veg_inventory_store_id=store_id,veg_inventory_veg_id__in=veg_id_list)
#             if day == 'Mon':
#                 active_list = inv.filter(veg_status_mon=1)
#                 active = active_list.count()
#                 # upcoming list and sold list
#                 upcoming=0
#                 sold = 0
#                 sold_list = []
#                 upcoming_list = []
#                 for item in active_list:
#                     veg = item.veg_inventory_veg_id
#                     veg_min_qty = float(veg.veg_min_qty)
#                     available_qty = float(item.veg_available_qty_mon) - float(item.veg_sold_qty_mon)
#                     if available_qty==0:
#                         sold+=1
#                         sold_list.append(veg)
#                     check_upcoming  = veg_min_qty*2
#                     if available_qty<check_upcoming:
#                         upcoming+=1
#                         upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':item.veg_available_qty_mon,'sold_qty':item.veg_sold_qty_mon})
                        
            
#             elif day == 'Tue':
#                 active_list = inv.filter(veg_status_tue=1)
#                 active = active_list.count()
#                 # upcoming list and sold list
#                 upcoming=0
#                 sold = 0
#                 sold_list = []
#                 upcoming_list = []
#                 for item in active_list:
#                     veg = item.veg_inventory_veg_id
#                     veg_min_qty = float(veg.veg_min_qty)
#                     available_qty = float(item.veg_available_qty_tue) - float(item.veg_sold_qty_tue)
#                     if available_qty==0:
#                         sold+=1
#                         sold_list.append(veg)
#                     check_upcoming  = veg_min_qty*2
#                     if available_qty<check_upcoming:
#                         upcoming+=1
#                         upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':item.veg_available_qty_tue,'sold_qty':item.veg_sold_qty_tue})
                
            
#             elif day == 'Wed':
#                 active_list = inv.filter(veg_status_wed=1)
#                 active = active_list.count()
#                 # upcoming list and sold list
#                 upcoming=0
#                 sold = 0
#                 sold_list = []
#                 upcoming_list = []
#                 for item in active_list:
#                     veg =item.veg_inventory_veg_id
#                     veg_min_qty = float(veg.veg_min_qty)
#                     available_qty = float(item.veg_available_qty_wed) - float(item.veg_sold_qty_wed)
#                     if available_qty==0:
#                         sold+=1
#                         sold_list.append(veg)
#                     check_upcoming  = veg_min_qty*2
#                     if available_qty<check_upcoming:
#                         upcoming+=1
#                         upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':item.veg_available_qty_wed,'sold_qty':item.veg_sold_qty_wed})
            
#             elif day == 'Thu':
#                 active_list = inv.filter(veg_status_thu=1)
#                 active = active_list.count()
#                 # upcoming list and sold list
#                 upcoming=0
#                 sold = 0
#                 sold_list = []
#                 upcoming_list = []
#                 for item in active_list:
#                     veg = item.veg_inventory_veg_id
#                     veg_min_qty = float(veg.veg_min_qty)
#                     available_qty = float(item.veg_available_qty_thu) - float(item.veg_sold_qty_thu)
#                     if available_qty==0:
#                         sold+=1
#                         sold_list.append(veg)
#                     check_upcoming  = veg_min_qty*2
#                     if available_qty<check_upcoming:
#                         upcoming+=1
#                         upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':item.veg_available_qty_thu,'sold_qty':item.veg_sold_qty_thu})
            
#             elif day == 'Fri':
#                 active_list = inv.filter(veg_status_fri=1)
#                 active = active_list.count()
#                 # upcoming list and sold list
#                 upcoming=0
#                 sold = 0
#                 sold_list = []
#                 upcoming_list = []
#                 for item in active_list:
#                     veg = item.veg_inventory_veg_id
#                     veg_min_qty = float(veg.veg_min_qty)
#                     available_qty = float(item.veg_available_qty_fri) - float(item.veg_sold_qty_fri)
#                     if available_qty==0:
#                         sold+=1
#                         sold_list.append(veg)
#                     check_upcoming  = veg_min_qty*2
#                     if available_qty<check_upcoming:
#                         upcoming+=1
#                         upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':item.veg_available_qty_fri,'sold_qty':item.veg_sold_qty_fri})
            
#             elif day == 'Sat':
#                 active_list = inv.filter(veg_status_sat=1)
#                 active = active_list.count()
#                 # upcoming list and sold list
#                 upcoming=0
#                 sold = 0
#                 sold_list = []
#                 upcoming_list = []
#                 for item in active_list:
#                     veg = item.veg_inventory_veg_id
#                     veg_min_qty = float(veg.veg_min_qty)
#                     available_qty = float(item.veg_available_qty_sat) - float(item.veg_sold_qty_sat)
#                     if available_qty==0:
#                         sold+=1
#                         sold_list.append(veg)
#                     check_upcoming  = veg_min_qty*2
#                     if available_qty<check_upcoming:
#                         upcoming+=1
#                         upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':item.veg_available_qty_sat,'sold_qty':item.veg_sold_qty_sat})

    
#             elif day == 'Sun':
#                 active_list = inv.filter(veg_status_sun=1)
#                 active = active_list.count()
#                 # upcoming list and sold list
#                 upcoming=0
#                 sold = 0
#                 sold_list = []
#                 upcoming_list = []
#                 for item in active_list:
#                     veg = item.veg_inventory_veg_id
#                     veg_min_qty = float(veg.veg_min_qty)
#                     available_qty = float(item.veg_available_qty_sun) - float(item.veg_sold_qty_sun)
#                     if available_qty==0:
#                         sold+=1
#                         sold_list.append(veg)
#                     check_upcoming  = veg_min_qty*2
#                     if available_qty<check_upcoming:
#                         upcoming+=1
#                         upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':item.veg_available_qty_sun,'sold_qty':item.veg_sold_qty_sun})

#             temp.update({'active':active, 'sold':sold, 'upcoming':upcoming, 'sold_list':sold_list, 'upcoming_list':upcoming_list,'store_id':store_id})
#             veg_dict.update({store_id_name_map.get(store_id):temp})

#         data.update({category_id_map.get(cat_id):veg_dict})

#     return data



def get_product_data(day):
    store_id_list = [1,6,15]
    category_id_list = [0,2,3,4,5]
    data = {}
    for cat_id in category_id_list:
        veg_dict = {}
        for store_id in store_id_list:
            temp = {}
            veg_id_list = list(Products.objects.filter(veg_type=cat_id).values_list('veg_id',flat=True))
            inv = Inventory.objects.filter(veg_inventory_store_id=store_id,veg_inventory_veg_id__in=veg_id_list)

            veg_status = 'veg_status_{}'.format(day_map.get(day))
            veg_available_qty = 'veg_available_qty_{}'.format(day_map.get(day))
            veg_sold_qty = 'veg_sold_qty_{}'.format(day_map.get(day))

            active_list = inv.filter(**{veg_status:1})
            active = active_list.count()
            # upcoming list and sold list
            upcoming=0
            sold = 0
            sold_list = []
            upcoming_list = []
            for item in active_list:
                veg = item.veg_inventory_veg_id
                veg_min_qty = float(veg.veg_min_qty)
                available_qty = float(getattr(item, veg_available_qty)) - float(getattr(item, veg_sold_qty))
                if available_qty==0:
                    sold+=1
                    sold_list.append(veg)
                check_upcoming  = veg_min_qty*2
                if available_qty<check_upcoming:
                    upcoming+=1
                    upcoming_list.append({'veg_id':veg.veg_id,'veg_name':veg.veg_name,'avl_qty':getattr(item, veg_available_qty),'sold_qty':getattr(item, veg_sold_qty)})

            temp.update({'active':active, 'sold':sold, 'upcoming':upcoming, 'sold_list':sold_list, 'upcoming_list':upcoming_list,'store_id':store_id})
            veg_dict.update({store_id_name_map.get(store_id):temp})

        data.update({category_id_map.get(cat_id):veg_dict})

    return data
