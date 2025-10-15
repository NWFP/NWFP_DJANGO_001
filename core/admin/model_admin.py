from django.contrib import admin
from core.models.page import Page
from core.models.student import Student
from core.models.team import Team

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('template_name','status','landing_page','activation_date', 'deactivation_date','description')
    # def start_date_display(self, obj):
    #     return obj.start_date.date() if obj.start_date else None
    # start_date_display.short_description = 'Activation Date'

    # def end_date_display(self, obj):
    #     return obj.end_date.date() if obj.end_date else None
    # end_date_display.short_description = 'Deactivation Date'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','organisation','project_title')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','team_type','work_package','image','staff_link', 'activation_date', 'deactivation_date')



#from core.admin.form_admin import PageForm
# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     form = PageForm
#     list_display = ('id','title','status','landing_page','comment','start_date_only', 'end_date_only', 'is_active')

#     def start_date_only(self, obj):
#         return obj.start_date.date() if obj.start_date else None
#     start_date_only.short_description = 'Activation Date'

#     def end_date_only(self, obj):
#         return obj.end_date.date() if obj.end_date else None
#     end_date_only.short_description = 'Deactivation Date'

#     def is_active(self, obj):
#         return obj.is_active # Assuming is_active is a boolean field in ActivatorModel