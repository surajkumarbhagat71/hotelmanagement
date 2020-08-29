from django.db import models
from django.utils import timezone

# Create your models here.

class Maneeger(models.Model):
    direcotr_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email_id = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    rant = models.IntegerField()

    def __str__(self):
        return self.title


class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_status = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


class UserDetails(models.Model):
    cast_id = models.AutoField(primary_key=True)
    room_number = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField(default=0)
    email_id = models.EmailField(default=0)
    adhar_no = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    cheak_in_time = models.DateTimeField(default=timezone.now)
    cheak_out_time = models.DateTimeField()
    advance_payment = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class EmplyeeCategory(models.Model):
    ec_id = models.AutoField(primary_key=True)
    emplyee_category =  models.CharField(max_length=200)

    def __str__(self):
        return self.emplyee_category


class Emplyee(models.Model):
    emplyee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    category = models.ForeignKey(EmplyeeCategory,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    email = models.EmailField(default=0)
    image = models.ImageField(upload_to='media/')
    address = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    join_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name








