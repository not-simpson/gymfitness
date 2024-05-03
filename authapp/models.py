from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=11)
    description=models.TextField()
    
    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=15)
    PhoneNumber=models.CharField(max_length=11)
    DOB=models.DateField()
    SelectMembershipplan=models.CharField(max_length=30)
    SelectTrainer=models.CharField(max_length=45)
    Address=models.TextField()
    paymentStatus=models.CharField(max_length=45,blank=True,null=True)
    Price=models.IntegerField(max_length=45,blank=True,null=True)
    DueDate=models.DateTimeField(null=True,blank=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.FullName
    
    
class Trainer(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=15)
    phone=models.CharField(max_length=11)
    salary=models.IntegerField(max_length=55)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.name
    
class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)
    
    def __int__(self):
        return self.id
    
class Gallery(models.Model):
    name=models.CharField("Name",max_length=30)
    image=models.ImageField("Upload Image",upload_to="Images")
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id
    
    
    
    
    
    
    
    
    
    
    
    
    
    