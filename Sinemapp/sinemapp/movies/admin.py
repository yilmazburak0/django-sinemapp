from django.contrib import admin

from movies.models import Genre, Movie, Person, Video

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','is_released','is_coming',)
    prepopulated_fields = {'slug': ('title',) }
    list_filter = ('genres','language','is_released','is_coming',)
    search_fields = ('title','description',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','gender','duty_type')
    list_filter = ('gender','duty_type')
    search_fields = ('first_name','last_name')
    

admin.site.register(Movie, MovieAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Genre)
admin.site.register(Video)

