from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

class Avatar_of_choice(models.Model):
    name = models.CharField('Название', max_length=50)
    usr = models.OneToOneField(User,on_delete=models.CASCADE,default='1',primary_key=True,related_name='chosen_avatar')

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    portrait = models.ImageField(upload_to ='user_images/',blank = True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    chr_class = models.CharField(max_length=13,null=TRUE,blank=TRUE)
    xp = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    background = models.CharField(max_length=100,null=TRUE,blank=TRUE)
    diety = models.CharField(max_length=100,null=TRUE,blank=TRUE)
    origin = models.CharField(max_length=100,null=TRUE,blank=TRUE)
    worldview = models.CharField(max_length=2,null=TRUE,blank=TRUE)
    attrib_strength = models.IntegerField(null=TRUE,blank=TRUE,default=10)
    attrib_agility = models.IntegerField(null=TRUE,blank=TRUE,default=10)
    attrib_charisma = models.IntegerField(null=TRUE,blank=TRUE,default=10)
    attrib_endurance = models.IntegerField(null=TRUE,blank=TRUE,default=10)
    attrib_intelligence = models.IntegerField(null=TRUE,blank=TRUE,default=10)
    attrib_wisdom = models.IntegerField(null=TRUE,blank=TRUE,default=10)
    armour_class = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    hp = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    speed = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_acrobatics = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_arcane = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_athletics = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_craft = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_decieve = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_diplomacy = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_intimidation = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_medicine = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_nature = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_occult = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_performance = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_religion = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_social = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_stealth = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_survival = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    skills_theft = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    save_resilience = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    save_reflex = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    save_resilience = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    save_will = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    weapon = models.CharField(max_length=100, null=TRUE,blank=TRUE) 
    attack = models.CharField(max_length=100, null=TRUE,blank=TRUE)
    damage = models.CharField(max_length=100, null=TRUE,blank=TRUE) 
    attention = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    dc_class = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    notes = models.TextField(null=TRUE,blank=TRUE)
    is_dying = models.IntegerField(null=TRUE,blank=TRUE,default=0)
    mortal_wounds = models.IntegerField(null=TRUE,blank=TRUE,default=0)

    def __str__(self):
        return self.name

# Create your models here.
