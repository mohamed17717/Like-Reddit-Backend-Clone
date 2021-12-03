from django.contrib import admin

from states.models import ExistingState, PendingState, PrivacyState

admin.site.register(ExistingState)
admin.site.register(PendingState)
admin.site.register(PrivacyState)
