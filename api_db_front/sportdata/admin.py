from django.contrib import admin, messages
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ['id', 'continent', 'countries_count']
    ordering = ['id']

    @admin.display(ordering='countries_count')
    def countries_count(self, continent):
        url = (
                reverse('admin:sportdata_country_changelist')
                + '?'
                + urlencode({
            'continent__id': str(continent.id)
        })
        )
        return format_html('<a href="{}">{}</a>', url, continent.countries_count)
        #return continent.countries_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            countries_count=Count('country')
        )


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country']
    ordering = ['id']
    list_select_related = ['continent']
