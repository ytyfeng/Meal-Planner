from django.contrib import admin
from life.models import *

# Register your models here.
admin.site.register(Item)

# register activity 
admin.site.register(Recipe)

# register skill
admin.site.register(Skill)