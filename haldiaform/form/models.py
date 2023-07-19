from django.db import models
from django.utils.text import slugify 
# Create your models here.
bth=[
    ("attached","attached"),
    ("common","common"),
]
room_cat=[
    (1,"single"),
    (2,"shared"),
]
class owner_details(models.Model):
    owner_name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    # total_rooms=models.IntegerField()

    def __str__(self):
        return self.owner_name

class Room(models.Model):
    owner=models.ForeignKey(owner_details,on_delete=models.CASCADE,blank=False)
    # phone_no=models.CharField(max_length=10)
    building_no = models.IntegerField(default=0)
    pincode=models.CharField(max_length=6,default="721657")
    locality=models.CharField(max_length=70,default="Ksudiramnager")
    address = models.TextField(max_length=100,default="Ksudiramnager")
    land_mark=models.CharField(max_length=100,null=True,blank=True,default=None)
    total_no_rooms = models.IntegerField(default=0)
    no_of_single_rooms=models.IntegerField(default=0)
    no_of_shared_room=models.IntegerField(default=0)
    price_of_single_room=models.IntegerField(default=0)
    price_of_double_room=models.IntegerField(default=0)
    electric_bill=models.IntegerField(default=10)
    no_of_bathrooms=models.IntegerField(default=0)
    bathroom=models.CharField(choices=bth,max_length=100,default=1)
    no_of_bathrooms = models.IntegerField(default=0)
    # shared_room_pictures=models.FileField(null=True,blank=True)
    slug = models.SlugField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.building_no)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.owner.phone_no
    
class room_images(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,blank=False)
    images = models.ImageField()

    
# class model_form_single(models.Model):
#     phone_no=models.CharField(max_length=10)
#     no_single_rooms=models.IntegerField()
#     single_room_price = models.IntegerField()
#     electric_bill=models.IntegerField()
#     bathroom=models.CharField(choices=bth,max_length=100)
#     single_room_pictures=models.FileField()

#     def __str__(self):
#         return self.phone_no