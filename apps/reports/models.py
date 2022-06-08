from datetime import tzinfo
from operator import mod
from django.db import models
from datetime import datetime
# import datetime
# Create your models here. 
class ffz_category(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)    

    class Meta:
        managed=False
        db_table='ffz_category'

class ffz_store(models.Model):
    store_id=models.IntegerField(primary_key=True)
    store_name=models.CharField(max_length=45)
    store_is_mdc=models.IntegerField()
    class Meta:
        managed=False
        db_table='ffz_stores'
    
    def __str__(self):
        return self.store_name
    
class ffz_main_city(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    main_store_id=models.ForeignKey(ffz_store,on_delete=models.CASCADE,db_column='parent_store_id')
    status=models.IntegerField()
    
    class Meta:
        managed=False
        db_table='ffz_main_city'
        
class ffz_users(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=45)
    user_email=models.CharField(max_length=45)
    user_phone=models.IntegerField()
    user_signup_date=models.DateTimeField()
    user_registration_type=models.IntegerField()
    user_email_verified=models.IntegerField()
    
    class Meta:
        managed=False
        db_table='ffz_users'
    
class ffz_vegitables(models.Model):
    veg_id=models.IntegerField(primary_key=True)
    veg_name=models.CharField(max_length=45)
    veg_basic_rate=models.IntegerField()
    veg_min_qty=models.FloatField()
    veg_measurement=models.CharField(max_length=45)
    veg_type=models.ForeignKey(
        ffz_category,
        on_delete=models.CASCADE,
        db_column='veg_type',
        )
    class Meta:
        managed=False
        db_table='ffz_vegitables'

class ffz_orders(models.Model):
    order_id=models.IntegerField()
    order_placed_id=models.IntegerField(primary_key=True)
    order_order_status_id=models.IntegerField()
    order_veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='order_veg_id',
        )
    order_date=models.DateTimeField()
    class Meta:
        managed=False
        db_table='ffz_orders'
        
        
class ffz_veg_price(models.Model):
    veg_price_id=models.IntegerField(primary_key=True)
    veg_price_veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='veg_price_veg_id'
        )
    veg_price_store_id=models.ForeignKey(
        ffz_store,
        on_delete=models.CASCADE,
        db_column='veg_price_store_id'
        )
    veg_price_basic_rate=models.FloatField()
    veg_price_modify_date=models.DateTimeField()
    
    class Meta:
        managed=False
        db_table='ffz_veg_price'
     
class ffz_inventory_log(models.Model):
    inventory_log_id=models.IntegerField(primary_key=True)
    inventory_added_date=models.DateField()
    inventory_veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='inventory_veg_id',
        )
    inventory_veg_qty=models.FloatField()
    inventory_log_type=models.IntegerField()
    inventory_price=models.FloatField()
    
    class Meta:
        managed=False
        db_table='ffz_inventory_log'
     

class ffz_veg_inventory(models.Model):
    veg_inventory_id=models.IntegerField(primary_key=True)
    veg_inventory_veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='veg_inventory_veg_id')
    veg_inventory_log_id=models.ForeignKey(
        ffz_inventory_log,
        on_delete=models.CASCADE,
        db_column='veg_inventory_log_id')
    veg_inventory_stock_in_hand=models.FloatField()
    
    class Meta:
        managed=False
        db_table='ffz_veg_inventory'

class Notify(models.Model):
    id=models.IntegerField(primary_key=True)
    veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='veg_id'
        )
    status=models.IntegerField()
    delivery_date=models.DateField()
    store_id=models.ForeignKey(
        ffz_store,
        on_delete=models.CASCADE,
        db_column='store_id'
        )
    
    class Meta:
        managed=False
        db_table='ffz_notify'

class ffz_payment_status(models.Model):
    payment_status_id=models.AutoField(primary_key=True)
    payment_status_name=models.CharField(max_length=45)
    
    class Meta:
        managed=False
        db_table='payment_status'

class placedOrderManager(models.Manager):
    
    def delivery_date_filter(self,start_date,end_date):
        items = []
        for obj in self.all():
            if datetime.strptime(obj.placed_order_delivery_date,'%Y-%m-%d') < end_date and datetime.strptime(obj.placed_order_delivery_date,'%Y-%m-%d') > start_date:
                items.append(obj)
        return items


class ffz_placed_orders(models.Model):
    placed_order_id=models.AutoField(primary_key=True)
    placed_order_date=models.DateTimeField(blank=True)
    placed_order_delivery_date=models.DateField(blank=True)
    placed_order_packed_time=models.DateTimeField(blank=True)
    placed_order_price=models.FloatField(blank=True)
    placed_order_shipping_charge=models.FloatField(blank=True)
    placed_order_gst=models.FloatField(blank=True)
    placed_order_packed_sum=models.FloatField(blank=True)
    placed_order_wallet_amount=models.FloatField(blank=True)
    placed_order_packed_wallet_adjustment=models.FloatField(blank=True)
    placed_order_discount=models.FloatField()
    placed_order_pq_total=models.FloatField()
    placed_order_order_status_id=models.CharField(max_length=45)
    placed_delivery_express_pref=models.IntegerField()
    placed_order_packed_sum=models.FloatField()
    placed_delivery_express_pref=models.IntegerField()
    placed_order_city_id=models.ForeignKey(
        ffz_main_city,
        on_delete=models.CASCADE,
        db_column='placed_order_city_id'
        )
    placed_order_payment_status_id=models.ForeignKey(
        ffz_payment_status,
        on_delete=models.CASCADE,
        db_column='placed_order_payment_status_id',blank=True)
    placed_order_payment_method=models.IntegerField()
    placed_order_delivery_status=models.IntegerField()
    placed_order_order_status_id=models.IntegerField(blank=True)
    placed_order_type_id=models.IntegerField(blank=True)
    placed_order_txtn_id=models.CharField(max_length=45)
    placed_order_user_id=models.ForeignKey(
        ffz_users,
        on_delete=models.CASCADE,
        db_column='placed_order_user_id',
        blank=True
        )
    placed_order_store_id=models.ForeignKey(
        ffz_store,
        on_delete=models.CASCADE,
        db_column='placed_order_store_id',
        blank=True
        )
    objects=placedOrderManager()
    
    class Meta:
        managed=False
        db_table='ffz_placed_orders'




