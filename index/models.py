# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TBook(models.Model):
    book_name = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    press = models.CharField(max_length=20, blank=True, null=True)
    public_time = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    now_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    vision = models.IntegerField(blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    paper = models.CharField(max_length=20, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    whether = models.IntegerField(blank=True, null=True)
    packing = models.CharField(max_length=10, blank=True, null=True)
    editor_recommend = models.TextField(blank=True, null=True)
    content_recommend = models.TextField(blank=True, null=True)
    about_author = models.TextField(blank=True, null=True)
    catalog = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    cate = models.ForeignKey('TCategory', models.DO_NOTHING, blank=True, null=True)
    sale = models.IntegerField(blank=True, null=True)
    new_time = models.DateField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 't_book'
    def discount(self):
        return "%.2f"%( self.now_price / self.price * 10)

class TCategory(models.Model):
    cate_name = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 't_category'








