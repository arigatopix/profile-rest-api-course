from django.contrib import admin

# import models
from profiles_api import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
''' แสดง models ในหน้า admin '''
