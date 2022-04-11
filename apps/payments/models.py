from django.db import models

class WalletTrans(models.Model):

    wallet_trans_id = models.AutoField(primary_key=True)
    wallet_trans_user_id = models.IntegerField()
    wallet_trans_amount = models.CharField(max_length=10)
    wallet_trans_status = models.IntegerField()
    wallet_trans_time = models.DateTimeField()
    wallet_trans_message = models.TextField()
    wallet_trans_placed_order_id = models.CharField(max_length=11)

    class Meta:
        db_table = "ffz_wallet_trans"

    def __str__(self):
        return str(self.wallet_trans_id)


class TransactionBefore(models.Model):
    bf_id = models.AutoField(primary_key=True)
    bf_tran_id = models.CharField(
        max_length=255, default="28092021", blank=True)
    bf_city_id = models.IntegerField(default=0)
    bf_user_id = models.IntegerField()
    bf_amount = models.CharField(max_length=50, blank=True, default=0)
    bf_tran_date = models.DateTimeField(blank=True)
    payment_verify_status = models.IntegerField(blank=True, default=0)
    user_promo_id = models.IntegerField(blank=True, default=None)
    bf_shipping_method = models.IntegerField(blank=True, default=0)
    bf_store_id = models.IntegerField(blank=True, default=0)
    bf_subscription_id = models.IntegerField(blank=True, default=None)
    bf_delivery_time_pref = models.IntegerField(blank=True, default=0)
    bf_delivery_express_pref = models.IntegerField(blank=True, default=0)
    bf_address_id = models.IntegerField(blank=True)
    bf_shipping_charge = models.CharField(
        max_length=100, default=0, blank=True)
    bf_wallet_amount = models.CharField(max_length=100, default=0, blank=True)
    bf_wallet_amount = models.CharField(max_length=100, default=0, blank=True)
    bf_checkout_addon_id = models.CharField(
        max_length=100, null=True, blank=True)
    bf_checkout_addon_amount = models.IntegerField(
        default=0, null=True, blank=True)

    class Meta:
        db_table = 'ffz_transaction_before'

    def __str__(self):
        return str(self.bf_id)


class CODTransactions(models.Model):
    cod_id = models.AutoField(primary_key=True)
    cod_trans_id = models.CharField(
        blank=True, null=True, max_length=100, default=None)
    cod_city_id = models.IntegerField(blank=True, default=None)
    cod_user_id = models.IntegerField(blank=True, default=None)
    cod_amount = models.IntegerField(blank=True, default=0)
    cod_trans_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    transaction_type = models.CharField(blank=True, null=True, max_length=50, default=None)
    user_promo_id = models.IntegerField(blank=True, default=None)
    cod_delivery_time_pref = models.IntegerField(
        blank=True, null=True, default=0)
    cod_shipping_method = models.IntegerField(blank=True, null=True, default=2)
    cod_store_id = models.IntegerField(blank=True, default=None)
    cod_shipping_charge = models.IntegerField(
        blank=True, null=True, default=None)
    cod_checkout_addon_id = models.CharField(
        blank=True, null=True, max_length=100, default=None)
    cod_checkout_addon_amount = models.IntegerField(
        blank=True, null=True, default=0)

    class Meta:
        db_table = 'ffz_cod_transaction'

    def __str__(self):
        return str(self.cod_id)


class Razorpay(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    delivery_value = models.CharField(default=0, blank=True, max_length=255)
    razor_order_id = models.CharField(default=0, blank=True, max_length=255)
    razor_payment_id = models.CharField(default=0, blank=True, max_length=255)
    razor_bf_id = models.IntegerField(default=0)
    razor_delivery_date = models.CharField(
        default=None, blank=True, max_length=255)
    order_id = models.CharField(default=0, blank=True, max_length=255)
    razor_status = models.IntegerField(default=0)
    create_date = models.DateTimeField(blank=True)
    modify_date = models.DateTimeField(blank=True)
    razor_order_from = models.IntegerField(default=0)
    razor_invoice_id = models.CharField(
        max_length=200, default=0, blank=True)
    razor_invoice_url = models.CharField(
        max_length=200, default=0, blank=True)
    razor_order_placed_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'ffz_razor_payment_history'


class PaymentTypes(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_type_name = models.CharField(
        max_length=255, null=True, default=None)
    payment_type_status = models.IntegerField(null=True, default=1)

    class Meta:
        db_table = "ffz_payment_types"

    def __str__(self):
        return str(self.payment_type_id)


class RazorPaymentHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user_ID = models.IntegerField(default=0, null=True)
    order_ID = models.CharField(max_length=250, default=0)
    razor_orderID = models.CharField(max_length=250, default=0)
    razor_paymentID = models.CharField(max_length=250, default=0)

    class Meta:
        db_table = "razor_payment_history"

    def __str__(self):
        return str(self.id)
