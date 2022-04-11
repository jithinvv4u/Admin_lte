from django.db import models

class Store(models.Model):
    store_id = models.CharField(max_length=10, primary_key=True)
    store_name = models.CharField(max_length=32)
    store_status = models.IntegerField(default=0)
    disable_daily_delivery = models.IntegerField(default=0)
    store_is_mdc = models.IntegerField(default=0)

    class Meta:
        db_table = "ffz_stores"

    def __str__(self):
        return self.store_id


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slag = models.CharField(max_length=200, null=True,
                            default=None, blank=True)
    locus_team_name = models.CharField(max_length=100, default=0)
    locus_team_id = models.CharField(max_length=255, default=None)
    locus_team_skill = models.TextField(blank=True, default=None)
    locus_homebase_code = models.CharField(
        max_length=100, default=None, blank=True)
    city_code = models.CharField(max_length=20, blank=True)
    city_cutoff_time = models.TimeField(auto_now=True)
    img = models.CharField(max_length=200)
    parent_slag = models.CharField(max_length=100, blank=True, default=0)
    parent_store_id = models.IntegerField()
    main_store_id = models.IntegerField(default=0)
    status = models.IntegerField()

    class Meta:
        db_table = "ffz_main_city"

    def __str__(self):
        return str(self.id)

    
class Address(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    user_address_user_id = models.CharField(max_length=11)
    user_address_name = models.CharField(max_length=255, blank=True)
    user_address_street = models.TextField(blank=True)
    user_address_city = models.CharField(max_length=255, blank=True)
    user_address_zip = models.CharField(max_length=50, blank=True)
    user_address_status = models.CharField(max_length=4, default=1)
    user_address_apartment = models.CharField(max_length=255, blank=True)
    user_address_flat_number = models.CharField(max_length=255, blank=True)
    user_address_type = models.CharField(max_length=20, default=1)
    user_address_type_name = models.CharField(max_length=20, blank=True)
    user_address_default = models.CharField(max_length=11, default=1)
    user_address_phone = models.CharField(max_length=20, blank=True)
    user_address_lat = models.TextField(blank=True, default=None)
    user_address_lon = models.TextField(blank=True, default=None)

    class Meta:
        db_table = "ffz_user_address"

    def __str__(self):
        return str(self.user_address_id)

    
class ZipCodes(models.Model):
    store_zip_code_id = models.AutoField(primary_key=True)
    store_zip_code_name = models.CharField(max_length=100, default=None)
    store_zip_code_value = models.CharField(max_length=6, default=None)
    store_zip_code_store_id = models.IntegerField(default=None)
    store_zip_code_city_id = models.IntegerField(default=1)
    store_zip_code_status = models.IntegerField(default=None)
    store_zip_code_sort_order = models.IntegerField(default=None)
    store_zip_code_added_date = models.DateTimeField(blank=True)
    store_zip_code_deleted_date = models.DateTimeField(
        default=None, blank=True)

    class Meta:
        db_table = "ffz_store_zip_codes"

    def __str__(self):
        return str(self.store_zip_code_id)


class ZipMapping(models.Model):
    zip_dp_id = models.AutoField(primary_key=True)
    zip_dp_pref_id = models.IntegerField(blank=False)
    zip_dp_zone_id = models.IntegerField(blank=False)
    zip_dp_status = models.IntegerField(blank=False, default=0)
    zip_dp_added_date = models.DateTimeField(blank=False)

    class Meta:
        db_table = 'ffz_delivery_zip_code_mapping'

    def __str__(self):
        return str(self.zip_dp_id)
