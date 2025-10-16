from django.contrib import admin
from core.models.page import Page
from core.models.student import Student
from core.models.team import Team
from core.models.organisation import Organisation
from core.models.data import Data
from core.models.tag import Tag
from core.models.theme import Theme
from core.models.testimony import Testimony
from core.models.project import Project


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('template_name','status','landing_page','activation_date', 'deactivation_date','description')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','team_type','work_package','image','staff_link', 'activation_date', 'deactivation_date')

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'website', 'Ror')

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')   

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('title','student','url','youtube_code')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','organisation','project')
    list_display = ('name', 'project',)
    list_filter = ('project',)
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','goal')
    filter_horizontal = ('data','tag','theme') 
    search_fields = ('title',)


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