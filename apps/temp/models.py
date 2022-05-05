from django.db import models

# Create your models here.
class ffz_category(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)    

    class Meta:
        managed=False
        db_table='ffz_category'

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
    veg_slug=models.CharField(max_length=45)
    veg_description=models.TextField(max_length=45)
    veg_fertilizers=models.TextField(max_length=45)
    veg_pesticides=models.TextField(max_length=45)
    veg_storage=models.CharField(max_length=45)
    veg_base_price_per=models.FloatField()
    veg_base_price_plus=models.FloatField()
    veg_current_rate_mon=models.FloatField()
    veg_current_rate_tue=models.FloatField()
    veg_current_rate_wed=models.FloatField()
    veg_current_rate_thu=models.FloatField()
    veg_current_rate_fri=models.FloatField()
    veg_current_rate_sat=models.FloatField()
    veg_current_rate_sun=models.FloatField()
    veg_market_rate=models.FloatField()
    veg_production_duration=models.CharField(max_length=45)
    veg_yield_duration=models.CharField(max_length=45)
    veg_differ_qty=models.FloatField()
    veg_measurements_id=models.CharField(max_length=45)
    veg_image=models.CharField(max_length=45)
    veg_sort_order=models.IntegerField()
    veg_pack_order=models.IntegerField()
    veg_featured=models.IntegerField()
    veg_remove_status=models.BooleanField()
    veg_sub_not_intrested=models.IntegerField()
    veg_hsn_code=models.CharField(max_length=45)
    veg_gst=models.CharField(max_length=45)
    veg_minimum_selling_price=models.IntegerField()
    subscription_qty=models.FloatField()
    add_to_subscription=models.IntegerField()
    veg_deep_link=models.CharField(max_length=45)
    veg_n_img_main_url=models.CharField(max_length=45)
    veg_n_img_thumb_url=models.CharField(max_length=45)
    veg_crate_qty=models.IntegerField()
    veg_auto_sort_order=models.IntegerField()
    veg_audit_status=models.IntegerField()
    veg_pq_adjust_status=models.IntegerField()
    veg_c_img_main_url=models.CharField(max_length=45)
    veg_c_img_thumb_url=models.CharField(max_length=45)
    class Meta:
        managed=False
        db_table='ffz_vegitables'

class ExcelFileUpload(models.Model):
    excel_file=models.FileField(upload_to='excel')