from django.contrib import admin
from .models import Promotion
from .models.tag import Tag
from .models.category import Category
from .models.imagem import Imagem

admin.site.register(Promotion)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Imagem)