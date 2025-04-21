from django.contrib import admin
from .models import Promotion
from .models.tag import Tag
from .models.category import Category

admin.site.register(Promotion)
admin.site.register(Tag)
admin.site.register(Category)