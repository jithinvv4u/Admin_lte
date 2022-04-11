from django.db import models

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    parent_id = models.IntegerField()
    status = models.IntegerField()
    sort_order = models.IntegerField()
    veg_img = models.CharField(max_length=10)
    cat_c_img_main_url = models.CharField(max_length=200, blank=True)
    cat_c_img_thumb_url = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "ffz_category"

    def __str__(self):
        return self.id


class Products(models.Model):
    veg_id = models.IntegerField(primary_key=True)
    veg_name = models.CharField(max_length=30)
    veg_slug = models.CharField(max_length=50, null=True, default=None,
                                blank=True)
    veg_description = models.CharField(max_length=300, blank=True)
    veg_fertilizers = models.TextField(blank=True)
    veg_pesticides = models.TextField(blank=True)
    veg_storage = models.CharField(max_length=300, blank=True)
    veg_basic_rate = models.IntegerField(default=0)
    # offer_percentage = models.IntegerField(default=0, blank=True)
    veg_base_price_per = models.IntegerField(default=0)
    veg_base_price_plus = models.IntegerField(default=0)
    # veg_current_rate = models.IntegerField(max_length=40)
    veg_current_rate_mon = models.IntegerField(default=0)
    veg_current_rate_tue = models.IntegerField(default=0)
    veg_current_rate_wed = models.IntegerField(default=0)
    veg_current_rate_thu = models.IntegerField(default=0)
    veg_current_rate_fri = models.IntegerField(default=0)
    veg_current_rate_sat = models.IntegerField(default=0)
    veg_current_rate_sun = models.IntegerField(default=0)
    veg_market_rate = models.IntegerField(default=0)
    veg_production_duration = models.CharField(max_length=100, blank=True)
    veg_yield_duration = models.CharField(max_length=100, blank=True)
    veg_min_qty = models.CharField(max_length=15)
    veg_differ_qty = models.CharField(max_length=15)
    veg_measurement = models.CharField(max_length=10)
    veg_image = models.CharField(max_length=50)
    veg_sort_order = models.IntegerField(default=1)
    veg_pack_order = models.IntegerField(default=10)
    veg_type = models.IntegerField(default=0)
    veg_featured = models.IntegerField(default=0)
    veg_remove_status = models.IntegerField(default=0)
    veg_sub_not_intrested = models.IntegerField(default=0)
    veg_hsn_code = models.CharField(max_length=255, default=0)
    veg_gst = models.CharField(max_length=255, default=0)
    veg_minimum_selling_price = models.IntegerField(default=0)
    subscription_qty = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    add_to_subscription = models.IntegerField(default=0)
    veg_deep_link = models.CharField(max_length=255, default=0, blank=True)
    veg_c_img_main_url = models.CharField(max_length=200, default=0)
    veg_c_img_thumb_url = models.CharField(max_length=200, default=0)
    veg_n_img_thumb_url = models.CharField(
        max_length=255, blank=True, default=0)
    veg_n_img_main_url = models.CharField(
        max_length=255, blank=True, default=0)
    veg_crate_qty = models.IntegerField(default=0)
    veg_auto_sort_order = models.IntegerField(default=0)
    veg_audit_status = models.IntegerField(default=0)
    # veg_current_rate = models.CharField(max_length=40)

    class Meta:
        db_table = "ffz_vegitables"

    def __str__(self):
        return str(self.veg_id)


class VegImages(models.Model):
    veg_image_id = models.IntegerField(primary_key=True)
    veg_image_veg_id = models.IntegerField(default=None)
    veg_image_path = models.CharField(max_length=255, default=None)
    veg_image_remote_url = models.CharField(max_length=255, null=True)
    veg_image_type = models.SmallIntegerField(default=None)
    veg_image_title = models.CharField(max_length=255, null=True)
    veg_image_details = models.TextField(null=True)
    veg_image_status = models.SmallIntegerField(default=None)

    class Meta:
        db_table = "ffz_veg_images"

    def __str__(self):
        return str(self.veg_image_veg_id)


class UserPopularSearches(models.Model):
    id = models.AutoField(primary_key=True)
    sku_id = models.IntegerField(blank=True, null=True)
    search_count = models.IntegerField(blank=True, null=True, default=0)
    last_searched_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ffz_user_popularsearch'

    def __str__(self):
        return str(self.id)


class RecommendedProducts(models.Model):
    id = models.AutoField(primary_key=True)
    veg_id = models.CharField(max_length=10)
    recommended_veg_id = models.CharField(max_length=10, null=True)
    last_updated_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=1)
    is_processed = models.BooleanField(default=True)

    class Meta:
        db_table = "ffz_recommended_products"

    def __str__(self):
        return str(self.id)


class VegetablePrice(models.Model):
    veg_price_id = models.AutoField(primary_key=True)
    veg_price_store_id = models.IntegerField(default=0)
    veg_price_veg_id = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='vegprice',
        db_column='veg_price_veg_id')
    veg_price_status = models.IntegerField(default=1)
    veg_price_basic_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_minimum_selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_base_per = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_base_plus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_current_rate_mon = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_current_rate_tue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_current_rate_wed = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_current_rate_thu = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_current_rate_fri = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_current_rate_sat = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_current_rate_sun = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_market_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    veg_price_modify_by = models.IntegerField(default=0)
    veg_price_modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ffz_veg_price"

    def __str__(self):
        return str(self.veg_price_id)


class ShippingCharge(models.Model):
    id = models.AutoField(primary_key=True)
    ffz_total_price = models.IntegerField(default=0)
    ffz_shipping_charge = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00, blank=True)
    ffz_shipping_store_id = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "ffz_shipping_charge_mapping"

    def __str__(self):
        return str(self.id)


class VegCategoryMapping(models.Model):
    veg_mapping_id = models.AutoField(primary_key=True)
    veg_mapping_veg_id = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='veg_mapping',
        db_column='veg_mapping_veg_id',
        default=None)
    veg_mapping_category_id = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='category_mapping',
        db_column='veg_mapping_category_id',
        default=None)
    veg_mapping_status = models.IntegerField(default=None)
    veg_mapping_added_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ffz_veg_category_mapping"

    def __str__(self):
        return str(self.veg_mapping_id)
