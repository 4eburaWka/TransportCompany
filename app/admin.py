from django.contrib import admin

from .models import Dispatcher, Machine, Driver, Client, Cargo


class DispatcherAdminModel(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_display_links = ('name', 'address')
    search_fields = ('name', 'address')


class MachineAdminModel(admin.ModelAdmin):
    list_display = ('model', 'lifting_capacity', 'dispatcher')
    list_display_links = ('model', 'lifting_capacity', 'dispatcher')
    search_fields = ('model', 'lifting_capacity', 'dispatcher')


class DriverAdminModel(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'surname', 'phone_number', 'profile_photo', 'machine', 'dispatcher')
    list_display_links = ('last_name', 'first_name', 'surname', 'phone_number', 'profile_photo', 'machine', 'dispatcher')
    search_fields = ('last_name', 'first_name', 'surname', 'phone_number', 'profile_photo', 'machine', 'dispatcher')


class ClientAdminModel(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'surname', 'phone_number', 'driver')
    list_display_links = ('last_name', 'first_name', 'surname', 'phone_number', 'driver')
    search_fields = ('last_name', 'first_name', 'surname', 'phone_number', 'driver')


class CargoAdminModel(admin.ModelAdmin):
    list_display = ('client', 'driver', 'dispatcher', 'weight')
    list_display_links = ('client', 'driver', 'dispatcher', 'weight')
    search_fields = ('client', 'driver', 'dispatcher', 'weight')


admin.site.register(Dispatcher, DispatcherAdminModel)
admin.site.register(Machine, MachineAdminModel)
admin.site.register(Driver, DriverAdminModel)
admin.site.register(Client, ClientAdminModel)
admin.site.register(Cargo, CargoAdminModel)
