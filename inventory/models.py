import uuid
from django.db import models


# Create your models here.
GENDER = (('M', 'Male'), ('F', 'Female'))
SHOE_SIZES = (('37', '37'), ('38', '38'), ('39', '39'), \
    ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), \
        ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'))
SHOE_CATEGORIES = (('Shoes', 'Shoes'), ('Slippers', 'Slippers'), ('Sandals', 'Sandals'), \
    ('Others', 'Others'))
ACCESORIES_CATEGORIES = (('Sunglasses', 'Sunglasses'), ('Bags', 'Bags'), \
    ('Watch', 'Watch'), ('Belt', 'Belt'), ('Wallet', 'Wallet'))
CLOTHES_SIZES = (('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'))
CLOTHES_CATEGORIES = (('T-Shirt', 'T-Shirt'), ('Shirt', 'Shirt'), ('Polo', 'Polo'))
COLORS = (('Blue', 'Blue'), ('Red', 'Red'), ('Black', 'Black'), ('Brown', 'Brown'), \
    ('Grey', 'Grey'), ('Webbing', 'Webbing'), ('White', 'White'))

class Product(models.Model):
    design_name = models.CharField(max_length=100)
    product_number = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER)
    quantity_in_stock = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(max_digits=7, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Batch(models.Model):
    batch_number = models.UUIDField(default=uuid.uuid4, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Batches"
    
    def __str__(self):
        return str(self.batch_number)

class Footwear(Product):
    color = models.CharField(max_length=50, choices=COLORS)
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING, related_name='shoe_batch')
    size = models.CharField(max_length=3, choices=SHOE_SIZES)
    category = models.CharField(max_length=20, choices=SHOE_CATEGORIES)

    class Meta:
        verbose_name_plural = "Footwears"
    
    def __str__(self):
        batch_num = str(self.batch.batch_number)
        prod_num = str(self.product_number)
        return str(self.design_name + '--' + batch_num + '--' + prod_num)


class Accessory(Product):
    color = models.CharField(max_length=50, choices=COLORS)
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING, related_name='accessory_batch')
    category = models.CharField(max_length=20, choices=ACCESORIES_CATEGORIES)

    class Meta:
        verbose_name_plural = "Accessories"

    def __str__(self):
        batch_num = str(self.batch.batch_number)
        prod_num = str(self.product_number)
        return str(self.design_name + '--' + batch_num + '--' + prod_num)


class Clothes(Product):
    color = models.CharField(max_length=50, choices=COLORS)
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING, related_name='clothes_batch')
    category = models.CharField(max_length=20, choices=CLOTHES_CATEGORIES)
    size = models.CharField(max_length=3, choices=CLOTHES_SIZES)

    class Meta:
        verbose_name_plural = "Clothes"
    
    def __str__(self):
        batch_num = str(self.batch.batch_number)
        prod_num = str(self.product_number)
        return str(self.design_name + '--' + batch_num + '--' + prod_num)