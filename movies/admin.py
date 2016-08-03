from django.contrib import admin

from .models import Movie, Theatre, Showhall, Time, Show
# from .models import Theatre
# from .models import Show


class ShowHallChoiceInline(admin.StackedInline):
    model = Showhall
    extra = 1


class ShowTimeChoiceInline(admin.TabularInline):
    model = Time
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'language')


class ShowAdmin(admin.ModelAdmin):
    list_display = ('show_slug', 'show_hall', 'movie', 'theatre')
    inlines = [ShowTimeChoiceInline]
    search_fields = ['show_slug']


class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', 'landmark', 'contact_no')
    inlines = [ShowHallChoiceInline]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Show, ShowAdmin)

#  'classes': ['collapse']
