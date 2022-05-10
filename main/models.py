from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

class Avatar_of_choice(models.Model):
    custom_avatar = models.BooleanField(default=False)
    portrait = models.ImageField(upload_to ='user_images/',null=True, blank=True)
    usr = models.OneToOneField(User,on_delete=models.CASCADE,default='1',primary_key=True,related_name='chosen_avatar')

    def __str__(self):
        return self.name

@receiver(post_delete, sender = Avatar_of_choice)
def usr_port_del(sender, instance, *args, **kwargs):
    try:
        instance.portrait.delete(save=False)
    except:
        pass

class Character(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=10000, default="", blank = True)
    portrait = models.ImageField(upload_to ='user_images/',blank = True)
    custom_avatar = models.BooleanField(default=False,blank = True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    high_concept = models.CharField(max_length=1000, default="", blank = True)
    trouble = models.CharField(max_length=1000, default="", blank = True)
    fate_point_number = models.IntegerField(default=3, blank = True)
    fate_point_refresh = models.IntegerField(default=3, blank = True)
    def __str__(self):
        return self.name

@receiver(post_delete, sender = Character)
def chr_port_del(sender, instance, *args, **kwargs):
    try:
        instance.portrait.delete(save=False)
    except:
        pass

class aspect(models.Model):
    desc = models.CharField(max_length=1000,default = "Пустой аспект")
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_aspects')
    def __str__(self):
        return self.desc

class skill(models.Model):
    name = models.CharField(max_length=100,default = "Неуказанное умение")
    level = models.IntegerField(default = 0, blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_skills')
    def __str__(self):
        return self.name

class stunt(models.Model):
    name = models.CharField(max_length=100, default = "Пустой трюк")
    desc = models.CharField(max_length=10000, default = "", blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_stunts')
    def __str__(self):
        return self.name

class extra(models.Model):
    name = models.CharField(max_length=100, default = "Пустое дополнение")
    cost = models.CharField(max_length=100, default = "", blank=True)
    attached_aspects = models.CharField(max_length=10000, default = "", blank=True)
    attached_stunts = models.CharField(max_length=10000, default = "", blank=True)
    attached_skills = models.CharField(max_length=10000, default = "", blank=True)
    details = models.CharField(max_length=10000, default = "", blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_extras')
    def __str__(self):
        return self.name

class consequence(models.Model):
    severity = models.CharField(max_length=100, default = "Неуточненная травма")
    desc = models.CharField(max_length=10000, default = "", blank=True)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_consequences')
    def __str__(self):
        return self.severity

class stress(models.Model):
    type = models.CharField(max_length=100, default = "Физический")
    level = models.IntegerField(default=1)
    avaliable = models.IntegerField(default=3)
    spent = models.IntegerField(default=0)
    chr = models.ForeignKey('Character', on_delete=models.CASCADE,related_name='character_stress')
    def __str__(self):
        return self.type


# Create your models here.
