from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    tilte = models.CharField(max_length=500)
    desc = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.tilte

class Content(models.Model):
    post_id = models.AutoField(primary_key= True)
    bp_id = models.IntegerField(default = 0)
    name = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    link = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    email = models.CharField(max_length=500, default="")
    phone = models.CharField(max_length=15, default="")
    
    def __str__(self):
        return self.name


class Youtube(models.Model):
    id = models.AutoField(primary_key= True)
    bp_id = models.IntegerField(default = 0)
    name = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    link = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)        

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username


class Contribute(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    
    def __str__(self):
        return self.name






   