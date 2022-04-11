from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True, default=None)
    user_role_id = models.IntegerField(default=3)
    user_name = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    user_email = models.EmailField(unique=True, blank=True, null=True)
    user_password = models.CharField(max_length=100, default=None, blank=True)
    user_phone = models.CharField(
        max_length=15, unique=True, default=None, null=True, blank=True)
    user_ref_id = models.CharField(default=0, max_length=15)
    user_company_id = models.IntegerField(default=0)
    user_flat_id = models.IntegerField(default=0)
    user_address = models.CharField(max_length=255, default=None)
    user_city = models.CharField(max_length=255, default=None)
    user_zip_code = models.CharField(max_length=255, default=None)
    user_house_no = models.CharField(max_length=255, default=None)
    user_reffered_id = models.CharField(max_length=300, default=0)
    user_email_verified = models.IntegerField(default=0)
    user_level_id = models.IntegerField(default=0)
    user_status = models.IntegerField(default=1)
    ref_max_count = models.IntegerField(default=None)
    user_total_amount = models.CharField(max_length=20, default=0)
    user_signup_date = models.DateTimeField()
    user_update_enabled = models.IntegerField(default=1)
    user_reset_token = models.CharField(max_length=255, default=None)
    user_token_expiry = models.DateTimeField()
    user_delivery_pref = models.CharField(max_length=255, default=None)
    user_lat = models.CharField(max_length=100, default=None)
    user_lon = models.CharField(max_length=100, default=None)
    user_store_id = models.IntegerField(default=1)
    user_city_id = models.IntegerField(default=0)
    user_group_id = models.CharField(default=1, max_length=15)
    user_sales_commision = models.CharField(max_length=20, default='0.00')
    user_beta_tester_status = models.IntegerField(default=0)
    user_otp = models.CharField(max_length=6, default=0)
    user_referral_status = models.IntegerField(default=1)
    user_referral_payment_date = models.DateTimeField(default=None)
    user_registration_type = models.IntegerField(default=4)
    user_tag = models.IntegerField(default=0)
    user_referal_url = models.CharField(max_length=255, default=0, blank=True)
    user_last_visit_date = models.DateTimeField(blank=True, null=True,
                                                verbose_name='last login')
    user_whatsapp_notification_status = models.IntegerField(default=0)

    class Meta:
        db_table = "ffz_users"

    def __str__(self):
        return str(self.user_id)


class TempUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_phone = models.CharField(
        max_length=10, blank=True, null=True, default=None)
    user_email = models.EmailField(
        max_length=100, blank=True, null=True, default=None)
    otp = models.IntegerField(blank=True)
    expiry_time = models.DateTimeField(blank=True)
    city = models.CharField(max_length=3, blank=True)
    # expiry_time = models.DateTimeField(auto_now_add=True, blank=True)
    ffz_temp_user_device_id = models.CharField(max_length=100, blank=True)
    is_deleted = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = "ffz_temp_user"

    def __str__(self):
        return str(self.id)

class UserMessage(models.Model):
    user_message_id = models.AutoField(primary_key=True)
    user_message_user_id = models.IntegerField(default=0, null=True)
    user_message_type  = models.IntegerField(default=0, null=True)
    user_message_content = models.CharField(max_length=250, default=0, null=True)
    user_message_date = models.DateTimeField(auto_now_add=True)
    user_message_admin_user_id = models.IntegerField(default=0, null=True)
    user_message_placed_id = models.IntegerField(default=0, null=True)
    user_message_store_id = models.IntegerField(default=0, null=True)
    user_message_note  = models.CharField(max_length=250, default=0)

    class Meta:
        db_table = "ffz_user_messages"

    def __str__(self):
        return str(self.user_message_id)