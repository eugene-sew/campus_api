from django.contrib import admin
from .models import Building, BuildingImage, Office, LectureHall

# Register your models here.

class BuildingImageInline(admin.TabularInline):
    model = BuildingImage

class OfficeInline(admin.TabularInline):
    model = Office

class LectureHallInline(admin.TabularInline):
    model = LectureHall

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    inlines = [BuildingImageInline, OfficeInline, LectureHallInline]
