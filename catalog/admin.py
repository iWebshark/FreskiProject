from django.contrib import admin
from .models import FrescoProvider, FretworkProvider, GlueProvider


@admin.register(FrescoProvider)
class FrescoProviderAdmin(admin.ModelAdmin):
    class Meta:
        model = FrescoProvider


@admin.register(FretworkProvider)
class FretworkProviderAdmin(admin.ModelAdmin):
    class Meta:
        model = FretworkProvider


@admin.register(GlueProvider)
class GlueProviderAdmin(admin.ModelAdmin):
    exclude = ('provider_link',)

    class Meta:
        model = GlueProvider
