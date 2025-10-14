from django.contrib import admin
from core.models.page import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id','title','status')