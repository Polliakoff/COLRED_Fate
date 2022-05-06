from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

class Avatar_of_choice(models.Model):
    custom_avatar = models.BooleanField(default=False)
    # name = models.CharField('Название', max_length=50)
    portrait = models.ImageField(upload_to ='user_images/',null=True, blank=True)
    usr = models.OneToOneField(User,on_delete=models.CASCADE,default='1',primary_key=True,related_name='chosen_avatar')

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=10000, default="", blank = True)
    portrait = models.ImageField(upload_to ='user_images/',blank = True)
    custom_avatar = models.BooleanField(default=False,blank = True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    high_concept = models.CharField(max_length=1000, default="", blank = True)
    trouble = models.CharField(max_length=1000, default="", blank = True)
    max_skill = models.IntegerField(default=5, blank = True)
    min_skill = models.IntegerField(default=1, blank = True)
    fate_point_number = models.IntegerField(default=3, blank = True)
    fate_point_refresh = models.IntegerField(default=3, blank = True)
    def __str__(self):
        return self.name


class aspect(models.Model):
    desc = models.CharField(max_length=1000,default = "Пустой аспект")
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_aspects')
    def __str__(self):
        return self.desc

class skill(models.Model):
    name = models.CharField(max_length=100,default = "")
    level = models.IntegerField(default = 0, blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_skills')
    def __str__(self):
        return self.name

class stunt(models.Model):
    name = models.CharField(max_length=100, default = "")
    desc = models.CharField(max_length=10000, default = "", blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_stunts')
    def __str__(self):
        return self.name

class extra(models.Model):
    name = models.CharField(max_length=100, default = "")
    cost = models.CharField(max_length=100, default = "", blank=True)
    attached_aspects = models.CharField(max_length=10000, default = "", blank=True)
    attached_stunts = models.CharField(max_length=10000, default = "", blank=True)
    attached_skills = models.CharField(max_length=10000, default = "", blank=True)
    details = models.CharField(max_length=10000, default = "", blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_extras')
    def __str__(self):
        return self.name

class consequence(models.Model):
    severity = models.CharField(max_length=100, default = "")
    desc = models.CharField(max_length=10000, default = "", blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_consequences')
    def __str__(self):
        return self.desc


# Create your models here.
