from django.contrib import admin

from pokedex.models import Type, Pokemon


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'evolve_from', 'type_1', 'type_2')
    ordering = ('number', )
    raw_id_fields = ('evolve_from', 'type_1', 'type_2', )
