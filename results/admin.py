from django.contrib import admin

from . import models


@admin.register(models.Agentname)
class AgentnameAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email", "phone", "pollingunit_uniqueid"]


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["state_name", "state_id"]


@admin.register(models.Lga)
class LgaAdmin(admin.ModelAdmin):
    list_display = ["lga_name", "lga_id", "state_id"]


@admin.register(models.Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ["ward_name", "ward_id", "lga_id"]


@admin.register(models.Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ["partyid", "partyname"]


@admin.register(models.AnnouncedPuResults)
class AnnouncedPuResultsAdmin(admin.ModelAdmin):
    list_display = ["polling_unit_uniqueid", "party_abbreviation", "party_score"]
    list_filter = ["polling_unit_uniqueid", "party_abbreviation"]


@admin.register(models.AnnouncedWardResults)
class AnnouncedWardResultsAdmin(admin.ModelAdmin):
    list_display = ["ward_name", "party_abbreviation", "party_score"]
    list_filter = ["ward_name", "party_abbreviation"]


@admin.register(models.AnnouncedStateResults)
class AnnouncedStateResultsAdmin(admin.ModelAdmin):
    list_display = ["state_name", "party_abbreviation", "party_score"]
    list_filter = ["state_name", "party_abbreviation"]


@admin.register(models.AnnouncedLgaResults)
class AnnouncedLgaResultsAdmin(admin.ModelAdmin):
    list_display = ["lga_name", "party_abbreviation", "party_score"]
    list_filter = ["lga_name", "party_abbreviation"]


@admin.register(models.PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ["polling_unit_name", "uniqueid", "polling_unit_id"]
    list_filter = ["lga_id"]
