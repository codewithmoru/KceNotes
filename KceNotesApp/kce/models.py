from django.db import models

# Create your models here.

#class Contact(models.Model):
 #  Name = models.CharField(max_length=122) 
  # Email = models.CharField(max_length=122)
   #Phone = models.CharField(max_length=12) 
   #Message = models.TextField() 
   #Date = models.DateField()    
   #def __str__(self):
        #return self.Name


class Notes1(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    excercise1 = models.FileField(max_length=200, default="")
    def __str__(self):
        return self.product_name        

class Notes2(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    excercise2 = models.FileField(max_length=200, default="")
    def __str__(self):
        return self.product_name        

class Notes3(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    excercise3 = models.FileField(max_length=200, default="")
    def __str__(self):
        return self.product_name        

class Notes4(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    excercise4 = models.FileField(max_length=200, default="application")
    def __str__(self):
        return self.product_name                                        
class TEACHING(models.Model):

    product_id = models.AutoField
    product_title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    content = models.CharField(max_length=300)
    pub_date = models.DateField()
    excercise = models.URLField(max_length=200, default="")
    def __str__(self):
        return self.product_title        


# import the standard Django Forms
# from built-in library
# creating a form

class Customer(models.Model):
    firstname1 = models.CharField(max_length=200)
    lastname1 = models.CharField(max_length=200)
    subject1 = models.TextField(max_length=200)
    def __str__(self):
       return self.firstname1

class Users(models.Model):
    firstname1 = models.CharField(max_length=200)
    lastname1 = models.CharField(max_length=200)
    subject1 = models.TextField(max_length=200)
    subject2 = models.TextField(max_length=200)
    Phone = models.TextField(max_length=12)
    def __str__(self):
       return self.firstname1