from django.db import models

class Promos(models.Model):
    CASHBACK_TYPE = 1
    INSTANT_DISCOUNT_TYPE = 2
    PROMO_TYPE_CHOICES = (
        (CASHBACK_TYPE, 'CASHBACK'),
        (INSTANT_DISCOUNT_TYPE, 'INSTANT_DISCOUNT')
    )
    PROMO_ACTIVE = 1
    PROMO_DISABLED = 0
    PROMO_STATUS_CHOICES = (
        (PROMO_ACTIVE, 'ACTIVE'),
        (PROMO_DISABLED, 'DISABLED')
    )
    promo_id = models.AutoField(primary_key=True)
    promo_title = models.CharField(blank=True, max_length=255, default=None)
    promo_message = models.TextField(blank=True, default=None)
    promo_status = models.IntegerField(blank=True, default=None, choices=PROMO_STATUS_CHOICES)
    promo_type = models.IntegerField(blank=True, default=None, choices=PROMO_TYPE_CHOICES)
    promo_start_date = models.DateTimeField(blank=True, default=None)
    promo_sign_up_from = models.DateField(blank=True, null=True)
    promo_sign_up_to = models.DateField(blank=True, null=True)
    promo_expiry = models.DateTimeField(blank=True, default=None)
    promo_discount_type = models.IntegerField(blank=True, default=None)
    promo_discount = models.DecimalField(
        decimal_places=2, max_digits=10, blank=True, default=None)
    promo_max_discount = models.DecimalField(
        decimal_places=2, max_digits=10, blank=True, default=None)
    promo_apply_type = models.IntegerField(blank=True, default=1)
    promo_custom_config = models.TextField(blank=True, null=True)
    promo_code = models.CharField(blank=True, null=True, max_length=255)
    promo_admin_notes = models.TextField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'ffz_promos'


class UserPromos(models.Model):
    user_promo_id = models.AutoField(primary_key=True)
    user_promo_promo_id = models.IntegerField()
    user_promo_user_id = models.IntegerField()
    user_promo_code = models.CharField(max_length=255)
    user_promo_used_status = models.IntegerField()
    user_promo_added_time = models.DateTimeField()
    user_promo_wallet_tr_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'ffz_user_promos'


class UserReferral(models.Model):
    id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField()
#     order_id = models.CharField(max_length=50, null=True)
#     user_referral_id = models.CharField(max_length=110)
#     active_refferal = models.CharField(max_length=1, default=0)
#     referal_cashback_child = models.DecimalField(
#         decimal_places=2, max_digits=10, null=True, default=None)
#     referral_cashback_parent = models.DecimalField(
#         decimal_places=2, max_digits=10, null=True, default=None)
#     referral_date = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "ffz_user_referral"

#     def __str__(self):
#         return str(self.id)


class UserCashback(models.Model):
    id = models.AutoField(primary_key=True)
    cashback_type = models.CharField(max_length=200, default=None)
    min_amount = models.DecimalField(
        decimal_places=2, max_digits=10, default=None)
    cashback_amount = models.DecimalField(
        decimal_places=2, max_digits=10, default=None)

    class Meta:
        db_table = "ffz_user_cashback"

    def __str__(self):
        return str(self.id)
