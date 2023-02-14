from django.contrib import admin

from . import models


@admin.register(models.ConsentSource)
class ConsentSourceAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ConsentSourceTranslation)
class ConsentSourceTranslationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.UserConsent)
class UserConsentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.EmailCampaign)
class EmailCampaignAdmin(admin.ModelAdmin):
    pass

@admin.register(models.EmailOptOut)
class EmailOptOutAdmin(admin.ModelAdmin):
    pass



