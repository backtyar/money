from django.contrib import admin
from consumption.models import Category, Consumption, UserCategory



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_category']
    list_display_links = ['id']


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'my_category']
    list_display_links = ['id']


# @admin.register(Consumption)
# class ConsumptionAdmin(admin.ModelAdmin):
#     list_display = ['id', 'expenses']
#     list_display_links = ['id']





