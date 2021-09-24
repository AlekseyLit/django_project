from django.contrib import admin
from discount import models as m
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(m.Categories)
admin.site.register(m.Discounts)
admin.site.register(m.Orders)
admin.site.register(m.Offers)