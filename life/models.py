from django.db import models

class Skill(models.Model):
    skill = models.CharField(max_length=15)
    
    def __str__(self):
      return 'Skill: ' + self.skill

    
class Item(models.Model):
    name = models.CharField(max_length=50)
    # image = models.ImageField() need to install Pillow and dependent libs
    price = models.FloatField()
    priceperoz = models.FloatField(null=True)
    purchasedate = models.DateField(default='', null=True)
    exp = models.DateField(default='', null=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    def __str__(self):
      return 'Item: ' + self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    # image = models.ImageField() need to install Pillow and dependent libs
    time = models.IntegerField() # time to cook
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Item, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=500)
    
    def __str__(self):
      return 'Recipe: ' + self.name
