from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    search_fields = ['brand', 'model']
    list_filter = ('brand', 'model')
    list_display = ('id',  'brand', 'model', 'review_count')


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
