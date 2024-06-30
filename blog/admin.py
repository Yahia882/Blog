from django.contrib import admin
from .models import Author, post_model,Tag


# Register your models here.

class postAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(post_model,postAdmin)
admin.site.register(Author)
admin.site.register(Tag)
