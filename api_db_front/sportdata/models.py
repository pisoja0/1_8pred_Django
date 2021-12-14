from django.db import models


class Continent(models.Model):
    continent = models.CharField(max_length=25)
    featured_country = models.ForeignKey(
        'Country', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

    def __str__(self) -> str:
        return self.continent

    class Meta:
        ordering = ['continent']


class Country(models.Model):
    country = models.CharField(max_length=255)
    continent = models.ForeignKey(Continent, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.country

    class Meta:
        ordering = ['country']

class Availible_Leagues(models.Model):
    league_id = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    country_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    current_season_id = models.CharField(max_length=255)




