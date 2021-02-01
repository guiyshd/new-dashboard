from django.db import models


class WcotaBaseNacional(models.Model):
    country = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    ibgeid = models.IntegerField(null=True, blank=True)
    cod_regiaodesaude = models.FloatField(null=True, blank=True)
    name_regiaodesaude = models.TextField(null=True, blank=True)
    deaths = models.IntegerField(null=True, blank=True)
    totalcases = models.IntegerField(null=True, blank=True)
    deaths_per_100k_inhabitants = models.FloatField(null=True, blank=True)
    totalcases_per_100k_inhabitants = models.FloatField(null=True, blank=True)
    deaths_by_totalcases = models.FloatField(null=True, blank=True)
    field_source = models.TextField(null=True, blank=True)
    date = models.TextField(null=True, blank=True)
    newcases = models.IntegerField(null=True, blank=True)
    newdeaths = models.IntegerField(null=True, blank=True)
    last_info_date = models.TextField(null=True, blank=True)
