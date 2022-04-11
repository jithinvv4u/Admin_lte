from django.db import models

class Settings(models.Model):
    settings_id = models.AutoField(primary_key=True)
    settings_store_id = models.IntegerField()
    settings_name = models.CharField(max_length=255)
    settings_desc = models.CharField(max_length=255, blank=True)
    settings_type = models.IntegerField(default=None, blank=True)
    settings_value = models.CharField(max_length=255, default=None, blank=True)
    settings_sort = models.DecimalField(
        decimal_places=2, max_digits=10, default=None, blank=True)

    class Meta:
        db_table = "ffz_settings"

    def __str__(self):
        return self.settings_id


class Blog(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    feature_image = models.CharField(max_length=300)


class Banner(models.Model):
    element_id = models.IntegerField(primary_key=True)
    element_name = models.CharField(max_length=200)
    element_type = models.CharField(max_length=100, blank=True, default=None)
    element_data = models.TextField(blank=True, default=None)
    element_status = models.IntegerField(blank=True, default=1)
    element_order = models.IntegerField(blank=True, default=None)
    element_for = models.IntegerField(blank=True, default=None)
    element_auto_log_user = models.IntegerField(null=True, default=0)
    element_store_id = models.IntegerField(blank=True, default=None)
    element_city = models.IntegerField(blank=True, default=None)

    class Meta:
        db_table = "ffz_page_configuration"

    def __str__(self):
        return str(self.element_id)


class HomeSliderImages(models.Model):
    page_slider_id = models.AutoField(primary_key=True)
    ffz_page_configuration_element_id = models.IntegerField(
        blank=False, default=0)
    page_slider_img_main_url = models.TextField(
        blank=True, null=True, default=None)
    page_slider_img_thumb_url = models.TextField(
        blank=True, null=True, default=None)

    class Meta:
        db_table = "ffz_page_configuration_slider_image"

    def __str__(self):
        return str(self.page_slider_id)


class Notify(models.Model):
    id = models.AutoField(primary_key=True)
    veg_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    email_phone = models.CharField(max_length=50, default=0, blank=True)
    status = models.IntegerField(default=1)
    time = models.IntegerField(default=0)
    ip = models.CharField(default=0, max_length=50)
    store_id = models.IntegerField(default=1, null=True)
    city_id = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = "ffz_notify"

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    ffz_user_review_id = models.AutoField(primary_key=True)
    ffz_user_review_user_id = models.IntegerField(default=0, blank=False)
    ffz_user_review_play = models.IntegerField(default=0, blank=False)
    ffz_user_review_fb = models.IntegerField(default=0, blank=False)
    ffz_user_review_insta = models.IntegerField(default=0, blank=False)

    class Meta:
        db_table = 'ffz_user_review'


class SubV2DeliveryDate(models.Model):
    id = models.AutoField(primary_key=True)
    ffz_subscriptions_pkey = models.IntegerField(blank=True)
    sub_delivery_date = models.DateField(blank=True)
    ffz_subscriptions_date_status = models.IntegerField(blank=True)
    user_id = models.IntegerField(blank=True)
    subscription_note = models.TextField(blank=True)
    sub_delivery_status = models.IntegerField(blank=True)
    sub_delivery_kit_id = models.IntegerField(blank=True)
    sub_delivery_kit_no = models.IntegerField(blank=True)
    sub_delivery_packed_date = models.DateTimeField(blank=True)
    subscription_extra_note = models.TextField(blank=True)
    sub_recharge_id = models.IntegerField(blank=True)

    class Meta:
        db_table = 'ffz_sub_v2_delivery_date'

    def __str__(self):
        return str(self.id)


class App_Settings(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,  null=True, blank=True)
    value = models.CharField(max_length=300,  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ffz_app_settings'

    def __str__(self):
        return str(self.id)
    

class PaidApiAlert(models.Model):	
    api_id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=250, default=0, null=True)
    count = models.IntegerField(default=None)
    threshold_value = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    threshold_completed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "ffz_paid_api_count"

    def __str__(self):
        return str(self.api_id)
