from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_placed_id = models.CharField(max_length=50, default=0)
    order_date = models.DateTimeField(blank=True, default='')
    order_delivery_date = models.CharField(max_length=50, blank=True)
    order_delivery_slot_id = models.IntegerField(
        default=None, null=True, blank=True)
    order_veg_id = models.CharField(max_length=10)
    order_veg_qty = models.CharField(max_length=50)
    order_user_id = models.IntegerField(default=None, blank=True)
    order_mrp = models.CharField(max_length=10)
    order_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_discount = models.CharField(max_length=10, default='0.00')
    order_price = models.CharField(max_length=10)
    order_gst = models.CharField(max_length=10, default=0)
    order_order_status_id = models.CharField(max_length=2, default=0)
    order_payment_status_id = models.CharField(max_length=2, default=0)
    order_status = models.CharField(max_length=2, default=0)
    order_active = models.CharField(max_length=2, default=1)
    order_soldout_inactive = models.CharField(max_length=2, default=0)
    order_store_id = models.CharField(max_length=3)
    order_city_id = models.IntegerField(default=0)
    order_temp_id = models.CharField(max_length=15, blank=True)
    order_total = models.CharField(
        max_length=255, default=0, blank=True, null=True)
    order_bf_id = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = "ffz_orders"

    def __str__(self):
        return str(self.order_id)


class CheckoutAddon(models.Model):
    addon_id = models.AutoField(primary_key=True)
    addon_type = models.CharField(max_length=10)
    addon_name = models.CharField(max_length=100)
    addon_status = models.BooleanField(default=1)
    addon_amount = models.CharField(max_length=20, default=0)
    addon_expirytime = models.DateTimeField()
    addon_store_id = models.CharField(max_length=10, default=1)

    class Meta:
        db_table = "ffz_checkout_addon"

    def __str__(self):
        return str(self.addon_id)


class CancelledOrders(models.Model):
    id = models.AutoField(primary_key=True)
    placed_order_id = models.IntegerField(default=0)
    amount_transfer_to = models.IntegerField(default=0)
    cancel_amount = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00)
    cancel_note = models.CharField(max_length=100, default=0)
    cancel_reason = models.CharField(max_length=100, default=0)
    cancel_by = models.IntegerField(default=0)
    modify_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ffz_placed_order_cancel_history"

    def __str__(self):
        return str(self.id)


class PlacedOrders(models.Model):
    placed_order_id = models.AutoField(primary_key=True)
    placed_order_delivery_date = models.CharField(
        max_length=50, default=None, blank=True)
    placed_delivery_express_pref = models.IntegerField(default=0)
    placed_order_date = models.DateTimeField()
    placed_order_user_id = models.IntegerField()
    placed_order_txtn_id = models.CharField(max_length=200)
    placed_order_mrp = models.DecimalField(max_digits=10, decimal_places=2)
    placed_order_savings_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    placed_order_discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    placed_order_price = models.DecimalField(max_digits=10, decimal_places=2)
    placed_order_order_status_id = models.IntegerField()
    placed_order_payment_status_id = models.IntegerField()
    placed_order_type_id = models.IntegerField(blank=True, null=True)
    placed_order_payment_method = models.IntegerField(blank=True, null=True)
    placed_order_wallet_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    placed_order_shipping_method = models.IntegerField(blank=True, null=True)
    placed_order_shipping_charge = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    placed_order_customer_group_id = models.IntegerField(blank=True, null=True)
    placed_order_delivery_emp_id = models.IntegerField(blank=True, null=True)
    placed_order_store_id = models.IntegerField(blank=True, null=True)
    placed_order_city_id = models.IntegerField(default=0)
    placed_order_delivery_location = models.CharField(
        max_length=255, blank=True, null=True)
    placed_order_delivery_zipcode = models.IntegerField(default=0)
    placed_order_admin_user_id = models.IntegerField(blank=True, null=True)
    placed_order_delivery_time_pref = models.CharField(
        max_length=200, blank=True, null=True)
    placed_order_packed_sum = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    placed_order_packed_wallet_adjustment = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    placed_order_gst = models.FloatField(blank=True, null=True)
    placed_order_packed_time = models.DateTimeField(blank=True, null=True)
    placed_order_sub_delivery_id = models.IntegerField(blank=True, null=True)
    placed_order_packed_status = models.IntegerField(blank=True)
    placed_order_packing_emp_id = models.IntegerField(blank=True)
    placed_order_user_promo_id = models.IntegerField(null=True, default=0)
    placed_order_locus_tour_id = models.IntegerField(default=0)
    placed_order_user_name = models.CharField(blank=True, max_length=30)
    placed_order_checkout_addon_id = models.CharField(
        max_length=100, null=True, blank=True)
    placed_order_checkout_addon_amount = models.IntegerField(
        default=0, null=True, blank=True)

    class Meta:
        managed = False
        db_table = "ffz_placed_orders"

    def __str__(self):
        return str(self.placed_order_id)


class DeliveryPreference(models.Model):
    delivery_preference_id = models.AutoField(primary_key=True)
    delivery_preference_city_id = models.IntegerField(default=0)
    delivery_preference_store_id = models.IntegerField(blank=False)
    delivery_preference = models.CharField(max_length=100, blank=False)
    delivery_preference_status = models.IntegerField(blank=False)
    delivery_preference_cutoff_time = models.TimeField(blank=False)
    delivery_preference_order_cap = models.IntegerField(blank=False, default=0)

    class Meta:
        db_table = 'ffz_delivery_preferences'

    def __str__(self):
        return str(self.delivery_preference_id)


class OrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    order_status_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order_status'


class Packed(models.Model):
    packed_id = models.AutoField(primary_key=True)
    packed_order_id = models.IntegerField(unique=True)
    packed_order_qty = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ffz_packed'
