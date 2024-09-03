from django.contrib import admin
from cars.models import Car, Brand

# Registering the brand table on the site
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Registering the car table on the site 
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)