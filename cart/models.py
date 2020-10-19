from django.db import models

from index.models import TBook
from user.models import TUser


class TCart(models.Model):
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 't_cart'


