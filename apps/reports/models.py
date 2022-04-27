from django.db import models

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
    
    class Meta:
        managed=False
        db_table='ffz_stores'
        
class ffz_users(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=45)
    
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
    order_placed_id=models.IntegerField(primary_key=True)
    order_order_status_id=models.IntegerField()
    order_veg_id=models.ForeignKey(
        ffz_vegitables,
        on_delete=models.CASCADE,
        db_column='order_veg_id',
        )
    
    class Meta:
        managed=False
        db_table='ffz_orders'
        
        
class ffz_veg_price(models.Model):
    veg_price_id=models.AutoField(primary_key=True)
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
   

class ffz_wallet_trans(models.Model):
    wallet_trans_id=models.IntegerField(primary_key=True)
    wallet_trans_user_id=models.ForeignKey(
        ffz_users,
        on_delete=models.CASCADE,
        db_column='wallet_trans_user_id'
        )
    wallet_trans_time=models.DateTimeField()
    wallet_trans_placed_order_id=models.IntegerField()
    wallet_trans_message=models.CharField(max_length=45)
    wallet_trans_status=models.IntegerField()
    wallet_trans_amount=models.FloatField()
    
    class Meta:
        managed=False
        db_table='ffz_wallet_trans'
    
class ffz_audit_log_details(models.Model):
    audit_log_detail_id=models.AutoField(primary_key=True)
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
   