from django.contrib import admin
from . import models

admin.site.register(models.Blog)
admin.site.register(models.BlogImg)
admin.site.register(models.BlogVideo)
admin.site.register(models.Comment)
admin.site.register(models.SocialMedia)