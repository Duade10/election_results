from django.contrib import admin

from . import models


@admin.register(models.Agentname, models.AnnouncedLgaResults, models.AnnouncedPuResults, models.AnnouncedStateResults, models.AnnouncedWardResults,
                models.Lga, models.Party, models.State, models.Ward)
class ResultsModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ["polling_unit_name", "uniqueid", "polling_unit_id"]