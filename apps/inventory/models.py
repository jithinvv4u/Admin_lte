from django.db import models
from apps.products.models import Products

class Inventory(models.Model):
    veg_inventory_id = models.AutoField(primary_key=True)
    veg_inventory_veg_id = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='inventory',
        db_column='veg_inventory_veg_id')
    veg_inventory_store_id = models.IntegerField(blank=True, default=0)
    veg_inventory_status = models.IntegerField(blank=True, default=0)
    veg_available_qty_mon = models.CharField(
        blank=True, default=0, max_length=10)
    veg_available_qty_tue = models.CharField(
        blank=True, default=0, max_length=10)
    veg_available_qty_wed = models.CharField(
        blank=True, default=0, max_length=10)
    veg_available_qty_thu = models.CharField(
        blank=True, default=0, max_length=10)
    veg_available_qty_fri = models.CharField(
        blank=True, default=0, max_length=10)
    veg_available_qty_sat = models.CharField(
        blank=True, default=0, max_length=10)
    veg_available_qty_sun = models.CharField(
        blank=True, default=0, max_length=10)
    veg_sold_qty_mon = models.CharField(blank=True, default=0, max_length=10)
    veg_sold_qty_tue = models.CharField(blank=True, default=0, max_length=10)
    veg_sold_qty_wed = models.CharField(blank=True, default=0, max_length=10)
    veg_sold_qty_thu = models.CharField(blank=True, default=0, max_length=10)
    veg_sold_qty_fri = models.CharField(blank=True, default=0, max_length=10)
    veg_sold_qty_sat = models.CharField(blank=True, default=0, max_length=10)
    veg_sold_qty_sun = models.CharField(blank=True, default=0, max_length=10)
    veg_status_mon = models.CharField(blank=True, default=0, max_length=2)
    veg_status_tue = models.CharField(blank=True, default=0, max_length=2)
    veg_status_wed = models.CharField(blank=True, default=0, max_length=2)
    veg_status_thu = models.CharField(blank=True, default=0, max_length=2)
    veg_status_fri = models.CharField(blank=True, default=0, max_length=2)
    veg_status_sat = models.CharField(blank=True, default=0, max_length=2)
    veg_status_sun = models.CharField(blank=True, default=0, max_length=2)
    veg_inventory_store_min_qty = models.DecimalField(
        blank=True, default=0, decimal_places=2, max_digits=10)
    veg_inventory_min_procurement_percentage = models.DecimalField(
        blank=True, default=None, decimal_places=2, max_digits=10)
    modify_by = models.IntegerField(blank=True, default=0)
    modify_date = models.DateTimeField(blank=True)
    veg_inventory_stock_in_hand = models.DecimalField(
        blank=True, max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'ffz_veg_inventory'


class InventryLog(models.Model):
    inventory_log_id = models.AutoField(primary_key=True)
    inventory_added_date = models.DateField()
    inventory_manuf_id = models.IntegerField(blank=True, null=True)
    inventory_collector_id = models.IntegerField(blank=True, null=True)
    inventory_regional_store_id = models.IntegerField(blank=True, null=True)
    inventory_log_admin_id = models.IntegerField(blank=True, null=True)
    inventory_veg_id = models.IntegerField()
    inventory_price = models.FloatField(blank=True, null=True)
    inventory_veg_qty = models.FloatField()
    inventory_log_added_date = models.DateTimeField()
    inventory_notes = models.TextField(blank=True, null=True)
    inventory_log_status = models.IntegerField()
    inventory_log_type = models.IntegerField()
    inventory_log_modified_date = models.DateTimeField(blank=True, null=True)
    inventory_wastage_type = models.IntegerField()
    inventory_store_id = models.IntegerField(blank=True, null=True)
    inventory_fi_id = models.IntegerField(blank=True, null=True)
    inventory_ibt_id = models.IntegerField(blank=True, null=True)
    inventory_intented_qty = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "ffz_inventory_log"

    def __str__(self):
        return str(self.inventory_log_id)
