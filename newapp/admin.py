from django.contrib import admin


from .models import (
    Cast, 
    Director, 
    Movie,
    CustomUser
)
admin.site.register(CustomUser)
admin.site.register(Cast)
admin.site.register(Director)
admin.site.register(Movie)

