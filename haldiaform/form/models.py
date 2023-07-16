from django.db import models

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
    total_rooms=models.IntegerField()

class model_form_shared(models.Model):
    phone_no=models.CharField(max_length=10)
    no_shared_rooms=models.IntegerField()
    shared_room_price = models.IntegerField()
    electric_bill=models.IntegerField()
    bathroom=models.CharField(choices=bth,max_length=100)
    shared_room_pictures=models.FileField()

    def __str__(self):
        return self.phone_no
    
class model_form_single(models.Model):
    phone_no=models.CharField(max_length=10)
    no_single_rooms=models.IntegerField()
    single_room_price = models.IntegerField()
    electric_bill=models.IntegerField()
    bathroom=models.CharField(choices=bth,max_length=100)
    single_room_pictures=models.FileField()

    def __str__(self):
        return self.phone_no