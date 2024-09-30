from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')

class CoursesInline(admin.TabularInline): # связь курсов с категориями
    model = models.Course
    exclude = ['created_at']
    extra = 1

class CategoryAdmin(admin.ModelAdmin): # доп поля для удобности
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ["title"]}),
        ('Dates', {
            'fields': ["created_at"], 
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)