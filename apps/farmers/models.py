from django.db import models

class Farmers(models.Model):
    manufacture_id = models.AutoField(primary_key=True)
    manufacture_name = models.CharField(max_length=255, blank=True)
    manufacture_code = models.CharField(max_length=255, blank=True)
    manufacture_license = models.CharField(max_length=255, blank=True)
    manufacture_status = models.IntegerField(blank=True)
    manufacture_description = models.TextField(blank=True)
    manufacture_location = models.CharField(max_length=255, blank=True)
    manufacture_image = models.CharField(max_length=255, blank=True)
    manufacture_img_main_url = models.TextField(
        default=None, blank=True, null=True)
    manufacture_img_thumb_url = models.TextField(
        default=None, blank=True, null=True)

    class Meta:
        db_table = "ffz_manufactures"

    def __str__(self):
        return str(self.manufacture_id)


class FarmerImages(models.Model):
    manufacture_image_id = models.AutoField(primary_key=True)
    manufacture_image_manufacture_id = models.ForeignKey(Farmers, 
    on_delete=models.CASCADE, 
    related_name='farmers_img', 
    db_column='manufacture_image_manufacture_id',
    default=None)
    manufacture_image_image = models.CharField(max_length=255, default=None)
    manufacture_image_status = models.IntegerField(default=None)

    class Meta:
        db_table = "ffz_manufacture_images"

    def __str__(self):
        return self.manufacture_id


class FarmersVeg(models.Model):
    manufacture_veg_id = models.AutoField(primary_key=True)
    veg_id = models.IntegerField(default=None)
    manufacture_id = models.IntegerField(default=None)
    manufacture_veg_code = models.CharField(max_length=255, default=None)
    manufacture_veg_status = models.IntegerField(default=None)

    class Meta:
        db_table = "ffz_manufacture_vegitables"

    def __str__(self): return self.manufacture_veg_id


class Farmer_Reg(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=100)
    farmer_manu_map_id = models.IntegerField(default=0, blank=True)
    farmer_profile_pic = models.CharField(max_length=300,  null=True, blank=True)
    farmer_location = models.CharField(max_length=150,  null=True, blank=True)
    farmer_is_vendor = models.IntegerField(default=0, blank=True)
    farmer_status = models.IntegerField(default=None)

    class Meta:
        db_table = 'farmer_reg'

    def __str__(self):
        return str(self.farmer_id)


class Farmer_Test(models.Model):
    f_test_id = models.AutoField(primary_key=True)
    f_test_farmer_id = models.IntegerField(default=0, blank=True, null=True)
    f_test_img = models.CharField(max_length=300,  null=True, blank=True)
    f_test_date = models.DateField(blank=True, null=True)
    f_test_status = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'farmer_tests'

    def __str__(self):
        return str(self.f_test_id)
