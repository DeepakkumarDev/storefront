from django.db import models
# Create your models here.

#  Dfining Many To Many Relationship
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

# Resolving Circular Relationships
#  Circular deendency haapned whn two class depend upon each other at the same time like product class on collectiona and vice vers at the same time

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+') 
    # + sign  will django to not to cretae dreverse relationship

class Product(models.Model):
    # sku = models.CharField(max_length=10,primary_key=True) # if do so django is not going to creted primary key for this model
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')#null=true
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2) # These two field are required
    inventory = models.IntegerField()
    last_update =models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion,related_name='products')
    # promotions = models.ManyToManyField(Promotion,related_name='products') # let it be for django convention

    
# what is revere relationshep how it works in django and mysql an=writ the query fro mysql and defined propley

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 's'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE ,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name=models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email =models.EmailField(max_length=255,unique=True)
    phone = models.CharField(max_length= 15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default= MEMBERSHIP_BRONZE )
    # class Meta:
    #     db_table = 'store_customers'
    #     indexes =[
    #         models.Index(fields=['last_name','first_name'])
    #     ]





class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True) # Django automatically Populated this Field
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_FAILED)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price =models.DecimalField(max_digits=6,decimal_places=2)



# Defining one to one relationship parent exist before a child customer exist beofre address

# class Address(models.Model):
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True) 
#     when we delete a model custmer address also be delete it called the cascading behaviour
#     customer = models.OneToOneField(Customer,on_delete=models.SET_NULL,primary_key=True)
#     in this case when we delete customer as parent then its child is not going to be delete but in this case we should use  model cascading behaviour
#     customer = models.OneToOneField(Customer,on_delete=models.PROTECT,primary_key=True)
#     it will prevent from deleting and custome is going to be null but in this case it is not appropritae why and how? 
#     customer = models.OneToOneField(Customer,on_delete=models.SET_DEFAULT,primary_key=True)

# Defining one to many Relationship

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE) 
  


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()







