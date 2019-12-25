from django.contrib import admin


from .models import (
    Cast, 
    Director, 
    Movie
)

admin.site.register(Cast)
admin.site.register(Director)
admin.site.register(Movie)

