
from django.contrib import admin

from main.models import Main, MainBanner
# Register your models here.
class MainInline(admin.TabularInline):
    model = MainBanner
    extra = 3


class MainAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_text1']}),
        (None, {'fields': ['title_text2']}),
        (None, {'fields': ['title_text3']}),
    ]
    inlines = [MainInline]
    #list_display = ('title_text1', 'title_text2',)

admin.site.register(Main, MainAdmin)
#admin.site.register(Choice)

