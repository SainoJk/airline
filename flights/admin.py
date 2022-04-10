from django.contrib import admin
from .models import Flight,Airport,Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")
class AirportAdmin(admin.ModelAdmin):
    list_display=("id","code","city")
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

# Register your models here.
admin.site.register(Flight,FlightAdmin)
admin.site.register(Airport,AirportAdmin)
admin.site.register(Passenger,PassengerAdmin)