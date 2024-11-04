from django.contrib import admin
from categorygame.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Buld)
class BuldAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}