class ffz_wallet_trans_history(models.Model):
    wallet_trans_id=models.IntegerField(primary_key=True)
    reson=models.CharField(max_length=45)
    
    class Meta:
        managed=False
        db_table='ffz_wallet_trans_history'
        
        
class ffz_wallet_trans(models.Model):
    wallet_trans_id=models.ForeignKey(
        ffz_wallet_trans_history,
        on_delete=models.CASCADE,
        db_column='wallet_trans_id',
        null=True,
        )
    wallet_trans_user_id=models.ForeignKey(
        ffz_users,
        on_delete=models.CASCADE,
        db_column='wallet_trans_user_id',
        )
    wallet_trans_time=models.DateTimeField(null=True,)
    wallet_trans_placed_order_id=models.ForeignKey(ffz_placed_orders,on_delete=models.CASCADE,db_column='wallet_trans_placed_order_id')
    # wallet_trans_placed_order_id=models.IntegerField()
    wallet_trans_message=models.CharField(max_length=45,null=True,)
    wallet_trans_status=models.IntegerField(null=True,)
    wallet_trans_amount=models.FloatField(null=True,)
    
    class Meta:
        managed=False
        db_table='ffz_wallet_trans'
    
class ffz_audit_log_details(models.Model):
    audit_log_detail_id=models.IntegerField(primary_key=True)
    audit_log_detail_veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='audit_log_detail_veg_id',
        )
    audit_log_detail_qty=models.FloatField()
    
    class Meta:
        managed=False
        db_table='ffz_audit_log_details'
       
class ffz_packed(models.Model):
    packed_id=models.IntegerField(primary_key=True)             #stock packed
    packed_order_id=models.ForeignKey(
        ffz_orders,
        on_delete=models.CASCADE,
        db_column='packed_order_id'
        )
    packed_order_qty=models.FloatField()
    
    class Meta:
        managed=False
        db_table='ffz_packed'

class ffz_veg_inventory(models.Model):
    veg_inventory_id=models.IntegerField(primary_key=True)
    veg_inventory_veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='veg_inventory_veg_id'
        )
    veg_inventory_store_id=models.ForeignKey(
        ffz_store,
        on_delete=models.CASCADE,
        db_column='veg_inventory_store_id'
        )
    veg_inventory_stock_in_hand=models.FloatField()
    
    class Meta:
        managed=False
        db_table='ffz_veg_inventory'
    

class ffz_user_referral(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(ffz_users,on_delete=models.CASCADE,db_column='user_id',related_name='user')
    order_id=models.ForeignKey(ffz_orders,on_delete=models.CASCADE,db_column='order_id')
    user_referral_id=models.ForeignKey(ffz_users,on_delete=models.CASCADE,db_column='user_referral_id',related_name='referred_user')
    active_refferal=models.IntegerField()
    referral_date=models.DateTimeField()
    
    class Meta:
        managed:False
        db_table='ffz_user_referral'
        
        
class ffz_razor_payment_history(models.Model):
    id=models.IntegerField(primary_key=True)
    razor_order_placed_id=models.ForeignKey(
        ffz_placed_orders,
        on_delete=models.CASCADE,
        db_column='razor_order_placed_id',
        related_name='razorpayment_history'
        )
    razor_payment_id=models.IntegerField()
    
    class Meta:
        managed=False
        db_table='ffz_razor_payment_history'

class ffz_transaction_before(models.Model):
    bf_id=models.AutoField(primary_key=True)
    bf_user_id=models.ForeignKey(
        ffz_users,
        on_delete=models.CASCADE,
        db_column='bf_user_id'
        )
    bf_amount=models.FloatField()
    
    class Meta:
        managed=False
        db_table='ffz_transaction_before'

# class ffz_wallet_trans_history(models.Model):
#     wallet_trans_id=models.IntegerField(primary_key=True)
#     reason=models.CharField(max_length=45)
    
#     class Meta:
#         managed=False
#         db_table='ffz_wallet_trans_history'

        
    
    
# class ffz_veg_measurement(models.Model):
#     veg_measurement_id=models.IntegerField(primary_key=True)
#     veg_measurement_name=models.CharField(max_length=45)
 
#     class Meta:
#         managed=False
#         db_table='ffz_veg_measurement'

# class VegCategoryMapping(models.Model):
#     veg_mapping_id = models.AutoField(primary_key=True)
#     veg_mapping_veg_id = models.ForeignKey(
#         ffz_vegitables,
#         on_delete=models.CASCADE,
#         related_name='veg_mapping',
#         db_column='veg_mapping_veg_id',
#         default=None)
#     veg_mapping_category_id = models.ForeignKey(
#         ffz_category,
#         on_delete=models.CASCADE,
#         related_name='category_mapping',
#         db_column='veg_mapping_category_id',
#         default=None)
#     veg_mapping_status = models.IntegerField(default=None)
#     veg_mapping_added_date = models.DateTimeField(auto_now=True)

#     class Meta:
#         managed=False
#         db_table = "ffz_veg_category_mapping"
   