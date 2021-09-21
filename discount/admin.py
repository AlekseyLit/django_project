from django.contrib import admin
from discount import models as m
# Register your models here.

admin.site.register(m.Categories)
admin.site.register(m.Discounts)