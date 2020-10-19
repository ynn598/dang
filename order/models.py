from django.db import models
from index.models import TBook
from user.models import TUser

class TAddress(models.Model):
    person = models.CharField(max_length=30,null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    post_code = models.CharField(max_length=6,blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        db_table = 't_address'

class TOrder(models.Model):
    receive = models.CharField(max_length=20, blank=True, null=True)
    send = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
    new_time = models.DateField(blank=True, null=True)
    sum_price = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        db_table = 't_order'

class TOrderItem(models.Model):
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        db_table = 't_order_item'

